from batch_rms_logger import process_files as rms_logger
from batch_max_peak_logger import process_files as peak_logger


directory_path = "./BASE"

print("")
print("================ RMS LOGGER ==================")
print('')
peak_logger(directory_path)
print('')
print("================ PEAK LOGGER =================")
print('')
rms_logger(directory_path);
print('')
