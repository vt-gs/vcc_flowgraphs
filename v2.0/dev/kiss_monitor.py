#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Kiss Monitor
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
import kiss
import sys
import vcc
from gnuradio import qtgui


class kiss_monitor(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Kiss Monitor")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Kiss Monitor")
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

        self.settings = Qt.QSettings("GNU Radio", "kiss_monitor")
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
        self.kiss_kiss_to_pdu_0 = kiss.kiss_to_pdu(True)
        self.blocks_socket_pdu_0_2 = blocks.socket_pdu("TCP_SERVER", '10.42.0.21', '8000', 1024, False)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0_2, 'pdus'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.kiss_kiss_to_pdu_0, 'out'), (self.vcc_qt_hex_text_0, 'pdus'))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.kiss_kiss_to_pdu_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "kiss_monitor")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


def main(top_block_cls=kiss_monitor, options=None):

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
