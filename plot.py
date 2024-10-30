import matplotlib.pyplot as plt

def plot_data(file_path):
    """
    Reads x-y coordinates from a file and generates a scatter plot.

    Args:
        file_path (str): Path to the file containing coordinates.
    """
    x_coords, y_coords = [], []

    with open(file_path, 'r') as file:
        next(file)  # Skip header row (if present)
        for line in file:
            x, y = map(float, line.split(','))
            x_coords.append(x)
            y_coords.append(y)

    # Print coordinates for debugging (optional)
    # print("X Coordinates:", x_coords)
    # print("Y Coordinates:", y_coords)

    plt.scatter(x_coords, y_coords)
    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('Scatter Plot of Coordinates')
    plt.grid(True)
    plt.show()
plot_data('C:/Users/USER/Desktop/SEAN/x_y_coordinates.txt')



