import socket
import argparse
from termcolor import colored


def get_arguments():
    parser = argparse.ArgumentParser(description='Fast TCP Port Scanner')
    parser.add_argument("-t", "--target", dest="target", required=True, help="Scan syntax: port_scanner.py -t <IP_TARGET> ")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Scan syntax: port_scanner.py -p 1-100")
    options = parser.parse_args()

    return options.target, options.port


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s

def port_scanner(port, host, s):

    try:
        s.connect((host, port))
        print(colored(f"\n[+] El puerto {port} esta abierto\n", 'green'))
        s.close()

    except(socket.timeout, ConnectionRefusedError):
        s.close()

def scan_ports(ports, target):

    for port in ports:
        s = create_socket()
        port_scanner(port, target, s)


def parse_ports(ports_str):

    if '-' in ports_str:
        start, end = map(int, ports_str.split('-'))
        return range(start, end+1)
    elif',' in ports_str:
        return map(int, ports_str(','))
    else:
        return (int(ports_str),)



def main():
    
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(ports, target)



if __name__ == '__main__':
    main()