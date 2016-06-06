# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0

from collections import Counter

def count_a_in_file(file_name):
    f = open(file_name)
    text = f.read()
    f.close()
    count = 0
    for car in text:
        if car == 'a':
            count += 1
    return count


print(count_a_in_file('2.txt'))
