# Batch RMS Normalizer

This is a simple Python script to batch process audio files by setting their RMS dBFS levels to a given target. This script may prove useful in situations where audio files volumes are too inconsistent and a general correction is required.

## Installation

Before using the script, make sure to install the required dependencies:

1. **Python 3.x:** If not already installed, you can download it from [python.org](https://www.python.org/downloads/).

2. **Pydub:** Install the Pydub library using the following command:

    ```bash
    pip install pydub
    ```

3. **ffmpeg:** Ensure ffmpeg is installed on your system. You can download it from [ffmpeg.org](https://ffmpeg.org/download.html), and make sure to add its directory to your system's PATH variable.

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the cloned repository directory.
3. Drag'n'drop audio files to the BASE folder.
4. Run the script using the command:

    ```bash
    python batch-rms-normalizer.py
    ```

5. Optionally, check BASE audio files levels and OUTPUT levels logged in the terminal.
6. Normalized audio files will be normalized to default value of -14dBFS.
7. Exported files can be found in OUTPUT folder, according to BASE file structure.

### Changing target dBFS level
1. Open the `batch-rms-normalizer.py` script in a text editor.
2. Set your desired Target dBFS Level in the variable `target_dBFS_level`.
3. Save the script.

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.
