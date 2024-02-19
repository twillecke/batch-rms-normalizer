import os
from pydub import AudioSegment

def rms(file_address):
    try:
        sound_file = AudioSegment.from_file(file_address)
        source_rms = sound_file.dBFS
        return source_rms
    except Exception as e:
        print(f"Error processing {file_address}: {e}")
        return None, None

def process_files(directory):
    try:
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                file_address = os.path.join(root, filename)

                if filename.lower().endswith((".wav", ".mp3", ".ogg", ".flac")):
                    source_rms = rms(file_address)
                    if source_rms is not None:
                        print("{:<50} {:<30} Source RMS: {:.2f} dBFS".format(file_address, filename, source_rms))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = "./BASE"
    process_files(directory_path)
