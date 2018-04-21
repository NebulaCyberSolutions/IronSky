def MetaShortCodes(data,config,meta):
	data = data.replace("[[URL]]",config.url+"/")
	data = data.replace("[[time-stamp]]",meta["time-stamp"])
	return data