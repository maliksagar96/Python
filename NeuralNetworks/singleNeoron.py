wts = [1,2,3]
inputs = [1,2,3]

bias = 2
output = []
for i,j in zip(inputs,wts):
    output.append(i*j)

op = sum(output) + bias
print(output)