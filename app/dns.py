import datetime, socket

def get_dns():
    out = 'ip;dns\n'
    f = open('in/ip')

    for ip in f:
        ip = ip.replace('\n', '')
        try:
            dns = socket.gethostbyaddr(ip)
            out += f"{ip};{dns[0]}\n"
        except:
            out += f"{ip};null\n"
    
    f.close
    f = open(f"out/{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}-dns.csv", 'w')
    f.write(out)
    f.close()