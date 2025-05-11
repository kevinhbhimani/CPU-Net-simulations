import os
import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
import os
import shutil
import struct
import pickle

siggen_dir='/global/homes/k/kbhimani/cpu_net_sims/WFSimulation/icpc_siggen/'
clust_dir= "/global/homes/k/kbhimani/cpu_net_sims/clust_data/"
waveform_dir="/pscratch/sd/k/kbhimani/cpu_net_data/waveforms/"
save_dir="/global/homes/k/kbhimani/cpu_net_sims/waveforms/"

# siggen_dir='/Users/kevinhbhimani/Desktop/cpu_net_sims/WFSimulation/icpc_siggen/'
# clust_dir= "/Users/kevinhbhimani/Desktop/cpu_net_sims/clust_data/"
# waveform_dir="/Users/kevinhbhimani/Desktop/waveforms/"
# save_dir="/Users/kevinhbhimani/Desktop/cpu_net_sims/waveforms/"
import glob  # import the glob module to find all the files matching a pattern

def delete_files_in_directory(directory_path):
    # Get a list of all files in the directory
    files = glob.glob(directory_path + '*')
    
    for file in files:
        try:
            os.remove(file)  # Try to delete each file
            # print(f"File {file} deleted successfully")
        except Exception as e:
            print(f"An error occurred while deleting the file {file}: {e}")

os.chdir(siggen_dir)
z_cut = 152.9-30/2

print("Creating events list")
for run in range(1,4):
    run_dir= clust_dir+"cpu_net_data_clust_"+str(run)+'.h5'
    print("procession file:", run_dir)
    f = pd.read_hdf(run_dir)
    edep = f["e_hit"].to_numpy()
    e_total = f["e_event"].to_numpy()
    x = f["x_hit"].to_numpy()
    y = f["y_hit"].to_numpy()
    z = f["z_hit"].to_numpy()
    event = f["event"].to_numpy()
    num_points= f["num_points"].to_numpy()
    zerodep_flag = (edep> 0)&(z>z_cut)&(e_total>2.100)&(e_total<2.105)
    edep = edep[zerodep_flag]
    e_total = e_total[zerodep_flag]
    x = x[zerodep_flag]
    y = y[zerodep_flag]
    z = z[zerodep_flag]-z_cut
    event = event[zerodep_flag]
    num_points = num_points[zerodep_flag]
    # print(e_total)
    # print(y)
    f = open(waveform_dir+"my_stester_commands.txt", "w")
    for i in range(0,len(x)):
        f.write("cart \n")
        f.write("tau 0\n")
        f.write("dif 1\n")
        f.write("ccs 0.1\n")
        str1 = "sig %f %f %f "%(x[i],y[i],z[i])
        str2 = waveform_dir+"unstacked_wf/sig_event%d_x_%.4fy_%.4fz_%.4f.spe\n"%(event[i],np.round(x[i],4),np.round(y[i],4),np.round(z[i],4))
        f.write(str1+str2)
        # if event[i]==46926024:
        #     print(str2)
        #     print("sim iter", i)
        #     print(y[i])
    f.write("quit\n")
    f.close()
    # print(y)
    print("Running Siggen to generate waveforms")
    sterster_comand = siggen_dir + "stester config_files/bege_Sp.config < " + waveform_dir + "my_stester_commands.txt"
    subprocess.run(sterster_comand, stdout=subprocess.DEVNULL, check=False, shell=True) #, stdout=subprocess.DEVNULL
    wfs=[]
    events_array=[]
    energy_dep=[]
    for j in range(0,len(x)):
        unstack_wf_dir = waveform_dir+"/unstacked_wf/sig_event%d_x_%.4fy_%.4fz_%.4f.spe"%(event[j],np.round(x[j],4),np.round(y[j],4),np.round(z[j],4))
        # print(unstack_wf_dir)
        # wf = np.loadtxt(unstack_wf_dir)
        # if(event[i]==88211636):
        #     print("here again!!")
        #     print(unstack_wf_dir)
        #     f = open(unstack_wf_dir, 'rb')
        # if event[j]==46926024:
        #     print(unstack_wf_dir)
        #     print('load iter', j)
        #     print(y[j])
        #     print(y[2])
        #     print('should be')
        # print('/pscratch/sd/k/kbhimani/cpu_net_data/waveforms/g4simple_waveforms_bege/sig_event46926024_x_-20.2344y_0.4999z_20.8668.spe')
        wf=0
        try:
            f = open(unstack_wf_dir, 'rb')
            head = f.read(36)
            yraw = f.read(500*4)
            y_wf = np.array(struct.unpack('f'*500, yraw))
            wf = np.array([0]*500+list(y_wf))
            
            # print(j)
        except (FileNotFoundError):
            # print("Wrong file or file path")
            # print(unstack_wf_dir)
            continue
        wfs.append(wf)
        events_array.append(event[j])
        energy_dep.append(edep[j])
        if(event[j]==19533107):
            print(event[j])
            print(wf)
                            
    wfs = np.asarray(wfs)
    events_array=np.asarray(events_array)
    energy_dep = np.asarray(energy_dep)

    for e in np.unique(events_array):
        eve_st = events_array[events_array==e]
        event_wf_st =  wfs[events_array==e]
        energy_dep_st = energy_dep[events_array==e]
        stack_wf = event_wf_st[0]*energy_dep_st[0]
        for i in range(1,len(eve_st)):
            stack_wf += event_wf_st[i]*energy_dep_st[i]
        final_stacked = stack_wf/np.sum(energy_dep_st)
        np.savetxt(waveform_dir+"/stacked_wf/" + 'wf_event_%d_energy_%d.txt'%(e,np.sum(energy_dep_st)*1000),final_stacked)
    save_file=save_dir+ "sep_sim"+str(run)+".pickle"
    
    print("Saving the waveforms in:", save_file)
    with open(save_file, 'wb') as handle:
        for i,fname in enumerate(os.listdir(waveform_dir+"/stacked_wf/"),0):
            path = os.path.join(waveform_dir+"/stacked_wf/",fname)
            if os.path.exists(path):
                wf = np.loadtxt(path)
                event_dict = {
                    "tp0":500,\
                    "wf":wf.astype(np.float32),\
                }
                pickle.dump(event_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    os.remove(waveform_dir+"my_stester_commands.txt")
    delete_files_in_directory(waveform_dir + "unstacked_wf/")
    delete_files_in_directory(waveform_dir + "stacked_wf/")
    save_file_all = save_dir + "sep_sim.pickle"
    import pickle

def combine_pickle_files(file_basename, n, output_filepath):
    combined_data = []

    # Load the data from each file and append it to the combined_data list
    for i in range(1, n+1):
        filepath = f"{file_basename}{i}.pickle"
        print("Adding file", filepath)
        with open(filepath, 'rb') as file:
            while True:
                try:
                    data = pickle.load(file)
                    combined_data.append(data)
                except EOFError:
                    break

    # Save the combined data into a new pickle file
    with open(output_filepath, 'wb') as output_file:
        for data in combined_data:
            pickle.dump(data, output_file, protocol=pickle.HIGHEST_PROTOCOL)

    print(f"Combined data saved in: {output_filepath}")


# Example usage:
file_basename = '/global/homes/k/kbhimani/cpu_net_sims/waveforms/sep_sim'
n = 3  # Adjust this number based on how many files you have
output_filepath = '/global/homes/k/kbhimani/cpu_net_sims/waveforms/sep_sim.pickle'
combine_pickle_files(file_basename, n, output_filepath)