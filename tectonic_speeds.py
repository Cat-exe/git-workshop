
# Import the library, matplotlib
import matplotlib.pyplot as plt

# List of oceanic vs. continental plate speeds
oceanic = [7.87, 7.74, 6.11, 7.69, 4.16, 4.0]
continental = [1.71, 4.34, 2.00, 3.35, 1.96, 2.14]

# Find the averages
oceanic_avg = sum(oceanic)/len(oceanic)
continental_avg = sum(continental)/len(continental)

bar_chart = plt.bar(x_locs, bar_heights, width = 3)
