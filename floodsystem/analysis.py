import matplotlib
import matplotlib.dates
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    dates_float = matplotlib.dates.date2num(dates)
    dates_shifted = []
    d0 = dates_float[-1]

    for i in range(len(dates_float)):
        dates_shifted.append(dates_float[i] - d0)
    
    p_coeff = np.polyfit(dates_shifted, levels, p)
    poly = np.poly1d(p_coeff)

    return poly, d0


def predict_future_level(dates, levels):
    """
    given the water level time history for a station,
    return tuple of future date, water level at thatdate
    """
    dates_float = matplotlib.dates.date2num(dates)
    dates_shifted = []
    d0 = dates_float[-1]

    for i in range(len(dates_float)):
        dates_shifted.append(dates_float[i]-d0)
    
    p_coeff = np.polyfit(dates_shifted, levels, 3)
    poly = np.poly1d(p_coeff)

    # extrapolating by 1 day
    future_date = max(dates_shifted) + 1
    return future_date, poly(future_date)
