import os
import itertools
import shutil
from scipy.io import wavfile
import numpy as np
from pydub import AudioSegment
from utils import copy_non_wav_files, group_audios

def get_modified_filename(source_filename):
    output_mapping = {
        "bass": "bass",
        "tenor": "tenor",
        "alto": "alto",
        "soprano": "soprano"
    }
    parts = source_filename.split('/') # need to change to '\\' for windows
    voice_type = parts[-2]
    modified_name = output_mapping[voice_type] 
    return modified_name + ".wav"

def mono_to_stereo(input_file, output_file):
    # Read the mono wav file
    sample_rate, mono_data = wavfile.read(input_file)

    # Create stereo data by duplicating the mono data to both channels
    stereo_data = np.column_stack((mono_data, mono_data))

    # Save the stereo wav file
    wavfile.write(output_file, sample_rate, stereo_data)

def generate_test(input_dir, output_dir):
    source_folders = ['alto', 'tenor', 'bass', 'soprano']
    test_folder = os.path.join(output_dir, "test")
    mixture_folder = os.path.join(test_folder, "mixture")
    mix_no = 1
    os.makedirs(test_folder, exist_ok=True)
    os.makedirs(mixture_folder, exist_ok=True)
    for song_folder in os.listdir(input_dir):
        song_path = os.path.join(input_dir, song_folder)

        if not os.path.isdir(song_path):
            continue

        combined_audio = AudioSegment.silent(duration=0) 
        for source_folder in source_folders:
            source_folder_path = os.path.join(song_path, source_folder)
            voice_files = os.listdir(source_folder_path)
            for source_file in voice_files:
                if "1" not in source_file:
                    continue
                source_file_path = os.path.join(source_folder_path, source_file)

                # Create a new folder for each voice type in the test folder
                voice_type_folder = os.path.join(test_folder, source_folder)
                os.makedirs(voice_type_folder, exist_ok=True)

                source_audio = AudioSegment.from_file(source_file_path)

                # Use the parameters of the first audio file for the combined file
                if source_folder == source_folders[0]:
                    combined_audio = source_audio

                else:
                    combined_audio = combined_audio.overlay(source_audio)

                # Copy the source track to the voice type folder
                shutil.copy2(source_file_path, os.path.join(voice_type_folder, source_file))
                os.remove(source_file_path)

        combined_audio.export(os.path.join(mixture_folder, f"mixture{mix_no}.wav"), format="wav")
        mix_no += 1


def generate_train(input_dir, output_dir):
    source_folders = ['alto', 'tenor', 'bass', 'soprano']
    train_folder = os.path.join(output_dir, "train")
    mixture_folder = os.path.join(train_folder, "mixture")
    os.makedirs(mixture_folder, exist_ok=True)
    mix_no = 1
    for song_folder in os.listdir(input_dir):
        song_path = os.path.join(input_dir, song_folder)

        if not os.path.isdir(song_path):
            continue

        # Generate all combinations of .wav files
        combinations = list(itertools.product(*[os.listdir(os.path.join(song_path, source_folder)) for source_folder in source_folders]))

        # Create a new folder for each voice type in the train folder
        for idx, combination in enumerate(combinations, start=1):
            combined_audio = AudioSegment.silent(duration=0)
            for source_folder, source_file in zip(source_folders, combination):
                source_file_path = os.path.join(song_path, source_folder, source_file)
                source_audio = AudioSegment.from_file(source_file_path)

                # Use the parameters of the first audio file for the combined file
                if source_folder == source_folders[0]:
                    combined_audio = source_audio

                else:
                    combined_audio = combined_audio.overlay(source_audio)

                # Copy individual .wav files
                voice_type_folder = os.path.join(train_folder, source_folder)
                os.makedirs(voice_type_folder, exist_ok=True)
                shutil.copy2(source_file_path, os.path.join(voice_type_folder, source_file))
        
            combined_audio.export(os.path.join(mixture_folder, f"mixture{mix_no}.wav"), format="wav")
            mix_no += 1


def preprocess_by_stem(input_dir, output_dir):
    print("**************** start generating test/train for csd ****************")
    temp_dir = "./csd_temp"
    temp_dir_2 = "./csd_temp_2"
    print("-----------------copying non wav files to temporary folder-----------------")
    copy_non_wav_files(input_dir, temp_dir)
    print("-----------------grouping audio by song and voice type-----------------")
    group_audios(temp_dir, temp_dir_2)
    print("-----------------generating test-----------------")
    generate_test(temp_dir_2, output_dir)
    print("-----------------generating train-----------------")
    generate_train(temp_dir_2, output_dir)
    shutil.rmtree(temp_dir_2)
    shutil.rmtree(temp_dir)


if __name__ == "__main__":
    # path to raw csd dataset
    root_dir = "ChoralSingingDataset"
    output_dir = "processed_csd_jukebox"
    preprocess_by_stem(root_dir, output_dir)
    
