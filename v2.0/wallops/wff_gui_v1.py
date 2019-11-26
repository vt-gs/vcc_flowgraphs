#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Wff Gui V1
# Author: Zach Leffke, KJ4QLP
# Description: Wallops Interface, with GUI
#
# Generated: Fri Sep 27 21:10:02 2019
# GNU Radio version: 3.7.12.0
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import kiss
import sys
import vcc
from gnuradio import qtgui


class wff_gui_v1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Wff Gui V1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Wff Gui V1")
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

        self.settings = Qt.QSettings("GNU Radio", "wff_gui_v1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.verbose_choose = verbose_choose = True
        self.ssid = ssid = 0
        self.scramble_label = scramble_label = ''
        self.output_label = output_label = ''
        self.kiss_label = kiss_label = ''
        self.input_label = input_label = ''
        self.hdlc_label = hdlc_label = ''
        self.callsign = callsign = 'WJ2XMS'
        self.ax25_label = ax25_label = ''

        ##################################################
        # Blocks
        ##################################################
        self._verbose_choose_options = (True, False, )
        self._verbose_choose_labels = ('True', 'False', )
        self._verbose_choose_group_box = Qt.QGroupBox('Verbose')
        self._verbose_choose_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._verbose_choose_button_group = variable_chooser_button_group()
        self._verbose_choose_group_box.setLayout(self._verbose_choose_box)
        for i, label in enumerate(self._verbose_choose_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._verbose_choose_box.addWidget(radio_button)
        	self._verbose_choose_button_group.addButton(radio_button, i)
        self._verbose_choose_callback = lambda i: Qt.QMetaObject.invokeMethod(self._verbose_choose_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._verbose_choose_options.index(i)))
        self._verbose_choose_callback(self.verbose_choose)
        self._verbose_choose_button_group.buttonClicked[int].connect(
        	lambda i: self.set_verbose_choose(self._verbose_choose_options[i]))
        self.top_grid_layout.addWidget(self._verbose_choose_group_box, 5, 0, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._ssid_tool_bar = Qt.QToolBar(self)
        self._ssid_tool_bar.addWidget(Qt.QLabel('SSID'+": "))
        self._ssid_line_edit = Qt.QLineEdit(str(self.ssid))
        self._ssid_tool_bar.addWidget(self._ssid_line_edit)
        self._ssid_line_edit.returnPressed.connect(
        	lambda: self.set_ssid(int(str(self._ssid_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._ssid_tool_bar, 5, 2, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._callsign_tool_bar = Qt.QToolBar(self)
        self._callsign_tool_bar.addWidget(Qt.QLabel('Callsign'+": "))
        self._callsign_line_edit = Qt.QLineEdit(str(self.callsign))
        self._callsign_tool_bar.addWidget(self._callsign_line_edit)
        self._callsign_line_edit.returnPressed.connect(
        	lambda: self.set_callsign(str(str(self._callsign_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._callsign_tool_bar, 5, 1, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.vcc_qt_hex_text_0_1_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_0_1_0_win = self.vcc_qt_hex_text_0_1_0;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_0_1_0_win, 3, 1, 1, 2)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.vcc_qt_hex_text_0_1 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_0_1_win = self.vcc_qt_hex_text_0_1;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_0_1_win, 2, 1, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.vcc_qt_hex_text_0_0_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_0_0_0_win = self.vcc_qt_hex_text_0_0_0;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_0_0_0_win, 2, 3, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 5):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.vcc_qt_hex_text_0_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_0_0_win = self.vcc_qt_hex_text_0_0;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_0_0_win, 1, 3, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 5):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.vcc_qt_hex_text_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_0_win = self.vcc_qt_hex_text_0;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_0_win, 1, 1, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.vcc_insert_src_callsign_pdu_0 = vcc.insert_src_callsign_pdu(callsign=callsign,ssid=ssid, verbose=verbose_choose)
        self.vcc_burst_scramble_bb_0 = vcc.burst_scramble_bb(0x21, 0x0, 16)
        self._scramble_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._scramble_label_formatter = None
        else:
          self._scramble_label_formatter = lambda x: str(x)

        self._scramble_label_tool_bar.addWidget(Qt.QLabel('SCRAMBLE'+": "))
        self._scramble_label_label = Qt.QLabel(str(self._scramble_label_formatter(self.scramble_label)))
        self._scramble_label_tool_bar.addWidget(self._scramble_label_label)
        self.top_grid_layout.addWidget(self._scramble_label_tool_bar, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._output_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._output_label_formatter = None
        else:
          self._output_label_formatter = lambda x: str(x)

        self._output_label_tool_bar.addWidget(Qt.QLabel('OUTPUT'+": "))
        self._output_label_label = Qt.QLabel(str(self._output_label_formatter(self.output_label)))
        self._output_label_tool_bar.addWidget(self._output_label_label)
        self.top_grid_layout.addWidget(self._output_label_tool_bar, 0, 3, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.kiss_pdu_to_kiss_0 = kiss.pdu_to_kiss()
        self._kiss_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._kiss_label_formatter = None
        else:
          self._kiss_label_formatter = lambda x: str(x)

        self._kiss_label_tool_bar.addWidget(Qt.QLabel('KISS'+": "))
        self._kiss_label_label = Qt.QLabel(str(self._kiss_label_formatter(self.kiss_label)))
        self._kiss_label_tool_bar.addWidget(self._kiss_label_label)
        self.top_grid_layout.addWidget(self._kiss_label_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.kiss_kiss_to_pdu_0 = kiss.kiss_to_pdu(True)
        self.kiss_hdlc_framer_0 = kiss.hdlc_framer(preamble_bytes=64, postamble_bytes=64)
        self.kiss_hdlc_deframer_0 = kiss.hdlc_deframer(check_fcs=True, max_length=300)
        self._input_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._input_label_formatter = None
        else:
          self._input_label_formatter = lambda x: str(x)

        self._input_label_tool_bar.addWidget(Qt.QLabel('Input'+": "))
        self._input_label_label = Qt.QLabel(str(self._input_label_formatter(self.input_label)))
        self._input_label_tool_bar.addWidget(self._input_label_label)
        self.top_grid_layout.addWidget(self._input_label_tool_bar, 0, 1, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._hdlc_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._hdlc_label_formatter = None
        else:
          self._hdlc_label_formatter = lambda x: str(x)

        self._hdlc_label_tool_bar.addWidget(Qt.QLabel('HDLC'+": "))
        self._hdlc_label_label = Qt.QLabel(str(self._hdlc_label_formatter(self.hdlc_label)))
        self._hdlc_label_tool_bar.addWidget(self._hdlc_label_label)
        self.top_grid_layout.addWidget(self._hdlc_label_tool_bar, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_descrambler_bb_0 = digital.descrambler_bb(0x21, 0, 16)
        self.blocks_socket_pdu_0_2 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '8000', 1024, False)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self._ax25_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._ax25_label_formatter = None
        else:
          self._ax25_label_formatter = lambda x: str(x)

        self._ax25_label_tool_bar.addWidget(Qt.QLabel('AX.25'+": "))
        self._ax25_label_label = Qt.QLabel(str(self._ax25_label_formatter(self.ax25_label)))
        self._ax25_label_tool_bar.addWidget(self._ax25_label_label)
        self.top_grid_layout.addWidget(self._ax25_label_tool_bar, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0_2, 'pdus'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.blocks_socket_pdu_0_2, 'pdus'), (self.vcc_qt_hex_text_0, 'pdus'))
        self.msg_connect((self.kiss_hdlc_deframer_0, 'out'), (self.kiss_pdu_to_kiss_0, 'in'))
        self.msg_connect((self.kiss_hdlc_deframer_0, 'out'), (self.vcc_qt_hex_text_0_0_0, 'pdus'))
        self.msg_connect((self.kiss_hdlc_framer_0, 'out'), (self.vcc_burst_scramble_bb_0, 'in'))
        self.msg_connect((self.kiss_hdlc_framer_0, 'out'), (self.vcc_qt_hex_text_0_1_0, 'pdus'))
        self.msg_connect((self.kiss_kiss_to_pdu_0, 'out'), (self.vcc_insert_src_callsign_pdu_0, 'in'))
        self.msg_connect((self.kiss_pdu_to_kiss_0, 'out'), (self.vcc_qt_hex_text_0_0, 'pdus'))
        self.msg_connect((self.vcc_burst_scramble_bb_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.vcc_insert_src_callsign_pdu_0, 'out'), (self.kiss_hdlc_framer_0, 'in'))
        self.msg_connect((self.vcc_insert_src_callsign_pdu_0, 'out'), (self.vcc_qt_hex_text_0_1, 'pdus'))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.digital_descrambler_bb_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.kiss_kiss_to_pdu_0, 0))
        self.connect((self.digital_descrambler_bb_0, 0), (self.kiss_hdlc_deframer_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wff_gui_v1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_verbose_choose(self):
        return self.verbose_choose

    def set_verbose_choose(self, verbose_choose):
        self.verbose_choose = verbose_choose
        self._verbose_choose_callback(self.verbose_choose)
        self.vcc_insert_src_callsign_pdu_0.set_verbose(self.verbose_choose)

    def get_ssid(self):
        return self.ssid

    def set_ssid(self, ssid):
        self.ssid = ssid
        Qt.QMetaObject.invokeMethod(self._ssid_line_edit, "setText", Qt.Q_ARG("QString", str(self.ssid)))
        self.vcc_insert_src_callsign_pdu_0.set_ssid(self.ssid)

    def get_scramble_label(self):
        return self.scramble_label

    def set_scramble_label(self, scramble_label):
        self.scramble_label = scramble_label
        Qt.QMetaObject.invokeMethod(self._scramble_label_label, "setText", Qt.Q_ARG("QString", self.scramble_label))

    def get_output_label(self):
        return self.output_label

    def set_output_label(self, output_label):
        self.output_label = output_label
        Qt.QMetaObject.invokeMethod(self._output_label_label, "setText", Qt.Q_ARG("QString", self.output_label))

    def get_kiss_label(self):
        return self.kiss_label

    def set_kiss_label(self, kiss_label):
        self.kiss_label = kiss_label
        Qt.QMetaObject.invokeMethod(self._kiss_label_label, "setText", Qt.Q_ARG("QString", self.kiss_label))

    def get_input_label(self):
        return self.input_label

    def set_input_label(self, input_label):
        self.input_label = input_label
        Qt.QMetaObject.invokeMethod(self._input_label_label, "setText", Qt.Q_ARG("QString", self.input_label))

    def get_hdlc_label(self):
        return self.hdlc_label

    def set_hdlc_label(self, hdlc_label):
        self.hdlc_label = hdlc_label
        Qt.QMetaObject.invokeMethod(self._hdlc_label_label, "setText", Qt.Q_ARG("QString", self.hdlc_label))

    def get_callsign(self):
        return self.callsign

    def set_callsign(self, callsign):
        self.callsign = callsign
        Qt.QMetaObject.invokeMethod(self._callsign_line_edit, "setText", Qt.Q_ARG("QString", str(self.callsign)))
        self.vcc_insert_src_callsign_pdu_0.set_callsign(self.callsign)

    def get_ax25_label(self):
        return self.ax25_label

    def set_ax25_label(self, ax25_label):
        self.ax25_label = ax25_label
        Qt.QMetaObject.invokeMethod(self._ax25_label_label, "setText", Qt.Q_ARG("QString", self.ax25_label))


def main(top_block_cls=wff_gui_v1, options=None):

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
