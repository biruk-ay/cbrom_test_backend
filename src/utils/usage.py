import psutil


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
    
    #maybe add time

    
    def get_all_info(self):
        return [self.get_user(),
                self.get_net(),
                self.get_disk(),
                self.get_memory(),
                self.get_cpu()]
    
if __name__ == "__main__":
    a = Usage()
    for i in (a.get_all_info()):
        print(str(i) + "\n\n")


# print(psutil.cpu_count(logical=False))
# print(psutil.disk_usage('/').total)
# print(psutil.net_io_counters().bytes_sent)
# # version_info = psutil.version_info
# for i, k in enumerate(psutil.version_info):
#     print(i,k)