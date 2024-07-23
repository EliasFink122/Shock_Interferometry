"""
Created on Tue Jul 23 2024

@author: Elias Fink (elias.fink22@imperial.ac.uk)

Simulation of 1D interferogram trace.

Methods:
    read_in:
        read in data from csv file
    convert_doppler:
        convert speeds to Doppler shifted wavelengths
"""
import numpy as np
from scipy.constants import speed_of_light as c

def read_in(path = "data.csv") -> np.array:
    '''
    Read in shock speed data.

    Args:
        path: full path to file

    Returns:
        data in numpy array
    '''
    data = np.loadtxt(path, delimiter=',', skiprows=1)
    return data

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
    x = np.linspace(-10*period, 10*period, 100)
    fringes = np.sin(x*2*np.pi/period)

    return fringes

if __name__ == "__main__":
    speed_arr = read_in()
    wavelengths = convert_doppler(5.5e-7, speed_arr)
