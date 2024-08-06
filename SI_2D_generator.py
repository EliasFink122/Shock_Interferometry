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
            x = i-num/2
            y = j-num/2
            phase = np.random.rand()*2*np.pi
            exp = np.log(max_speed/10) * np.sin(1/num*(np.sqrt(x**2 + y**2)))**2
            modulation = 1#np.exp(exp) * np.exp(1j*phase)
            ideal_beam = max_speed*np.exp(-((x**2 + y**2)/(2*(0.5*num)**2))**5)
            speeds[i, j] = np.abs(ideal_beam*modulation)
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
