import include.strings as strings
from include.meta_shortcodes import *
def LoadCodes(defs, config):
	defs_c = {}
	for name, location in defs.items():
		try:
			html = open(config.shortcode_location+"/"+location, 'r').read()
			html = MetaShortCodes(html,config)
			defs_c.update({name:html})
		except FileNotFoundError:
			print(strings.load_codes["failed"])
			print(strings.load_codes["requested"]+name+strings.load_codes["cant_find"]+location)
			input(strings.load_codes["check"])
			quit()
	return defs_c