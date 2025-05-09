import pyeapi
import os
import yaml


pyeapi.load_config('eapi.conf')
yfile = open('switches.yml', 'r')
switch_dict = yaml.safe_load(yfile)

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

for switch in switch_dict['switches']:
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string='True')
    path = directory + '/' + switch + '.cfg'
    file = open(path,'w')
    file.write(running_config)
    file.close()
    print(f"Backing up {switch}")