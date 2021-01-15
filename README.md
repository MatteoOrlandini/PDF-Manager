# PDF manager to lock or unlock your PDFs

This [python program](https://github.com/MatteoOrlandini/PDF-Manager/blob/master/main.py) allows the user to unlock or lock several PDFs in one click. It uses a [configuration file](https://github.com/MatteoOrlandini/PDF-Manager/blob/master/config.txt) to set where the original PDFs are, where the locked/unlocked PDFs will be saved and the password. This program reads the `config.txt` file or uses the command line configuration. In the `config.txt` file is used, the first line of `config.txt` is the name of the source folder where the original PDFs are, the second line is the name of the destination folder where the locked/unlocked PDFs will be saved and the third line is the password. The default names are "Original PDF", "Modified PDF" and "password". Next, a folder named "Modified PDF" will be created if it doesn't already exist. Finally, the program prints out the number of PDF unlocked.

# Getting Started
## Prerequisites

* [Python](https://www.python.org/) 
* [Pikepdf library](https://pypi.org/project/pikepdf/)
* [Os library](https://docs.python.org/3/library/os.html)
* [Argparse](https://docs.python.org/3/library/argparse.html)

### Install pikepdf

Open a command window and type `pip install pikepdf`

### Edit the configuration file

Open `config.txt` file and change the lines using a text editor. The first line is the name of the source folder where the original PDFs are, by default is "Original PDF". The second line is the name of the destination folder where the locked/unlocked PDFs will be saved, by default is "Modified PDF". The third line is the password, by default is "password".

### Prepare the files

Create a new folder called "Original PDF" or with the same name as the first line of the file `config.txt` and copy the PDF files you want to lock/unlock.

# Usage
```python .\main.py -h
usage: main.py [-h] [-f | -c] [-l | -u]

Lock or unlock your PDF

optional arguments:
  -h, --help          show this help message and exit
  -f, --file          Use the configuration file
  -c, --command_line  Configure the cript using the command line
  -l, --lock          Lock your PDF(s) with password
  -u, --unlock        Unlock your PDF(s)
```

You can either use the configuration file `config.txt` (using argument `-f` or `--file`) or the command line option (using argument `-c` or `--command_line`), moreover you can lock your PDF(s) (using argument `-l` or `--lock`) or unlock your PDF(s) (using argument `-u` or `--unlock`).

## Example

* If you want to use the configuration file `config.txt` and lock your PDF(s), open the Command Prompt as Administrator and type `python .\main.py -f -l`.

* If you want to use the configuration file `config.txt` and unlock your PDF(s), open the Command Prompt and type `python .\main.py -f -u`.

* If you want to use the command line and lock your PDF(s), open the Command Prompt as Administrator and type `python .\main.py -c -l`. Next, the command window will show you 
```
Insert source folder name:
Insert destination folder folder name:
Insert password:
```

* If you want to use the command line and unlock your PDF(s), open the Command Prompt and type `python .\main.py -c -u`. Next, the command window will show you 
```
Insert source folder name:
Insert destination folder folder name:
Insert password:
```