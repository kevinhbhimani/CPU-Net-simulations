from dspeed.processors import avg_current, upsampler, moving_window_multi, min_max
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm
import numpy as np
from dspeed.processors import time_point_thresh
from dspeed.errors import DSPFatal
import numpy as np

def calc_current_amplitude(waveform, plot=False):
    """
    Process a waveform through the specified DSP chain, with optional plotting.
    
    Parameters:
    waveform : numpy.ndarray
        The waveform to process.
    plot : bool
        Whether to plot the intermediate steps.
    
    Returns:
    A_max : float
        The maximum amplitude of the current waveform after processing.
    """
    waveform = waveform/1000
    if plot:
        plt.figure(figsize=(14, 10))  # Increased figure size
        
        plt.subplot(5, 1, 1)  # Added subplot for initial waveform
        plt.plot(waveform, label="Initial Waveform")
        plt.title("Initial Waveform")
        plt.legend()

    # Step 1: Calculate the current waveform
    current = np.zeros(len(waveform) - 1)
    avg_current(waveform, 1, current)
    
    # Plot the current waveform
    if plot:
        plt.subplot(5, 1, 2)
        plt.plot(current, label="Current Waveform")
        plt.title("Step 1: Current Waveform")
        plt.legend()
    
    # Step 2: Upsample the current waveform
    upsample_factor = 16
    upsampled_current = np.zeros((len(current) - 1) * upsample_factor)
    upsampler(current, upsample_factor, upsampled_current)
    
    # Plot the upsampled current waveform
    if plot:
        plt.subplot(5, 1, 3)
        plt.plot(upsampled_current, label="Upsampled Current Waveform")
        plt.title("Step 2: Upsampled Current Waveform")
        plt.legend()
    
    # Step 3: Apply moving window to the upsampled current
    window_length = 48
    num_mw = 3
    mw_type = 0  # Alternate moving windows right and left
    smoothed_current = np.zeros_like(upsampled_current)
    moving_window_multi(upsampled_current, window_length, num_mw, mw_type, smoothed_current)
    
    # Plot the smoothed current waveform
    if plot:
        plt.subplot(5, 1, 4)
        plt.plot(smoothed_current, label="Smoothed Current Waveform")
        plt.title("Step 3: Smoothed Current Waveform")
        plt.legend()
    
    # Step 4: Find A-Max in the smoothed current waveform
    t_min, t_max, A_min, A_max = np.zeros(1), np.zeros(1), np.zeros(1), np.zeros(1)
    min_max(smoothed_current, t_min, t_max, A_min, A_max)
    
    # Plot the final waveform highlighting A-Max
    if plot:
        plt.subplot(5, 1, 5)
        plt.plot(smoothed_current, label="Final Smoothed Current Waveform")
        plt.scatter(t_max, A_max, color='red', label="A-Max")
        plt.title("Step 4: Final Smoothed Current Waveform with A-Max")
        plt.legend()
        plt.tight_layout()  # Adjust layout to make sure everything fits
        plt.show()
    
    return A_max[0]


def process_all_waveforms(directory):
    A_max_values = []
    for filename in tqdm(os.listdir(directory)):
        if filename.endswith(".txt"):
            waveform_path = os.path.join(directory, filename)
            waveform = np.loadtxt(waveform_path)
            A_max = calc_current_amplitude(waveform)
            A_max_values.append(A_max)
    return A_max_values



def calculate_tn(wf, n=90):
    """
    Calculate the time point of the maximum amplitude (tp_max) and the time
    when the waveform reaches n% of its maximum amplitude (tn).

    Parameters
    ----------
    wf : np.ndarray
        The waveform array, assumed to be baseline-subtracted and pole-zero corrected.

    Returns
    -------
    t90 : float
        The time point (in samples) where the waveform reaches n% of its maximum amplitude.
    tp_max : int
        The index of the maximum amplitude in the waveform.
    """
    # Ensure wf is a numpy array
    wf = np.asarray(wf)

    # Find the maximum amplitude and its index
    max_amplitude = np.max(wf)
    tp_max = np.argmax(wf)

    # Calculate n% of the maximum amplitude
    
    threshold_n = n/100 * max_amplitude

    # Initialize t90 as NaN
    tn = np.nan

    # Search for the crossing point
    for i in range(len(wf)):
        if wf[i] >= threshold_n:
            tn = i
            break
    return tn