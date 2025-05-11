import pandas as pd
import numpy as np
import subprocess
import os
import struct
from tools import process_run_csv

# Specify your runs and file paths.
run_start = 15
run_end = 20 
base_directory = "/work/users/k/b/kbhimani/cpu_net_g4sims/data_ornl/"
base_filename = "data_run_{}.csv"
offset = 1000000 + 1

energy_ranges = {
    (2614, 2615): "fep_wf",
    (2103, 2104): "sep_wf",
    (1592, 1593): "dep_wf"
}

# Setup for simulation.
config_path = "/nas/longleaf/home/kbhimani/ornl_sims/icpc_siggen/config_files/V06649A.config"
siggen_dir = "/nas/longleaf/home/kbhimani/ornl_sims/icpc_siggen/"
stester_executable = os.path.join(siggen_dir, "stester")
os.chdir(siggen_dir)
wf_len = 1000  # Based on output of siggen.

# Process runs.
for run_number in range(run_start, run_end):
    print(f"Processing run {run_number}...")
    filename = base_directory + base_filename.format(run_number)
    run_df = process_run_csv(filename, run_number, offset)

    for energy_range, folder_name in energy_ranges.items():
        filtered_run_df = run_df[(run_df['e_total'] >= energy_range[0]) & (run_df['e_total'] <= energy_range[1])]
        
        if filtered_run_df.empty:
            print(f"No events found for run {run_number} in the energy range {energy_range}.")
            continue
        
        output_dir = os.path.join(siggen_dir, "waveforms", folder_name)
        os.makedirs(output_dir, exist_ok=True)

        print(f"Processing {folder_name} for run {run_number}...")
        for event_id in filtered_run_df['event'].unique():
            # print(f"Processing event {event_id}...")
            event_hits = filtered_run_df[filtered_run_df['event'] == event_id]

            # Prepare stester commands.
            command_file_path = os.path.join(output_dir, f"my_stester_commands_event_{event_id}.txt")
            with open(command_file_path, "w") as f:
                f.write("cart \n")
                f.write("tau 0\n")
                f.write("dif 1\n")
                f.write("ccs 0.1\n")
                for index, hit in event_hits.iterrows():
                    waveform_filename = f"waveform_event{event_id}_hit{index}.spe"
                    waveform_path = os.path.join(output_dir, waveform_filename)
                    f.write(f"sig {hit['x_hit']:.2f} {hit['y_hit']:.2f} {hit['z_hit']:.2f} {waveform_path}\n")
                f.write("quit\n")

            # Run stester.
            stester_command = f"{stester_executable} {config_path} < {command_file_path}"
            subprocess.run(stester_command, shell=True, check=False, stdout=subprocess.DEVNULL)
            os.remove(command_file_path)  # Clean up command file.

            # Initialize variables for aggregation.
            aggregate_waveform = np.zeros(wf_len)  # Assuming wf_len samples per waveform.
            total_deposited_energy = 0  # Track the total deposited energy.

            # Process each waveform file.
            for index, hit in event_hits.iterrows():
                waveform_filename = f"waveform_event{event_id}_hit{index}.spe"
                waveform_path = os.path.join(output_dir, waveform_filename)
                edep = hit['edep']

                try:
                    with open(waveform_path, 'rb') as f:
                        head = f.read(36)  # Skip header.
                        yraw = f.read(wf_len*4)  # Read waveform data.
                        wf = np.array(struct.unpack('f'*wf_len, yraw))
                        aggregate_waveform += wf * edep
                        total_deposited_energy += edep
                    os.remove(waveform_path)  # Clean up waveform file.
                except Exception as e:
                    # print(f"Error processing file {waveform_path}: {e}")
                    continue

            # Compute the energy-weighted average waveform.
            if total_deposited_energy > 0:
                average_waveform = aggregate_waveform / total_deposited_energy
                average_waveform = np.nan_to_num(average_waveform)
                # Save the energy-weighted average waveform.
                average_waveform_filename = f"waveform_event_{event_id}_energy_{total_deposited_energy:.2f}.txt"
                average_waveform_path = os.path.join(output_dir, average_waveform_filename)
                np.savetxt(average_waveform_path, average_waveform)
                # print(f"Energy-weighted average waveform for event {event_id} saved.")
