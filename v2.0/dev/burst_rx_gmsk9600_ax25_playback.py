#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: VCC Burst TX/RX, 9600 Baud GMSK, AX.25, w/ PTT
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
from burst_rx_es_hier import burst_rx_es_hier  # grc-generated hier_block
from datetime import datetime as dt; import string; import math
from fsk_burst_detector import fsk_burst_detector  # grc-generated hier_block
from gmsk_ax25_rx_hier import gmsk_ax25_rx_hier  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import gr_sigmf
import pyqt
import sip
import vcc
from gnuradio import qtgui


class burst_rx_gmsk9600_ax25_playback(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "VCC Burst TX/RX, 9600 Baud GMSK, AX.25, w/ PTT")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("VCC Burst TX/RX, 9600 Baud GMSK, AX.25, w/ PTT")
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

        self.settings = Qt.QSettings("GNU Radio", "burst_rx_gmsk9600_ax25_playback")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S" )
        self.gs_id = gs_id = "VTGS"
        self.samp_rate = samp_rate = float(250e3)
        self.fn = fn = "VCC_{:s}_{:s}".format(gs_id, ts_str)
        self.trigger_thresh = trigger_thresh = 2
        self.rx_offset = rx_offset = samp_rate/2.0
        self.rx_gain = rx_gain = 20
        self.rx_freq = rx_freq = 401.08e6
        self.rate_factor = rate_factor = .5
        self.interp_2 = interp_2 = 1
        self.interp = interp = 48
        self.fsk_dev = fsk_dev = 10000
        self.fp = fp = "/vtgs/captures/vcc/{:s}".format(fn)
        self.fine_offset = fine_offset = 0
        self.filt_cut = filt_cut = 8e3
        self.decim_2 = decim_2 = 4
        self.decim = decim = int(samp_rate/2000)
        self.chan_filt_trans = chan_filt_trans = 1000
        self.chan_filt_cutoff = chan_filt_cutoff = 24000
        self.ceres_offset = ceres_offset = -40e3

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
        self.top_grid_layout.addWidget(self.main_tab, 0, 0, 2, 8)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self._rate_factor_tool_bar = Qt.QToolBar(self)
        self._rate_factor_tool_bar.addWidget(Qt.QLabel("rate_factor"+": "))
        self._rate_factor_line_edit = Qt.QLineEdit(str(self.rate_factor))
        self._rate_factor_tool_bar.addWidget(self._rate_factor_line_edit)
        self._rate_factor_line_edit.returnPressed.connect(
        	lambda: self.set_rate_factor(eng_notation.str_to_num(str(self._rate_factor_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rate_factor_tool_bar, 2, 0, 1, 8)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fine_offset_tool_bar = Qt.QToolBar(self)
        self._fine_offset_tool_bar.addWidget(Qt.QLabel("fine_offset"+": "))
        self._fine_offset_line_edit = Qt.QLineEdit(str(self.fine_offset))
        self._fine_offset_tool_bar.addWidget(self._fine_offset_line_edit)
        self._fine_offset_line_edit.returnPressed.connect(
        	lambda: self.set_fine_offset(eng_notation.str_to_num(str(self._fine_offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fine_offset_tool_bar)
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
        self.vcc_qt_hex_text_tx_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_tx_0_win = self.vcc_qt_hex_text_tx_0;
        self.main_tab_grid_layout_1.addWidget(self._vcc_qt_hex_text_tx_0_win, 5, 0, 2, 6)
        for r in range(5, 7):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 6):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)

        self.sigmf_source_0 = gr_sigmf.source('/vtgs/captures/vcc/VCC_VTGS_20191227_155437.sigmf-data', "cf32" + ("_le" if sys.byteorder == "little" else "_be"), False)
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
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.010)
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
        self.qtgui_waterfall_sink_x_0.set_update_time(0.0010)
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
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Threshold", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0.set_y_axis(-10, 10)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_win, 2, 4, 1, 4)
        for r in range(2, 3):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1_0_1 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate, #bw
        	"VCC RX Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0_1.set_update_time(0.0010)
        self.qtgui_freq_sink_x_1_0_1.set_y_axis(-130, -60)
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
        self.pyqt_meta_text_output_0 = pyqt.meta_text_output()
        self._pyqt_meta_text_output_0_win = self.pyqt_meta_text_output_0;
        self.main_tab_grid_layout_1.addWidget(self._pyqt_meta_text_output_0_win, 3, 6, 4, 2)
        for r in range(3, 7):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(6, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)

        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate / decim *interp, chan_filt_cutoff, chan_filt_trans, firdes.WIN_HAMMING, 6.76))
        self.gmsk_ax25_rx_hier_0 = gmsk_ax25_rx_hier(
            lpf_cutoff=7.2e3,
            lpf_trans=1e3,
            quad_demod_gain=(samp_rate/decim*interp/decim_2*interp_2)/(2*math.pi*fsk_dev/8.0),
            samp_rate=48000,
            samps_per_symb=5,
        )
        self.fsk_burst_detector_0 = fsk_burst_detector(
            avg_len=100,
            cons_offset=3,
            decim=decim,
            fsk_dev=fsk_dev,
            interp=interp,
            samp_rate=samp_rate,
        )
        self._filt_cut_tool_bar = Qt.QToolBar(self)
        self._filt_cut_tool_bar.addWidget(Qt.QLabel("filt_cut"+": "))
        self._filt_cut_line_edit = Qt.QLineEdit(str(self.filt_cut))
        self._filt_cut_tool_bar.addWidget(self._filt_cut_line_edit)
        self._filt_cut_line_edit.returnPressed.connect(
        	lambda: self.set_filt_cut(eng_notation.str_to_num(str(self._filt_cut_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._filt_cut_tool_bar)
        self.burst_rx_es_hier_0 = burst_rx_es_hier(
            avg_len=100,
            baud=9600,
            samp_rate=samp_rate/decim*interp,
            samps_per_symb=10,
            trigger_thresh=trigger_thresh,
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*rate_factor,True)
        self.blocks_socket_pdu_0_2 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '8000', 1024, False)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate *interp /decim, analog.GR_COS_WAVE, -1 * fine_offset, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1 * ceres_offset, 1, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, trigger_thresh)
        self.analog_agc2_xx_0 = analog.agc2_cc(10, 1e-1, 65536, 1)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.burst_rx_es_hier_0, 'meta'), (self.pyqt_meta_text_output_0, 'pdus'))
        self.msg_connect((self.gmsk_ax25_rx_hier_0, 'kiss'), (self.blocks_socket_pdu_0_2, 'pdus'))
        self.msg_connect((self.gmsk_ax25_rx_hier_0, 'kiss'), (self.vcc_qt_hex_text_tx_0, 'pdus'))
        self.connect((self.analog_agc2_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.burst_rx_es_hier_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.fsk_burst_detector_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_1_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.burst_rx_es_hier_0, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.burst_rx_es_hier_0, 1), (self.rational_resampler_xxx_3, 0))
        self.connect((self.fsk_burst_detector_0, 0), (self.burst_rx_es_hier_0, 1))
        self.connect((self.fsk_burst_detector_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.gmsk_ax25_rx_hier_0, 0), (self.qtgui_freq_sink_x_1, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.rational_resampler_xxx_3, 0), (self.gmsk_ax25_rx_hier_0, 0))
        self.connect((self.sigmf_source_0, 0), (self.blocks_throttle_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "burst_rx_gmsk9600_ax25_playback")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

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

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_decim(int(self.samp_rate/2000))
        self.set_rx_offset(self.samp_rate/2.0)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1_0_1.set_frequency_range(self.rx_freq, self.samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.chan_filt_cutoff, self.chan_filt_trans, firdes.WIN_HAMMING, 6.76))
        self.gmsk_ax25_rx_hier_0.set_quad_demod_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.fsk_burst_detector_0.set_samp_rate(self.samp_rate)
        self.burst_rx_es_hier_0.set_samp_rate(self.samp_rate/self.decim*self.interp)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.rate_factor)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate *self.interp /self.decim)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn
        self.set_fp("/vtgs/captures/vcc/{:s}".format(self.fn))

    def get_trigger_thresh(self):
        return self.trigger_thresh

    def set_trigger_thresh(self, trigger_thresh):
        self.trigger_thresh = trigger_thresh
        Qt.QMetaObject.invokeMethod(self._trigger_thresh_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.trigger_thresh)))
        self.burst_rx_es_hier_0.set_trigger_thresh(self.trigger_thresh)
        self.analog_const_source_x_0.set_offset(self.trigger_thresh)

    def get_rx_offset(self):
        return self.rx_offset

    def set_rx_offset(self, rx_offset):
        self.rx_offset = rx_offset

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate)
        self.qtgui_freq_sink_x_1_0_1.set_frequency_range(self.rx_freq, self.samp_rate)

    def get_rate_factor(self):
        return self.rate_factor

    def set_rate_factor(self, rate_factor):
        self.rate_factor = rate_factor
        Qt.QMetaObject.invokeMethod(self._rate_factor_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rate_factor)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.rate_factor)

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
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.chan_filt_cutoff, self.chan_filt_trans, firdes.WIN_HAMMING, 6.76))
        self.gmsk_ax25_rx_hier_0.set_quad_demod_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.fsk_burst_detector_0.set_interp(self.interp)
        self.burst_rx_es_hier_0.set_samp_rate(self.samp_rate/self.decim*self.interp)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate *self.interp /self.decim)

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

    def get_fine_offset(self):
        return self.fine_offset

    def set_fine_offset(self, fine_offset):
        self.fine_offset = fine_offset
        Qt.QMetaObject.invokeMethod(self._fine_offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fine_offset)))
        self.analog_sig_source_x_0_0_0.set_frequency(-1 * self.fine_offset)

    def get_filt_cut(self):
        return self.filt_cut

    def set_filt_cut(self, filt_cut):
        self.filt_cut = filt_cut
        Qt.QMetaObject.invokeMethod(self._filt_cut_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.filt_cut)))

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
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp / self.decim_2 * self.interp_2)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.chan_filt_cutoff, self.chan_filt_trans, firdes.WIN_HAMMING, 6.76))
        self.gmsk_ax25_rx_hier_0.set_quad_demod_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.fsk_burst_detector_0.set_decim(self.decim)
        self.burst_rx_es_hier_0.set_samp_rate(self.samp_rate/self.decim*self.interp)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate *self.interp /self.decim)

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


def main(top_block_cls=burst_rx_gmsk9600_ax25_playback, options=None):

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
