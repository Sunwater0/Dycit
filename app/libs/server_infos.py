# This is the library which allows you to recover the information of the server on which the DYCIT application transforms.
# This bookstore (like all the others in Dycit) is under License GPLV3.
# - Creator: SunWater_ -
# - Support: contact.sunwater@gmail.com -

# Imports
import psutil


## Get RAM stats
# Get total virtual RAM
def get_total_virtual_ram():
    ram = psutil.virtual_memory()
    return ram.total

# Get used virtual RAM
def get_used_virtual_ram():
    ram = psutil.virtual_memory()
    return ram.used

# Get free virtual RAM
def get_free_virtual_ram():
    ram = psutil.virtual_memory()
    return ram.free


## Get disk stats
# Get total disk space
def get_total_storage():
    storage = psutil.disk_usage('/')
    return storage.total

# Get free disk space
def get_free_storage():
    storage = psutil.disk_usage('/')
    return storage.free

# Get used disk space
def get_used_storage():
    storage = psutil.disk_usage('/')
    return storage.used


## Test
if __name__ == "__main__":
    print('-- RAM infos --')
    print("Total RAM: "+str(get_total_virtual_ram()))
    print("Free RAM: "+str(get_free_virtual_ram()))
    print("Used RAM: "+str(get_used_virtual_ram()))

    print('-- Storage infos --')
    print("Total storage: "+str(get_total_storage()))
    print("Free storage: "+str(get_free_storage()))
    print("Used storage: "+str(get_used_storage()))