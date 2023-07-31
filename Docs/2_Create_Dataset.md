# Create Dataset

## Overview

In this project, we are working with "The Simpsons Characters Dataset" obtained from Kaggle. You can download the dataset from the following link: [The Simpsons Characters Dataset](https://www.kaggle.com/datasets/alexattia/the-simpsons-characters-dataset?resource=download)

**Note:** You don't have to download it separately, as it's already included in the project.

The dataset is available in the folder named `simpsons_dataset`. For our model to work properly, we have configured the `config.yaml` file with the `resize_method: interpolate` and set the width and height to 128x128, indicating that our model will only handle images of these sizes.

## Converting Images to CSV

Before training our model, we need to convert the images inside the `simpsons_dataset` folder into a CSV file for better handling. To do this, follow these steps:

1. Navigate to the `utilities.py` file.
2. Modify the path from line 84 to your current dataset path.


Once these steps are completed, you will have your dataset in CSV format and ready to use for training the model!

---