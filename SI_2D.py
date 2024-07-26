"""
Created on Tue Jul 23 2024

@author: Elias Fink (elias.fink22@imperial.ac.uk)

Simulation of 2D interferogram trace.

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
import matplotlib.pyplot as plt
from scipy.constants import speed_of_light as c

def read_in(path = "data2d.csv") -> np.array:
    '''
    Read in shock speed data.

    Args:
        path: full path to file

    Returns:
        data in numpy array
    '''
    data = np.loadtxt(path)
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

def transform(wavelengths: np.ndarray) -> np.ndarray:
    '''
    Find interferogram by applying a Fourier transform with the Mach Zehnder geometry

    Args:
        wavelengths: 2d array of wavelengths

    Returns:
        interferogram
    '''
