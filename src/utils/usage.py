import psutil
from datetime import datetime

class Usage:
    def __init__(self) -> None:
        pass
    
    def get_user(self):
        return psutil.users()
    
    def get_net(self):
        return psutil.net_if_addrs().get('eno1')

    def get_disk(self):
        return psutil.disk_usage('/')
    
    def get_memory(self):
        return psutil.virtual_memory()
    
    def get_cpu(self):
        return psutil.cpu_count(logical=False)
    
    def get_time(self):
        return datetime.now()

    
    def get_all_info(self):
        return [self.get_user(),
                self.get_net(),
                self.get_disk(),
                self.get_memory(),
                self.get_cpu(),
                self.get_time()]
    
if __name__ == "__main__":
    a = Usage()
    for i in (a.get_all_info()):
        print(str(i) + "\n\n")
