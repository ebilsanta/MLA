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

#SBATCH --mail-user=weilun.teo.2021@scis.smu.edu.sg
#SBATCH --job-name=unmixJob                

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

# Uncomment these if you're running for the first time or if packages have changed.
# conda install mpi4py=3.0.3
# conda install pytorch=1.4 cudatoolkit=10.0 -c pytorch
## UNINSTALL + REINSTALL PROTOBUFF????
# pip install torchvision==0.5
# pip install -r ./requirements.txt
# pip install -e .
# conda install av=7.0.01 -c conda-forge
# pip install ./tensorboardX

##pip uninstall cffi soundfile
##pip install soundfile==0.10.3.post1
# conda install -c conda-forge libsndfile

# Find out which GPU you are using
srun whichgpu

# Run your command
srun python unmix_encoder/train.py --hps=vqvae --name=encoder_bass_b6 --sr=44100 --sample_length=393216 --bs=6 --audio_files_dir="unmix/data/mixture" --labels=False --train --aug_shift --aug_blend --encoder=True --channel=_1 --restore_vqvae="/common/home/projectgrps/IS460/IS460G10/jukebox/logs/vqvae_bass_b6/checkpoint_step_60001.pth.tar"
