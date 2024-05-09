import argparse
import logging
from batch_rms_logger import process_files as rms_logger
from batch_max_peak_logger import process_files as peak_logger

def setup_logging():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO  # Change to logging.DEBUG for more detailed output
    )

def main():
    """
    Perform audio analysis on files in a specified directory.
    """
    parser = argparse.ArgumentParser(description='Perform audio analysis on files in a specified directory.')
    parser.add_argument('-d', '--directory', default="./source_sounds", help='Directory containing audio files to analyze (default: ./source_sounds)')
    parser.add_argument('--min-rms', type=float, default=-20, help='Minimum RMS level for analysis (default: -20 dBFS)')
    parser.add_argument('--max-rms', type=float, default=-12, help='Maximum RMS level for analysis (default: -12 dBFS)')
    parser.add_argument('--max-peak', type=float, default=-3, help='Maximum True Peak level for analysis (default: -3 dBFS)')

    args = parser.parse_args()

    setup_logging()

    rms_range = {"min": args.min_rms, "max": args.max_rms}

    logging.info("Starting audio analysis")
    print("\n")

    logging.info("Performing True Peak analysis")
    peak_logger(args.directory, args.max_peak)
    print("\n")

    logging.info("Performing RMS analysis")
    rms_logger(args.directory, rms_range)
    print("\n")

    logging.info("Audio analysis completed")

if __name__ == "__main__":
    main()
