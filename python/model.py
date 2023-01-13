import numpy as np
from enum_type import EnumType
from keras.layers import GRU, Dense, Input
from keras.models import Model
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import coremltools;

# because we are doing all the training on iOS device
# the training data will have no effect. it will learn from the user data as it been generated on device
data = []
for event_type in list(EnumType):
    data.append([event_type, 0])

# Split the data into training and test sets
X = np.array([d[0] for d in data])

# Splits the X array into two arrays, X_train and X_test with a test size of 0.2
X_train, X_test = train_test_split(X, test_size=0.2)

# Creates an array X_train containing the numerical values of the event_type enum items in the X_train array
X_train = np.array([event_type.value for event_type in X_train])

# Creates an array X_test containing the numerical values of the event_type enum items in the X_test array
X_test = np.array([event_type.value for event_type in X_test])

# one-hot-encoding from enum to numerical value
X_train = to_categorical(X_train)
X_test = to_categorical(X_test)

# adds a new dimension to both arrays on axis 1
X_train = np.expand_dims(X_train, axis=1)
X_test = np.expand_dims(X_test, axis=1)

# Assigns the length of the enum to both variables
input_size = len(EnumType)
output_size = len(EnumType)

# Define the input layer
inputs = Input(shape=(1, input_size))

# Define the GRU layer. A type of recurrent neural network that can handle input of varying length
gru = GRU(units=64, return_sequences=True)(inputs)

# Define the output layer, with softmax activation function which returns probability distribution over the output
outputs = Dense(output_size, activation='softmax')(gru)

# Create the model
model = Model(inputs, outputs)

# Compile the model with optimizer, loss function and evaluation metric
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

# Fit the model with the training data
model.fit(X_train, X_train, epochs=10, batch_size=64)

# Save the model
model.save('gru_model.h5')

# CoreML converting code not working at the moment
# Convert to CoreML model for iOS
#coreml_model = coremltools.converters.keras.convert(model, input_names=['input_1'], output_names=['dense'])
#coreml_model.save('GRU.mlmodel')