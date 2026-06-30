import socket
def get_ports(domain):
    
    try:
        ip=socket.gethostbyname(domain)
        portlar=[]
        for port in  range(1,1025):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result=s.connect_ex((ip,port))
            if result == 0:
                print(f"açık port bulundu: ",{port})
                portlar.append(port)
        s.close()
        print(f"tarama bitti. açık portlar:",{portlar})

    except Exception as e:
        print (f"hata:",{e})


            

