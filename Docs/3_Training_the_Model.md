## Training the Model

Now that we have our CSV file for training and our `config.yaml` for model configurations, let's proceed with training our image recognizer. Open your command line or terminal and run the following command:

```bash
ludwig train --dataset <path_to_csv_file> --config <path_to_config_file> --output_directory <path_to_export_results>
```

Replace `<path_to_csv_file>` with the path to your CSV file generated from the images. Similarly, replace `<path_to_config_file>` with the path to your `config.yaml` file containing the model configurations. Lastly, set `<path_to_export_results>` to the desired location where you want to export the training results.

Be patient as the training process may take some time, depending on your hardware and the complexity of your model.

## Using the Trained Model

Once the training is completed, congratulations! You now have your own Image Recognizer model for Simpsons characters. You are ready to test it and use it for predictions.

Feel free to use the trained model to make predictions on new images or integrate it into your own projects. Enjoy your image recognition journey!