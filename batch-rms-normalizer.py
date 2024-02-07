import os
from pydub import AudioSegment

def match_target_amplitude(sound, target_dBFS_level):
    change_in_dBFS = target_dBFS_level - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

def normalize_audio(file_address, filename, directory, output_directory, target_dBFS_level):
    try:
        sound_file = AudioSegment.from_file(file_address)
        normalized_sound = match_target_amplitude(sound_file, target_dBFS_level)
         
        relative_path = os.path.relpath(file_address, directory)
        output_file_path = os.path.join(output_directory, f"{relative_path}")
                        
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        normalized_sound.export(output_file_path, format=os.path.splitext(filename)[-1][1:])

        source_rms = sound_file.dBFS
        output_rms = normalized_sound.dBFS

        return source_rms, output_rms
    except Exception as e:
        print(f"Error processing {file_address}: {e}")
        return None, None

def process_files(directory, output_directory, target_dBFS_level):
    try:
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                file_address = os.path.join(root, filename)

                if filename.lower().endswith((".wav", ".mp3", ".ogg", ".flac")):
                    source_rms, output_rms = normalize_audio(file_address, filename, directory, output_directory, target_dBFS_level)
                    if source_rms is not None and output_rms is not None:
                        print("{:<50} {:<30} Source RMS: {:.2f} dBFS  -->  Output RMS: {:.2f} dBFS".format(file_address, filename, source_rms, output_rms))
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = "./BASE"
    output_path = "./OUTPUT"
    target_dBFS_level = -14
    process_files(directory_path, output_path, target_dBFS_level)
