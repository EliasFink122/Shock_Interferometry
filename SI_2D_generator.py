"""
Created on Thu Jul 25 2024

@author: Elias Fink (elias.fink22@imperial.ac.uk)

Generate data for 2D shock front speed profile.

Methods:
    profile:
        generate randomised speed profile
    generate_data:
        save data into sample file
"""
import numpy as np

def profile(num: int, max_speed: float) -> np.ndarray:
    '''
    Generate speed profile.

    Args:
        num: number of data points
        max_speed: final speed
    '''
    speeds = np.zeros((num, num))
    for i, _ in enumerate(speeds):
        for j, _ in enumerate(speeds):
            speeds[i, j] = max_speed*np.exp(-(((i-num/2)**2 + (j-num/2)**2)/(2*(0.5*num)**2))**5)
    return speeds

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
