# GRU-CoreML: An CoreML compatible gated recurrent unit neural network for dynamic prediction

## Description

This repository contains an implementation of a GRU neural network that can be used in iOS apps with Core ML. The model is trained on user data collected while the app is running (all training on device), making it more accurate over time. The model is able to predict the next enum value based on previous selected enum values and time.

## Requirements

-   iOS 13.0+
-   Xcode 11+
-   Python 3+
-   Keras 2.4+
-   Tensorflow 2+
-   Coremltools 4+

## Usage

1.  Clone the repository:

`git clone https://github.com/denismurphy/gru-coreml.git` 

2.  Open the project in Xcode and add the Core ML and Core Data frameworks.
    
3.  Use the provided Python script to train the model on your data.
    
4.  Convert the trained model to Core ML format using the coremltools package.
    
5.  Drag and drop the generated .mlmodel file into your Xcode project.
    
6.  Use the model in your iOS app to make predictions.
    
7.  Collect data and update the model while the app is running.
    

## Limitations

-   The model is only able to predict the next enum value based on previous selected enum values and time.

-   The accuracy of the model depends on the quality and quantity of the data used to train it.
-   The model is only compatible with iOS 13.0 and above.

## Future Work

-   Implementing LSTM in addition to GRU to see which one gives better results
-   Experiment with different architectures like stacked layers, bidirectional layers
-   Implementing more sophisticated data collection and processing methods to improve the model's performance.

## Contributions

All contributions are welcome, feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## Authors

-   **Denis Murphy**

## License

This project is licensed under the MIT License.
