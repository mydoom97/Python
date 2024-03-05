import subprocess

IP = input("Enter IP address: ")
number = input("次数：")

def ping_host(host):
    result = subprocess.call('ping -c '+number+' '+host, shell=True)
    if result. == 0:
is_online,output = ping_host(IP)