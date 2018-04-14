import sys
import include.strings as strings
def Parameters(config):
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
	return config