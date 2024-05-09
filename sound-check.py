import argparse
from batch_rms_logger import process_files as rms_logger
from batch_max_peak_logger import process_files as peak_logger

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform audio analysis on files in a specified directory.')
    parser.add_argument('-d', '--directory', default="./source_sounds", help='Directory containing audio files to analyze')

    args = parser.parse_args()

    print("")
    print("==============================================")
    print("                  PEAK LOGGER                 ")
    print("==============================================")
    peak_logger(args.directory)
    print("==============================================")
    print('')
    print('')
    print("==============================================")
    print("                  RMS LOGGER                  ")
    print("==============================================")
    rms_logger(args.directory)
    print("==============================================")
