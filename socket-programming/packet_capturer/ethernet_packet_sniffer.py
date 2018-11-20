import struct  # structure contains complete raw packet
import socket  # for socket


# unpacks the ethernet frame from raw_data
def unpack_ethernet_frame(raw_data):
    # first 14bytes are for dest,src mac address and protocol
    dest_mac, src_mac, protocol = struct.unpack("!6s6sH", raw_data[0:14])
    final_dest_mac = convert_into_readable_mac(dest_mac)
    final_src_mac = convert_into_readable_mac(src_mac)
    final_protocol = socket.htons(protocol)
    return final_dest_mac, final_src_mac, final_protocol


# convert mac address in proper format
def convert_into_readable_mac(byte_mac):
    # map works as function and sequence
    str_mac = map('{:02x}'.format, byte_mac)
    str_mac = ":".join(str_mac)
    return str_mac


def main():
    # create socket for raw packet
    my_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    # listen forever
    while True:
        # recvfrom returns tuple of (raw_data, address)
        (raw_data, address) = my_socket.recvfrom(65535)

        # raw data will contain ip ethernet header and data.
        # as per ethernet packet, first header is : 6bytes, 6bytes, 2bytes for dest_mac,src_mac,type_length respectively
        # remaining is data and at last there is trailer of 4bytes
        dest_mac, src_mac, protocol = unpack_ethernet_frame(raw_data)
        print("| DESTINATION MAC : {} SOURCE MAC : {} PROTOCOl : {} DATA : {}|\n".format(dest_mac, src_mac, protocol,raw_data[14:]))
main()

