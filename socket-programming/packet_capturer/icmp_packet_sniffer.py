import struct  #  structure contains complete raw packet
import socket  # for socket


def unpack_icmp_frame(raw_icmp_header):
    icmp_header = raw_icmp_header[0:4]
    icmp_header = struct.unpack("!BBH", icmp_header)
    icmp_type = icmp_header[0]
    code = icmp_header[1]
    checksum = icmp_header[2]
    print("ICMP Header : \nType : {} Code : {} Checksum : {}\n".format(icmp_type, code, checksum))


def main():
    # create socket for particular icmp packet
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    # listen forever
    while True:
        (raw_data, address) = my_socket.recvfrom(65535)
        unpack_icmp_frame(raw_data[0:20])


main()
