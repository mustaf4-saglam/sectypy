import socket
def get_ports(domain):
    
    try:
        en_populer_portlar = [
    20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 
    110, 111, 135, 137, 138, 139, 143, 161, 162, 389, 
    443, 445, 465, 500, 514, 515, 587, 631, 873, 993, 
    995, 1080, 1433, 1521, 1723, 2049, 3128, 3306, 3389, 5432, 
    5900, 5985, 6379, 8000, 8080, 8443, 8888, 9000, 9200, 27017
]
        ip=socket.gethostbyname(domain)
        portlar=[]
        for port in  range(en_populer_portlar):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result=s.connect_ex((ip,port))
            if result == 0:
                portlar.append(port)
            s.close()
        print(f"tarama bitti. açık portlar:{portlar}")
        return portlar

    except Exception as e:
        print (f"hata:",{e})