#
# ------------------------------------------------------------
# Copyright (c) All rights reserved
# SiLab, Institute of Physics, University of Bonn
# ------------------------------------------------------------

from basil.HL.RegisterHardwareLayer import HardwareLayer
import logging

class FadcConf(HardwareLayer):

    def __init__(self, intf, conf):
        super(FadcConf, self).__init__(intf, conf)
        
    def init(self):

        logging.debug("Initializing FADC Configuration...")

        self._intf.set_data([0x00, 0x10])  # RESET ADC
        self._intf.start()
        while not self._intf.is_done():
            pass
        
        self._intf.set_data([0x02, 0x07])  # SET 16 bit mode
        self._intf.start()
        while not self._intf.is_done():
            pass
            
        self._intf.set_data([0x03, 0x00]) # PATTERN OFF
        self._intf.start()
        while not self._intf.is_done():
            pass