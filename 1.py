# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list

n = [1, 2, 3, 4, 5]

def double_list(input_list):
    newList = []
    for item in input_list:
        item *= 2
        newList.append(item)
    return newList


print(double_list(n))
