import os, sys
import config
import shortcodes
import shutil

def Parameters():
	for argument in sys.argv:
		argument_split = argument.split("=")
		if argument_split[0] in "--url -u":
			config.url = argument_split[1]
			print("URL VALUE: "+config.url)
			continue
		if argument_split[0] in "--parse -p":
			config.parse_types = argument_split[1]
			print("PARSE TYPES VALUE: "+config.parse_types)
			continue
		if argument_split[0] in "--shortcodes -s":
			config.shortcode_location = argument_split[1]
			print("SHORTCODE LOCATION VALUE: "+config.shortcode_location)
			continue
		if argument_split[0] in "--output -o":
			config.output_location = argument_split[1]
			print("OUTPUT LOCATION VALUE: "+config.output_location)
			continue
		if argument_split[0] in "--template -t":
			config.template_location = argument_split[1]
			print("TEMPLATE LOCATION VALUE: "+config.template_location)
			continue
		if argument_split[0] in "--auto-purge -a":
			config.auto_purge = True
			print("AUTO PURGE VALUE: True")

def CheckOutput():
	if not os.path.isdir(config.output_location):
		os.mkdir(config.output_location)
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
			print("OVERWRITING INSTEAD.")
def MetaShorcodes(data):
	data = data.replace("[[URL]]",config.url+"/")
	return data

def LoadCodes(defs):
	defs_c = {}
	for name, location in defs.items():
		try:
			html = open(config.shortcode_location+"/"+location, 'r').read()
			html = MetaShorcodes(html)
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
			output_file = config.output_location+"/"+dirName+"/"+fname
			output_file = output_file.replace(config.template_location,"")#removes the template location from the output path
			parts = os.path.split(output_file)
			if not os.path.isdir(parts[0]):#makes sure we have a directory to write to
				os.mkdir(parts[0])
			print("Output: "+output_file)
			if(fname.split(".")[1].lower() in config.parse_types):
				test = open(dirName+"/"+fname, 'r').read()
				#meta-shortcodes
				test = MetaShorcodes(test)
				#end meta-shortcodes
				for name, data in prefabs.items():
					test = test.replace("{{"+name+"}}",data)
				file = open(output_file, 'w')
				file.write(test)
			else:
				print("NOT PARSING: "+fname)
				shutil.copyfile(dirName+"/"+fname, output_file)

def Start():
	Parameters()
	CheckOutput()
	defs = LoadCodes(shortcodes.defs)
	Build(config.template_location,defs)

Start()