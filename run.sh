cd /nas/longleaf/home/kbhimani/ornl_sims/
run_vals=($(seq 21 1 100))
for run_iter in "${run_vals[@]}"
do
    echo "Running simulation for run $run_iter"
    # time g4simple ornl_run.mac 1> /dev/null
    /nas/longleaf/home/kbhimani/ornl_sims/g4simple/install/bin/g4simple ornl_run.mac 1> /dev/null
    echo "Finished simulation for run $run_iter"
    # mv /work/users/k/b/kbhimani/cpu_net_g4sims/data_ornl/g4_out.hdf5 /work/users/k/b/kbhimani/cpu_net_g4sims/data_ornl/data_run_$run_iter.hdf5
    mv /work/users/k/b/kbhimani/cpu_net_g4sims/data_ornl/g4_out_nt_g4sntuple.csv /work/users/k/b/kbhimani/cpu_net_g4sims/data_ornl/data_run_$run_iter.csv
    # python hdf5PostProc/postprochdf5.py /pscratch/sd/k/kbhimani/cpu_net_data/cpu_net_data_1.hdf5
done
