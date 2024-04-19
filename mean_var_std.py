import numpy as np

def calculate(lst):

    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(lst).reshape(3, 3)

    mean = [list(arr.mean(axis=0)), list(arr.mean(axis=1)), arr.mean()]
    variance = [list(arr.var(axis=0)), list(arr.var(axis=1)), arr.var()]
    std_dev = [list(arr.std(axis=0)), list(arr.std(axis=1)), arr.std()]
    max_val = [list(arr.max(axis=0)), list(arr.max(axis=1)), arr.max()]
    min_val = [list(arr.min(axis=0)), list(arr.min(axis=1)), arr.min()]
    sum_val = [list(arr.sum(axis=0)), list(arr.sum(axis=1)), arr.sum()]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    return calculations
