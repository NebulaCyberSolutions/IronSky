import os
import shutil
import include.strings as strings
def CheckOutput(config):
	if not os.path.isdir(config.output_location):
		os.mkdir(config.output_location)
	if os.listdir(config.output_location) != []:
		if(config.auto_purge == True):
			answer = "y" 
		else:
			answer = input(strings.check_output["warning"])
		if(answer.lower()[0]=="y"):
			print(strings.check_output["purging"]) 
			for dirName, subdirList, fileList in os.walk(config.output_location):
				for f in fileList:
					os.unlink(os.path.join(dirName, f))
				for d in subdirList:
					shutil.rmtree(os.path.join(dirName, d))
		else:
			print(strings.check_output["overwriting"])