## Handwritten Digit Recognition with a Neural Network and Interactive Drawing App

In this project, I implemented a Convolutional Neural Network (CNN) to recognize handwritten digits (0–9). The model was trained on the MNIST dataset, which contains 28x28 grayscale images of digits.

After training the CNN, I developed a simple interactive application that allows users to draw a digit on a canvas. The drawing is processed, resized to the correct input dimensions, and then passed to the trained CNN, which predicts the digit in real time.

The work was divided into three main parts:

Data Preparation & Model Training

Loading and preprocessing the MNIST dataset.

Designing, training, and evaluating the CNN.

Model Deployment

Saving the trained model and reusing it in the application environment.

Interactive Drawing App

Building a graphical interface with a drawing canvas.

Preprocessing the user’s input to fit the CNN format.

Displaying the predicted digit instantly.

Outcome:
The result is a trained CNN with strong accuracy on MNIST, integrated into an interactive app where users can freely draw digits and immediately see the model’s prediction.
