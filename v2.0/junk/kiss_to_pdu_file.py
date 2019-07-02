#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Kiss To Pdu File
# GNU Radio version: 3.7.13.4
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
import kiss
import message_tools
import sys
import vcc
from gnuradio import qtgui


class kiss_to_pdu_file(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Kiss To Pdu File")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Kiss To Pdu File")
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

        self.settings = Qt.QSettings("GNU Radio", "kiss_to_pdu_file")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.vcc_qt_hex_text_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_0_win = self.vcc_qt_hex_text_0;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_0_win)
        self.message_tools_message_file_sink_0 = message_tools.message_file_sink('/home/zleffke/github/vtgs/vcc_flowgraphs/v2.0/dev/hdlc_test_frame.pdu',False)
        self.message_tools_message_file_sink_0.set_unbuffered(False)
        self.kiss_kiss_to_pdu_0 = kiss.kiss_to_pdu(True)
        self.kiss_hdlc_framer_0 = kiss.hdlc_framer(preamble_bytes=64, postamble_bytes=64)
        self.blocks_socket_pdu_0_2 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '8000', 1024, False)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0_2, 'pdus'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.kiss_hdlc_framer_0, 'out'), (self.message_tools_message_file_sink_0, 'print_pdu'))
        self.msg_connect((self.kiss_hdlc_framer_0, 'out'), (self.vcc_qt_hex_text_0, 'pdus'))
        self.msg_connect((self.kiss_kiss_to_pdu_0, 'out'), (self.kiss_hdlc_framer_0, 'in'))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.kiss_kiss_to_pdu_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "kiss_to_pdu_file")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


def main(top_block_cls=kiss_to_pdu_file, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
