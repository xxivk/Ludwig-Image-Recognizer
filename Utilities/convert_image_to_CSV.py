import os
import csv

# Replace this with the absolute path to your data folder
data_folder = "simpsons_dataset"

csv_file_path = "train.csv"

# Create or overwrite the CSV file with UTF-8 encoding
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)


    # Write the header
    writer.writerow(["image_name", "label"])

    # Loop through the dataset and write the absolute image paths
    for root, _, files in os.walk(data_folder):
        for file in files:
            if file.endswith(".jpg"):
                image_path = os.path.join(root, file)

                try:
                    # Write the absolute image path to the CSV file
                    writer.writerow([image_path])
                except Exception as e:
                    print(f"Error writing image path: {image_path}, Error: {e}")






