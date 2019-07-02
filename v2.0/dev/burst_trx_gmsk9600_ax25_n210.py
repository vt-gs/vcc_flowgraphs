#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Burst Trx Gmsk9600 Ax25 N210
# Author: Zach Leffke, KJ4QLP
# Description: VCC Burst TX/RX, 9600 Baud GMSK, AX.25
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

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from datetime import datetime as dt; import string
from gmsk_tx_burst_hier2 import gmsk_tx_burst_hier2  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import gpredict
import pyqt
import rffe_ctl
import sip
import time
import vcc
from gnuradio import qtgui


class burst_trx_gmsk9600_ax25_n210(gr.top_block, Qt.QWidget):

    def __init__(self, rf_freq=401.12e6):
        gr.top_block.__init__(self, "Burst Trx Gmsk9600 Ax25 N210")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Burst Trx Gmsk9600 Ax25 N210")
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

        self.settings = Qt.QSettings("GNU Radio", "burst_trx_gmsk9600_ax25_n210")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.rf_freq = rf_freq

        ##################################################
        # Variables
        ##################################################
        self.uplink_freq = uplink_freq = rf_freq
        self.tx_tune = tx_tune = rf_freq - uplink_freq
        self.samp_rate = samp_rate = float(250e3)
        self.uplink_offset = uplink_offset = -1* tx_tune
        self.tx_offset = tx_offset = 0
        self.tx_gain = tx_gain = 10
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.rx_offset = rx_offset = samp_rate/2.0
        self.rx_gain = rx_gain = 10
        self.rx_freq = rx_freq = 401.12e6
        self.interp = interp = 24
        self.decim = decim = int(samp_rate/2000)
        self.bb_gain = bb_gain = .75

        ##################################################
        # Blocks
        ##################################################
        self._tx_gain_tool_bar = Qt.QToolBar(self)
        self._tx_gain_tool_bar.addWidget(Qt.QLabel('TX Gain'+": "))
        self._tx_gain_line_edit = Qt.QLineEdit(str(self.tx_gain))
        self._tx_gain_tool_bar.addWidget(self._tx_gain_line_edit)
        self._tx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_tx_gain(eng_notation.str_to_num(str(self._tx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._tx_gain_tool_bar, 4, 2, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel('RX Gain'+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 5, 4, 1, 2)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._bb_gain_tool_bar = Qt.QToolBar(self)
        self._bb_gain_tool_bar.addWidget(Qt.QLabel('BB Gain'+": "))
        self._bb_gain_line_edit = Qt.QLineEdit(str(self.bb_gain))
        self._bb_gain_tool_bar.addWidget(self._bb_gain_line_edit)
        self._bb_gain_line_edit.returnPressed.connect(
        	lambda: self.set_bb_gain(eng_notation.str_to_num(str(self._bb_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._bb_gain_tool_bar, 4, 0, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.vcc_qt_hex_text_tx = vcc.qt_hex_text()
        self._vcc_qt_hex_text_tx_win = self.vcc_qt_hex_text_tx;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_tx_win, 6, 0, 2, 4)
        for r in range(6, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)

        self._uplink_offset_tool_bar = Qt.QToolBar(self)

        if None:
          self._uplink_offset_formatter = None
        else:
          self._uplink_offset_formatter = lambda x: eng_notation.num_to_str(x)

        self._uplink_offset_tool_bar.addWidget(Qt.QLabel("uplink_offset"+": "))
        self._uplink_offset_label = Qt.QLabel(str(self._uplink_offset_formatter(self.uplink_offset)))
        self._uplink_offset_tool_bar.addWidget(self._uplink_offset_label)
        self.top_grid_layout.addWidget(self._uplink_offset_tool_bar, 5, 0, 1, 2)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_1.set_clock_source('external', 0)
        self.uhd_usrp_source_1.set_time_source('external', 0)
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rf_freq, rx_offset), 0)
        self.uhd_usrp_source_1.set_gain(rx_gain, 0)
        self.uhd_usrp_source_1.set_antenna('RX2', 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.10.6", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_clock_source('external', 0)
        self.uhd_usrp_sink_0.set_time_source('external', 0)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(rf_freq, tx_offset), 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('RX Freq'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 4, 4, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rffe_ctl_tag_ptt_pdu_0 = rffe_ctl.tag_ptt_pdu(samp_rate,"tx_sob","tx_eob","tx_time","TX")
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=interp,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=interp,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_1_0_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim*interp, #bw
        	"RX Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_1_0_0_0.set_y_axis(-150, 0)
        self.qtgui_freq_sink_x_1_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_1_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0_0_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_1_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pyqt_text_output_0 = pyqt.text_output()
        self._pyqt_text_output_0_win = self.pyqt_text_output_0;
        self.top_grid_layout.addWidget(self._pyqt_text_output_0_win, 8, 0, 2, 4)
        for r in range(8, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.gpredict_doppler_0 = gpredict.doppler("0.0.0.0", 7356, False)
        self.gpredict_MsgPairToVar_1 = gpredict.MsgPairToVar(self.set_uplink_freq)
        self.gmsk_tx_burst_hier2_0 = gmsk_tx_burst_hier2(
            bt=.5,
            delay_enable=1,
            pad_front=0,
            pad_tail=0,
            ptt_delay=.200,
            samp_rate=samp_rate,
        )
        self.blocks_tag_debug_1 = blocks.tag_debug(gr.sizeof_gr_complex*1, '', ""); self.blocks_tag_debug_1.set_display(True)
        self.blocks_socket_pdu_0_2 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '8000', 1024, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '8001', 1024, True)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((bb_gain, ))
        self.blocks_message_debug_0 = blocks.message_debug()
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1 * tx_tune, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0, 'pdus'), (self.pyqt_text_output_0, 'pdus'))
        self.msg_connect((self.blocks_socket_pdu_0_2, 'pdus'), (self.gmsk_tx_burst_hier2_0, 'kiss/ax25'))
        self.msg_connect((self.gmsk_tx_burst_hier2_0, 'ax25'), (self.vcc_qt_hex_text_tx, 'pdus'))
        self.msg_connect((self.gpredict_doppler_0, 'freq'), (self.gpredict_MsgPairToVar_1, 'inpair'))
        self.msg_connect((self.rffe_ctl_tag_ptt_pdu_0, 'ptt'), (self.blocks_socket_pdu_0, 'pdus'))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.gmsk_tx_burst_hier2_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.gmsk_tx_burst_hier2_0, 0), (self.blocks_tag_debug_1, 0))
        self.connect((self.gmsk_tx_burst_hier2_0, 0), (self.rffe_ctl_tag_ptt_pdu_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_1_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_1_0_0_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.rational_resampler_xxx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "burst_trx_gmsk9600_ax25_n210")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq
        self.set_tx_tune(self.rf_freq - self.uplink_freq)
        self.set_uplink_freq(self.rf_freq)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rf_freq, self.rx_offset), 0)
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(self.rf_freq, self.tx_offset), 0)

    def get_uplink_freq(self):
        return self.uplink_freq

    def set_uplink_freq(self, uplink_freq):
        self.uplink_freq = uplink_freq
        self.set_tx_tune(self.rf_freq - self.uplink_freq)

    def get_tx_tune(self):
        return self.tx_tune

    def set_tx_tune(self, tx_tune):
        self.tx_tune = tx_tune
        self.set_uplink_offset(self._uplink_offset_formatter(-1* self.tx_tune))
        self.analog_sig_source_x_0.set_frequency(-1 * self.tx_tune)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_rx_offset(self.samp_rate/2.0)
        self.set_decim(int(self.samp_rate/2000))
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1_0_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp)
        self.gmsk_tx_burst_hier2_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_uplink_offset(self):
        return self.uplink_offset

    def set_uplink_offset(self, uplink_offset):
        self.uplink_offset = uplink_offset
        Qt.QMetaObject.invokeMethod(self._uplink_offset_label, "setText", Qt.Q_ARG("QString", self.uplink_offset))

    def get_tx_offset(self):
        return self.tx_offset

    def set_tx_offset(self, tx_offset):
        self.tx_offset = tx_offset
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(self.rf_freq, self.tx_offset), 0)

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        Qt.QMetaObject.invokeMethod(self._tx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.tx_gain)))
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)


    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str

    def get_rx_offset(self):
        return self.rx_offset

    def set_rx_offset(self, rx_offset):
        self.rx_offset = rx_offset
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rf_freq, self.rx_offset), 0)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.uhd_usrp_source_1.set_gain(self.rx_gain, 0)


    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp
        self.qtgui_freq_sink_x_1_0_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_freq_sink_x_1_0_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        Qt.QMetaObject.invokeMethod(self._bb_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.bb_gain)))
        self.blocks_multiply_const_vxx_0.set_k((self.bb_gain, ))


def argument_parser():
    description = 'VCC Burst TX/RX, 9600 Baud GMSK, AX.25'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "", "--rf-freq", dest="rf_freq", type="eng_float", default=eng_notation.num_to_str(401.12e6),
        help="Set rf_freq [default=%default]")
    return parser


def main(top_block_cls=burst_trx_gmsk9600_ax25_n210, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(rf_freq=options.rf_freq)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
