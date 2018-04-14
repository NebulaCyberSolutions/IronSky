import user.config.shortcodes as shortcodes
import user.config.config as config_file
from include.parameters import *
from include.checkout import *
from include.load_codes import *
from include.build import *

def Start():
	config = Parameters(config_file)
	CheckOutput(config)
	defs = LoadCodes(shortcodes.defs,config)
	Build(defs,config)
Start()