import os, sys
import config
import shortcodes
import shutil
import strings

def Parameters():
	for argument in sys.argv:
		argument_split = argument.split("=")
		if argument_split[0] in "--url -u":
			config.url = argument_split[1]
			print(strings.arg_read["url"]+config.url)
			continue
		if argument_split[0] in "--parse -p":
			config.parse_types = argument_split[1]
			print(strings.arg_read["parse"]+config.parse_types)
			continue
		if argument_split[0] in "--shortcodes -s":
			config.shortcode_location = argument_split[1]
			print(strings.arg_read["shortcode"]+config.shortcode_location)
			continue
		if argument_split[0] in "--output -o":
			config.output_location = argument_split[1]
			print(strings.arg_read["output"]+config.output_location)
			continue
		if argument_split[0] in "--template -t":
			config.template_location = argument_split[1]
			print(strings.arg_read["template"]+config.template_location)
			continue
		if argument_split[0] in "--auto-purge -a":
			config.auto_purge = True
			print(strings.arg_read["purge"])

def CheckOutput():
	if not os.path.isdir(config.output_location):
		os.mkdir(config.output_location)
	if os.listdir(config.output_location) != []:
		if(config.auto_purge == True):
			purge = "y" 
		else:
			purge = input(strings.check_output["warning"])
		if(purge.lower()[0]=="y"):
			print(strings.check_output["purging"]) 
			for dirName, subdirList, fileList in os.walk(config.output_location):
				for f in fileList:
					os.unlink(os.path.join(dirName, f))
				for d in subdirList:
					shutil.rmtree(os.path.join(dirName, d))
		else:
			print(strings.check_output["overwriting"])
def MetaShortCodes(data):
	data = data.replace("[[URL]]",config.url+"/")
	return data

def LoadCodes(defs):
	defs_c = {}
	for name, location in defs.items():
		try:
			html = open(config.shortcode_location+"/"+location, 'r').read()
			html = MetaShortCodes(html)
			defs_c.update({name:html})
		except FileNotFoundError:
			print(strings.load_codes["failed"])
			print(strings.load_codes["requested"]+name+strings.load_codes["cant_find"]+location)
			input(strings.load_codes["check"])
			quit()
	return defs_c


def Build(rootDir,prefabs):
	print(strings.build["look"]+rootDir)
	for dirName, subdirList, fileList in os.walk(rootDir):
		print(strings.build["found"]+'%s' % dirName)
		for fname in fileList:
			print('\t%s' % fname)
			output_file = config.output_location+"/"+dirName+"/"+fname
			output_file = output_file.replace(config.template_location,"")#removes the template location from the output path
			parts = os.path.split(output_file)
			if not os.path.isdir(parts[0]):#makes sure we have a directory to write to
				os.mkdir(parts[0])
			print(strings.build["output"]+output_file)
			if(fname.split(".")[1].lower() in config.parse_types):
				test = open(dirName+"/"+fname, 'r').read()
				#meta-shortcodes
				test = MetaShortCodes(test)
				#end meta-shortcodes
				for name, data in prefabs.items():
					test = test.replace("{{"+name+"}}",data)
				file = open(output_file, 'w')
				file.write(test)
			else:
				print(strings.build["no_parse"]+fname)
				shutil.copyfile(dirName+"/"+fname, output_file)

def Start():
	Parameters()
	CheckOutput()
	defs = LoadCodes(shortcodes.defs)
	Build(config.template_location,defs)

Start()