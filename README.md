# Anti-Duplicator
The script searches for duplicate files in the specified folder.
# How to use
The script requires the installed Python interpreter version 3.5
To call the help, run the script with the -h or --help option.
```bash
~$ python duplicates.py -h
usage: duplicates.py [-h] folder_path

positional arguments:
  folder_path  folder to find duplicates

optional arguments:
  -h, --help   show this help message and exit
```
To start searching for duplicate files in a folder, you must specify the path to the folder using the space after the script is called.
```bash
~$ python duplicates.py C:\devman
------------------------------------------------------------------------------------------------------------------------
File "description" has duplicate:
C:\devman\.git\description
C:\devman\10_coursera\.git\description
C:\devman\11_duplicates\.git\description
C:\devman\12_image_resize\.git\description
C:\devman\14_pre_commit_hook\.git\description
C:\devman\15_midnighters\.git\description
C:\devman\17_sites_monitoring\.git\description
C:\devman\3_bars\.git\description
C:\devman\5_lang_frequency\.git\description
------------------------------------------------------------------------------------------------------------------------
File "HEAD" has duplicate:
C:\devman\.git\HEAD
C:\devman\10_coursera\.git\HEAD
C:\devman\11_duplicates\.git\HEAD
C:\devman\12_image_resize\.git\HEAD
C:\devman\14_pre_commit_hook\.git\HEAD
C:\devman\15_midnighters\.git\HEAD
C:\devman\17_sites_monitoring\.git\HEAD
C:\devman\3_bars\.git\HEAD
C:\devman\5_lang_frequency\.git\HEAD
------------------------------------------------------------------------------------------------------------------------
File "applypatch-msg.sample" has duplicate:
C:\devman\.git\hooks\applypatch-msg.sample
C:\devman\10_coursera\.git\hooks\applypatch-msg.sample
C:\devman\11_duplicates\.git\hooks\applypatch-msg.sample
C:\devman\12_image_resize\.git\hooks\applypatch-msg.sample
C:\devman\14_pre_commit_hook\.git\hooks\applypatch-msg.sample
C:\devman\15_midnighters\.git\hooks\applypatch-msg.sample
C:\devman\17_sites_monitoring\.git\hooks\applypatch-msg.sample
C:\devman\3_bars\.git\hooks\applypatch-msg.sample
C:\devman\5_lang_frequency\.git\hooks\applypatch-msg.sample
------------------------------------------------------------------------------------------------------------------------
File "commit-msg.sample" has duplicate:
C:\devman\.git\hooks\commit-msg.sample
C:\devman\10_coursera\.git\hooks\commit-msg.sample
C:\devman\11_duplicates\.git\hooks\commit-msg.sample
C:\devman\12_image_resize\.git\hooks\commit-msg.sample
C:\devman\14_pre_commit_hook\.git\hooks\commit-msg.sample
C:\devman\15_midnighters\.git\hooks\commit-msg.sample
C:\devman\17_sites_monitoring\.git\hooks\commit-msg.sample
C:\devman\3_bars\.git\hooks\commit-msg.sample
C:\devman\5_lang_frequency\.git\hooks\commit-msg.sample
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
