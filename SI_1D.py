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
    plot_trace:
        get trace of interferograms from wavelengths
"""
import numpy as np
from scipy.constants import speed_of_light as c
import matplotlib.pyplot as plt
from matplotlib import animation

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
    xs = np.linspace(-5*period, 5*period, 1000)
    fringes = np.square(np.sin(xs*2*np.pi/period))

    fringes_xy = np.zeros((len(xs), len(xs)))
    for i, _ in enumerate(fringes_xy):
        for j, _ in enumerate(fringes_xy):
            fringes_xy[i, j] = fringes[i]

    plt.cla()
    plt.imshow(fringes_xy, cmap = 'Greys')

    return fringes

def plot_trace(wavelengths: np.ndarray):
    '''
    Plot trace of interferograms.

    Args:
        wavelengths: wavelength array
    '''

    plt.rcParams['animation.html'] = "jshtml"
    plt.rcParams['figure.dpi'] = 500
    plt.rcParams['animation.embed_limit'] = 20
    plt.ion()
    fig, _ = plt.subplots()

    def animate(i):
        '''
        Animation
        '''
        interferogram(wavelengths[i])

    anim = animation.FuncAnimation(fig, animate, frames=len(wavelengths))
    writervideo = animation.PillowWriter(fps=10)
    anim.save('trace.gif', writer=writervideo)
    plt.close()

if __name__ == "__main__":
    time_arr, speed_arr = read_in()
    wavelength_arr = convert_doppler(5.5e-7, speed_arr)
    plot_trace(wavelength_arr)
