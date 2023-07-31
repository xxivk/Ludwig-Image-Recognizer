import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import os

# Read the 'test.csv' and 'label_predictions.csv' files
test_df = pd.read_csv('test.csv')
predictions_df = pd.read_csv('results\prediction\label_predictions.csv', header=None, names=['predicted_label'])

# Create the directory for saving the predicted images
predicted_images_dir = 'predicted_images'
os.makedirs(predicted_images_dir, exist_ok=True)

# Iterate through each row and save the image with the predicted and actual labels
for index, row in test_df.iterrows():
    image_path = row['image_name']
    predicted_label = predictions_df.at[index, 'predicted_label']
    
    # Get the actual label from the image_path (extracting the last part of the path before the underscore)
    actual_label = image_path.split('\\')[-1].split('_')[0]
    
    # Open the image using PIL
    image = Image.open(image_path)
    
    # Display the image with the predicted and actual labels as title
    plt.imshow(image)
    plt.title(f'Predicted Label: {predicted_label}, Actual Label: {actual_label}')
    plt.axis('off')
    
    # Save the image with the predicted and actual labels as the filename
    save_path = os.path.join(predicted_images_dir, f'{predicted_label}_actual_{actual_label}.jpg')
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()

print("Predicted images saved in the 'predicted_images' directory.")
