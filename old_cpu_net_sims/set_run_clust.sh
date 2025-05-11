cd /global/homes/k/kbhimani/cpu_net_sims

# echo "Running test cluster"
# python3 post_proc_cluster.py /pscratch/sd/k/kbhimani/cpu_net_data/cpu_net_data_test.hdf5 0

# echo "Running cluster 1"
# python3 post_proc_cluster.py /pscratch/sd/k/kbhimani/cpu_net_data/cpu_net_data_1.hdf5 1
# echo "Finish running cluster 1"

echo "Running cluster 2"
python3 post_proc_cluster.py /pscratch/sd/k/kbhimani/cpu_net_data/cpu_net_data_2.hdf5 2
echo "Finish running cluster 2"

echo "Running cluster 3"
python3 post_proc_cluster.py /pscratch/sd/k/kbhimani/cpu_net_data/cpu_net_data_3.hdf5 3
echo "Finish running cluster 3"

cd /global/homes/k/kbhimani/cpu_net_sims/WFSimulation/icpc_siggen/
make clean
make
python3 /global/homes/k/kbhimani/cpu_net_sims/siggen_run.py
