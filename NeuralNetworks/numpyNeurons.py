import numpy as np

weights1 = [0.2, 0.8, -0.5, 1]
weights2 = [.5, -.91, .26,-.5]
weights3 = [-.26, -.27, .17,.87]

weights = [weights1, weights2, weights3]

inputs = [1, 2, 3, 2.5]

bias1 = 2
bias2 = 3
bias3 = 0.5
bias = [bias1, bias2, bias3]

output = np.dot(weights, inputs)  + bias

print(output)