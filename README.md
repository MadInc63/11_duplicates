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
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Заявка на предоставление информационных сервисов.doc
 duplicate: d:\backup\07.09.2015\Документы\Регламент\Заявка на предоставление информационных сервисов.doc
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Резюме.docx
 duplicate: d:\backup\07.09.2015\Документы\ЗКС\Резюме.docx
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Apex site design\.DS_Store
 duplicate: d:\backup\07.09.2015\Рабочий стол\Apex site design\.DS_Store
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Apex site design\Apex-Site-51.jpg
 duplicate: d:\backup\07.09.2015\Рабочий стол\Apex site design\Apex-Site-51.jpg
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Apex site design\Apex-Site-52.jpg
 duplicate: d:\backup\07.09.2015\Рабочий стол\Apex site design\Apex-Site-52.jpg
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Apex site design\Apex-Site-53.jpg
 duplicate: d:\backup\07.09.2015\Рабочий стол\Apex site design\Apex-Site-53.jpg
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Apex site design\Apex-Site-54.jpg
 duplicate: d:\backup\07.09.2015\Рабочий стол\Apex site design\Apex-Site-54.jpg
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Apex site design\Apex-Site-55-Mouse-Over.jpg
 duplicate: d:\backup\07.09.2015\Рабочий стол\Apex site design\Apex-Site-55-Mouse-Over.jpg
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Apex site design\Apex-Site-55.jpg
 duplicate: d:\backup\07.09.2015\Рабочий стол\Apex site design\Apex-Site-55.jpg
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Apex site design\Apex-Site-56.jpg
 duplicate: d:\backup\07.09.2015\Рабочий стол\Apex site design\Apex-Site-56.jpg
------------------------------------------------------------------------------------------------------------------------
 File:      d:\backup\07.09.2015\Документы\Apex site design\INDD\Apex-Site-5.indd
 duplicate: d:\backup\07.09.2015\Рабочий стол\Apex site design\INDD\Apex-Site-5.indd
------------------------------------------------------------------------------------------------------------------------
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
