import os, sys
import config
import shortcodes
import shutil

def CheckOutput():
	if os.listdir(config.output_location) != []:
		if(config.auto_purge == True):
			purge = "y" 
		else:
			purge = input("OUTPUT DIRECTORY IS NOT EMPTY\nWOULD YOU LIKE TO PURGE THE OUTPUT DIRECTORY?\n[Yes/No]")
		if(purge.lower()[0]=="y"):
			print("PURGING!") 
			for dirName, subdirList, fileList in os.walk(config.output_location):
				for f in fileList:
					os.unlink(os.path.join(dirName, f))
				for d in subdirList:
					shutil.rmtree(os.path.join(dirName, d))
		else:
			print("OVERWERITING INSTEAD.")

def LoadCodes(defs):
	defs_c = {}
	for name, location in defs.items():
		try:
			html = open(config.short_code_location+"/"+location, 'r').read()
			defs_c.update({name:html})
		except FileNotFoundError:
			print("LOADING SHORT CODE FAILED!")
			print("The requested template file "+name+" does not exist at: "+location)
			input("Please check 'shortcodes.py' to make sure this file name and path are correct.")
			quit()
	return defs_c


def Build(rootDir,prefabs):
	print("Looking through "+rootDir)
	for dirName, subdirList, fileList in os.walk(rootDir):
		print('Found directory: %s' % dirName)
		for fname in fileList:
			print('\t%s' % fname)
			test = open(dirName+"/"+fname, 'r').read()
			for name, data in prefabs.items():
				test = test.replace("{{"+name+"}}",data )
			output_file = config.output_location+"/"+dirName+"/"+fname
			output_file = output_file.replace(config.template_location,"")#removes the template location from the output path
			parts = os.path.split(output_file)
			if not os.path.isdir(parts[0]):#makes sure we have a directory to write to
				os.mkdir(parts[0])
			print("Output: "+output_file+"\n\n")
			file = open(output_file, 'w')
			file.write(test)

CheckOutput()
defs = LoadCodes(shortcodes.defs)
Build(config.template_location,defs)