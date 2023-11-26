import numpy as np
import os
from scipy.io.wavfile import write

# Directory path TODO: Change accordingly
# Path of np files 
dir_path = '/common/home/projectgrps/IS460/IS460G10/jukebox/results_new_basswav/'

# Sample rate of 44100Hz for the output .wav file (adjust to original sample rate if different)
sample_rate = 44100

#TODO: Change accordingly
# Path of output wav file folders
output_folder = "/common/home/projectgrps/IS460/IS460G10/jukebox/results_new_basswav/results_wav/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through all files in the directory
for filename in os.listdir(dir_path):
    # Check if the file is a .npy file
    if filename.endswith('.npy'):
        # Load the data from .npy file
        input_file_path = os.path.join(dir_path, filename)
        data = np.load(input_file_path)

        # Construct the output filename by replacing .npy with .wav
        output_file_path = os.path.join(dir_path, 'results_wav', filename.replace('.npy', '.wav'))

        # Save as .wav file
        write(output_file_path, sample_rate, data)
        print(f"Converted {input_file_path} to {output_file_path}")

print("All .npy files have been converted to .wav!")
