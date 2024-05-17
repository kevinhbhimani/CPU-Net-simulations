#!/bin/bash
#
# Perlmutter cluster job slurm submission script            
# execute as:                                           
# check job detail: jobstats or scontrol show job <JobID>  or squeue --job 37985561  <JobID> or sqs                 
#--------------------------------------------------------------------------      
#            
#SBATCH --job-name=khb-ornl-simulate
#                                                                                             
# directories to put log files ... so you know what is happening to your jobs   
#                                                                  
#SBATCH --output=/nas/longleaf/home/kbhimani/ornl_sims/logs/job_log_.sh.o%j       
#SBATCH --error=/nas/longleaf/home/kbhimani/ornl_sims/logs/job_error_log_.sh.o%j     
#SBATCH --qos=regular
#SBATCH --time=5-00:00:00
#SBATCH --mem=128GB
# uncomment the lines below to get email notification about your job                       
#SBATCH --mail-type=begin,end,fail
#SBATCH --mail-user=kevin_bhimani@unc.edu
#---------------------------------------------------------------------------   
#!/bin/bash
python /nas/longleaf/home/kbhimani/ornl_sims/simulate.py