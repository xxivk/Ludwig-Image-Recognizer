## Testing the Trained Model

So far, we are making good progress! You may have noticed a new folder in your working directory that contains the training results, including the model file with the extension `.ckpt` and other files for analyzing the model's performance.

Now, let's put our trained model to the test!

1. First, we need another set of images for the Simpsons characters to evaluate the model. For your convenience, I've prepared a folder named `test_image` with some sample images. Please note that we need to resize these images to the required size (128x128) before prediction. The images have already been resized for you, but you can resize images yourself by using the Python file located at `Utilities/resize_test_images.py`.

2. Next, we need to create a dataset for testing our images in the `test_image` folder. To do this, navigate to the file `Utilities/convert_image_to_CSV.py` and make the following modifications:

   - Set `data_folder` to the path of the `test_image` folder.
   - In line 7, set `csv_file_path` to the desired name for the test CSV file, e.g., `test.csv`.
   - Comment out the label in line 15 by changing it to `writer.writerow(["image_name"])#, "label"])` because we only need to predict the label (check `config.yaml` for further information).
   - In line 20, select the image format used in the `test_image` folder (e.g., jpg).

   After making these changes, run the Python script, and it will generate the CSV file `test.csv`, which will be used for prediction.

   **Note:** Ludwig supports various image formats as input for training and prediction. The supported image formats are typically those supported by the Python Imaging Library (PIL) or its fork, Pillow. These formats include, but are not limited to:
   - JPEG (.jpg, .jpeg)
   - PNG (.png)
   - BMP (.bmp)
   - GIF (.gif)
   - TIFF (.tiff, .tif)
   - WebP (.webp)
   - PPM (.ppm)
   - PGM (.pgm)
   - PBM (.pbm)
   - SR (.sr)
   - RAS (.ras)
   - ICO (.ico)

## Predicting with the Model

Now that we have our test dataset ready, let's use our trained model to make predictions!

Run the following command in your command line or terminal:

```bash
ludwig predict --model_path <path_to_model_folder> --dataset <path_to_test_csv> --output_directory <path_to_store_prediction_results>
```

Replace `<path_to_model_folder>` with the path to the folder containing your trained model files (including the `.ckpt` file). Similarly, replace `<path_to_test_csv>` with the path to the `test.csv` file generated in the previous step. Lastly, set `<path_to_store_prediction_results>` to the desired location where you want to store the prediction results.

After you run this command, Ludwig will perform predictions on the test images, and you should find a new folder with the prediction results.

Congratulations! You've successfully tested your own Image Recognizer for Simpsons characters. Enjoy exploring and using your image recognition model!