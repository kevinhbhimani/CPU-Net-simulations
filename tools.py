import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
def process_run(filename, run_number, offset):
    """
    Process simulation data from an HDF5 file for a specific run.

    Parameters:
    filename (str): Path to the HDF5 file containing simulation data.
    run_number (int): The current run number, used to adjust event identifiers.
    offset (int): The offset value applied to event numbers to ensure uniqueness across runs.

    Returns:
    pandas.DataFrame: A DataFrame containing filtered and processed hit data, 
                      including unique event identifiers, deposited energy ('edep' in keV), 
                      and the total deposited energy per event ('e_total').
    """
    g4sfile = h5py.File(filename, 'r')
    
    g4sntuple = g4sfile['default_ntuples']['g4sntuple']

    # build a pandas DataFrame from the hdf5 datasets we will use
    g4sdf = pd.DataFrame({
        'x_hit': np.array(g4sntuple['x']['pages']),
        'y_hit': np.array(g4sntuple['y']['pages']),
        'z_hit': np.array(g4sntuple['z']['pages']),
        'event': np.array(g4sntuple['event']['pages']),
        'Edep': np.array(g4sntuple['Edep']['pages']),
        'volID': np.array(g4sntuple['volID']['pages']),
        'iRep': np.array(g4sntuple['iRep']['pages'])
    })
    # Adjust event numbers to make them unique across runs
    g4sdf['event'] += run_number * offset
    
    detector_hits = g4sdf.loc[(g4sdf.Edep>0)&(g4sdf.volID==1)]

    procdf = detector_hits.rename(columns={'iRep':'detID', 'Edep':'edep'})
    procdf['edep'] = procdf['edep']*1000
    procdf['z_hit'] = abs(procdf['z_hit'] -  round(procdf['z_hit'].min(),2))
    procdf['e_total'] = procdf.groupby('event')['edep'].transform('sum')
    return procdf

import pandas as pd
import numpy as np

def process_run_csv(filename, run_number, offset):
    """
    Process simulation data from a CSV file for a specific run.

    Parameters:
    filename (str): Path to the CSV file containing simulation data.
    run_number (int): The current run number, used to adjust event identifiers.
    offset (int): The offset value applied to event numbers to ensure uniqueness across runs.

    Returns:
    pandas.DataFrame: A DataFrame containing filtered and processed hit data,
                      including unique event identifiers, deposited energy ('edep' in keV),
                      and the total deposited energy per event ('e_total').
    """
    # Skip the initial rows that do not contain data
    skip_rows = 24  # Adjust based on your file's header lines
    
    # Define column names as they appear in your CSV file
    column_names = ['nEvents', 'event', 'pid', 'trackID', 'parentID', 'step', 'KE', 'Edep', 'x', 'y', 'z', 'lx', 'ly', 'lz', 'pdx', 'pdy', 'pdz', 't', 'volID', 'iRep']
    
    # Load the data, skipping the header rows and assigning column names
    data = pd.read_csv(filename, skiprows=skip_rows, header=None, names=column_names)
    
    # Adjust event numbers to make them unique across runs
    data['event'] += run_number * offset

    # Filter for hits where energy was deposited in the detector volume
    detector_hits = data.loc[(data['Edep'] > 0) & (data['volID'] == 1)]

    # Process the DataFrame to match the required structure
    proc_df = detector_hits.rename(columns={'iRep': 'detID', 'Edep': 'edep'}).copy()
    proc_df['edep'] *= 1000  # Convert 'edep' to keV
    proc_df['z_hit'] = abs(proc_df['z'] - round(proc_df['z'].min(), 2))  # Adjust 'z_hit' if needed
    proc_df['e_total'] = proc_df.groupby('event')['edep'].transform('sum')  # Calculate total deposited energy per event

    # Select and rename columns to match the expected output structure
    proc_df = proc_df[['event', 'x', 'y', 'z_hit', 'edep', 'volID', 'detID', 'e_total']]
    proc_df.rename(columns={'x': 'x_hit', 'y': 'y_hit'}, inplace=True)

    return proc_df





