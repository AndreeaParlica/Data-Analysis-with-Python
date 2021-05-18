# Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

# The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

# The returned dictionary should follow this format:

# {
#   'mean': [axis1, axis2, flattened],
#   'variance': [axis1, axis2, flattened],
#   'standard deviation': [axis1, axis2, flattened],
#   'max': [axis1, axis2, flattened],
#   'min': [axis1, axis2, flattened],
#   'sum': [axis1, axis2, flattened]
# }

# If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.


import numpy as np

def calculate(list):
    array = np.array(list)

    try:
        matrix = array.reshape((3, 3))
    except ValueError:
        raise ValueError("List must contain nine numbers.")
    else:
        mean = [np.mean(matrix, axis=0).tolist(), np.mean(
            matrix, axis=1).tolist(), np.mean(array).tolist()]

        variance = [np.var(matrix, axis=0).tolist(), np.var(
            matrix, axis=1).tolist(), np.var(array).tolist()]

        # feel free to use np.std() instead
        standard_deviation = [(np.array(v) ** 0.5).tolist() for v in variance]

        max = [np.max(matrix, axis=0).tolist(), np.max(
            matrix, axis=1).tolist(), np.max(array).tolist()]
        min = [np.min(matrix, axis=0).tolist(), np.min(
            matrix, axis=1).tolist(), np.min(array).tolist()]
        sum = [np.sum(matrix, axis=0).tolist(), np.sum(
            matrix, axis=1).tolist(), np.sum(array).tolist()]

        calculations = {
            "mean": mean,
            "variance": variance,
            "standard deviation": standard_deviation,
            "max": max,
            "min": min,
            "sum": sum
        }

        return calculations
