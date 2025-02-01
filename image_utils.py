from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(file_path):
     try:
    image = Image.open(file_path)
    image_array = np.array(image)
    return image_array
  except FileNotFoundError:
    print(f"Error: Image file not found")
    return None
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

def edge_detection(image):
    gray_image = np.mean(image_array, axis=2)
    kernelY = np.array([[1 ,2 ,1], [0 ,0 ,0], [-1, -2, -1]])
    kernelX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    
    # Apply the filters using convolution
    edgeX = convolve2d(gray_image, kernelX, mode='constant',cval=0.0)
    edgeY = convolve2d(gray_image, kernelY, mode='constant', cval=0.0)

    # Combine the edges
    edgeMAG = np.sqrt(np.square(edgeX) + np.square(edgeY))

    return edgeMAG
