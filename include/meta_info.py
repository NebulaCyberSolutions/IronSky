import datetime
def MetaInfo():
    meta_data = {}
    meta_data.update({"time-stamp":str(datetime.datetime.utcnow())+" UTC"})
    return meta_data
    
