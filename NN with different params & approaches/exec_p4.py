import network3p4
from network3p4 import Network
from network3p4 import ConvPoolLayer, FullyConnectedLayer, SoftmaxLayer
training_data, validation_data, test_data = network3p4.load_data_shared()
mini_batch_size = 10
net = Network([
        ConvPoolLayer(image_shape=(mini_batch_size, 1, 28, 28), 
                      filter_shape=(5, 1, 5, 5), 
                      poolsize=(2, 2)),
        FullyConnectedLayer(n_in=5*12*12, n_out=30),
        SoftmaxLayer(n_in=30, n_out=10)], mini_batch_size)
net.SGD(training_data, mini_batch_size, 0.1, 
            validation_data, test_data, es=10)