weights = [-0.5, 0.5, 0.25]
data_set = [[2, 1], [4, 5], [5, 3], [3, 2]]
training_rate = 0.1
actual_values = [1, 0, 0, 1]

iterations = 1
icount = 0
pos_neg = 0
def validation_func(result):
    if result >= 0:
        return 1
    else:
        return 0

def adjust_weights(failed_set):
    weights[0] += fake_round(training_rate * pos_neg * 1)
    weights[0] = fake_round(weights[0])
    for i in range(1, len(weights)):
        weights[i] += training_rate * pos_neg * failed_set[i-1]
        weights[i] = fake_round(weights[i])

def fake_round(num):
    num = round(num * 100)/100
    return num

unsolved = True
calc_result = 0

while unsolved:
    print('iteration:', iterations)
    for i in range(0, len(data_set)):
        calc_result = weights[0]
        for j in range(1, len(weights)):
            calc_result += data_set[i][j-1]*weights[j]
        y = validation_func(calc_result)
        d = actual_values[i]
        if y == d:
            icount +=1
        else:
            icount = 0
            pos_neg = d - y
            adjust_weights(data_set[i])
        if icount >= 4:
            unsolved = False
        print(weights)
    iterations += 1

print('done')
print('final weights:', weights)
print('iterations:', iterations-1)