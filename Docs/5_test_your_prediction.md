Now you have trained and predict your dataset lets see the result we need the following files :
1 - Prediction CSV = the csv file that generated after prediction 
2 - test dataset CSV = the test csv file that we create before in step 4 

go to file Utilities\save_predicted_images.py  and modify the following :
line 7 test_df = pd.read_csv('test.csv') add the test csv file
line 8 predictions_df = pd.read_csv('add_Prediction_CSV_file', header=None, names=['predicted_label'])
line 11 predicted_images_dir = 'set_path_for_predicted_images'to store it 

now run the python file !
you will see there is new folder called predicted_images  with predicted label from out model.! we done 


DONT BUY ME COFFEE BUT ME A HOUSE !