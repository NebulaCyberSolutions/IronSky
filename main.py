import config.shortcodes as shortcodes
from include.parameters import *
from include.checkout import *
from include.load_codes import *
from include.build import *

def Start():
	Parameters()
	CheckOutput()
	defs = LoadCodes(shortcodes.defs)
	Build(config.template_location,defs)
Start()