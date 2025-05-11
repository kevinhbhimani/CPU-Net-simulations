import numpy as np
import sys
import h5py
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from tqdm import tqdm
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import DBSCAN


clust_eps = 0.01 # distance for which two points are considered neighbors in DBSCAN
energy_cut= 1 # only energy above 1 MeV are considered


if(len(sys.argv) != 3):
    print('Usage: post_proc_cluster.py [filename.hdf5] [run number]')
    sys.exit()

# have to open the input file with h5py (g4 doesn't write pandas-ready hdf5)
g4sfile_name = sys.argv[1]
run_num = sys.argv[2]

# g4sfile_name = "/pscratch/sd/k/kbhimani/cpu_net_data/cpu_net_data_1.hdf5"
print("Importing data")
g4sfile = h5py.File(g4sfile_name, 'r')
g4sntuple = g4sfile['default_ntuples']['g4sntuple']

g4sdf = pd.DataFrame(np.array(g4sntuple['x']['pages']), columns=['x_hit'])
g4sdf = g4sdf.join(pd.DataFrame(np.array(g4sntuple['y']['pages']), columns=['y_hit']), lsuffix = '_caller', rsuffix = '_other')
g4sdf = g4sdf.join(pd.DataFrame(np.array(g4sntuple['z']['pages']), columns=['z_hit']), lsuffix = '_caller', rsuffix = '_other')
g4sdf = g4sdf.join(pd.DataFrame(np.array(g4sntuple['event']['pages']), columns=['event']), lsuffix = '_caller', rsuffix = '_other')
g4sdf = g4sdf.join(pd.DataFrame(np.array(g4sntuple['Edep']['pages']), columns=['Edep']), lsuffix = '_caller', rsuffix = '_other')
g4sdf = g4sdf.join(pd.DataFrame(np.array(g4sntuple['volID']['pages']), columns=['volID']), lsuffix = '_caller', rsuffix = '_other')
g4sdf = g4sdf.join(pd.DataFrame(np.array(g4sntuple['iRep']['pages']), columns=['iRep']), lsuffix = '_caller', rsuffix = '_other')

print("Getting events list")
detector_hits = g4sdf.loc[(g4sdf.Edep>0)&(g4sdf.volID==1)]
procdf = pd.DataFrame(detector_hits.groupby(['event','volID','iRep'], as_index=False)['Edep'].sum())
procdf = procdf.rename(columns={'iRep':'detID', 'Edep':'energy'})
indexes_of_interest = (procdf['energy'] > energy_cut)
procdf = procdf[indexes_of_interest]
event_list= procdf["event"]
event_list = [* set(event_list)]

def clust_center(x_val, e_vals):
     return np.sum(x_val*e_vals)/np.sum(e_vals)
    
def cluster_number(x_val):
    count = 0
    for i in x_val:
            count +=1
    return count

print("Running clustering")
model = DBSCAN(eps=clust_eps)
sim_df = pd.DataFrame([])
cut= g4sdf["Edep"]>0&(g4sdf.volID==1)
iter=0
for i in tqdm(event_list):
    if (iter%10000==0):
        print("Clustering iteration:", iter, 'of', len(event_list))
    data_load = g4sdf[cut & (g4sdf["event"]==i)]
    e_event=data_load["Edep"].sum()
    data = data_load[['x_hit','y_hit','z_hit']]
    pred = model.fit_predict(data) #sample_weight=normalized_weights
    for lab in set(model.labels_):
        x_clust_temp = clust_center(data_load["x_hit"][model.labels_==lab], data_load["Edep"][model.labels_==lab])
        y_clust_temp = clust_center(data_load["y_hit"][model.labels_==lab], data_load["Edep"][model.labels_==lab])
        z_clust_temp = clust_center(data_load["z_hit"][model.labels_==lab], data_load["Edep"][model.labels_==lab])
        e_clust_temp = data_load["Edep"][model.labels_==lab].sum()
        num_points = cluster_number((data_load["Edep"][model.labels_==lab]))
        df2 = pd.DataFrame([[x_clust_temp, y_clust_temp, z_clust_temp, e_clust_temp,e_event, int(i), num_points]], columns = ['x_hit', 'y_hit', 'z_hit','e_hit', 'e_event', 'event', 'num_points'])
        sim_df=pd.concat([sim_df, df2],ignore_index=True)
    iter+=1

file_save= '/global/homes/k/kbhimani/cpu_net_sims/clust_data/cpu_net_data_clust_' + run_num + '.h5'
print("Saving output to file", file_save)
store = pd.HDFStore(file_save)
store['sim_df'] = sim_df  
store.close()
