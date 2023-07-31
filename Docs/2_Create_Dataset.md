First i have downloaded the dataset from Kaggle link is here https://www.kaggle.com/datasets/alexattia/the-simpsons-characters-dataset?resource=download

# note you dont have to download it its already in the project .
the dataset is in folder named simpsons_dataset 
as you see before when creating config.yaml file we used resize resize_method: interpolate and both of width and height is set into 128x128 so OUR MODEL WONT DEAL BUT ONLY WITH THOSE SIZES !
## converting Images inside simpsons_dataset folder to CSV file !
go to Utilities\convert_image_to_CSV.py line 5  and modify the path to your current dataset path and set the csv_file_path name to gives you output as CSV file.
after this we have our dataset and ready to Train our model !!
