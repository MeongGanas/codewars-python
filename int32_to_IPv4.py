def int32_to_ip(int32):
    # your code here
    int32 = '{:032b}'.format(int32)
    int32 = [int32[i:i+8] for i in range(0, len(int32), 8)]
    return '.'.join(str(int(i, 2)) for i in int32)

# from ipaddress import IPv4Address

# def int32_to_ip(int32):
#     return str(IPv4Address(int32))


print(int32_to_ip(0))
