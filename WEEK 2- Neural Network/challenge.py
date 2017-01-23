import numpy as np
class NeuralNetwork():
    def __init__(self,no_of_hidden_layers,no_of_neurons_per_layer,input_dim, output_dim):
        self.no_hl = no_of_hidden_layers
        self.no_neuron = no_of_neurons_per_layer
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_layers = []
        random.seed(1)

        # making the framework of the model
        for i in range(self.no_hl):
            if i == 0:
                hidden_layer = 2*np.random.random((input_dim , no_neuron[i])) -1
            elif i == self.no_hl -1:
                hidden_layer = 2*np.random.random((no_of_neurons_per_layer[i],output_dim)) - 1
            else:
                hidden_layer = 2*np.random.random((no_of_neurons_per_layer[i-1],no_of_neurons_per_layer[i]))
            self.hidden_layers.append(hidden_layer)

        def __sigmoid(self,x):
            # x is a tensor i.e. a matrix in this case
            return 1/(1+ np.exp(-x))

        #TODO define the backprop algrithm
        # in feedfowrd X is in format as [n,m] where n is the number of training samples and m is the no of features

        def feedforward(self,X):
            for i in range(self.no_hl + 1):

# execution code
"""
if __name__ == '__main__':

    #TODO get the trainig and testing data and lavels
    train_x
    train_y
    test_x
    test_y

    no_of_hidden_layers = 3
    no_of_neurons_per_layer = np.array([10, 10, 10])
    input_dim = 10
    output_dim = 3
    nn = NeuralNetwork(no_of_hidden_layers,no_of_neurons_per_layer,input_dim,output_dim)


    # data loading and preprocessing step

    nn.train(train_x, train_y,lr = 0.01, iter = 100)

    print "Neural Network started .. "
    pred = nn.predict(test_x)
    #TODO make the accuracy statement
"""
