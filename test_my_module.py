from my_module import plot_function, Chooser, solve_problem, square_number
import numpy as np
import pytest

def test_plot_function():
    try:
        plot_function(np.sin, (-np.pi, np.pi))  # Plot sin(x) over the range -π to π
    except Exception as e:
        pytest.fail(f"plot_function raised an exception: {e}")

def test_chooser():
    items = [10, 20, 30, 40]
    chooser = Chooser(items)
    
    assert chooser.choose(2) == 30, "Chooser failed on valid index"
    
    assert chooser.choose(5) is None, "Chooser failed on out-of-bounds index"

    assert chooser.choose(-1) is None, "Chooser failed on negative index"

def test_solve_problem():
    assert solve_problem([1, 2, 3, 4, 5]) == 15, "solve_problem failed on [1, 2, 3, 4, 5]"

    assert solve_problem([]) == 0, "solve_problem failed on empty list"
    assert solve_problem([-1, -2, -3]) == -6, "solve_problem failed on negative numbers"
    assert solve_problem([10, -5, 5]) == 10, "solve_problem failed on mixed numbers"

def test_square_number():
    result = square_number(4)
    assert result == 16, f"Expected 16, but got {result}"

    result = square_number(0)
    assert result == 0, f"Expected 0, but got {result}"

    result = square_number(-3)
    assert result == 9, f"Expected 9, but got {result}"