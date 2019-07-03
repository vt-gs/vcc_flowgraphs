#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Burst Rx Gmsk
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
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import burst
import es
import kiss
import math
import pdu_utils
import pmt
import pyqt
import sip
import sys
import vcc
from gnuradio import qtgui


class burst_rx_gmsk(gr.top_block, Qt.QWidget):

    def __init__(self, center_freq=401.12e6, lpf_cutoff=24e3, lpf_cutoff_2=7.2e3, lpf_trans=1e3):
        gr.top_block.__init__(self, "Burst Rx Gmsk")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Burst Rx Gmsk")
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

        self.settings = Qt.QSettings("GNU Radio", "burst_rx_gmsk")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.center_freq = center_freq
        self.lpf_cutoff = lpf_cutoff
        self.lpf_cutoff_2 = lpf_cutoff_2
        self.lpf_trans = lpf_trans

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250000
        self.interp_2 = interp_2 = 1
        self.interp = interp = 24*2
        self.decim_2 = decim_2 = 2
        self.decim = decim = int(samp_rate/2000)
        self.baud = baud = 9600
        self.samps_per_symb = samps_per_symb = int((samp_rate/decim*interp/decim_2*interp_2)/baud)
        self.offset = offset = 0
        self.fsk_dev = fsk_dev = 10000
        self.avg_len_snr = avg_len_snr = 100.0
        self.avg_len_det = avg_len_det = 100.0

        ##################################################
        # Blocks
        ##################################################
        self._offset_tool_bar = Qt.QToolBar(self)
        self._offset_tool_bar.addWidget(Qt.QLabel("offset"+": "))
        self._offset_line_edit = Qt.QLineEdit(str(self.offset))
        self._offset_tool_bar.addWidget(self._offset_line_edit)
        self._offset_line_edit.returnPressed.connect(
        	lambda: self.set_offset(eng_notation.str_to_num(str(self._offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._offset_tool_bar, 2, 4, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._avg_len_snr_tool_bar = Qt.QToolBar(self)
        self._avg_len_snr_tool_bar.addWidget(Qt.QLabel("avg_len_snr"+": "))
        self._avg_len_snr_line_edit = Qt.QLineEdit(str(self.avg_len_snr))
        self._avg_len_snr_tool_bar.addWidget(self._avg_len_snr_line_edit)
        self._avg_len_snr_line_edit.returnPressed.connect(
        	lambda: self.set_avg_len_snr(eng_notation.str_to_num(str(self._avg_len_snr_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._avg_len_snr_tool_bar, 3, 6, 1, 2)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._avg_len_det_tool_bar = Qt.QToolBar(self)
        self._avg_len_det_tool_bar.addWidget(Qt.QLabel("avg_len_det"+": "))
        self._avg_len_det_line_edit = Qt.QLineEdit(str(self.avg_len_det))
        self._avg_len_det_tool_bar.addWidget(self._avg_len_det_line_edit)
        self._avg_len_det_line_edit.returnPressed.connect(
        	lambda: self.set_avg_len_det(eng_notation.str_to_num(str(self._avg_len_det_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._avg_len_det_tool_bar, 2, 6, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.vcc_vstp_aggregator_simple_0 = vcc.vstp_aggregator_simple(fc=center_freq, l_type="downlink", d_type="live")
        self.vcc_trigger_timestamp_pdu_0 = vcc.trigger_timestamp_pdu(threshold=-2)
        self.vcc_qt_hex_text_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_0_win = self.vcc_qt_hex_text_0;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_0_win, 4, 0, 1, 4)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.vcc_burst_snr_0 = vcc.burst_snr(int(avg_len_snr), samp_rate * interp / decim / baud)
        self.vcc_burst_cfo_est_gmsk_0 = vcc.burst_cfo_est_gmsk(samp_rate * interp / decim)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_ccc(
                interpolation=interp_2,
                decimation=decim_2,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=interp_2,
                decimation=decim_2,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=interp,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / decim*interp, #bw
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-100, 20)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / decim*interp, #bw
        	"RX Spectrum", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.0010)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-150, 0)
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
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 0, 4, 1, 4)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pyqt_meta_text_output_0 = pyqt.meta_text_output()
        self._pyqt_meta_text_output_0_win = self.pyqt_meta_text_output_0;
        self.top_grid_layout.addWidget(self._pyqt_meta_text_output_0_win, 1, 7, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(7, 8):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.pyqt_ctime_plot_0 = pyqt.ctime_plot('')
        self._pyqt_ctime_plot_0_win = self.pyqt_ctime_plot_0;
        self.top_grid_layout.addWidget(self._pyqt_ctime_plot_0_win, 1, 4, 1, 3)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 7):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.pdu_utils_extract_metadata_0_0 = pdu_utils.extract_metadata(pmt.intern("snr"), 1.0, 0.0)
        self.pdu_utils_extract_metadata_0 = pdu_utils.extract_metadata(pmt.intern("cfo_est"), 1.0, 0.0)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate / decim *interp / decim_2 *interp_2, lpf_cutoff_2, lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate / decim *interp, lpf_cutoff, lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.kiss_pdu_to_kiss_0 = kiss.pdu_to_kiss()
        self.kiss_nrzi_decode_0 = kiss.nrzi_decode()
        self.kiss_hdlc_deframer_0 = kiss.hdlc_deframer(check_fcs=True, max_length=300)
        self.es_trigger_edge_f_0 = es.trigger_edge_f(-2,baud*samps_per_symb,int(avg_len_det*2),gr.sizeof_gr_complex,300)
        self.es_sink_0 = es.sink(1*[gr.sizeof_gr_complex],4,64,0,2,0)
        self.es_handler_pdu_0 = es.es_make_handler_pdu(es.es_handler_print.TYPE_C32)
        self.digital_descrambler_bb_0 = digital.descrambler_bb(0x21, 0, 16)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samps_per_symb*(1+0.0), 0.25*0.175*0.175, 0.25, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.burst_length_detect_c_0 = burst.length_detect_c()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*8,True)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", '127.0.0.1', '52001', 10000, False)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_float*1, 1)
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.complex_t, 'est_len')
        (self.blocks_pdu_to_tagged_stream_0_0).set_min_output_buffer(48000)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.complex_t, 'est_len')
        (self.blocks_pdu_to_tagged_stream_0).set_min_output_buffer(48000)
        self.blocks_pdu_remove_0 = blocks.pdu_remove(pmt.intern("es::event_buffer"))
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(int(avg_len_det), 1/avg_len_det, 4000, 1)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/zleffke/captures/lithium_20180327/downlink_data_1.fc32', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((3, ))
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*offset, 1, 0)
        self.analog_quadrature_demod_cf_1_0 = analog.quadrature_demod_cf((samp_rate/decim*interp/decim_2*interp_2)/(2*math.pi*fsk_dev/8.0))
        self.analog_quadrature_demod_cf_1 = analog.quadrature_demod_cf((samp_rate/decim*interp)/(2*math.pi*fsk_dev/8.0))
        self.analog_agc2_xx_0 = analog.agc2_cc(10, 1e-1, 65536, 1)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_pdu_remove_0, 'pdus'), (self.burst_length_detect_c_0, 'cpdus'))
        self.msg_connect((self.burst_length_detect_c_0, 'cpdus'), (self.vcc_burst_snr_0, 'in'))
        self.msg_connect((self.es_handler_pdu_0, 'pdus_out'), (self.blocks_pdu_remove_0, 'pdus'))
        self.msg_connect((self.es_trigger_edge_f_0, 'edge_event'), (self.es_handler_pdu_0, 'handle_event'))
        self.msg_connect((self.es_trigger_edge_f_0, 'which_stream'), (self.es_sink_0, 'schedule_event'))
        self.msg_connect((self.kiss_hdlc_deframer_0, 'out'), (self.kiss_pdu_to_kiss_0, 'in'))
        self.msg_connect((self.kiss_hdlc_deframer_0, 'out'), (self.vcc_vstp_aggregator_simple_0, 'raw'))
        self.msg_connect((self.kiss_pdu_to_kiss_0, 'out'), (self.vcc_qt_hex_text_0, 'pdus'))
        self.msg_connect((self.pdu_utils_extract_metadata_0, 'msg'), (self.vcc_vstp_aggregator_simple_0, 'meta'))
        self.msg_connect((self.pdu_utils_extract_metadata_0_0, 'msg'), (self.vcc_vstp_aggregator_simple_0, 'meta'))
        self.msg_connect((self.vcc_burst_cfo_est_gmsk_0, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.vcc_burst_cfo_est_gmsk_0, 'corrected'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.vcc_burst_cfo_est_gmsk_0, 'corrected'), (self.pdu_utils_extract_metadata_0, 'dict'))
        self.msg_connect((self.vcc_burst_cfo_est_gmsk_0, 'out'), (self.pyqt_ctime_plot_0, 'cpdus'))
        self.msg_connect((self.vcc_burst_cfo_est_gmsk_0, 'out'), (self.pyqt_meta_text_output_0, 'pdus'))
        self.msg_connect((self.vcc_burst_snr_0, 'out'), (self.pdu_utils_extract_metadata_0_0, 'dict'))
        self.msg_connect((self.vcc_burst_snr_0, 'out'), (self.vcc_burst_cfo_est_gmsk_0, 'in'))
        self.msg_connect((self.vcc_trigger_timestamp_pdu_0, 'ts'), (self.vcc_vstp_aggregator_simple_0, 'meta'))
        self.msg_connect((self.vcc_vstp_aggregator_simple_0, 'out'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.vcc_vstp_aggregator_simple_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.vcc_vstp_aggregator_simple_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))
        self.connect((self.analog_agc2_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_quadrature_demod_cf_1, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.analog_quadrature_demod_cf_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_1_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.es_trigger_edge_f_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.vcc_trigger_timestamp_pdu_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_descrambler_bb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_descrambler_bb_0, 0), (self.kiss_nrzi_decode_0, 0))
        self.connect((self.es_trigger_edge_f_0, 0), (self.es_sink_0, 0))
        self.connect((self.kiss_nrzi_decode_0, 0), (self.kiss_hdlc_deframer_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_quadrature_demod_cf_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.es_trigger_edge_f_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_1_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_quadrature_demod_cf_1_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_1, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.qtgui_freq_sink_x_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "burst_rx_gmsk")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.vcc_vstp_aggregator_simple_0.set_center_freq(self.center_freq)

    def get_lpf_cutoff(self):
        return self.lpf_cutoff

    def set_lpf_cutoff(self, lpf_cutoff):
        self.lpf_cutoff = lpf_cutoff
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))

    def get_lpf_cutoff_2(self):
        return self.lpf_cutoff_2

    def set_lpf_cutoff_2(self, lpf_cutoff_2):
        self.lpf_cutoff_2 = lpf_cutoff_2
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp / self.decim_2 *self.interp_2, self.lpf_cutoff_2, self.lpf_trans, firdes.WIN_HAMMING, 6.76))

    def get_lpf_trans(self):
        return self.lpf_trans

    def set_lpf_trans(self, lpf_trans):
        self.lpf_trans = lpf_trans
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp / self.decim_2 *self.interp_2, self.lpf_cutoff_2, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samps_per_symb(int((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/self.baud))
        self.set_decim(int(self.samp_rate/2000))
        self.vcc_burst_snr_0.set_sps(self.samp_rate * self.interp / self.decim / self.baud)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp / self.decim_2 *self.interp_2, self.lpf_cutoff_2, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*8)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_quadrature_demod_cf_1_0.set_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate/self.decim*self.interp)/(2*math.pi*self.fsk_dev/8.0))

    def get_interp_2(self):
        return self.interp_2

    def set_interp_2(self, interp_2):
        self.interp_2 = interp_2
        self.set_samps_per_symb(int((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/self.baud))
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp / self.decim_2 *self.interp_2, self.lpf_cutoff_2, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.analog_quadrature_demod_cf_1_0.set_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp
        self.set_samps_per_symb(int((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/self.baud))
        self.vcc_burst_snr_0.set_sps(self.samp_rate * self.interp / self.decim / self.baud)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp / self.decim_2 *self.interp_2, self.lpf_cutoff_2, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.analog_quadrature_demod_cf_1_0.set_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate/self.decim*self.interp)/(2*math.pi*self.fsk_dev/8.0))

    def get_decim_2(self):
        return self.decim_2

    def set_decim_2(self, decim_2):
        self.decim_2 = decim_2
        self.set_samps_per_symb(int((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/self.baud))
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp / self.decim_2 *self.interp_2, self.lpf_cutoff_2, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.analog_quadrature_demod_cf_1_0.set_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_samps_per_symb(int((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/self.baud))
        self.vcc_burst_snr_0.set_sps(self.samp_rate * self.interp / self.decim / self.baud)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate*self.interp/self.decim*self.interp_2/self.decim_2)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp / self.decim_2 *self.interp_2, self.lpf_cutoff_2, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.analog_quadrature_demod_cf_1_0.set_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate/self.decim*self.interp)/(2*math.pi*self.fsk_dev/8.0))

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samps_per_symb(int((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/self.baud))
        self.vcc_burst_snr_0.set_sps(self.samp_rate * self.interp / self.decim / self.baud)

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samps_per_symb*(1+0.0))

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        Qt.QMetaObject.invokeMethod(self._offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.offset)))
        self.analog_sig_source_x_0.set_frequency(-1*self.offset)

    def get_fsk_dev(self):
        return self.fsk_dev

    def set_fsk_dev(self, fsk_dev):
        self.fsk_dev = fsk_dev
        self.analog_quadrature_demod_cf_1_0.set_gain((self.samp_rate/self.decim*self.interp/self.decim_2*self.interp_2)/(2*math.pi*self.fsk_dev/8.0))
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate/self.decim*self.interp)/(2*math.pi*self.fsk_dev/8.0))

    def get_avg_len_snr(self):
        return self.avg_len_snr

    def set_avg_len_snr(self, avg_len_snr):
        self.avg_len_snr = avg_len_snr
        Qt.QMetaObject.invokeMethod(self._avg_len_snr_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.avg_len_snr)))
        self.vcc_burst_snr_0.set_length(int(self.avg_len_snr))

    def get_avg_len_det(self):
        return self.avg_len_det

    def set_avg_len_det(self, avg_len_det):
        self.avg_len_det = avg_len_det
        Qt.QMetaObject.invokeMethod(self._avg_len_det_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.avg_len_det)))
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.avg_len_det), 1/self.avg_len_det)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--center-freq", dest="center_freq", type="eng_float", default=eng_notation.num_to_str(401.12e6),
        help="Set Center Frequency [default=%default]")
    parser.add_option(
        "", "--lpf-cutoff", dest="lpf_cutoff", type="eng_float", default=eng_notation.num_to_str(24e3),
        help="Set LPF Cut Off [default=%default]")
    parser.add_option(
        "", "--lpf-cutoff-2", dest="lpf_cutoff_2", type="eng_float", default=eng_notation.num_to_str(7.2e3),
        help="Set LPF Cut Off 2 [default=%default]")
    parser.add_option(
        "", "--lpf-trans", dest="lpf_trans", type="eng_float", default=eng_notation.num_to_str(1e3),
        help="Set LPF Trans [default=%default]")
    return parser


def main(top_block_cls=burst_rx_gmsk, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(center_freq=options.center_freq, lpf_cutoff=options.lpf_cutoff, lpf_cutoff_2=options.lpf_cutoff_2, lpf_trans=options.lpf_trans)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
