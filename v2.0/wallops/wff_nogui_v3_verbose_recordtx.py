#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Wff Nogui V3 Verbose Recordtx
# Author: Zach Leffke, KJ4QLP
# Description: Wallops Interface, No GUI
#
# Generated: Fri Jan 10 09:31:05 2020
# GNU Radio version: 3.7.12.0
##################################################

from datetime import datetime as dt; import string; import math
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import gr_sigmf
import kiss
import pdu_utils
import vcc


class wff_nogui_v3_verbose_recordtx(gr.top_block):

    def __init__(self, callsign='WJ2XMS', client_port='8000', gs_id='WFF', post_bytes=64, pre_bytes=64, sc_id='VCC-A', server_ip='0.0.0.0', ssid=0, verbose=0, wallops_dn_port='56101', wallops_up_port='56100'):
        gr.top_block.__init__(self, "Wff Nogui V3 Verbose Recordtx")

        ##################################################
        # Parameters
        ##################################################
        self.callsign = callsign
        self.client_port = client_port
        self.gs_id = gs_id
        self.post_bytes = post_bytes
        self.pre_bytes = pre_bytes
        self.sc_id = sc_id
        self.server_ip = server_ip
        self.ssid = ssid
        self.verbose = verbose
        self.wallops_dn_port = wallops_dn_port
        self.wallops_up_port = wallops_up_port

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S" )
        self.fn_up = fn_up = "{:s}_{:s}_{:s}".format(gs_id, sc_id, ts_str)
        self.fn_dn = fn_dn = "{:s}_{:s}_{:s}".format(sc_id, gs_id, ts_str)
        self.fp_up = fp_up = "/gnuradio/captures/{:s}".format(fn_up)
        self.fp_dn = fp_dn = "/gnuradio/captures/{:s}".format(fn_dn)

        ##################################################
        # Blocks
        ##################################################
        self.vcc_insert_time_tag_bb_0_0 = vcc.insert_time_tag_bb('core:datetime', 'packet_len')
        self.vcc_insert_time_tag_bb_0 = vcc.insert_time_tag_bb('core:datetime', 'packet_len')
        self.vcc_insert_src_callsign_pdu_0 = vcc.insert_src_callsign_pdu(callsign=callsign,ssid=ssid, verbose=bool(verbose))
        self.vcc_burst_scramble_bb_0 = vcc.burst_scramble_bb(0x21, 0x0, 16)
        self.sigmf_sink_1 = gr_sigmf.sink("ri8", fp_dn, gr_sigmf.sigmf_time_mode_absolute, False)
        self.sigmf_sink_1.set_global_meta("core:sample_rate", 0)
        self.sigmf_sink_1.set_global_meta("core:description", 'Wallops Flight Facility Interface, Downlink')
        self.sigmf_sink_1.set_global_meta("core:author", 'Zach Leffke, zleffke@vt.edu')
        self.sigmf_sink_1.set_global_meta("core:license", 'MIT')
        self.sigmf_sink_1.set_global_meta("core:hw", 'WFF UHF Ground Station')
        self.sigmf_sink_1.set_global_meta('vcc:spacecraft', 'VCC-A')
        self.sigmf_sink_1.set_global_meta('vcc:ground_station', 'WFF')
        self.sigmf_sink_1.set_global_meta('vcc:callsign', 'WJ2XMS-0')
        self.sigmf_sink_1.set_global_meta('vcc:tap_point', 'Packed Bytes, NRZ-I decoded, before descrambling')

        self.sigmf_sink_0 = gr_sigmf.sink("ri8", fp_up, gr_sigmf.sigmf_time_mode_absolute, False)
        self.sigmf_sink_0.set_global_meta("core:sample_rate", 0)
        self.sigmf_sink_0.set_global_meta("core:description", 'Wallops Flight Facility Interface, Uplink')
        self.sigmf_sink_0.set_global_meta("core:author", 'Zach Leffke, zleffke@vt.edu')
        self.sigmf_sink_0.set_global_meta("core:license", 'MIT')
        self.sigmf_sink_0.set_global_meta("core:hw", 'WFF UHF Ground Station')
        self.sigmf_sink_0.set_global_meta('vcc:spacecraft', 'VCC-A')
        self.sigmf_sink_0.set_global_meta('vcc:ground_station', 'WFF')
        self.sigmf_sink_0.set_global_meta('vcc:uplink_callsign', 'WJ2XMS-0')
        self.sigmf_sink_0.set_global_meta('vcc:tap_point', 'KISS input')

        self.pdu_utils_pack_unpack_0 = pdu_utils.pack_unpack(pdu_utils.MODE_PACK_BYTE, pdu_utils.BIT_ORDER_MSB_FIRST)
        self.kiss_pdu_to_kiss_0 = kiss.pdu_to_kiss()
        self.kiss_kiss_to_pdu_0 = kiss.kiss_to_pdu(True)
        self.kiss_hdlc_framer_0 = kiss.hdlc_framer(preamble_bytes=pre_bytes, postamble_bytes=post_bytes)
        self.kiss_hdlc_deframer_0 = kiss.hdlc_deframer(check_fcs=True, max_length=300)
        self.digital_descrambler_bb_0 = digital.descrambler_bb(0x21, 0, 16)
        self.blocks_socket_pdu_2 = blocks.socket_pdu("TCP_SERVER", server_ip, wallops_dn_port, 1500, False)
        self.blocks_socket_pdu_1 = blocks.socket_pdu("TCP_SERVER", server_ip, wallops_up_port, 1500, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", server_ip, client_port, 1024, False)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/zleffke/vcc/captures/uva_no-op_ax25_scram.dat', False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0, 'pdus'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.blocks_socket_pdu_2, 'pdus'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.kiss_hdlc_deframer_0, 'out'), (self.kiss_pdu_to_kiss_0, 'in'))
        self.msg_connect((self.kiss_hdlc_framer_0, 'out'), (self.vcc_burst_scramble_bb_0, 'in'))
        self.msg_connect((self.kiss_kiss_to_pdu_0, 'out'), (self.vcc_insert_src_callsign_pdu_0, 'in'))
        self.msg_connect((self.kiss_pdu_to_kiss_0, 'out'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.kiss_pdu_to_kiss_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.kiss_pdu_to_kiss_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))
        self.msg_connect((self.pdu_utils_pack_unpack_0, 'pdu_out'), (self.blocks_pdu_to_tagged_stream_0_0_0, 'pdus'))
        self.msg_connect((self.pdu_utils_pack_unpack_0, 'pdu_out'), (self.blocks_socket_pdu_1, 'pdus'))
        self.msg_connect((self.vcc_burst_scramble_bb_0, 'out'), (self.pdu_utils_pack_unpack_0, 'pdu_in'))
        self.msg_connect((self.vcc_insert_src_callsign_pdu_0, 'out'), (self.kiss_hdlc_framer_0, 'in'))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_descrambler_bb_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.vcc_insert_time_tag_bb_0_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.vcc_insert_time_tag_bb_0, 0))
        self.connect((self.digital_descrambler_bb_0, 0), (self.kiss_hdlc_deframer_0, 0))
        self.connect((self.vcc_insert_time_tag_bb_0, 0), (self.kiss_kiss_to_pdu_0, 0))
        self.connect((self.vcc_insert_time_tag_bb_0, 0), (self.sigmf_sink_0, 0))
        self.connect((self.vcc_insert_time_tag_bb_0_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.vcc_insert_time_tag_bb_0_0, 0), (self.sigmf_sink_1, 0))

    def get_callsign(self):
        return self.callsign

    def set_callsign(self, callsign):
        self.callsign = callsign
        self.vcc_insert_src_callsign_pdu_0.set_callsign(self.callsign)

    def get_client_port(self):
        return self.client_port

    def set_client_port(self, client_port):
        self.client_port = client_port

    def get_gs_id(self):
        return self.gs_id

    def set_gs_id(self, gs_id):
        self.gs_id = gs_id
        self.set_fn_up("{:s}_{:s}_{:s}".format(self.gs_id, self.sc_id, self.ts_str))
        self.set_fn_dn("{:s}_{:s}_{:s}".format(self.sc_id, self.gs_id, self.ts_str))

    def get_post_bytes(self):
        return self.post_bytes

    def set_post_bytes(self, post_bytes):
        self.post_bytes = post_bytes

    def get_pre_bytes(self):
        return self.pre_bytes

    def set_pre_bytes(self, pre_bytes):
        self.pre_bytes = pre_bytes

    def get_sc_id(self):
        return self.sc_id

    def set_sc_id(self, sc_id):
        self.sc_id = sc_id
        self.set_fn_up("{:s}_{:s}_{:s}".format(self.gs_id, self.sc_id, self.ts_str))
        self.set_fn_dn("{:s}_{:s}_{:s}".format(self.sc_id, self.gs_id, self.ts_str))

    def get_server_ip(self):
        return self.server_ip

    def set_server_ip(self, server_ip):
        self.server_ip = server_ip

    def get_ssid(self):
        return self.ssid

    def set_ssid(self, ssid):
        self.ssid = ssid
        self.vcc_insert_src_callsign_pdu_0.set_ssid(self.ssid)

    def get_verbose(self):
        return self.verbose

    def set_verbose(self, verbose):
        self.verbose = verbose
        self.vcc_insert_src_callsign_pdu_0.set_verbose(bool(self.verbose))

    def get_wallops_dn_port(self):
        return self.wallops_dn_port

    def set_wallops_dn_port(self, wallops_dn_port):
        self.wallops_dn_port = wallops_dn_port

    def get_wallops_up_port(self):
        return self.wallops_up_port

    def set_wallops_up_port(self, wallops_up_port):
        self.wallops_up_port = wallops_up_port

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn_up("{:s}_{:s}_{:s}".format(self.gs_id, self.sc_id, self.ts_str))
        self.set_fn_dn("{:s}_{:s}_{:s}".format(self.sc_id, self.gs_id, self.ts_str))

    def get_fn_up(self):
        return self.fn_up

    def set_fn_up(self, fn_up):
        self.fn_up = fn_up
        self.set_fp_up("/gnuradio/captures/{:s}".format(self.fn_up))

    def get_fn_dn(self):
        return self.fn_dn

    def set_fn_dn(self, fn_dn):
        self.fn_dn = fn_dn
        self.set_fp_dn("/gnuradio/captures/{:s}".format(self.fn_dn))

    def get_fp_up(self):
        return self.fp_up

    def set_fp_up(self, fp_up):
        self.fp_up = fp_up

    def get_fp_dn(self):
        return self.fp_dn

    def set_fp_dn(self, fp_dn):
        self.fp_dn = fp_dn


def argument_parser():
    description = 'Wallops Interface, No GUI'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "-c", "--callsign", dest="callsign", type="string", default='WJ2XMS',
        help="Set WJ2XMS [default=%default]")
    parser.add_option(
        "-p", "--client-port", dest="client_port", type="string", default='8000',
        help="Set 8000 [default=%default]")
    parser.add_option(
        "", "--gs-id", dest="gs_id", type="string", default='WFF',
        help="Set gs_id [default=%default]")
    parser.add_option(
        "", "--post-bytes", dest="post_bytes", type="intx", default=64,
        help="Set post_bytes [default=%default]")
    parser.add_option(
        "", "--pre-bytes", dest="pre_bytes", type="intx", default=64,
        help="Set pre_bytes [default=%default]")
    parser.add_option(
        "", "--sc-id", dest="sc_id", type="string", default='VCC-A',
        help="Set sc_id [default=%default]")
    parser.add_option(
        "-i", "--server-ip", dest="server_ip", type="string", default='0.0.0.0',
        help="Set 0.0.0.0 [default=%default]")
    parser.add_option(
        "-s", "--ssid", dest="ssid", type="intx", default=0,
        help="Set ssid [default=%default]")
    parser.add_option(
        "-v", "--verbose", dest="verbose", type="intx", default=0,
        help="Set verbose [default=%default]")
    parser.add_option(
        "", "--wallops-dn-port", dest="wallops_dn_port", type="string", default='56101',
        help="Set 56101 [default=%default]")
    parser.add_option(
        "", "--wallops-up-port", dest="wallops_up_port", type="string", default='56100',
        help="Set 56100 [default=%default]")
    return parser


def main(top_block_cls=wff_nogui_v3_verbose_recordtx, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(callsign=options.callsign, client_port=options.client_port, gs_id=options.gs_id, post_bytes=options.post_bytes, pre_bytes=options.pre_bytes, sc_id=options.sc_id, server_ip=options.server_ip, ssid=options.ssid, verbose=options.verbose, wallops_dn_port=options.wallops_dn_port, wallops_up_port=options.wallops_up_port)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
