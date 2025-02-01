from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
     try:
    img = Image.open(image_path)
    img_array = np.array(img)
    return img_array
  except FileNotFoundError:
    print(f"Error: Image file not found at {image_path}")
    return None
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

# Example usage:
image_array = load_image('/content/image.jpg') # Replace 'image.jpg' with the path to your image file

if image_array is not None:
  print("Image loaded successfully!")
  print("Image shape:", image_array.shape)
  # You can further process the image_array here.


def edge_detection(image):
    pass # Replace the `pass` with your code
 # Convert to grayscale
    grayscale_image = np.mean(image_array, axis=2).astype(np.float32)

    # Define the filters
    kernelY = np.array([[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]])
    kernelX = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]])
    
    # Apply the filters using convolution
    edgeX = convolve2d(grayscale_image, kernelX, mode='same', boundary='fill', fillvalue=0)
    edgeY = convolve2d(grayscale_image, kernelY, mode='same', boundary='fill', fillvalue=0)

    # Combine the edges
    edgeMAG = np.sqrt(np.square(edgeX) + np.square(edgeY))

    return edgeMAG
