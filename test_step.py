number = 4982579
num2str = str(number)
num2list = list(num2str)
index_list = []
for i in num2list:
    for k in range(len(num2str)):
        index_list.append(k)

    # print(i)
# index_list.reverse()
print(index_list)
print(num2list)
