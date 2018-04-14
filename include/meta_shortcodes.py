def MetaShortCodes(data,config):
	data = data.replace("[[URL]]",config.url+"/")
	return data