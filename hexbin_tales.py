import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mpl_colors
import numpy as np
import random
import time
import requests
import duckdb
import math
import mplcursors

def draw_hexagon(ax, center, size, facecolor='none'):
    """Draw a hexagon with a given size at center (x, y)"""
    hexagon = patches.RegularPolygon(center, numVertices=6, radius=size,
                                     orientation=np.radians(30), facecolor=facecolor)
    ax.add_patch(hexagon)

def draw_hexagon_grid(ax, grid_width, grid_height, hex_size, values_df, distribution):
    """Draw a grid of hexagons colored by values from the DataFrame."""
    # The distance between centers of two consecutive hexagons in the grid
    dx = 3/2 * hex_size
    dy = np.sqrt(3) * hex_size

    # Normalize the 'Value' column for the colormap
    if distribution == "log":
        norm = mpl_colors.LogNorm(values_df['amount'].min(), values_df['amount'].max())
        cmap = plt.get_cmap('plasma')  # You can choose your colormap
    else:
        norm = mpl_colors.Normalize(values_df['amount'].min(), values_df['amount'].max())
        cmap = plt.get_cmap('inferno')  # You can choose your colormap

    # Calculate the offset for centering the hexagon grid
    offset_x = (grid_width / 2) * dx
    offset_y = (grid_height / 2) * dy

    # Create the hexagon grid
    for x in range(grid_width):
        for y in range(grid_height):
            index = x * grid_height + y
            if index < len(values_df):
                value = values_df.loc[index, 'amount']
                color = cmap(norm(value))  # Map the value to a color
            else:
                color = 'white'

            center_x = (x * dx) - offset_x
            center_y = ((y + (x % 2) / 2) * dy) - offset_y

            # Save center_x, center_y, and color in the DataFrame
            values_df.at[index, 'center_x'] = center_x
            values_df.at[index, 'center_y'] = center_y
            values_df.at[index, 'color'] = norm(value)

            draw_hexagon(ax, (center_x, center_y), hex_size, facecolor=color)
    
    return values_df

# Read records of projects with direct donations greater than $10
query_result = pd.read_csv('2023_direct_donations_by_project.csv')

# Determine the size of the grid based on the number of results in the query
grid_size = math.ceil(math.sqrt(len(query_result)))

# Sort the DataFrame based on creation date
query_result.sort_values(by='created_at', ascending=False, inplace=True)
query_result.reset_index(drop=True, inplace=True)

# Set up the plot
fig, ax1 = plt.subplots()
ax1.set_aspect('equal')

# Set the limits of the plot
ax1.set_xlim(-20, 20)
ax1.set_ylim(-20, 20)

# Remove the axes for visual appeal
ax1.axis('off')
ax1.set_facecolor('black')

# Size of the hexagon 
hex_size = 0.5

def update(frame):
    # normal distribution
    plt.pause(0.1)
    df_norm = draw_hexagon_grid(ax1, grid_size, grid_size, hex_size, query_result, "")

    #log distribution
    plt.pause(0.1)
    df_log = draw_hexagon_grid(ax1, grid_size, grid_size, hex_size, query_result, "log")
    df_log.to_csv("2023_direct_donations_by_project_updated.csv")

# Create the animation
ani = FuncAnimation(fig, update, frames=1, repeat=True)

plt.show()
