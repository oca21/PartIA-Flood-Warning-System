import matplotlib
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

    # Create set of 10 data points on interval (1000, 1002)
    x = np.linspace(10000, 10002, 10)
    y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, 4)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)