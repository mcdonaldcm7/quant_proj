#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 21:16:53 2026

@author: lq-mcdonald
"""

"""
This files contains tests for the 4 moving averages implemented
"""

import unittest
import numpy as np
from simple_moving_average import SMA


class TestMovingAverages(unittest.TestCase):
    def setUp(self):
        self.prices = [143.55, 143, 144, 141.05, 140.53, 141.04, 141.57, 139.91, 133.46, 133.48,
        130.52, 131.61, 134.17, 140.35, 135.98, 129.46, 136.12, 141.94, 137.16, 135.33]
        
    def test_simple_moving_average(self):
        """Tests and the validates the Simple Moving Average"""
        period = 10
        expected = [ np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 140.159, 138.856,
         137.717, 136.734, 136.664, 136.209, 135.051, 134.506, 134.709, 135.079, 135.264]
        result = SMA(self.prices, period)
        self.assertAlmostEqual(expected, result, places=3)
        
if __name__ == "__main__":
    unittest.main()