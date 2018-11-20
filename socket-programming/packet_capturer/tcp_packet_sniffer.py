import struct  # structure contains complete raw packet
import socket  # for socket

def unpack_ip_frame(raw_ip_data):
    raw_ip_header = raw_ip_data[0:20]
    ip_header = struct.unpack("!2B3H2BH4s4s", raw_ip_header)
    protocol = ip_header[6]
    if (protocol == 6):
        unpack_tcp_frame(raw_ip_data[20:])

def unpack_tcp_frame(raw_tcp_data):

    raw_tcp_header = raw_tcp_data[:20]
    tcp_header = struct.unpack("!2H2LHHHH", raw_tcp_header)
    source_port = tcp_header[0]
    destination_port = tcp_header[1]
    sequence_number = tcp_header[2]
    ack_number = tcp_header[3]
    offset_reserved_tcp_flags = tcp_header[4]
    # shift 12 bits right to get offset part only and Multiply by 4 to get byte count
    offset = (offset_reserved_tcp_flags >> 12) * 4
    # get each flag by ANDING and right shifting remaining flags
    flag_cwr = (offset_reserved_tcp_flags & 128) >> 7
    flag_ece = (offset_reserved_tcp_flags & 64) >> 6
    flag_urg = (offset_reserved_tcp_flags & 32) >> 5
    flag_ack = (offset_reserved_tcp_flags & 16) >> 4
    flag_push = (offset_reserved_tcp_flags & 8) >> 3
    flag_rst = (offset_reserved_tcp_flags & 4) >> 2
    flag_syn = (offset_reserved_tcp_flags & 2) >> 1
    flag_fin = (offset_reserved_tcp_flags & 1)

    window = tcp_header[5]
    checksum = tcp_header[6]
    urg_pointer = tcp_header[7]

    print(
        "TCP Header : \nSRC PORT : {} DEST PORT : {} SEQ NUM : {} ACK NUM : {} \nOFFSET : {}  \nFLAGS : CWR:{}, ECE:{}, URG:{}, ACK:{}, PUSH:{}, RST:{}, SYN:{}, FIN:{} \nWINDOW: {} CHECHSUM:{} URG POINTER : {}\n\n".format(
            source_port, destination_port, sequence_number, ack_number, offset, flag_cwr, flag_ece, flag_urg,
            flag_ack,
            flag_push,
            flag_rst, flag_syn, flag_fin, window, checksum, urg_pointer))


def main():
    my_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        (raw_data, address) = my_socket.recvfrom(65535)
        raw_data = raw_data[14:]
        unpack_ip_frame(raw_data)


main()
