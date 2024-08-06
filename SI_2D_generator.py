"""
Created on Thu Jul 25 2024

@author: Elias Fink (elias.fink22@imperial.ac.uk)

Generate data for 2D shock front speed profile.

Methods:
    profile:
        generate randomised speed profile
    generate_data:
        save data into sample file
    time_evolving:
        generate dataset with time evolution property
"""
import numpy as np
from multiprocessing import Pool

def profile(num: int, max_speed: float, width = 0.5) -> np.ndarray:
    '''
    Generate speed profile.

    Args:
        num: number of data points
        max_speed: final speed
        width: width of super Gaussian relative to image

    Returns:
        speeds array
    '''
    speeds = np.zeros((num, num))
    for i, _ in enumerate(speeds):
        for j, _ in enumerate(speeds):
            x = i-num/2
            y = j-num/2
            phase = np.random.rand()*2*np.pi
            exp = np.log(max_speed/10) * np.sin(1/num*(np.sqrt(x**2 + y**2)))**2
            modulation = 1#np.exp(exp) * np.exp(1j*phase)
            ideal_beam = max_speed*np.exp(-((x**2 + y**2)/(2*(width*num)**2))**5)
            speeds[i, j] = np.abs(ideal_beam*modulation)
    return speeds

def time_evolving(num: int, max_speed: float, timesteps = 400) -> np.ndarray:
    '''
    Generate time evolving shape

    Args:
        num: resolution
        max_speed: maximum speed
        timesteps: number of timesteps
    '''
    timestep = 2e-4
    def profile_gen(i):
        return profile(num, max_speed, 0.5+i*timestep)
    with Pool() as pool:
        arrs = pool.map(profile_gen, range(timesteps))
    return arrs

def generate_data(num: int, max_speed: float):
    '''
    Save data in file.

    Args:
        num: number of data points
        max_speed: final speed
    '''
    print("Generating data...")
    speeds = profile(num, max_speed)

    print("Saving data...")
    np.savetxt("data2d.csv", speeds)
    print("Finished!")

if __name__ == '__main__':
    generate_data(1000, 5e7)
