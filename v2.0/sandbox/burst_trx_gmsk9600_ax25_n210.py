#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: VCC Single Channel Command - VT
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
from PyQt4.QtCore import QObject, pyqtSlot
from burst_rx_es_hier import burst_rx_es_hier  # grc-generated hier_block
from datetime import datetime as dt; import string; import math
from fsk_burst_detector import fsk_burst_detector  # grc-generated hier_block
from gmsk_ax25_rx_hier import gmsk_ax25_rx_hier  # grc-generated hier_block
from gmsk_tx_burst_hier_callsign import gmsk_tx_burst_hier_callsign  # grc-generated hier_block
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
import gr_sigmf
import pyqt
import rffe_ctl
import sip
import time
import vcc
from gnuradio import qtgui


class burst_trx_gmsk9600_ax25_n210(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "VCC Single Channel Command - VT")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("VCC Single Channel Command - VT")
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
        # Variables
        ##################################################
        self.tx_freq = tx_freq = 401.12e6
        self.uplink_freq = uplink_freq = tx_freq
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S" )
        self.gs_id = gs_id = "VTGS"
        self.tx_tune = tx_tune = tx_freq - uplink_freq
        self.samp_rate = samp_rate = float(250e3)
        self.man_tune = man_tune = 0.0
        self.fn = fn = "VCC_{:s}_{:s}".format(gs_id, ts_str)
        self.uplink_offset = uplink_offset = -1* tx_tune
        self.tx_tune_sel = tx_tune_sel = 0
        self.tx_sel = tx_sel = [tx_tune, -1*man_tune]
        self.tx_offset = tx_offset = samp_rate/2
        self.tx_gain = tx_gain = 10
        self.trigger_thresh = trigger_thresh = -2
        self.rx_offset = rx_offset = samp_rate/2.0
        self.rx_gain = rx_gain = 20
        self.rx_freq = rx_freq = 401.08e6
        self.interp_2 = interp_2 = 1
        self.interp = interp = 48
        self.fsk_dev = fsk_dev = 10000
        self.fp = fp = "/vtgs/captures/vcc/{:s}".format(fn)
        self.decim_2 = decim_2 = 2
        self.decim = decim = int(samp_rate/2000)
        self.chan_filt_trans = chan_filt_trans = 1000
        self.chan_filt_cutoff = chan_filt_cutoff = 24000
        self.ceres_offset = ceres_offset = 40000
        self.bb_gain = bb_gain = .75

        ##################################################
        # Blocks
        ##################################################
        self.main_tab = Qt.QTabWidget()
        self.main_tab_widget_0 = Qt.QWidget()
        self.main_tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_0)
        self.main_tab_grid_layout_0 = Qt.QGridLayout()
        self.main_tab_layout_0.addLayout(self.main_tab_grid_layout_0)
        self.main_tab.addTab(self.main_tab_widget_0, 'Full Band')
        self.main_tab_widget_1 = Qt.QWidget()
        self.main_tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_1)
        self.main_tab_grid_layout_1 = Qt.QGridLayout()
        self.main_tab_layout_1.addLayout(self.main_tab_grid_layout_1)
        self.main_tab.addTab(self.main_tab_widget_1, 'RX Channel')
        self.main_tab_widget_2 = Qt.QWidget()
        self.main_tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_2)
        self.main_tab_grid_layout_2 = Qt.QGridLayout()
        self.main_tab_layout_2.addLayout(self.main_tab_grid_layout_2)
        self.main_tab.addTab(self.main_tab_widget_2, 'TX Channel')
        self.top_grid_layout.addWidget(self.main_tab, 0, 0, 2, 8)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._tx_tune_sel_options = (0, 1, )
        self._tx_tune_sel_labels = ('Auto', 'Manual', )
        self._tx_tune_sel_tool_bar = Qt.QToolBar(self)
        self._tx_tune_sel_tool_bar.addWidget(Qt.QLabel('TX Tune Mode'+": "))
        self._tx_tune_sel_combo_box = Qt.QComboBox()
        self._tx_tune_sel_tool_bar.addWidget(self._tx_tune_sel_combo_box)
        for label in self._tx_tune_sel_labels: self._tx_tune_sel_combo_box.addItem(label)
        self._tx_tune_sel_callback = lambda i: Qt.QMetaObject.invokeMethod(self._tx_tune_sel_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._tx_tune_sel_options.index(i)))
        self._tx_tune_sel_callback(self.tx_tune_sel)
        self._tx_tune_sel_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_tx_tune_sel(self._tx_tune_sel_options[i]))
        self.main_tab_grid_layout_2.addWidget(self._tx_tune_sel_tool_bar, 3, 1, 1, 1)
        for r in range(3, 4):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._tx_gain_tool_bar = Qt.QToolBar(self)
        self._tx_gain_tool_bar.addWidget(Qt.QLabel('TX Gain'+": "))
        self._tx_gain_line_edit = Qt.QLineEdit(str(self.tx_gain))
        self._tx_gain_tool_bar.addWidget(self._tx_gain_line_edit)
        self._tx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_tx_gain(eng_notation.str_to_num(str(self._tx_gain_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._tx_gain_tool_bar, 2, 3, 1, 1)
        for r in range(2, 3):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._tx_freq_tool_bar = Qt.QToolBar(self)
        self._tx_freq_tool_bar.addWidget(Qt.QLabel('TX Freq'+": "))
        self._tx_freq_line_edit = Qt.QLineEdit(str(self.tx_freq))
        self._tx_freq_tool_bar.addWidget(self._tx_freq_line_edit)
        self._tx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_tx_freq(eng_notation.str_to_num(str(self._tx_freq_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._tx_freq_tool_bar, 2, 0, 1, 1)
        for r in range(2, 3):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._trigger_thresh_tool_bar = Qt.QToolBar(self)
        self._trigger_thresh_tool_bar.addWidget(Qt.QLabel('Trigger Thresh'+": "))
        self._trigger_thresh_line_edit = Qt.QLineEdit(str(self.trigger_thresh))
        self._trigger_thresh_tool_bar.addWidget(self._trigger_thresh_line_edit)
        self._trigger_thresh_line_edit.returnPressed.connect(
        	lambda: self.set_trigger_thresh(eng_notation.str_to_num(str(self._trigger_thresh_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_1.addWidget(self._trigger_thresh_tool_bar, 4, 4, 1, 2)
        for r in range(4, 5):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 6):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel('RX Gain'+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._rx_gain_tool_bar, 4, 2, 1, 2)
        for r in range(4, 5):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('RX Freq'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._rx_freq_tool_bar, 4, 0, 1, 2)
        for r in range(4, 5):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._ceres_offset_tool_bar = Qt.QToolBar(self)
        self._ceres_offset_tool_bar.addWidget(Qt.QLabel('Ceres Offset'+": "))
        self._ceres_offset_line_edit = Qt.QLineEdit(str(self.ceres_offset))
        self._ceres_offset_tool_bar.addWidget(self._ceres_offset_line_edit)
        self._ceres_offset_line_edit.returnPressed.connect(
        	lambda: self.set_ceres_offset(eng_notation.str_to_num(str(self._ceres_offset_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_1.addWidget(self._ceres_offset_tool_bar, 3, 4, 1, 2)
        for r in range(3, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 6):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self._bb_gain_tool_bar = Qt.QToolBar(self)
        self._bb_gain_tool_bar.addWidget(Qt.QLabel('BB Gain'+": "))
        self._bb_gain_line_edit = Qt.QLineEdit(str(self.bb_gain))
        self._bb_gain_tool_bar.addWidget(self._bb_gain_line_edit)
        self._bb_gain_line_edit.returnPressed.connect(
        	lambda: self.set_bb_gain(eng_notation.str_to_num(str(self._bb_gain_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._bb_gain_tool_bar, 2, 2, 1, 1)
        for r in range(2, 3):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.vcc_qt_hex_text_tx_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_tx_0_win = self.vcc_qt_hex_text_tx_0;
        self.main_tab_grid_layout_1.addWidget(self._vcc_qt_hex_text_tx_0_win, 5, 0, 2, 6)
        for r in range(5, 7):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 6):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)

        self.vcc_qt_hex_text_tx = vcc.qt_hex_text()
        self._vcc_qt_hex_text_tx_win = self.vcc_qt_hex_text_tx;
        self.main_tab_grid_layout_2.addWidget(self._vcc_qt_hex_text_tx_win, 0, 0, 2, 2)
        for r in range(0, 2):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)

        self._uplink_offset_tool_bar = Qt.QToolBar(self)

        if None:
          self._uplink_offset_formatter = None
        else:
          self._uplink_offset_formatter = lambda x: eng_notation.num_to_str(x)

        self._uplink_offset_tool_bar.addWidget(Qt.QLabel("uplink_offset"+": "))
        self._uplink_offset_label = Qt.QLabel(str(self._uplink_offset_formatter(self.uplink_offset)))
        self._uplink_offset_tool_bar.addWidget(self._uplink_offset_label)
        self.main_tab_grid_layout_2.addWidget(self._uplink_offset_tool_bar, 2, 1, 1, 1)
        for r in range(2, 3):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
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
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rx_freq, rx_offset), 0)
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
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(tx_freq, tx_offset), 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.sigmf_sink_0 = gr_sigmf.sink("cf32", fp, gr_sigmf.sigmf_time_mode_absolute, False)
        self.sigmf_sink_0.set_global_meta("core:sample_rate", samp_rate)
        self.sigmf_sink_0.set_global_meta("core:description", 'VCC TM/TC v1.0.0, GMSK9600, AX.25, w/ PTT')
        self.sigmf_sink_0.set_global_meta("core:author", 'Zach Leffke')
        self.sigmf_sink_0.set_global_meta("core:license", 'MIT')
        self.sigmf_sink_0.set_global_meta("core:hw", '2X M2 400CP30, ARR Preamp, N210 w/ UBX')

        self.rffe_ctl_tag_ptt_pdu_0 = rffe_ctl.tag_ptt_pdu(samp_rate,"tx_sob","tx_eob","tx_time","TX")
        self.rational_resampler_xxx_4 = filter.rational_resampler_ccc(
                interpolation=interp/2,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_3 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=2,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=2,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_ccc(
                interpolation=interp_2,
                decimation=decim_2,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=interp,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / decim*interp / decim_2 * interp_2, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.0010)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(True)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-50, 50)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0.enable_grid(True)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 1, 0, 1, 8)
        for r in range(1, 2):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 8):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1_0_1 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate, #bw
        	"VCC RX Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0_1.set_update_time(0.0010)
        self.qtgui_freq_sink_x_1_0_1.set_y_axis(-150, -40)
        self.qtgui_freq_sink_x_1_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0_1.enable_grid(True)
        self.qtgui_freq_sink_x_1_0_1.set_fft_average(0.2)
        self.qtgui_freq_sink_x_1_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0_1.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_1_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0_1.set_plot_pos_half(not True)

        labels = ['pre-d', 'agc_filt', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_1_0_1_win, 0, 0, 1, 8)
        for r in range(0, 1):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 8):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim*interp/2, #bw
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
        self.main_tab_grid_layout_2.addWidget(self._qtgui_freq_sink_x_1_0_0_win, 0, 2, 2, 2)
        for r in range(0, 2):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / decim*interp / decim_2 * interp_2, #bw
        	"Ceres Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.0010)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-50, 50)
        self.qtgui_freq_sink_x_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(True)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not True)

        labels = ['pre-d', 'agc_filt', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_1_0_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*interp/decim*interp_2/decim_2, #bw
        	"Burst RX Spectrum", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_1.enable_grid(True)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['orig', 'corr', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_1_win, 0, 4, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.pyqt_text_output_0 = pyqt.text_output()
        self._pyqt_text_output_0_win = self.pyqt_text_output_0;
        self.main_tab_grid_layout_2.addWidget(self._pyqt_text_output_0_win, 4, 0, 1, 4)
        for r in range(4, 5):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)

        self.pyqt_meta_text_output_0 = pyqt.meta_text_output()
        self._pyqt_meta_text_output_0_win = self.pyqt_meta_text_output_0;
        self.main_tab_grid_layout_1.addWidget(self._pyqt_meta_text_output_0_win, 3, 6, 4, 2)
        for r in range(3, 7):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(6, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)

        self._man_tune_tool_bar = Qt.QToolBar(self)
        self._man_tune_tool_bar.addWidget(Qt.QLabel('TX Freq Offset'+": "))
        self._man_tune_line_edit = Qt.QLineEdit(str(self.man_tune))
        self._man_tune_tool_bar.addWidget(self._man_tune_line_edit)
        self._man_tune_line_edit.returnPressed.connect(
        	lambda: self.set_man_tune(eng_notation.str_to_num(str(self._man_tune_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._man_tune_tool_bar, 3, 0, 1, 1)
        for r in range(3, 4):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate / decim *interp, chan_filt_cutoff, chan_filt_trans, firdes.WIN_HAMMING, 6.76))
        self.gpredict_doppler_0 = gpredict.doppler("0.0.0.0", 7356, True)
        self.gpredict_MsgPairToVar_1 = gpredict.MsgPairToVar(self.set_uplink_freq)
        self.gmsk_tx_burst_hier_callsign_0 = gmsk_tx_burst_hier_callsign(
            bb_gain=bb_gain,
            bt=.5,
            delay_enable=1,
            pad_front=0,
            pad_tail=0,
            ptt_delay=0.250,
            samp_rate=250000,
            callsign="WJ2XMS",
            ssid=1,
        )
        self.gmsk_ax25_rx_hier_0 = gmsk_ax25_rx_hier(
            lpf_cutoff=7.2e3,
            lpf_trans=1e3,
            quad_demod_gain=(samp_rate/decim*interp/decim_2*interp_2)/(2*math.pi*fsk_dev/8.0),
            samp_rate=48000,
            samps_per_symb=5,
        )
        self.fsk_burst_detector_0 = fsk_burst_detector(
            avg_len=100.0,
            cons_offset=3,
            decim=decim,
            fsk_dev=fsk_dev,
            interp=interp,
            samp_rate=samp_rate,
        )
        self.burst_rx_es_hier_0 = burst_rx_es_hier(
            avg_len=100,
            baud=9600,
            samp_rate=samp_rate/decim*interp,
            samps_per_symb=10,
            trigger_thresh=trigger_thresh,
        )
        self.blocks_socket_pdu_0_2 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '8000', 1024, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '8001', 1024, True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1 * ceres_offset, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1 * tx_sel[tx_tune_sel], 1, 0)
        self.analog_agc2_xx_0 = analog.agc2_cc(10, 1e-1, 65536, 1)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0, 'pdus'), (self.pyqt_text_output_0, 'pdus'))
        self.msg_connect((self.blocks_socket_pdu_0_2, 'pdus'), (self.gmsk_tx_burst_hier_callsign_0, 'kiss/ax25'))
        self.msg_connect((self.burst_rx_es_hier_0, 'meta'), (self.pyqt_meta_text_output_0, 'pdus'))
        self.msg_connect((self.gmsk_ax25_rx_hier_0, 'kiss'), (self.blocks_socket_pdu_0_2, 'pdus'))
        self.msg_connect((self.gmsk_ax25_rx_hier_0, 'kiss'), (self.vcc_qt_hex_text_tx_0, 'pdus'))
        self.msg_connect((self.gmsk_tx_burst_hier_callsign_0, 'ax25'), (self.vcc_qt_hex_text_tx, 'pdus'))
        self.msg_connect((self.gpredict_doppler_0, 'freq'), (self.gpredict_MsgPairToVar_1, 'inpair'))
        self.msg_connect((self.rffe_ctl_tag_ptt_pdu_0, 'ptt'), (self.blocks_socket_pdu_0, 'pdus'))
        self.connect((self.analog_agc2_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_4, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.burst_rx_es_hier_0, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.burst_rx_es_hier_0, 1), (self.rational_resampler_xxx_3, 0))
        self.connect((self.fsk_burst_detector_0, 0), (self.burst_rx_es_hier_0, 1))
        self.connect((self.gmsk_ax25_rx_hier_0, 0), (self.qtgui_freq_sink_x_1, 1))
        self.connect((self.gmsk_tx_burst_hier_callsign_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.gmsk_tx_burst_hier_callsign_0, 0), (self.rffe_ctl_tag_ptt_pdu_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.burst_rx_es_hier_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.fsk_burst_detector_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.rational_resampler_xxx_3, 0), (self.gmsk_ax25_rx_hier_0, 0))
        self.connect((self.rational_resampler_xxx_4, 0), (self.qtgui_freq_sink_x_1_0_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.qtgui_freq_sink_x_1_0_1, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.sigmf_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "burst_trx_gmsk9600_ax25_n210")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tx_freq(self):
        return self.tx_freq

    def set_tx_freq(self, tx_freq):
        self.tx_freq = tx_freq
        Qt.QMetaObject.invokeMethod(self._tx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.tx_freq)))
        self.set_uplink_freq(self.tx_freq)
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(self.tx_freq, self.tx_offset), 0)
        self.set_tx_tune(self.tx_freq - self.uplink_freq)

    def get_uplink_freq(self):
        return self.uplink_freq

    def set_uplink_freq(self, uplink_freq):
        self.uplink_freq = uplink_freq
        self.set_tx_tune(self.tx_freq - self.uplink_freq)

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn("VCC_{:s}_{:s}".format(self.gs_id, self.ts_str))

    def get_gs_id(self):
        return self.gs_id

    def set_gs_id(self, gs_id):
        self.gs_id = gs_id
        self.set_fn("VCC_{:s}_{:s}".format(self.gs_id, self.ts_str))

    def get_tx_tune(self):
        return self.tx_tune

    def set_tx_tune(self, tx_tune):
        self.tx_tune = tx_tune
        self.set_tx_sel([self.tx_tune, -1*self.man_tune])
        self.set_uplink_offset(self._uplink_offset_formatter(-1* self.tx_tune))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_tx_offset(self.samp_rate/2)
        self.set_rx_offset(self.samp_rate/2.0)
        self.set_decim(int(self.samp_rate/2000))
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate)
        self.qtgui_freq_sink_x_1_0_1.set_frequency_range(self.rx_freq, self.samp_rate)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp/2)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.chan_filt_cutoff, self.chan_filt_trans, firdes.WIN_HAMMING, 6.76))
        self.gmsk_ax25_rx_hier_0.set_quad_demod_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.fsk_burst_detector_0.set_samp_rate(self.samp_rate)
        self.burst_rx_es_hier_0.set_samp_rate(self.samp_rate/self.decim*self.interp)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_man_tune(self):
        return self.man_tune

    def set_man_tune(self, man_tune):
        self.man_tune = man_tune
        self.set_tx_sel([self.tx_tune, -1*self.man_tune])
        Qt.QMetaObject.invokeMethod(self._man_tune_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.man_tune)))

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn
        self.set_fp("/vtgs/captures/vcc/{:s}".format(self.fn))

    def get_uplink_offset(self):
        return self.uplink_offset

    def set_uplink_offset(self, uplink_offset):
        self.uplink_offset = uplink_offset
        Qt.QMetaObject.invokeMethod(self._uplink_offset_label, "setText", Qt.Q_ARG("QString", self.uplink_offset))

    def get_tx_tune_sel(self):
        return self.tx_tune_sel

    def set_tx_tune_sel(self, tx_tune_sel):
        self.tx_tune_sel = tx_tune_sel
        self._tx_tune_sel_callback(self.tx_tune_sel)
        self.analog_sig_source_x_0.set_frequency(-1 * self.tx_sel[self.tx_tune_sel])

    def get_tx_sel(self):
        return self.tx_sel

    def set_tx_sel(self, tx_sel):
        self.tx_sel = tx_sel
        self.analog_sig_source_x_0.set_frequency(-1 * self.tx_sel[self.tx_tune_sel])

    def get_tx_offset(self):
        return self.tx_offset

    def set_tx_offset(self, tx_offset):
        self.tx_offset = tx_offset
        self.uhd_usrp_sink_0.set_center_freq(uhd.tune_request(self.tx_freq, self.tx_offset), 0)

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        Qt.QMetaObject.invokeMethod(self._tx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.tx_gain)))
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)


    def get_trigger_thresh(self):
        return self.trigger_thresh

    def set_trigger_thresh(self, trigger_thresh):
        self.trigger_thresh = trigger_thresh
        Qt.QMetaObject.invokeMethod(self._trigger_thresh_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.trigger_thresh)))
        self.burst_rx_es_hier_0.set_trigger_thresh(self.trigger_thresh)

    def get_rx_offset(self):
        return self.rx_offset

    def set_rx_offset(self, rx_offset):
        self.rx_offset = rx_offset
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.rx_offset), 0)

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
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.rx_offset), 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate)
        self.qtgui_freq_sink_x_1_0_1.set_frequency_range(self.rx_freq, self.samp_rate)

    def get_interp_2(self):
        return self.interp_2

    def set_interp_2(self, interp_2):
        self.interp_2 = interp_2
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.gmsk_ax25_rx_hier_0.set_quad_demod_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp/2)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.chan_filt_cutoff, self.chan_filt_trans, firdes.WIN_HAMMING, 6.76))
        self.gmsk_ax25_rx_hier_0.set_quad_demod_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.fsk_burst_detector_0.set_interp(self.interp)
        self.burst_rx_es_hier_0.set_samp_rate(self.samp_rate/self.decim*self.interp)

    def get_fsk_dev(self):
        return self.fsk_dev

    def set_fsk_dev(self, fsk_dev):
        self.fsk_dev = fsk_dev
        self.gmsk_ax25_rx_hier_0.set_quad_demod_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.fsk_burst_detector_0.set_fsk_dev(self.fsk_dev)

    def get_fp(self):
        return self.fp

    def set_fp(self, fp):
        self.fp = fp

    def get_decim_2(self):
        return self.decim_2

    def set_decim_2(self, decim_2):
        self.decim_2 = decim_2
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.gmsk_ax25_rx_hier_0.set_quad_demod_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate/self.decim*self.interp/2)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.chan_filt_cutoff, self.chan_filt_trans, firdes.WIN_HAMMING, 6.76))
        self.gmsk_ax25_rx_hier_0.set_quad_demod_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.fsk_burst_detector_0.set_decim(self.decim)
        self.burst_rx_es_hier_0.set_samp_rate(self.samp_rate/self.decim*self.interp)

    def get_chan_filt_trans(self):
        return self.chan_filt_trans

    def set_chan_filt_trans(self, chan_filt_trans):
        self.chan_filt_trans = chan_filt_trans
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.chan_filt_cutoff, self.chan_filt_trans, firdes.WIN_HAMMING, 6.76))

    def get_chan_filt_cutoff(self):
        return self.chan_filt_cutoff

    def set_chan_filt_cutoff(self, chan_filt_cutoff):
        self.chan_filt_cutoff = chan_filt_cutoff
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.chan_filt_cutoff, self.chan_filt_trans, firdes.WIN_HAMMING, 6.76))

    def get_ceres_offset(self):
        return self.ceres_offset

    def set_ceres_offset(self, ceres_offset):
        self.ceres_offset = ceres_offset
        Qt.QMetaObject.invokeMethod(self._ceres_offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ceres_offset)))
        self.analog_sig_source_x_0_0.set_frequency(-1 * self.ceres_offset)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        Qt.QMetaObject.invokeMethod(self._bb_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.bb_gain)))
        self.gmsk_tx_burst_hier_callsign_0.set_bb_gain(self.bb_gain)


def main(top_block_cls=burst_trx_gmsk9600_ax25_n210, options=None):

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
