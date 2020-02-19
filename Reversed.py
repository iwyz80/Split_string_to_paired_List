def expanded_form(num):
    """ Print non negative integers in expanded form"""
    # convert int to string
    str2num = str(num)

    list_index = []  # List to hold the indexes
    list_out = []  # list to hold the expanded form
    list_f = ''  # string to print the final output

    for i in range(len(str2num)):
        list_index.append(i)
    list_index.reverse()
    for i in range(len(str2num)):
        if str2num[i] != '0':
            list_out.append(str2num[i] + ('0' * list_index[i]))
        list_f = ' + '.join(list_out)
    return (list_f)


print(expanded_form(num=434609012300))
