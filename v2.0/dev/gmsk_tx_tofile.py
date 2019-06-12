#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: VCC Simple Transceiver, CERES_FILESIM_20190512_222916.422921_UTC_250k.fc32
# Author: Zach Leffke, KJ4QLP
# Description: Generates GMSK spectrum, records to file
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from datetime import datetime as dt; import string
from fsk_tx_hier import fsk_tx_hier  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import vcc
from gnuradio import qtgui


class gmsk_tx_tofile(gr.top_block, Qt.QWidget):

    def __init__(self, mode='FILESIM', sat_name='CERES'):
        gr.top_block.__init__(self, "VCC Simple Transceiver, CERES_FILESIM_20190512_222916.422921_UTC_250k.fc32")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("VCC Simple Transceiver, CERES_FILESIM_20190512_222916.422921_UTC_250k.fc32")
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

        self.settings = Qt.QSettings("GNU Radio", "gmsk_tx_tofile")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.mode = mode
        self.sat_name = sat_name

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.samp_rate = samp_rate = float(250000)
        self.fn = fn = "{:s}_{:s}_{:s}_{:s}k.fc32".format(sat_name, mode, ts_str, str(int(samp_rate/1e3)))
        self.interp = interp = 24
        self.fp = fp = "/captures/{:s}".format(fn)
        self.decim = decim = int(samp_rate/2000)
        self.bb_gain = bb_gain = .75

        ##################################################
        # Blocks
        ##################################################
        self._bb_gain_range = Range(0, 1, .01, .75, 200)
        self._bb_gain_win = RangeWidget(self._bb_gain_range, self.set_bb_gain, 'TX bb_gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._bb_gain_win, 4, 10, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(10, 12):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.vcc_qt_hex_text_tx = vcc.qt_hex_text()
        self._vcc_qt_hex_text_tx_win = self.vcc_qt_hex_text_tx;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_tx_win, 6, 8, 2, 4)
        for r in range(6, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(8, 12):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=interp,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_1_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim*interp, #bw
        	"TX Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_1_0_0.set_y_axis(-150, 0)
        self.qtgui_freq_sink_x_1_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_1_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_1_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_0_win, 0, 8, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(8, 12):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fsk_tx_hier_0 = fsk_tx_hier(
            bb_gain=0.75,
            bt=.5,
            samp_rate=250000,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_socket_pdu_0_2 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '8000', 1024, False)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0_2, 'pdus'), (self.fsk_tx_hier_0, 'kiss/ax25'))
        self.msg_connect((self.fsk_tx_hier_0, 'out'), (self.vcc_qt_hex_text_tx, 'pdus'))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.fsk_tx_hier_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_1_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "gmsk_tx_tofile")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_mode(self):
        return self.mode

    def set_mode(self, mode):
        self.mode = mode
        self.set_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.sat_name, self.mode, self.ts_str, str(int(self.samp_rate/1e3))))

    def get_sat_name(self):
        return self.sat_name

    def set_sat_name(self, sat_name):
        self.sat_name = sat_name
        self.set_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.sat_name, self.mode, self.ts_str, str(int(self.samp_rate/1e3))))

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.sat_name, self.mode, self.ts_str, str(int(self.samp_rate/1e3))))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_decim(int(self.samp_rate/2000))
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp)
        self.set_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.sat_name, self.mode, self.ts_str, str(int(self.samp_rate/1e3))))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn
        self.set_fp("/captures/{:s}".format(self.fn))

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp)

    def get_fp(self):
        return self.fp

    def set_fp(self, fp):
        self.fp = fp

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain


def argument_parser():
    description = 'Generates GMSK spectrum, records to file'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "", "--mode", dest="mode", type="string", default='FILESIM',
        help="Set mode [default=%default]")
    parser.add_option(
        "", "--sat-name", dest="sat_name", type="string", default='CERES',
        help="Set sat_name [default=%default]")
    return parser


def main(top_block_cls=gmsk_tx_tofile, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(mode=options.mode, sat_name=options.sat_name)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
