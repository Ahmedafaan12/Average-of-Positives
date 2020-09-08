test_values= [1,-1,-2,4,5,7,9,-10]

def average_of_positives_1(test_values):
    total = 0
    position = 0
    for t in test_values:
        if t > 0:
            position = position + 1
            total= total + t
    average = total/ position
    return average
print("The average of positive list 1 is:" , average_of_positives_1(test_values))

def average_of_positives_2(test_values):
    test_list1= []
    total1 = 0
    position1 = 0
    for j in test_values:
        if j > 0:
            test_list1.append(j)
            position1 = position1 + 1
            total1 = total1 + j
    average1 = total1/ position1
    return average1
print("The average of positive list two is:" , average_of_positives_2(test_values))