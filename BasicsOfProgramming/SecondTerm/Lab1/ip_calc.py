"""
Ip calculator
"""
def get_ip_from_raw_address(raw_address: str) -> str:
    """
    Extracts ip address from raw address
    >>> get_ip_from_raw_address("172.22.120.22/18")
    '172.22.120.22'
    """
    ip_adress = raw_address.partition("/")
    return ip_adress[0]

def address_into_binary(address: str) -> str:
    """
    Transforms address into binary mask
    >>> address_into_binary("255.255.192.0")
    '11111111.11111111.11000000.00000000'
    """
    return '.'.join([bin(int(x)+256)[3:] for x in address.split('.')])

def binary_into_address(binary: str) -> str:
    """
    Transforms binary mask into ip address
    >>> binary_into_address("11111111.11111111.11000000.00000000")
    '255.255.192.0'
    """
    return '.'.join([str(int(x, 2)) for x in binary.split('.')])

def get_network_address_from_raw_address(raw_address: str) -> str:
    """
    Gets a network address from raw address
    >>> get_network_address_from_raw_address("172.22.120.22/18")
    '172.22.64.0'
    """
    ip_ad = get_ip_from_raw_address(raw_address)
    mask = get_binary_mask_from_raw_address(raw_address)
    mask_ip = binary_into_address(mask)
    net_ad = []
    for i in range(0, 4):
        new_part = int(ip_ad.split('.')[i]) & int(mask_ip.split('.')[i])
        net_ad.append(str(new_part))
    return ".".join(net_ad)

def get_broadcast_address_from_raw_address(raw_address: str) -> str:
    """
    Gets a broadcast address from raw address
    >>> get_broadcast_address_from_raw_address("172.22.120.22/18")
    '172.22.127.255'
    """
    ip_ad = get_ip_from_raw_address(raw_address)
    mask = get_binary_mask_from_raw_address(raw_address)
    mask_ip = binary_into_address(mask)
    inverted_m = ".".join([str(255 - int(octet)) for octet in mask_ip.split(".")])
    broad_ad = []
    for i in range(0, 4):
        new_part = int(ip_ad.split('.')[i]) | int(inverted_m.split('.')[i])
        broad_ad.append(str(new_part))
    return ".".join(broad_ad)

def get_binary_mask_from_raw_address(raw_address: str) -> str:
    """
    Makes a binary mask from raw address
    >>> get_binary_mask_from_raw_address("172.22.120.22/18")
    '11111111.11111111.11000000.00000000'
    """
    sep_raw = raw_address.partition("/")
    mask = [0, 0, 0, 0]
    for i in range(int(sep_raw[2])):
        mask[i//8] += 1 << (7 - i % 8)
    return '.'.join([bin(int(x)+256)[3:] for x in mask])

def get_first_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    Gets the first usable ip
    >>> get_first_usable_ip_address_from_raw_address("172.22.120.22/18")
    '172.22.64.1'
    """
    ip_ad = get_network_address_from_raw_address(raw_address).split(".")
    last_part = str(int(ip_ad[-1])+1)
    del ip_ad[-1]
    ip_ad.append(last_part)
    return ".".join(ip_ad)

def get_penultimate_usable_ip_address_from_raw_address(raw_address: str) -> str:
    """
    Gets the penultimate usable ip address
    >>> get_penultimate_usable_ip_address_from_raw_address("172.22.120.22/18")
    '172.22.127.253'
    """
    broad_ip = get_broadcast_address_from_raw_address(raw_address).split(".")
    last_part = str(int(broad_ip[-1]) - 2)
    del broad_ip[-1]
    broad_ip.append(last_part)
    return ".".join(broad_ip)

def get_number_of_usable_hosts_from_raw_address(raw_address: str) -> int:
    """
    Counts the number of usable hosts
    >>> get_number_of_usable_hosts_from_raw_address("172.22.120.22/18")
    16382
    """
    mask = get_binary_mask_from_raw_address(raw_address)
    num_of_1 = mask.count("1")
    amount_of_hosts_in_mask = 32 - num_of_1
    return 2**amount_of_hosts_in_mask-2

def get_ip_class_from_raw_address(raw_address: str) -> str:
    """
    Defines the ip class
    >>> get_ip_class_from_raw_address("172.22.120.22/18")
    'B'
    """
    ip_ad = get_ip_from_raw_address(raw_address).split(".")
    if int(ip_ad[0])<127:
        net_class = "A"
    elif 127<int(ip_ad[0])<192:
        net_class = "B"
    elif 192<=int(ip_ad[0])<224:
        net_class = "C"
    elif 224<=int(ip_ad[0])<240:
        net_class = "D"
    elif 240<=int(ip_ad[0])<148:
        net_class = "E"
    else:
        net_class = "Error"
    return net_class

def check_private_ip_address_from_raw_address(raw_address: str) -> bool:
    """
    Checks whether the ip address is private or no
    >>> check_private_ip_address_from_raw_address("172.22.120.22/18")
    True
    """
    ip_ad = get_ip_from_raw_address(raw_address).split(".")
    if int(ip_ad[0])==10:
        checker = True
    elif int(ip_ad[0])==172 and 16<=int(ip_ad[1])<32:
        checker = True
    elif int(ip_ad[0])==192 and int(ip_ad[1])==168:
        checker = True
    else:
        checker = False
    return checker

print(address_into_binary("255.255.192.0"))
if __name__ == '__main__':
    try:
        ip = input()
        if '/' not in ip and ip.count('.') == 3:
            print('Missing prefix')
        elif ip.count('.') != 3:
            print('Error')
        else:
            print('IP address:', get_ip_from_raw_address(ip))
            print('Network Address:', get_network_address_from_raw_address(ip))
            print('Broadcast Address:', get_broadcast_address_from_raw_address(ip))
            print('Binary Subnet Mask:', get_binary_mask_from_raw_address(ip))
            print('First usable host IP:', get_first_usable_ip_address_from_raw_address(ip))
            print('Penultimate usable host IP:', \
get_penultimate_usable_ip_address_from_raw_address(ip))
            print('Number of usable Hosts:', get_number_of_usable_hosts_from_raw_address(ip))
            print('IP class:', get_ip_class_from_raw_address(ip))
            print('IP type private:', check_private_ip_address_from_raw_address(ip))

    except:
        print('Error')
