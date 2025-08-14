import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from viz3d import load_state_space
import math
import random

class Problem:
    def __init__(self, image_path):
        self.X, self.Y, self.Z = load_state_space(image_path)
        self.X, self.Y = np.meshgrid(self.X, self.Y)
        
    def show(self):
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        plt.show()

    def draw_path(self, path,name):
        path_x = [p[0] for p in path]
        path_y = [p[1] for p in path]
        path_z = [self.Z[p[1], p[0]] for p in path]
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.X, self.Y, self.Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        
        line = ax.plot(path_x, path_y, path_z, 'r-', zorder=5, linewidth=0.5, label='Path') 

        scatter = ax.scatter(path_x, path_y, path_z, color='black', s=5, alpha=0.8, zorder=5, label='Path Points')

        handles, labels = ax.get_legend_handles_labels()
        if labels:
            ax.legend()
        
        ax.set_title(name)
        plt.show()
    
    def get_neighbors(self, state):
        """Generates and returns a list of neighbors for a given state."""
        x, y, _ = state
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.X.shape[1] and 0 <= ny < self.X.shape[0]:
                neighbors.append((nx, ny, int(self.Z[ny, nx])))
        return neighbors

    def safe_exp(self, value):
        """Safely calculates the exponential of a value."""
        if value > 700:
            return float('inf')
        return math.exp(value)
    
    def random_state(self):
        """Generates random state."""
        x = random.randint(0, self.X.shape[1] - 1)
        y = random.randint(0, self.X.shape[0] - 1)
        return x,y
