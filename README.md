# Sound Requirements Utils

This is a simple Python script to batch process audio files by setting their RMS dBFS levels to a given target. This script may prove useful in situations where audio files volumes are too inconsistent and a general correction is required.

## Installation

Before using the script, make sure to install the required dependencies:

1. **Python 3.x:** If not already installed, you can download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository to your local machine.

4. **Pydub:** Install the Pydub library using the following command:

    ```bash
    pip install pydub
    ```

4. **ffmpeg:** Ensure ffmpeg is installed on your system. You can download it from [ffmpeg.org](https://ffmpeg.org/download.html), and make sure to add its directory to your system's PATH variable.

## RMS and True Peak logger 
1. Run the script from the command line with the following options:
    ```py
    python sound_check.py [-h] [-d DIRECTORY] [--min-rms MIN_RMS] [--max-rms MAX_RMS] [--max-peak MAX_PEAK]
    ```
2. Navigate to the cloned repository directory.
3. Run the script using the command:

    ```bash
    python sound-check.py
    ```

    - `-h, --help`: Show the help message and exit.
    - `-d DIRECTORY, --directory DIRECTORY`: Specify the directory containing the audio files to analyze (default: ./source_sounds).
    - `--min-rms MIN_RMS`: Set the minimum RMS level for analysis (default: -20 dBFS).
    - `--max-rms MAX_RMS`: Set the maximum RMS level for analysis (default: -12 dBFS).
    - `--max-peak MAX_PEAK`: Set the maximum True Peak level for analysis (default: -3 dBFS).

### Changing audio files RMS levels
 1. Run the script using the following command:

    ```bash
    python normalize_audio.py [-d DIRECTORY] [-o OUTPUT_DIRECTORY] [-t TARGET_DBFS_LEVEL]
    ```

    - `-t, --target-dBFS-level`: (Optional) Target dBFS level for normalization. Default is `-14`.
    - `-d, --directory`: (Optional) Path to the directory containing audio files to normalize. Default is `./BASE`.
    - `-o, --output-directory`: (Optional) Path to the directory to save normalized audio files. Default is `./output`.

2. After running the script, normalized audio files will be saved in the default or specified output directory.

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.
