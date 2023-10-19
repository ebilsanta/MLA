from pydub import AudioSegment
import soundfile as sf
import os
import itertools
import shutil

def convert_64_to_32_bit(input_file_path):
    # Load the 64-bit WAV file using soundfile
    
    audio_data, sample_rate = sf.read(input_file_path)

    shutil.os.remove(input_file_path)

    # Save as 32-bit WAV
    sf.write(input_file_path, audio_data, sample_rate, subtype='FLOAT')

def copy_non_wav_files(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through files in the input directory
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            # Check if the file is not a .wav file
            if file.endswith(".wav"):
                # Get the full path of the source and destination files
                source_file = os.path.join(root, file)
                destination_file = os.path.join(output_dir, file)

                # Copy the file to the output directory
                shutil.copy2(source_file, destination_file)

def group_audios(input_dir, output_dir):
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".wav"):
            # Parse file name to get song_name and voice_type
            if "CSD_LI_soprano" in file_name:
                convert_64_to_32_bit(os.path.join(input_dir, file_name))
            
            parts = file_name.split('_')
            song_name = parts[1]
            voice_type = parts[2]

            # Create directory structure if it doesn't exist
            song_dir = os.path.join(output_dir, song_name)
            voice_dir = os.path.join(song_dir, voice_type)

            if not os.path.exists(song_dir):
                os.makedirs(song_dir)
            if not os.path.exists(voice_dir):
                os.makedirs(voice_dir)

            # Get the full path of the source and destination files
            source_file = os.path.join(input_dir, file_name)
            destination_file = os.path.join(voice_dir, file_name)

            # Copy the file to the output directory
            shutil.copy2(source_file, destination_file)


def get_modified_filename(source_filename):
    output_mapping = {
        "bass": "bass",
        "tenor": "vocals",
        "alto": "drums",
        "soprano": "other"
    }
    parts = source_filename.split('/')
    voice_type = parts[-2]
    modified_name = output_mapping[voice_type] 
    return modified_name + ".wav"

def generate_train_test(input_dir, output_dir):
    source_folders = ['alto', 'tenor', 'bass', 'soprano']
    for song_folder in os.listdir(input_dir):
        song_path = os.path.join(input_dir, song_folder)

        if not os.path.isdir(song_path):
            continue

        # Generate all combinations of .wav files
        combinations = list(itertools.product(*[os.listdir(os.path.join(song_path, source_folder)) for source_folder in source_folders]))

        # Create a mix folder for each combination
        for idx, combination in enumerate(combinations, start=1):
            mix_folder = os.path.join(output_dir, f"mix{idx}")
            os.makedirs(mix_folder, exist_ok=True)

            # Combine the selected .wav files
            combined_audio = AudioSegment.silent(duration=0)  # Create an empty audio segment

            for source_folder, source_file in zip(source_folders, combination):
                source_file_path = os.path.join(song_path, source_folder, source_file)
                source_audio = AudioSegment.from_file(source_file_path)

                # Use the parameters of the first audio file for the combined file
                if source_folder == source_folders[0]:
                    combined_audio = source_audio

                else:
                    combined_audio = combined_audio.overlay(source_audio)

                # Copy individual .wav files
                modified_filename = get_modified_filename(source_file_path)
                shutil.copy(source_file_path, os.path.join(mix_folder, modified_filename))

            # Save the combined audio as mixture.wav
            combined_audio.export(os.path.join(mix_folder, 'mixture.wav'), format="wav")

def preprocess_csd_like_musdb(raw_csd_dir, output_dir):
    temp_dir = "./temp_dir"
    temp_dir_2 = "./temp_dir_2"
    print("-----------------copying non wav files to temporary folder-----------------")
    copy_non_wav_files(raw_csd_dir, temp_dir)
    print("-----------------grouping audio by song and voice type-----------------")
    group_audios(temp_dir, temp_dir_2)
    shutil.rmtree(temp_dir)
    print("-----------------generating train tests-----------------")
    generate_train_test(temp_dir_2, output_dir)
    shutil.rmtree(temp_dir_2)

if __name__ == "__main__":
    # path to raw csd dataset
    root_dir = "./ChoralSingingDataset"
    output_dir = "./processed_csd"
    preprocess_csd_like_musdb(root_dir, output_dir)
    
