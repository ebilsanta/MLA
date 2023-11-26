#!/bin/bash

#################################################
## TEMPLATE VERSION 1.01                       ##
#################################################
## ALL SBATCH COMMANDS WILL START WITH #SBATCH ##
## DO NOT REMOVE THE # SYMBOL                  ## 
#################################################

#SBATCH --nodes=1                   
#SBATCH --cpus-per-task=4           
#SBATCH --mem=16GB                  
#SBATCH --gres=gpu:1                
#SBATCH --time=24:00:00             
#SBATCH --mail-type=BEGIN,END,FAIL  
#SBATCH --output=%u.%j.out  

# Make sure you've replaced these with the appropriate values from 'myinfo':
#SBATCH --partition=project        
#SBATCH --account=is460  
#SBATCH --qos=is460qos     
#SBATCH --requeue

#SBATCH --mail-user=allynezhang.2021@scis.smu.edu.sg
#SBATCH --job-name=evalJukebox                

#################################################
##            END OF SBATCH COMMANDS           ##
#################################################

# Purge the environment, load the modules we require.
module purge
module load Anaconda3/2022.05

# Create a virtual environment can be commented off if you already have a virtual environment
# conda create -n myenvnamehere
# conda create --name unmix python=3.7.5

# Do not remove this line even if you have executed conda init
eval "$(conda shell.bash hook)"

# This command assumes that you've already created the environment previously
# We're using an absolute path here. You may use a relative path, as long as SRUN is execute in the same working directory
conda activate /common/home/projectgrps/IS460/IS460G10/miniconda3/envs/unmix

## Run commands on local machine to save time debugging
# activate unmix
# cd unmix
# conda install mpi4py=3.0.3
# conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c nvidia
# pip install -r ./requirements.txt
# pip install -e .
# conda install av=7.0.01 -c conda-forge
# pip install ./tensorboardX
# We do this below because protobuf fails to install straight. Replace with your path
# rm -r /common/home/projectgrps/IS460/IS460G10/miniconda3/envs/unmix/lib/python3.7/site-packages/protobuf* 
# pip install protobuf==3.20.0
# We do this thing below again bc somehow that's how the dependencies work out
# conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch -c nvidia 
# pip uninstall cffi soundfile
# pip install soundfile==0.10.3.post1
# conda install -c conda-forge libsndfile

# Find out which GPU you are using
srun whichgpu

# Run your command
# --id [channel id] --name [channel name] --vqvae [vqvae step] --encoder [encoder step] --freeze [Jukebox, if necessary]
srun python predict_channel.py --id 4 --name test_vqvae --vqvae 60001 
#--id 4
#--name bass
#sbatch predict_job.sh
#scancel <jobid>
#This typically takes ~5min