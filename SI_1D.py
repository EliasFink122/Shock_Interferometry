"""
Created on Tue Jul 23 2024

@author: Elias Fink (elias.fink22@imperial.ac.uk)

Simulation of 1D interferogram trace.

Methods:
    read_in:
        read in data from csv file
    convert_doppler:
        convert speeds to Doppler shifted wavelengths
    interferogram:
        generate interferogram from wavelength
    trace_animation:
        get animation of interferograms from wavelengths
"""
import numpy as np
from scipy.constants import speed_of_light as c
import matplotlib.pyplot as plt

def gse(arr: list, num = 10) -> list:
    '''
    Get evenly spaced out elements from array:

    Args:
        arr: input array
        num: number of elements

    Returns:
        elements
    '''
    out = arr[np.round(np.linspace(0, len(arr)-1, num)).astype(int)]
    return out

def read_in(path = "data.csv") -> np.array:
    '''
    Read in shock speed data.

    Args:
        path: full path to file

    Returns:
        data in numpy array
    '''
    data = np.loadtxt(path, delimiter=',', skiprows=1)
    return data[:, 0], data[:, 1]

def convert_doppler(wavelength: float, speeds: np.ndarray) -> np.ndarray:
    '''
    Convert speeds to Doppler shifted wavelength.

    Args:
        wavelength: unshifted laser wavelength in m
        speeds: speed array from data

    Returns:
        shifted wavelengths as array
    '''
    betas = speeds/c
    new_wavelengths = wavelength * np.sqrt((1+betas)/(1-betas))

    return new_wavelengths

def interferogram(wavelength: float, opt_depth = 1) -> np.ndarray:
    '''
    Generate Mach Zehnder interferogram.

    Args:
        opt_depth: optical depth difference of second arm
        wavelength: wavelength of light

    Returns:
        positions of fringes
    '''
    period = wavelength/(2*opt_depth*np.sin(np.pi/10))

    plot_range = 1e-5
    xs = np.linspace(0, plot_range, 1000)
    fringes = np.square(np.sin(xs*2*np.pi/period))

    return xs, fringes

def trace_animation(wavelengths: np.ndarray):
    '''
    Animate trace of interferograms.

    Args:
        wavelengths: wavelength array
    '''
    plt.figure()
    plt.title("Interferogram")

    for wavelength in wavelengths:
        xs, fringes = interferogram(wavelength)
        fringes_xy = np.zeros((len(fringes), len(fringes)))
        for k, _ in enumerate(fringes_xy):
            for j, _ in enumerate(fringes_xy):
                fringes_xy[k, j] = fringes[k]
        ticks = [f"{tick*1e9:.0f}" for tick in gse(xs)]
        plt.xticks(gse(np.arange(len(fringes_xy))), ticks)
        plt.yticks(gse(np.arange(len(fringes_xy))), ticks)
        plt.xlabel("x [nm]")
        plt.ylabel("y [nm]")
        plt.imshow(fringes_xy, cmap = 'Greys', animated = True, origin = 'lower')
        plt.pause(0.5)

    plt.show()

def plot_trace(times: np.ndarray, wavelengths: np.ndarray):
    '''
    Plot trace of interferograms.

    Args:
        times: times of speed measurements
        wavelengths: wavelength array
    '''
    plt.figure()
    plt.title("Interferogram trace")
    xs, _ = interferogram(wavelengths[0])
    plot_arr = np.zeros((len(xs), len(times)*100))
    for k, wavelength in enumerate(wavelengths):
        _, fringes = interferogram(wavelength)
        for i, _ in enumerate(plot_arr):
            for j in range(100):
                plot_arr[i, 100*k + j] = fringes[i]
    plt.imshow(plot_arr, cmap = 'Greys', origin = 'lower')
    ticks_x = [f"{tick:.0f}" for tick in gse(times)]
    ticks_y = [f"{tick*1e9:.0f}" for tick in gse(xs)]
    plt.xticks(gse(np.arange(len(plot_arr[0]))), ticks_x)
    plt.yticks(gse(np.arange(len(plot_arr))), ticks_y)
    plt.xlabel("Time [s]")
    plt.ylabel("Fringe positions [nm]")
    plt.show()

if __name__ == "__main__":
    time_arr, speed_arr = read_in()
    wavelength_arr = convert_doppler(5.5e-7, speed_arr)
    # trace_animation(wavelength_arr)
    plot_trace(time_arr, wavelength_arr)
