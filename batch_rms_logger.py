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

def process_files(directory: str, rms_range: dict = {"min": -20, "max": -12}):
    try:
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                file_address = os.path.join(root, filename)

                if filename.lower().endswith((".wav", ".mp3", ".ogg", ".flac")):
                    source_rms = rms(file_address)
                    if source_rms is not None:
                        check_str = "  ✓" if rms_range["min"] <= source_rms <= rms_range["max"] else f'  ✕  (FAILED: RMS should be in between {rms_range["min"]} and {rms_range["max"]})'
                        print("{:<70}  Source RMS: {:.2f} dBFS".format(file_address,source_rms) + check_str)                        
    except Exception as e:
        print(f"Error: {e}")
