def asciiValue(string):
    counter = 0
    string_list = list(string)
    for i in string_list:
        num_val = ord(i)
        counter += num_val
    print(counter)

asciiValue("Computer")
