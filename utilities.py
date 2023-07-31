import os
import csv
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

class Utilities:
    def __init__(self):
        pass

    def image_to_csv(self, data_folder, csv_file_path):
        """
        Write the image paths and labels from the data folder to a CSV file.

        Args:
            data_folder (str): Path to the root data folder containing image files in subdirectories.
            csv_file_path (str): Path to the CSV file where the image paths and labels will be written.
        """
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["image_name", "label"])
            
            for root, _, files in os.walk(data_folder):
                for file in files:
                    if file.endswith(".jpg"):
                        image_path = os.path.join(root, file)
                        label = os.path.basename(root)
                        
                        try:
                            writer.writerow([image_path, label])
                        except Exception as e:
                            print(f"Error writing image path: {image_path}, Error: {e}")

    def resize_images(self, data_folder, desired_width, desired_height):
        """
        Resize images in the specified data folder to the desired width and height.

        Args:
            data_folder (str): Path to the folder containing the images to be resized.
            desired_width (int): The desired width of the images after resizing.
            desired_height (int): The desired height of the images after resizing.
        """
        for filename in os.listdir(data_folder):
            if filename.endswith(".jpg"):
                image_path = os.path.join(data_folder, filename)
                img = Image.open(image_path)
                img_resized = img.resize((desired_width, desired_height))
                img_resized.save(image_path)

    def save_predicted_images(self, test_csv_path, predictions_csv_path, predicted_images_dir):
        """
        Load test and prediction data, display images with predicted and actual labels, and save them.

        Args:
            test_csv_path (str): Path to the CSV file containing test data with image paths.
            predictions_csv_path (str): Path to the CSV file containing prediction results with labels.
            predicted_images_dir (str): Directory path where the predicted images will be saved.
        """
        test_df = pd.read_csv(test_csv_path)
        predictions_df = pd.read_csv(predictions_csv_path, header=None, names=['predicted_label'])

        os.makedirs(predicted_images_dir, exist_ok=True)

        for index, row in test_df.iterrows():
            image_path = row['image_name']
            predicted_label = predictions_df.at[index, 'predicted_label']
            actual_label = image_path.split('\\')[-1].split('_')[0]

            image = Image.open(image_path)

            plt.imshow(image)
            plt.title(f'Predicted Label: {predicted_label}, Actual Label: {actual_label}')
            plt.axis('off')

            save_path = os.path.join(predicted_images_dir, f'{predicted_label}_actual_{actual_label}.jpg')
            plt.savefig(save_path, bbox_inches='tight')
            plt.close()

            # Show the image (uncomment this line if you want to see the images while the code runs)
            # plt.show()

        print("Predicted images saved in the specified directory.")


if __name__ == "__main__":
    # Specify the paths to the data and files
    data_folder = "test_image"
    csv_file_path = "test.csv"
    test_csv_path = 'test.csv'
    predictions_csv_path = 'label_predictions.csv'
    predicted_images_dir = 'predicted_images'  # Replace this with the desired directory path


    
    # Create an instance of the Utilities class
    utils = Utilities()

    # Resize images in the data folder to the desired width and height
    # utils.resize_images(data_folder, desired_width=128, desired_height=128)

    # Write the image paths and labels from the data folder to a CSV file
    #utils.save_predicted_images(test_csv_path, predictions_csv_path, predicted_images_dir)

    # Load test and prediction data, display images with predicted and actual labels, and save them
    #utils.save_predicted_images(test_csv_path, predictions_csv_path, predicted_images_dir)
