def remove_duplicates(value):
    str=""
    for i in value:
        if i not in str:
            str=str+i
    return str

print(remove_duplicates("11223445566666ababzzz@@@123##"))
