import user.config.config as config
def MetaShortCodes(data):
	data = data.replace("[[URL]]",config.url+"/")
	return data