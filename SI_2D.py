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

def transform(wavelengths: np.ndarray, refr_index = 1.33, length = 1) -> np.ndarray:
    '''
    Find Mach Zehnder interferogram

    Args:
        wavelengths: 2d array of wavelengths
        refr_index: refractive index of medium in interferometer
        length: length of optical medium


    Returns:
        interferogram
    '''
    phases = (refr_index - 1)*2*np.pi*length/wavelengths
    intensities = np.square(np.abs(np.exp(1j*phases) - 1))
    return intensities

def plot_visar(intensities: np.ndarray):
    '''
    Plot VISAR image.

    Args:
        intensities: intensities in 2D array
    '''
    plt.figure()
    plt.title("2D VISAR simulation")
    plt.imshow(intensities, cmap = "Greys")
    plt.xlabel("x [mm]")
    plt.ylabel("y [mm]")
    plt.savefig("visar_2d.png", dpi = 1000)
    plt.show()

if __name__ == "__main__":
    speed_arr = read_in()
    wavelength_arr = convert_doppler(5.5e-7, speed_arr)
    intensity_arr = transform(wavelength_arr)
    plot_visar(intensity_arr)
