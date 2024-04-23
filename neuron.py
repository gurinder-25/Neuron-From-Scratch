from data_for_neuron import intercept
from data_for_neuron import slope

# Neuron function with simplified logic
def neuron(inputs, weights, bias, activation_func):
    weighted_sum = sum(z[0]*z[1] for z in zip(inputs, weights)) + bias
    for i in range(len(inputs)):
        weighted_sum+=inputs[i]*weights[i]
    return activation_func(weighted_sum)

def step(x):
    return 0 if x>0 else 1

# Given weights and inputs (here 0.38 is intercept and -3.23 is slope)
weights = [1, (-1*(slope))]
bias = -1*(intercept)
snack1 = [2, 5]
snack2 = [1, 1]

print("snack 1:", neuron(snack1, weights, bias, step))
print("snack 2:", neuron(snack2, weights, bias, step))