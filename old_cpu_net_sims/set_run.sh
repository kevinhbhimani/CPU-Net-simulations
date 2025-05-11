cd /nas/longleaf/home/kbhimani/cpu_net_sims/
run_vals=($(seq 0 1 100))
for run_iter in "${run_vals[@]}"
do
    echo $run_iter
    g4simple run.mac
    mv /work/users/k/b/kbhimani/cpu_net_g4sims/data/g4_out.hdf5 /work/users/k/b/kbhimani/cpu_net_g4sims/data/data_run_$run_iter.hdf5
    python hdf5PostProc/postprochdf5.py /pscratch/sd/k/kbhimani/cpu_net_data/cpu_net_data_1.hdf5
done
