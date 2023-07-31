from PIL import Image
import os

data_folder = "C:/Users/crypto/Desktop/Simpsons/kaggle_simpson_testset/kaggle_simpson_testset"

# Specify the desired width and height
desired_width = 128
desired_height = 128

# Loop through the images in the directory and resize them
for filename in os.listdir(data_folder):
    if filename.endswith(".jpg"):
        image_path = os.path.join(data_folder, filename)
        img = Image.open(image_path)
        img_resized = img.resize((desired_width, desired_height))
        img_resized.save(image_path)
