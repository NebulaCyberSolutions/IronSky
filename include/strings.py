#values should be read-only but this is not enforced
arg_read = {}
arg_read.update({"url":"URL Value: "})
arg_read.update({"parse":"Parse Types Value: "})
arg_read.update({"shortcode":"ShortCode Location Value: "})
arg_read.update({"output":"Output Location Value: "})
arg_read.update({"template":"Template Location Value: "})
arg_read.update({"purge":"Auto Purge: True"})

check_output = {}
check_output.update({"warning":"OUTPUT DIRECTORY IS NOT EMPTY\nWould you like to purge the output directory?\n[Yes/No]"});
check_output.update({"purging": "Purging!"});
check_output.update({"overwriting": "Overwriting instead."});

load_codes = {}
load_codes.update({"failed":"LOADING SHORTCODE FAILED!"})
load_codes.update({"requested":"The requested template file "})
load_codes.update({"cant_find":" does not exist at: "})
load_codes.update({"check":"Please check 'shortcodes.py' to make sure this file name and path are correct."})

build = {}
build.update({"look":"Looking through "})
build.update({"found":"Found directory: "})
build.update({"output":"Output: "})
build.update({"no_parse":"Not Parsing: "})