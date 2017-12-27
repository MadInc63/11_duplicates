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
~$ python duplicates.py d:\backup
------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Сайт 24.08.2015\index.html
 duplicate: d:\backup\07.09.2015\Документы\Сайт 25.08.2015\index.html
 duplicate: d:\backup\07.09.2015\Документы\Сайт 25.08.2015 без изменений\index.html
 duplicate: d:\backup\07.09.2015\Документы\Сайт Old Server 31.08.2015\index.html
------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Сайт 24.08.2015\new_about_eng.css
 duplicate: d:\backup\07.09.2015\Документы\Сайт 25.08.2015 без изменений\new_about_eng.css
 duplicate: d:\backup\07.09.2015\Документы\Сайт Old Server 31.08.2015\new_about_eng.css
------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Сайт 24.08.2015\new_development_eng.css
 duplicate: d:\backup\07.09.2015\Документы\Сайт 25.08.2015 без изменений\new_development_eng.css
 duplicate: d:\backup\07.09.2015\Документы\Сайт Old Server 31.08.2015\new_development_eng.css
------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Сайт 24.08.2015\new_development_eng.html
 duplicate: d:\backup\07.09.2015\Документы\Сайт 25.08.2015 без изменений\new_development_eng.html
 duplicate: d:\backup\07.09.2015\Документы\Сайт Old Server 31.08.2015\new_development_eng.html
------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Сайт 24.08.2015\documents\_notes\dwsync.xml
 duplicate: d:\backup\07.09.2015\Документы\Сайт 25.08.2015\documents\_notes\dwsync.xml
 duplicate: d:\backup\07.09.2015\Документы\Сайт 25.08.2015 без изменений\documents\_notes\dwsync.xml
 duplicate: d:\backup\07.09.2015\Документы\Сайт New AllinOne 31.08.2015\documents\_notes\dwsync.xml
------------------------------------------------------------------------------------------------------------------
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
