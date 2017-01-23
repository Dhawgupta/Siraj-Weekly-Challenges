from numpy import exp, array , random, dot
class NeuralNetwork():
    def __init__(self):
        random.seed(1)
        self.synaptic_weights = 2*random.random((3,1)) - 1
    def __sigmoid(self,x):
        return 1/(1+exp(-x))

    def __sigmoid_derivative(self,x):
        return  x*(1-x)

    def train(self, training_set_inputs,training_set_outputs,num_iter):
        for iteration in  range(num_iter):
            output = self.think(training_set_inputs)

            error = training_set_outputs - output
            adjustment = dot(training_set_inputs.T, error*self.__sigmoid_derivative(output))
            self.synaptic_weights += adjustment

    def think(self,inputs):
        return self.__sigmoid(dot(inputs,self.synaptic_weights))

if __name__ == '__main__':

    neural_network = NeuralNetwork()
    print "Random starting synaptic weights"
    print neural_network.synaptic_weights

    # training set having 4 exp , each of 3 inputs
    # and 1 output value
    training_set_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    # training the neural neural_network
    # doing 10,000 times and making small adjustments
    neural_network.train(training_set_inputs,training_set_outputs,10000)

    print 'New weights after training are :'
    print neural_network.synaptic_weights

    print "Considering New situation [1,0,0] -> "
    print neural_network.think(array([1,0,0]))
