# Question 1


# creating sum_list function

def SumOfList(list):
    total = 0
    for i in range(0, len(list)):
        total += list[i]
    return total


# creating a list
My_list1 = [6, 51, 67, 3, 22]

total = SumOfList(My_list1)

print("Sum of all elements in given list: ", total)
