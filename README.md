# 🧠 GRU-CoreML: An CoreML compatible gated recurrent unit neural network for dynamic prediction

## 🚀 Description

This repository houses an implementation of a Gated Recurrent Unit (GRU) neural network, specifically designed for iOS apps using Core ML. What makes this model unique is its ability to learn and improve over time by training on user data collected during app usage. The model specializes in predicting the next enum value based on previously selected enum values and time.

## 🛠️ Requirements

- iOS 13.0+
- Xcode 11+
- Python 3+
- Keras 2.4+
- TensorFlow 2+
- Coremltools 4+

## 🔧 Usage

1. Clone the repository:
   ```
   git clone https://github.com/denismurphy/gru-coreml.git
   ```

2. Open the project in Xcode and add the Core ML and Core Data frameworks.

3. Use the provided Python script to train the model on your data.

4. Convert the trained model to Core ML format using the coremltools package.

5. Drag and drop the generated .mlmodel file into your Xcode project.

6. Integrate the model in your iOS app for predictions.

7. Implement data collection and model updating mechanisms for continuous improvement.

## ⚠️ Limitations

- The model is currently limited to predicting the next enum value based on previous enum values and time.
- Model accuracy is dependent on the quality and quantity of training data.
- Compatible only with iOS 13.0 and above.

## 🔮 Future Work

- [ ] Implement LSTM alongside GRU for performance comparison
- [ ] Experiment with advanced architectures (e.g., stacked layers, bidirectional layers)
- [ ] Develop more sophisticated data collection and processing methods
- [ ] Explore multi-task learning capabilities

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
