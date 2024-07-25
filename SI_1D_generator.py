"""
Created on Thu Jul 25 2024

@author: Elias Fink (elias.fink22@imperial.ac.uk)

Generate data for 1D shock front speed profile.

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
    speeds = np.linspace(0, max_speed, num)
    noise = (np.random.rand(num) - 0.5) * max_speed/5
    return np.abs(speeds + noise)

def generate_data(num: int, max_speed: float, final_time: float = None):
    '''
    Save data in file.

    Args:
        num: number of data points
        max_speed: final speed
        final_time: time for whole process to take place
    '''
    if final_time is None:
        final_time = num

    print("Generating data...")
    data = np.zeros((num, 2))
    times = np.array(range(num))*final_time/num
    speeds = profile(num, max_speed)
    for i in range(num):
        data[i] = [times[i], speeds[i]]

    print("Saving data...")
    np.savetxt("data.csv", data)
    print("Finished!")

if __name__ == '__main__':
    generate_data(100, 5e7, 1e-4)
