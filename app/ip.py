import datetime, socket

def get_ips():
    out = 'dns;ip\n'
    f = open('in/dns')

    for dns in f:
        dns = dns.replace('\n', '')
        try:
            ip = socket.gethostbyname(dns)
            out += f"{dns};{ip}\n"
        except:
            out += f"{dns};null\n"
    
    f.close
    f = open(f"out/{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}-ips.csv", 'w')
    f.write(out)
    f.close()