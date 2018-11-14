# If we use raw_data packet then, the complete packet starts with ethernet.
# Hence to get ipv4 packet from raw_data we have to remove first 14bytes.
# Or else you can also use socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP to get directly ipv4 packet

import struct  #  structure contains complete raw packet
import socket  # for socket


def unpack_ip_frame(raw_ip_data):

    raw_ip_header = raw_ip_data[0:20]
    ip_header = struct.unpack("!2B3H2BH4s4s", raw_ip_header)
    version_and_hlen = ip_header[0]
    version = version_and_hlen >> 4  # right side shift 4 bit to get left 4 bit
    # Multiply by 4 to get byte count
    hlen = (version_and_hlen & 15) * 4
    tos = ip_header[1]
    total_length = ip_header[2]
    id = ip_header[3]
    fragments_and_IPFlags = ip_header[4]
    ttl = ip_header[5]
    protocol = ip_header[6]
    header_checksum = ip_header[7]
    source_address = ip_header[8]
    destination_address = ip_header[9]
    if (protocol == 1):
        print("ICMP Packet : ")
    if (protocol == 6):
        print("TCP Packet : ")
    if (protocol == 17):
        print("UDP Packet : ")

    print(
        "VER : {}  HLEN : {} TOS : {}  TOTAL LENGTH : {} \n IDENTIFICATION : {}  FRAGMENTATION_AND_FLAGS : {} \n TTY : {} PROTOCOL : {} HEADER_CHEKSUM : {} \n SOURCE IP : {}\n TARGET IP : {}\n".format(
            str(version), hlen, tos, total_length, id, fragments_and_IPFlags, ttl, protocol, header_checksum,
            (socket.inet_ntoa(source_address)), (socket.inet_ntoa(destination_address))))


def main():
    # create socket for raw packet
    my_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))
    # listen forever
    while True:
        # recvfrom returns tuple of (raw_data, address)
        (raw_data, address) = my_socket.recvfrom(65535)
        # First 14 bytes for ethernet packet. We already created seperate packet sniffer for that. Hence ignoring it.
        raw_data = raw_data[14:]
        # After first 14 bit, ipv4 packet will start.
        unpack_ip_frame(raw_data)


main()
