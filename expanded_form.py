def expanded_form(num):

    str2num = str(num)
    new_num = str2num[::-1]
    list_index = []
    list_out = []
    list_f = ''

    for i in new_num:
        list_index.append((new_num.index(i)))
    list_index.reverse()
    for i in range(len(str2num)):
        if str2num[i] != '0':
            list_out.append(str2num[i] + ('0' * list_index[i]))
        list_f = ' + '.join(list_out)
    print(list_f)


expanded_form(‭1234)
