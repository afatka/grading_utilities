#! usr/bin/env python
#A.K.A. The Combiner
#This script takes a folder, creates a new folder in the same directory with '_combined' appended. 
#It then walks the source directory and combines all Maya files in the same folder into a single Maya file
#saving that new file into the '_combined' directory. 

import maya.cmds as cmds
import os

def build_3DF_assets():
	ext_of_interest = ('.ma', '.mb')
	log('build 3DF assets running')
	source_dir, source_name = os.path.split(cmds.fileDialog2(fileMode = 3)[0])
	log('dir: {}'.format(source_dir))
	log('source_name: {}'.format(source_name))
	target_name = source_name + '_combined'
	log('Target: {}'.format(target_name))
	if not os.path.exists(os.path.join(source_dir, target_name)):
		os.makedirs(os.path.join(source_dir, target_name))
	log('Source: {}'.format(source_name))

	for folder, subfolders, filenames in os.walk(os.path.join(source_dir, source_name)):
		files_for_import = []
		# log('folder: {}'.format(folder))
		# log('subfolders: \n{}'.format(subfolders))
		#log('filenames: \n{}'.format(filenames))
		for f in filenames: 
			if f.endswith(ext_of_interest):
				files_for_import.append(f)
		if files_for_import:
			log('folder: {}'.format(folder))
			log('{}'.format(os.path.split(folder))) 
			log('Importing files \n{}'.format(files_for_import))

			# parent_folder = os.path.split(os.path.split(folder)[0])[1]
			parent_folder = os.path.split(folder)[1]
			log('Parent: {}'.format(parent_folder))
			if not os.path.exists(os.path.join(source_dir, target_name, parent_folder)):
				os.makedirs(os.path.join(source_dir, target_name, parent_folder))
			cmds.file(newFile = True, force = True)
			for import_file in files_for_import:
				cmds.file(os.path.join(folder, import_file), i = True, groupReference = True, groupName = import_file, namespace = import_file.rsplit('_', 2)[0])
			cmds.file(rename = os.path.join(source_dir, target_name, parent_folder, parent_folder))
			cmds.file( save = True)
	cmds.file(newFile = True, force = True)




def log(message, dev = True):
	if dev:
		print(message)
