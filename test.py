ind = list()


def choice_index_occurences(str, choice):
    for l in range(0, len(str)):
        if str[l] == choice:
            ind.append(l)


choice_index_occurences("Hello everyone!", "e")

print(ind)
