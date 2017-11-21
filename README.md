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
~$ python duplicates.py d:\arduino
Duplicates file: d:\arduino\libraries\ds3231-master\Makefile, d:\arduino\libraries\ds3231-master\examples\rtc_ds3231_alarm\Makefile
Duplicates file: d:\arduino\libraries\LCDMenuLib\examples\LCDML_000_serialmonitor\LCDML_CONTROL.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_001_lcd_liquidcrystal\LCDML_CONTROL.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_100_initscreen\LCDML_CONTROL.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_101_menu_with_parameter\LCDML_CONTROL.ino
, d:\arduino\libraries\LCDMenuLib\examples\LCDML_102_dynamic_menu\LCDML_CONTROL.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_103_hidden_menu_elemnts\LCDML_CONTROL.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_104_change_value\LCDML_CONTROL.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_200_backend_basics\LCDML_CONTROL.ino
Duplicates file: d:\arduino\libraries\LCDMenuLib\examples\LCDML_000_serialmonitor\LCDML_FUNC_BACKEND.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_001_lcd_liquidcrystal\LCDML_FUNC_BACKEND.ino
Duplicates file: d:\arduino\libraries\LCDMenuLib\examples\LCDML_001_lcd_liquidcrystal\LCDML_DISP.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_100_initscreen\LCDML_DISP.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_101_menu_with_parameter\LCDML_DISP.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_102_dynamic_menu\LCDML_DISP.ino, d:\arduino\
libraries\LCDMenuLib\examples\LCDML_103_hidden_menu_elemnts\LCDML_DISP.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_104_change_value\LCDML_DISP.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_200_backend_basics\LCDML_DISP.ino
Duplicates file: d:\arduino\libraries\LCDMenuLib\examples\LCDML_001_lcd_liquidcrystal\LCDML_FUNC_DISP.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_002_lcd_i2c\LCDML_FUNC_DISP.ino
Duplicates file: d:\arduino\libraries\LCDMenuLib\examples\LCDML_002_lcd_i2c\LCDML_CONTROL.ino, d:\arduino\libraries\LCDMenuLib\examples\LCDML_003_glcd_u8glib\LCDML_CONTROL.ino
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
