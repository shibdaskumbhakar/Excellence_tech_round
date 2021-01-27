# Question 3

# function for count maximum consecutive
def max_consecutive(list):
    coun = 0
    max_count = 0

    for i in range(len(My_list)):
        if My_list[i] == 1:
            count = count + 1
        else:
            count = 0
        if count > max_count:
            max_count = count

    return max_count


# creating a list
My_list = [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]

answer = max_consecutive(My_list)
print(answer)
