from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = load_image('/content/image.jpg')  # Replace with your image path

if image is not None:
    # Apply median filter for noise reduction
    clean_image = median(image, ball(3))

    # Perform edge detection
    edgeMAG = edge_detection(clean_image)

    # Display the histogram to choose a threshold
    plt.hist(edgeMAG.ravel(), bins=256)
    plt.show()

    # Choose a threshold value based on the histogram (example: 50)
    threshold = 50  
    edge_binary = edgeMAG > threshold

    # Convert the binary array to an image and save it
    edge_image = Image.fromarray((edge_binary * 255).astype(np.uint8))
    edge_image.save('my_edges.png')
    plt.imshow(edge_binary, cmap='gray')
    plt.show()
