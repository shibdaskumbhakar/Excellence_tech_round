# Question 2


def find_max_value(mydict):
    d = dict()
    all_values = mydict.values()
    max_value = max(all_values)
    # find the key of max value
    for key, value in mydict.items():
        if max_value == value:
            d[key] = max_value

    return d


# creating a dict
mydict = {"1": 20, "2": 50, "3": 70, "5": 76, "12": 98}

answer = find_max_value(mydict)
print(answer)
