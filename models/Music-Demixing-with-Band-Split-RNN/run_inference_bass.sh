#!/bin/bash

#################################################
## TEMPLATE VERSION 1.01                       ##
#################################################
## ALL SBATCH COMMANDS WILL START WITH #SBATCH ##
## DO NOT REMOVE THE # SYMBOL                  ## 
#################################################

#SBATCH --nodes=1                   # How many nodes required? Usually 1
#SBATCH --cpus-per-task=12           # Number of CPU to request for the job
#SBATCH --mem=16GB                   # How much memory does your job require?
#SBATCH --gres=gpu:1                # Do you require GPUS? If not delete this line
#SBATCH --time=01-00:00:00          # How long to run the job for? Jobs exceed this time will be terminated
                                    # Format <DD-HH:MM:SS> eg. 5 days 05-00:00:00
                                    # Format <DD-HH:MM:SS> eg. 24 hours 1-00:00:00 or 24:00:00
#SBATCH --mail-type=BEGIN,END,FAIL  # When should you receive an email?
#SBATCH --output=/common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/smu_sbatch_job_logs/inference_job_logs/%u.%j.out          # Where should the log files go?
                                    # You must provide an absolute path eg /common/home/module/username/
                                    # If no paths are provided, the output file will be placed in your current working directory

################################################################
## EDIT AFTER THIS LINE IF YOU ARE OKAY WITH DEFAULT SETTINGS ##
################################################################

#SBATCH --partition=project                 # The partition you've been assigned
#SBATCH --account=is460   # The account you've been assigned (normally student)
#SBATCH --qos=is460qos       # What is the QOS assigned to you? Check with myinfo command
#SBATCH --mail-user=kevano.2020@business.smu.edu.sg # Who should receive the email notifications
#SBATCH --job-name=bsrnnInferBassTrainedProductionData     # Give the job a name

#################################################
##            END OF SBATCH COMMANDS           ##
#################################################

# Purge the environment, load the modules we require.
# Refer to https://violet.smu.edu.sg/origami/module/ for more information
module purge
module load Python/3.10.12

# Create a virtual environment
# python3 -m venv ~/myenv

# This command assumes that you've already created the environment previously
# We're using an absolute path here. You may use a relative path, as long as SRUN is executed in the same working directory
# source ~/myenv/bin/activate
source /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/venv-BSRNN-3.10/bin/activate
cd /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/src

# If you require any packages, install it as usual before the srun job submission.
# pip install -r /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/src/requirements.txt
# conda install -c conda-forge ffmpeg

# Set ENV Variables
export CUDA_VISIBLE_DEVICES=0
export WANDB_API_KEY="efec9d4452e32a791be2b6c0c7a59bb74c66f9ee"
export MUSDB_DIR="/common/scratch/projectgrps/IS460/IS460G4/datasets/combined_processed_dataset_converted_stereo"

# Find out which GPU you are using
srun whichgpu

# Submit your job to the cluster
# for cantoria
srun --gres=gpu:1 python3 inference.py -i /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_inference_output/cantoria_mix1.wav -o /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_inference_output/inference_production_csd_esmuc/ -t bass -c /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_saved_models/trained_on_production_csd_esmuc/bass/weights/epoch49-train_loss0.35.ckpt -d cuda
srun --gres=gpu:1 python3 inference.py -i /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_inference_output/cantoria_mix2.wav -o /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_inference_output/inference_production_csd_esmuc/ -t bass -c /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_saved_models/trained_on_production_csd_esmuc/bass/weights/epoch49-train_loss0.35.ckpt -d cuda
# for csd_esmuc
srun --gres=gpu:1 python3 inference.py -i /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_inference_output/csd_esmuc_mix1.wav -o /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_inference_output/inference_production_csd_esmuc/ -t bass -c /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_saved_models/trained_on_production_csd_esmuc/bass/weights/epoch49-train_loss0.35.ckpt -d cuda
srun --gres=gpu:1 python3 inference.py -i /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_inference_output/csd_esmuc_mix2.wav -o /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_inference_output/inference_production_csd_esmuc/ -t bass -c /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/bsrnn_saved_models/trained_on_production_csd_esmuc/bass/weights/epoch49-train_loss0.35.ckpt -d cuda

# CODES TO WRITE INTO UR TERMINAL
# chmod +x /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/run_inference_bass.sh
# sbatch /common/home/projectgrps/IS460/IS460G4/Music-Demixing-with-Band-Split-RNN/run_inference_bass.sh