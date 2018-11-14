import struct  # structure contains complete raw packet
import socket  # for socket


def unpack_ip_frame(raw_ip_data):
    raw_ip_header = raw_ip_data[0:20]
    ip_header = struct.unpack("!2B3H2BH4s4s", raw_ip_header)
    protocol = ip_header[6]
    if (protocol == 17):
        unpack_udp_packet(raw_ip_data[20:])


def unpack_udp_packet(raw_udp):
    try:
        raw_udp_header = raw_udp[:8]
        udp_header = struct.unpack("!4H", raw_udp_header)
        source_port = udp_header[0]
        dest_port = udp_header[1]
        length = udp_header[2]
        checksum = udp_header[3]
        print("UDP packet : \nSource Port : {} Dest Port : {} Lentgh : {} Checksum : {}".format(source_port, dest_port,
                                                                                                length, checksum))
        print("Data : \n", raw_udp[8:])
    except Exception as exception:
        pass


if __name__ == '__main__':
    while True:
        mySocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
        (raw_data, client_addr) = mySocket.recvfrom(65535)
        # For Ethernet header
        raw_data = raw_data[14:]
        # For IPV4 header
        unpack_ip_frame(raw_data)

