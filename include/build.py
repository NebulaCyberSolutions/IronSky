import os
import shutil
import include.strings as strings
from include.meta_shortcodes import *
def Build(shortcodes, config):
	rootDir = config.template_location;
	print(strings.build["look"]+rootDir)
	for dirName, subdirList, fileList in os.walk(rootDir):
		print(strings.build["found"]+'%s' % dirName)
		for fname in fileList:
			print('\t%s' % fname)
			output_file = config.output_location+dirName+"/"+fname
			output_file = output_file.replace(config.template_location,"")#removes the template location from the output path
			path_parts = os.path.split(output_file)
			if not os.path.isdir(path_parts[0]):#makes sure we have a directory to write to
				os.mkdir(path_parts[0])
			print(strings.build["output"]+output_file)
			if(fname.split(".")[1].lower() in config.parse_types):
				template_file = open(dirName+"/"+fname, 'r').read()
				#meta-shortcodes
				template_file = MetaShortCodes(template_file,config)
				#end meta-shortcodes
				for name, data in shortcodes.items():
					template_file = template_file.replace("{{"+name+"}}",data)
				file = open(output_file, 'w')
				file.write(template_file)
			else:
				print(strings.build["no_parse"]+fname)
				shutil.copyfile(dirName+"/"+fname, output_file)