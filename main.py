import pikepdf
import os
import argparse

def argument_parser():
	parser = argparse.ArgumentParser(description = "Lock or unlock your PDF")
	config = parser.add_mutually_exclusive_group()
	config.add_argument("-f", "--file", help = "Use the configuration file", action = "store_true")
	config.add_argument("-c", "--command_line", help = "Configure the cript using the command line", action = "store_true")
	
	selection = parser.add_mutually_exclusive_group()
	selection.add_argument("-l", "--lock", help = "Lock your PDF(s) with password", action = "store_true")
	selection.add_argument("-u", "--unlock", help = "Unlock your PDF(s)", action = "store_true")
	args = parser.parse_args()
	return parser, args.lock, args.unlock, args.file, args.command_line
			
def read_configuration_file(file_name):
	file = open(file_name, "r")
	lines = file.readlines() 
	source_folder = lines[0].replace("\n", "")
	destination_folder = lines[1].replace("\n", "")
	password = lines[2].replace("\n", "")
	file.close()
	return source_folder, destination_folder, password
	
def create_destination_folder(destination_folder):
	try:
		os.mkdir(destination_folder)
		print("Directory", destination_folder, "created") 
	except FileExistsError:
		print("Directory", destination_folder, "already exists")
		
		
def unlock_PDf(source_folder, destination_folder, password):
	count = 0
	for item in os.scandir(source_folder):
		if ".pdf" in item.name:
			file_name = item.name
			mypdf = pikepdf.open(source_folder+"/"+file_name, password) # open the locked pdf in source folder

			mypdf.save(destination_folder+"/"+file_name) # save the unlocked pdf in destination folder
			
			print ("\t\"" + file_name + "\"" + " unlocked")
			count = count + 1
	return count 
	
def lock_PDf(source_folder, destination_folder, password):
	count = 0
	for item in os.scandir(source_folder):
		if ".pdf" in item.name:
			file_name = item.name
			mypdf = pikepdf.open(source_folder+"/"+file_name) # open the unlocked pdf in source folder

			mypdf.save(destination_folder+"/"+file_name, password) # save the locked pdf in destination folder
			
			print ("\t\"" + file_name + "\"" + " locked")
			count = count + 1
	return count 

def resume_operations(count):
	if (count < 2 and count != 0):
		print ("\tFile processed:", count)
	else:
		print ("\tFiles processed:", count)
		
def main():

	parser, lock, unlock, file, command_line = argument_parser()
		
	if file:
		# read configuration file
		source_folder, destination_folder, password = read_configuration_file(file_name = "config.txt")
	elif command_line:
		source_folder = input('Insert source folder name: ')
		destination_folder = input('Insert destination_folder folder name: ')
		password = input('Insert password: ')
	else:
		parser.print_help()

	# Create destination folder
	create_destination_folder(destination_folder)

	if unlock:
		# unlock all PDF(s) in source folder
		count = unlock_PDf(source_folder, destination_folder, password)
	elif lock:
		# lock all PDF(s) in source folder
		count = lock_PDf(source_folder, destination_folder, password)
	else:
		parser.print_help()
		
	resume_operations(count)

if __name__ == "__main__":
    main()