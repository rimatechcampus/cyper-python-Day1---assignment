# ! reverse the string

#! method 1
my_str = 'abcd1234'
new_str = my_str[::-1]
print(new_str)


#! method 2
my_str = 'abcd1234'
converted_str = reversed(my_str)
my_new = ''.join(converted_str)
print(my_new)
