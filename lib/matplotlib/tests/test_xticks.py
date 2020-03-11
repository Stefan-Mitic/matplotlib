import pytest
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import numpy as np

# Test for setting one tick on the x-axis  
@image_comparison(baseline_images=['xticks'], extensions=['png'])
def test_xticks():
    _, ax3 = plt.subplots(1, 1, figsize=(3, 3))
    for ax in [ax3]:
        ax.plot([1, 2])
    ax3.set_xticks([2])

# Test for setting one tick on the x-axis for a large scale
@image_comparison(baseline_images=['xticks_large_scale'], extensions=['png'])
def test_xticks_large_scale():
    _, ax3 = plt.subplots(1, 1, figsize=(3, 3))
    for ax in [ax3]:
        ax.plot([1, 2])
    ax3.set_xticks([100])

# Test for setting one tick on the x-axis for a smaller scale
@image_comparison(baseline_images=['xticks_small_scale'], extensions=['png'])
def test_xticks_small_scale():
    _, ax3 = plt.subplots(1, 1, figsize=(3, 3))
    for ax in [ax3]:
        ax.plot([1, 2])
    ax3.set_xticks([0.5])
    
# Test for normal behavior with no ticks set 
@image_comparison(baseline_images=['xticks_empty'], extensions=['png'])
def test_xticks_empty():
    _, ax3 = plt.subplots(1, 1, figsize=(3, 3))
    for ax in [ax3]:
        ax.plot([1, 2])
    ax3.set_xticks([])

# Test for normal behavior with a tick range 
@image_comparison(baseline_images=['xticks_range'], extensions=['png'])
def test_xticks_range():
    _, ax3 = plt.subplots(1, 1, figsize=(3, 3))
    for ax in [ax3]:
        ax.plot([1, 2])
    ax3.set_xticks([1, 2])
    
