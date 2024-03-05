import subprocess
import time

def ping_host(host, timeout=1):
   while True:
       try:
           # 调用系统的ping命令
           result = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True, timeout=timeout)
           
           # 判断ping命令执行结果
           if result.returncode == 0:
               print(f"Host {host} is up and reachable.")
           else:
               print(f"Host {host} is down or unreachable.")
       except subprocess.CalledProcessError as e:
           print(f"An error occurred: {e}")
       except KeyboardInterrupt:
           print("Ping process interrupted by user.")
           break
       except Exception as e:
           print(f"An unexpected exception occurred: {e}")
           break
       
       # 等待一段时间再次ping
       time.sleep(1)  # 休眠1秒，根据需要调整

# 替换'example.com'为你想要ping的主机名或IP地址
host_to_ping = 'www.baidu.com'
ping_host(host_to_ping)