import requests
import platform
import psutil
import json
import getpass


def get_system_info():
    uname = platform.uname()
    system_info = {}
    system_info['system'] = uname.system
    system_info['node'] = uname.node
    system_info['release'] = uname.release
    system_info['processor'] = uname.processor
    system_info['bit_architecture'] = platform.architecture()[0]
    system_info['current_cpu_freq'] = str(psutil.cpu_freq().current)
    return system_info


def get_memory_info():
    mem = psutil.virtual_memory()
    memory = {}
    memory['total'] = mem.total
    memory['available'] = mem.available
    memory['used'] = mem.used
    memory['free'] = mem.free
    return memory

def get_partition_info():
    disk_partition = psutil.disk_partitions()[0]
    partition = {}
    partition['device'] = disk_partition.device
    partition['mount point'] = disk_partition.mountpoint
    partition['file system type'] = disk_partition.fstype
    partition['opts'] = disk_partition.opts
    return partition

def get_disk_info():
    disk_obj = psutil.disk_usage('/')
    disk = {}
    disk['total'] = disk_obj.total
    disk['used'] = disk_obj.used
    disk['free'] = disk_obj.free
    disk['partition'] = get_partition_info()
    return disk

url = 'http://127.0.0.1:5000/computer_info?pretty=true'
headers = {
    'Content-Type' : 'application/json'
}

data = {
    'username': getpass.getuser(),
    'system_info': get_system_info(),
    'memory': get_memory_info(),
    'disk': get_disk_info()
}
json_data = json.dumps(data)
response = requests.post(url, headers=headers, data=json_data)

print(response.json())
