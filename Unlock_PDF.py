import pikepdf
import os

# read configuration file
file = open("config.txt", "r")
lines = file.readlines() 
source_folder = lines[0].replace("\n", "")
destination_folder = lines[1].replace("\n", "")
password = lines[2].replace("\n", "")
file.close()

count = 0

# Create destination folder
try:
	os.mkdir(destination_folder)
	print("Directory ", destination_folder, " created") 
except FileExistsError:
	print("Directory ", destination_folder, " already exists")

# read all the files in source folder
for item in os.scandir(source_folder):
	if ".pdf" in item.name:
		file_name = item.name
		mypdf = pikepdf.open(source_folder+file_name, password) # open the locked pdf in source folder

		mypdf.save(destination_folder+file_name) # save the unlocked pdf in destination folder
		
		print ("\t\"" + file_name + "\"" + " unlocked")
		count = count + 1
		
if (count < 2):
	print ("\tFile unlocked:", count)
else:
	print ("\tFiles unlocked:", count)
