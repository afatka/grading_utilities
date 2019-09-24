# Sel2Clip.py
# Created by Adam Fatka adam.fatka@gmail.com

# script captures the selection in Maya and copies the string to the clipboard. 

import maya.cmds as cmds
try:
	import pyperclip
except:
	try:
		import sys
		sys.path.append('/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')
		import pyperclip
	except:
		cmds.error('pyerpclip not installed. Please install pyperclip')

def sel2clip( long_form = False):
	selection = cmds.ls(selection = True, long = long_form, transforms = True)
	print(selection)
	if len(selection) < 1:
		cmds.error('No selection detected, don\'t be dumb...')
	elif len(selection) == 1:
		pyperclip.copy(selection[0])
	else:
		to_clipboard = "{}, and {}".format(', '.join(selection[:-1]), selection[-1])
		# print(to_clipboard)
		pyperclip.copy(to_clipboard)

	print('Selection Copied To Clipboard')
