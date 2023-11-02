import os
import shutil

VOICE_TYPE_MAPPING = {'A': 'alto', 'S': 'soprano', 'T': 'tenor', 'B': 'bass', 'M': 'mixture'}

def process_audio_files(source_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through the files in the 'Audio' folder
    mix_num = 1
    song_name_to_mix = {}
    audio_folder = os.path.join(source_folder, 'Audio')
    for filename in os.listdir(audio_folder):
        if filename.endswith('.wav'):
            if 'MixOrgan' in filename:
                continue

            # Extract song_name and voice_type
            parts = filename.split('_')
            song_name = parts[1]
            voice_type = VOICE_TYPE_MAPPING[parts[2][0]]

            # Create folder for this mix if it doesn't exist
            if song_name not in song_name_to_mix:
                song_name_to_mix[song_name] = mix_num
                mix_num += 1
            mix_folder = os.path.join(output_folder, f'mix{song_name_to_mix[song_name]}')
            if not os.path.exists(mix_folder):
                os.makedirs(mix_folder)

            # Copy the file to the appropriate folder in the output directory
            shutil.copy(os.path.join(audio_folder, filename), os.path.join(mix_folder, f'{voice_type}.wav'))


    print(f'Processed audio files from {source_folder} to {output_folder}')

# Example usage:
if __name__ == '__main__':
    process_audio_files('CantoriaDataset_v1.0.0', 'processed_cantoria_for_testing')
