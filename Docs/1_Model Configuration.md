
# Ludwig Image Recognizer

![Ludwig Logo](https://ludwig.ai/latest/images/ludwig_logo.svg)

Ludwig Image Recognizer is a deep learning model that uses the power of [Ludwig](https://ludwig-ai.github.io/ludwig/) to recognize and classify images of characters. It utilizes the popular ResNet image encoder to learn meaningful representations from the input images and predicts the character label associated with each image.

## Model Configuration

The model configuration is defined in the `ludwig.yaml` file. Below is an explanation of the configuration for this image recognizer:

```yaml
input_features:
  -
    name: image_name
    type: image
    encoder: resnet
    preprocessing:
      resize_method: interpolate
      width: 128
      height: 128
```

Explanation of `input_features`:

- `name: image_name`: This is the name of the input feature. You can choose any name you prefer.
- `type: image`: Indicates that this input feature is of type 'image', as we are dealing with image data.
- `encoder: resnet`: Specifies the image encoder to be used, in this case, ResNet.
- `preprocessing`: Defines the preprocessing steps for the input images.
  - `resize_method: interpolate`: This method is used to resize the images to a specific size, in this case, 128x128 pixels.
  - `width: 128`: The width of the resized image.
  - `height: 128`: The height of the resized image.

```yaml
output_features:
  -
    name: label
    type: category
```

Explanation of `output_features`:

- `name: label`: This is the name of the output feature. Here, it is 'label', representing the character label prediction.
- `type: category`: Indicates that the output feature is of type 'category', as we are performing a categorical prediction task.

```yaml
training:
  batch_size: 16
  epochs: 50
```

Explanation of `training`:

- `batch_size: 16`: Specifies the batch size used during training. Adjust this value based on your hardware resources and model size.
- `epochs: 50`: Indicates the number of epochs (iterations) to train the model. Increase or decrease as needed to optimize performance.

---

Please note that this is just a basic configuration for an image recognizer model using Ludwig. Depending on your specific use case and data, you may need to adjust the configuration accordingly. For more details and advanced options, refer to the official Ludwig documentation.

For running the training, you can use the following command:

```bash
ludwig train --config <path_to_config_file>
```

Replace `<path_to_config_file>` with the actual path to your `ludwig.yaml` configuration file.

Happy training with Ludwig! 🚀

---