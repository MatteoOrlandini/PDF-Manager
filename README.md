# PDF unlocker for protected PDF

This [python program](https://github.com/MatteoOrlandini/PDF-Unlocker/blob/master/Unlock_PDF.py) allows the user to unlock several PDFs in one click. It uses a [configuration file](https://github.com/MatteoOrlandini/PDF-Unlocker/blob/master/config.txt) to set where the locked PDFs are, where the unlocked PDFs will be saved and the password. This program reads the config.txt file, the first line is the name of the source folder where the locked PDFs are, the second line is the name of the destination folder where the unlocked PDFs will be saved and the third line is the password. The default names are "PDF", "PDF UNLOCKED" and "password". Next, a folder named "PDF UNLOCKED" will be created if it doesn't already exist. The PDF are now opened using the password and saved in "PDF UNLOCKED" folder. Finally, the program prints out the number of PDF unlocked.

# Prereqs
* [Python](https://www.python.org/) 
* [Pikepdf library](https://pypi.org/project/pikepdf/)
* [Os library](https://docs.python.org/3/library/os.html)

# How to run 
1. Install pikepdf

Open a command window and type `pip install pikepdf`

2. Edit the configuration file

Open "config.txt" file and change the lines using a text editor. The first line is the name of the source folder where the locked PDFs are, by default is "PDF". The second line is the name of the destination folder where the unlocked PDFs will be saved, by default is "PDF UNLOCKED". The third line is the password, by default is "password".

3. Prepare the files

Create a new folder called "PDF" or with the same name as the first line of the file "config.txt" and copy the PDF files you want to unlock.

4. Run

Open a command window and type `python Unlock_PDF.py`
