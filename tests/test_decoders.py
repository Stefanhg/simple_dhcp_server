import base64

from simple_dhcp_server.decoders import ReadBootProtocolPacket, options, WriteBootProtocolPacket

raw_data_packet = b'02010600f7b41ad100000000c0a800640000000000000000000000007c7a914bca6c00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000638253633501053604c0a800010104ffffff000304c0a800010604c0a80001ff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'.upper()

data_packet =  base64.b16decode(raw_data_packet)


def test_read_boot_protocol_packet():
    data = data_packet
    assert data[0] == 2
    p = ReadBootProtocolPacket(data)
    assert p.message_type == 2
    assert p.hardware_type == 1
    assert p.hardware_address_length == 6
    assert p.hops == 0
    assert p.transaction_id == 4155775697
    assert p.seconds_elapsed == 0
    assert p.bootp_flags == 0
    assert p.client_ip_address == '192.168.0.100'
    assert p.your_ip_address == '0.0.0.0'
    assert p.next_server_ip_address == '0.0.0.0'
    assert p.relay_agent_ip_address == '0.0.0.0'
    assert p.client_mac_address.lower() == '7c:7a:91:4b:ca:6c'
    assert p.magic_cookie == '99.130.83.99'
    assert p.dhcp_message_type == 'DHCPACK'
    assert p.options[53] == b'\x05'
    assert p.server_identifier == '192.168.0.1'
    assert p.subnet_mask == '255.255.255.0'
    assert p.router == ['192.168.0.1']
    assert p.domain_name_server == ['192.168.0.1']
    str(p)

def test_write_boot_protocol_packet():
    pass
    #p = ReadBootProtocolPacket(raw_data_packet)
    #pr = WriteBootProtocolPacket(p)
    #assert pr.to_bytes() == data_packet


class TestsOptions:
    def test_setattr(self):
        assert options[18][0] == 'extensions_path', options[18][0]
        assert options[25][0] == 'path_mtu_plateau_table', options[25][0]
        assert options[33][0] == 'static_route', options[33][0]
        assert options[50][0] == 'requested_ip_address', options[50][0]
        assert options[64][0] == 'network_information_service_domain', options[64][0]
        assert options[76][0] == 'stda_server', options[76][0]
