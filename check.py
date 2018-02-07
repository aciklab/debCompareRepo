import sys
import re

######
# https://github.com/nyucel/pardus-check/blob/master/get_package_info.py
######

def get_package_info(package_info, info):
    return re.search(info+": (.*)\n", package_info).group(1)

def get_package_sha256sum(package_info):
    return get_package_info(package_info, 'SHA256')

def get_package_version(package_info):
    return get_package_info(package_info, 'Version')
    
def get_package_name(package_info):
    return get_package_info(package_info, 'Package')

def get_package_filename(package_info):
    return './' + '/'.join(get_package_info(package_info, 'Filename').split('/')[2:])
###

packages_file_path = sys.argv[1]
packages_file = file(packages_file_path).read()
packages_list = packages_file.split('\n\n')

sha256 = {}
version = {}

print(len(packages_list))
for package_info in packages_list:
    if len(package_info) < 10:
	continue
    #package_name = get_package_name(package_info)
    package_filename = get_package_filename(package_info)
    package_sha256sum = get_package_sha256sum(package_info)
    package_version = get_package_version(package_info)
    sha256[package_filename] = package_sha256sum
    version[package_filename] = package_version

print(len(sha256))
print(len(version))

