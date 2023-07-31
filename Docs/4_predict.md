So far we are doing good you might noticed new folder in your working Dir contains train results and the model file called .ckpt and other files to analysis the model process .

## lets test it now to see if its works !!
1 - lets bring other image for same simpsons and i already did it for you in folder named : test_image
Note : please not that we need to resize the images as we mentioned before 128x128 ( because our model set for this sizes) you can resize images by going to python file here Utilities\resize_test_images.py
but i already done it for you .
2- lets lets create Dataset for testing our images in folder test_image as you see it contains pictures we need to convert it as CSV file to predict, go to file Utilities\convert_image_to_CSV.py and modify the following:
 1 - data_folder = "set_image_folder" add the path for test_image folder,and in line 7 set csv_file_path = "name_csv" so the test.csv file stored 
 2 - make sure you comment label in line 15 writer.writerow(["image_name"])#, "label"])because we dont need label we want to predict the label ( check config.yaml) for further information
 3 - in line 20 select image format as we have its jpg , run the code you will get CSV file for test.
 note : Ludwig supports various image formats as input for training and prediction. When using image data in Ludwig, the supported image formats are typically those supported by the Python Imaging Library (PIL) or its fork, Pillow. These formats include, but are not limited to:
JPEG (.jpg, .jpeg)
PNG (.png)
BMP (.bmp)
GIF (.gif)
TIFF (.tiff, .tif)
WebP (.webp)
PPM (.ppm)
PGM (.pgm)
PBM (.pbm)
SR (.sr)
RAS (.ras)
ICO (.ico)
## lets predict now !
ludwig predict --model_path <path_to_model_folder>  --dataset <path_to_test_csv>--output_directory <path_to_store_prediction_results>

after you ran this command it should gives you new folder for prediction results 
