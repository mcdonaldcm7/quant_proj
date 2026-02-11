#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 11:53:20 2026

@author: lq-mcdonald
"""

import numpy as np

def SMA(arr: np.ndarray, n=12):
    """
    Simple Moving Average (SMA) fundamentally returns the average for the price over n days and returns
    the values. This type of moving average doesn't attach any importance to prices based on the date
    
    - arr: A numpy array containing the price values
    - n: size of the moving average window
    
    return: An array of the simple moving avreages
    """
    
    if not isinstance(arr, np.ndarray()):
        raise TypeError("Expected a numpy array, but received type: {}".format(type(arr)))
        
    if arr is None or len(arr) == 0 or len(arr) < n:
        return []
    
    sma = [np.nan for i in range(n - 1)] # fills the first (n - 1) elements with NaN values
    for i in range(0, len(arr)):
        sma[n + 1] = sum(arr[i : n + i]) / n
    return np.array(sma)