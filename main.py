from image_utils import load_image, edge_detection
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
import numpy as np
import matplotlib.pyplot as plt

# Load the image
import urllib.request
import matplotlib.pyplot as plt
from image_utils import load_image  # מייבאים את הפונקציה מקובץ image_utils.py

url = "https://raw.githubusercontent.com/your_username/your_repo/main/image.jpg"  
file_path = "image.jpg"

urllib.request.urlretrieve(url, file_path)
print("✔ התמונה נשמרה בהצלחה:", file_path)

# 3. טעינת התמונה עם הפונקציה מ-image_utils.py
image_array = load_image(file_path)

# 4. הצגת התמונה
plt.imshow(image_array)
plt.axis("off")
plt.show()

# 5. בדיקת הצורה של התמונה
print("📏 גודל התמונה:", image_array.shape)

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
