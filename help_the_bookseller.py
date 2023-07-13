def stock_list(list_of_art, list_of_cat):
    check = [i.split() for i in list_of_art if i[0] in list_of_cat]
    if len(check) > 0:
        res = {i: 0 for i in list_of_cat}
        for i in check:
            res[i[0][0]] += int(i[1])
        return ' - '.join([f"({i} : {res[i]})" for i in res])
    return ''


b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]
print(stock_list(b, c))
