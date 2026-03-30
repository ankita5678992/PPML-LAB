import numpy as np

arr = np.array([10, 20, 30, 40])

# Save array to file
np.save('my_array.npy', arr)

# Load array from file
loaded_arr = np.load('my_array.npy')

print("Loaded Array:", loaded_arr)