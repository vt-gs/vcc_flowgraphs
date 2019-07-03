#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Burst RX Processor
# Description: Event Stream Based Burst Processor
# GNU Radio version: 3.7.13.5
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import burst
import es
import pdu_utils
import pmt
import sys
import vcc
from gnuradio import qtgui


class burst_rx_es_hier(gr.top_block, Qt.QWidget):

    def __init__(self, avg_len=100, baud=9600, samp_rate=96000, samps_per_symb=10, trigger_thresh=-2):
        gr.top_block.__init__(self, "Burst RX Processor")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Burst RX Processor")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "burst_rx_es_hier")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.avg_len = avg_len
        self.baud = baud
        self.samp_rate = samp_rate
        self.samps_per_symb = samps_per_symb
        self.trigger_thresh = trigger_thresh

        ##################################################
        # Blocks
        ##################################################
        self.vcc_trigger_timestamp_pdu_0 = vcc.trigger_timestamp_pdu(threshold=trigger_thresh)
        self.vcc_burst_snr_0 = vcc.burst_snr(avg_len, samps_per_symb)
        self.vcc_burst_cfo_est_gmsk_0 = vcc.burst_cfo_est_gmsk(samp_rate)
        self.pdu_utils_extract_metadata_0_0 = pdu_utils.extract_metadata(pmt.intern("snr"), 1.0, 0.0)
        self.pdu_utils_extract_metadata_0 = pdu_utils.extract_metadata(pmt.intern("cfo_est"), 1.0, 0.0)
        self.es_trigger_edge_f_0 = es.trigger_edge_f(trigger_thresh,int(samp_rate / 2.0),avg_len * 2,gr.sizeof_gr_complex,300)
        self.es_sink_0 = es.sink(1*[gr.sizeof_gr_complex],4,64,0,2,0)
        self.es_handler_pdu_0 = es.es_make_handler_pdu(es.es_handler_print.TYPE_C32)
        self.burst_length_detect_c_0 = burst.length_detect_c()
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.complex_t, 'est_len')
        (self.blocks_pdu_to_tagged_stream_0_0).set_min_output_buffer(48000)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.complex_t, 'est_len')
        (self.blocks_pdu_to_tagged_stream_0).set_min_output_buffer(48000)
        self.blocks_pdu_remove_0 = blocks.pdu_remove(pmt.intern("es::event_buffer"))



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_pdu_remove_0, 'pdus'), (self.burst_length_detect_c_0, 'cpdus'))
        self.msg_connect((self.burst_length_detect_c_0, 'cpdus'), (self.vcc_burst_snr_0, 'in'))
        self.msg_connect((self.es_handler_pdu_0, 'pdus_out'), (self.blocks_pdu_remove_0, 'pdus'))
        self.msg_connect((self.es_trigger_edge_f_0, 'edge_event'), (self.es_handler_pdu_0, 'handle_event'))
        self.msg_connect((self.es_trigger_edge_f_0, 'which_stream'), (self.es_sink_0, 'schedule_event'))
        self.msg_connect((self.pdu_utils_extract_metadata_0, 'msg'), (self, 'meta'))
        self.msg_connect((self.pdu_utils_extract_metadata_0_0, 'msg'), (self, 'meta'))
        self.msg_connect((self.vcc_burst_cfo_est_gmsk_0, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.vcc_burst_cfo_est_gmsk_0, 'corrected'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.vcc_burst_cfo_est_gmsk_0, 'corrected'), (self.pdu_utils_extract_metadata_0, 'dict'))
        self.msg_connect((self.vcc_burst_snr_0, 'out'), (self.pdu_utils_extract_metadata_0_0, 'dict'))
        self.msg_connect((self.vcc_burst_snr_0, 'out'), (self.vcc_burst_cfo_est_gmsk_0, 'in'))
        self.msg_connect((self.vcc_trigger_timestamp_pdu_0, 'ts'), (self, 'meta'))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self, 1))
        self.connect((self.es_trigger_edge_f_0, 0), (self.es_sink_0, 0))
        self.connect((self, 0), (self.es_trigger_edge_f_0, 1))
        self.connect((self, 1), (self.es_trigger_edge_f_0, 0))
        self.connect((self, 1), (self.vcc_trigger_timestamp_pdu_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "burst_rx_es_hier")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_avg_len(self):
        return self.avg_len

    def set_avg_len(self, avg_len):
        self.avg_len = avg_len
        self.vcc_burst_snr_0.set_length(self.avg_len)

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb
        self.vcc_burst_snr_0.set_sps(self.samps_per_symb)

    def get_trigger_thresh(self):
        return self.trigger_thresh

    def set_trigger_thresh(self, trigger_thresh):
        self.trigger_thresh = trigger_thresh
        self.vcc_trigger_timestamp_pdu_0.set_threshold(self.trigger_thresh)
        self.es_trigger_edge_f_0.set_thresh(self.trigger_thresh)


def argument_parser():
    description = 'Event Stream Based Burst Processor'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "", "--avg-len", dest="avg_len", type="intx", default=100,
        help="Set Avgerage Length [default=%default]")
    parser.add_option(
        "", "--baud", dest="baud", type="eng_float", default=eng_notation.num_to_str(9600),
        help="Set Symbol Rate [default=%default]")
    parser.add_option(
        "", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(96000),
        help="Set Sample Rate [default=%default]")
    parser.add_option(
        "", "--samps-per-symb", dest="samps_per_symb", type="eng_float", default=eng_notation.num_to_str(10),
        help="Set Samps / Symb [default=%default]")
    parser.add_option(
        "", "--trigger-thresh", dest="trigger_thresh", type="eng_float", default=eng_notation.num_to_str(-2),
        help="Set Trigger Threshold [default=%default]")
    return parser


def main(top_block_cls=burst_rx_es_hier, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(avg_len=options.avg_len, baud=options.baud, samp_rate=options.samp_rate, samps_per_symb=options.samps_per_symb, trigger_thresh=options.trigger_thresh)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
