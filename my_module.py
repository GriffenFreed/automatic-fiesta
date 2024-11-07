import matplotlib.pyplot as plt
import numpy as np

def plot_function(func, x):
    x = np.linspace(x[0], x[1], 100)
    y = func(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Plot of {func.__name__}')
    plt.grid(True)
    plt.show()

class Chooser:
    def __init__(self, items):
        self.items = items

    def choose(self, index):
        return self.items[index] if 0 <= index < len(self.items) else None

def solve_problem(nums):
    return sum(nums)
