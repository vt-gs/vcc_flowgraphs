#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Simple Sigmf Playback 1Chan
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
import sip
import sys
from gnuradio import qtgui


class simple_sigmf_playback_1chan(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Simple Sigmf Playback 1Chan")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Simple Sigmf Playback 1Chan")
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

        self.settings = Qt.QSettings("GNU Radio", "simple_sigmf_playback_1chan")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250000
        self.rate_factor = rate_factor = 2
        self.decim = decim = 5
        self.ceres_offset = ceres_offset = 40e3

        ##################################################
        # Blocks
        ##################################################
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
        self._ceres_offset_tool_bar = Qt.QToolBar(self)
        self._ceres_offset_tool_bar.addWidget(Qt.QLabel('Ceres Offset'+": "))
        self._ceres_offset_line_edit = Qt.QLineEdit(str(self.ceres_offset))
        self._ceres_offset_tool_bar.addWidget(self._ceres_offset_line_edit)
        self._ceres_offset_line_edit.returnPressed.connect(
        	lambda: self.set_ceres_offset(eng_notation.str_to_num(str(self._ceres_offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._ceres_offset_tool_bar)
        self.sigmf_source_0 = gr_sigmf.source('/vtgs/captures/vcc/VCC_VTGS_20190716_071133.sigmf-data', "cf32" + ("_le" if sys.byteorder == "little" else "_be"), False)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	401.08e6 + ceres_offset, #fc
        	samp_rate /decim, #bw
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
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 1, 0, 1, 8)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1_0_1 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	401.08e6 + ceres_offset, #fc
        	samp_rate / decim, #bw
        	"VCC RX Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0_1.set_update_time(0.0010)
        self.qtgui_freq_sink_x_1_0_1.set_y_axis(-150, -60)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_1_win, 0, 0, 1, 8)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*rate_factor,True)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1 * ceres_offset, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_1_0_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.sigmf_source_0, 0), (self.blocks_throttle_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "simple_sigmf_playback_1chan")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(401.08e6 + self.ceres_offset, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_1_0_1.set_frequency_range(401.08e6 + self.ceres_offset, self.samp_rate / self.decim)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.rate_factor)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)

    def get_rate_factor(self):
        return self.rate_factor

    def set_rate_factor(self, rate_factor):
        self.rate_factor = rate_factor
        Qt.QMetaObject.invokeMethod(self._rate_factor_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rate_factor)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.rate_factor)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0.set_frequency_range(401.08e6 + self.ceres_offset, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_1_0_1.set_frequency_range(401.08e6 + self.ceres_offset, self.samp_rate / self.decim)

    def get_ceres_offset(self):
        return self.ceres_offset

    def set_ceres_offset(self, ceres_offset):
        self.ceres_offset = ceres_offset
        Qt.QMetaObject.invokeMethod(self._ceres_offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ceres_offset)))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(401.08e6 + self.ceres_offset, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_1_0_1.set_frequency_range(401.08e6 + self.ceres_offset, self.samp_rate / self.decim)
        self.analog_sig_source_x_0_0.set_frequency(-1 * self.ceres_offset)


def main(top_block_cls=simple_sigmf_playback_1chan, options=None):

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
