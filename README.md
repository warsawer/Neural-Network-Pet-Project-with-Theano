# Neural Network (with Theano)
## Introduction
This is a Theano-based program for training and running simple neural
networks.

Supports several layer types (fully connected, convolutional, max
pooling, softmax), and activation functions (sigmoid, tanh, and
rectified linear units, with more easily added).

When run on a CPU, this program is much faster.  However, hand-made networks (I mean without any libraries, like in [this repo](https://github.com/Warszawer/Neural-Network-from-Scratch)) it can also
be run on a GPU, which makes it faster still.

Because the code is based on Theano, the code is different in many
ways [from my previous network](https://github.com/Warszawer/Neural-Network-from-Scratch).  However, where possible I have
tried to maintain consistency with the earlier programs.  In
particular, the API is similar to [network.py](https://github.com/Warszawer/Neural-Network-from-Scratch/blob/main/network.py).  Note that I have
focused on making the code simple, easily readable, and easily
modifiable.  It is not optimized, and omits many desirable features.

This program incorporates ideas from the [Theano documentation](https://theano-pymc.readthedocs.io/en/latest/) on
convolutional neural nets.

## What is a Neural Network?
Great question!

A Neural Network can be thought of as a series of nodes (or neurons) that are interconnected, much like they are in the brain. The network can have any number (N) of inputs and any number (M) of outputs. In between the inputs and outputs are a series of "hidden" neurons that make up the hidden layers of the network. These hidden layers provide the meat of the network and allow for some of the neat functionalities we can get out of a Neural Network.

## How Do I Use this Program?
For getting result you need to run "exec" files. They contain the necessary code to run the Neural Network calculation.

## Resources
I used a few resources while building this project. I'm super thankful for those who have done a lot of work previously.
- [Neural Networks and Deep Learning book](http://neuralnetworksanddeeplearning.com)
- [First course of the Deep Learning Specialization by DeepLearning.AI](https://www.coursera.org/learn/neural-networks-deep-learning)
