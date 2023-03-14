# Introduction

Started in 1960's Deep Learning is a subfield of Artificial Intelligence and Machine Learning that is inspired by the structure of human brain.

Deep learning algorithms attempt to draw similar conclusions as humans would by continually analyzing data with a given logical structure called Neural Network.

- Neural Network is inspired by the structure of human brain.
- Examples of some Deep learning models are ANN, CNN, RNN, GAN etc.

This is also be said to be a part of a broader family of machine learning methods based on artificial neural network with representation learning.

Deep Learning Algorithms uses multiple layers to progressively extract higher-level features from the raw input.

- For example, in image processing, lower layers may identify edges, while higher layer may identify the concepts relevant to a human such as digits or letters or faces.

## Why DL

Applicability: Can be applied to a wide domain of problems.

Performance: state of the art

### Why it's Popular now?

Dataset: With the boom of Internet era data also boomed and hence we have lot of data and not just data but labelled data.

- Some examples of popular public dataset in major fields:
  - Text: SQuad
  - Image: Microsoft Coco
  - Video: Youtube 8M
  - Audio: Google Audioset

Hardware: For different devices we can use different and custom hardwares.

- Moore's law: Moore the co-founder of Intel said that the number of transistors in a dense integrated circuit (IC) doubles about every two years.
- For large dataset one can use GPU, TPU.
- For Mobile one can use Mobile CPU, GPU, DSP or NPU.
- For Smart watch or glass one can use Edge TPU, NPU.

Framework/Libraries: TensorFlow, Keras, PyTorch and UI based drag and drop systems like AutoML.

Architecture

- Transfer Learning.
  - Text Classification: BERT
  - Image Classification: ResNET
  - Image Segmentation: UNet
  - Image Translation: Pix2Pix
  - Object Detection: YOLO
  - Speech Generation: WaveNET

Community

## AI VS ML VS DL

AI is any technique that enables computer to mimic human behaviour.

ML is ability to learn without explicitly being programmed.

DL is extracting patterns from data using neural networks.

### DL VS ML

Data Dependency: Deep learning requires more amount of data.

- []()

Hardware Dependency: DL require powerful GPUs (costly hardware) while ML models can be trained with CPU.

Training Time: Training time with DL is quite high.

Feature Selection: With Representation learning DL extracts features automatically

Interpretability: DL is like a black box and hence fails for interpretability because we don't know what learning was done by DL to come to a conclusion.

## Application of DL

Self Driving Car
Game Playing Agents
Virtual Assistance
Image Colorization
Adding audio to mute videos
Image Caption Generation
Text Translation
Pixel Restoration
Object Detection
Generate Audio, Video, Image, Text using GAN

# Types of Neural Network

There are a lot of Neural Networks some of them are:

- MLP (Multilayer Perceptron): Mostly used in supervised problems.
- CNN (Convolutional Neural Network): Mostly used in Image and Video Processing.
- RNN (Recurrent Neural Network):
  - LSTM (Long Short Term Memory)
- Auto Encoders: Compression without lossing the quality
- GAN (Generative adversarial network)

# Perceptron

## History

An artificial neuron is a mathematical function based on a model of biological neurons, where each neuron takes inputs, weighs them separately, sums them up and passes this sum through a nonlinear function to produce output.

It is an elementary unit in an artificial neural network.

## Introduction

A neural network link that contains computations to track features and uses Artificial Intelligence in the input data is known as Perceptron. This neural links to the artificial neurons using simple logic gates with binary outputs.

A Perceptron is an algorithm for supervised learning of binary classifiers.

The Perceptron algorithm learns the weights for the input signals in order to draw a linear decision boundary.

## Geometric Intuition of Perceptron

Line, Plane and Hyperplane

Limitation of only linearly seperable dataset

## Types of Perceptron

There are 2 major types of perceptron

- Single layer: Single layer perceptron can learn only linearly separable patterns.
- Multilayer: Multilayer perceptrons can learn about two or more layers having a greater processing power.

## Perceptron VS Neuron

It is said that DL is heavily inspired by human's nervous system and hence it is a good idea to compare Perceptron with Neuron.

Neurons are interconnected nerve cells in the human brain that are involved in processing and transmitting chemical and electrical signals.

- Dendrites are branches that receive information from other neurons.
- Cell nucleus or Soma processes the information received from dendrites.
- Synapse is the connection between an axon and other neuron dendrites.
- Axon is a cable that is used by neurons to send information.

An artificial neuron invokes the mathematical function and has node, input, weights, and output equivalent to the cell nucleus, dendrites, synapse, and axon, respectively, compared to a biological neuron.

Perceptron is weakly inspired by Neuron the reason to say that are:

- Neuron is quite complex.
- The internal processing in the Nucleus is unknown.
- Neuroplasticity

## Training Perceptron

Dot product, bias and non-linearity (activation function)

### Common Activation Function

Sigmoid

Hyperbolic Tangent

Rectified Linear Unit (ReLU)

> All activation functions are non-linear.

### Perceptron Rule

EPOCHS and Conevergence
learning rate

**Alogorithm**

```py
# M1
for i in EPOCHS:
  data = dataset.random()
  Wn = Wo + n(Yi - Yio)Xi

# M2
while convergence:
  data = dataset.random()
  Wn = Wo + n(Yi - Yio)Xi
```

### Loss Functions

# ANN

Layers
Input layer
Hidden Layers
Output layer
Perceptron
Weights
