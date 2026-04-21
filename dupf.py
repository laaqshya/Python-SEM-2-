def find_duplicates(lst):
    dup = []
    for i in lst:
        if lst.count(i) > 1 and i not in dup:
            dup.append(i)
    return dup

lst = [1, 2, 2, 3, 4, 4, 5]
print("Duplicates:", find_duplicates(lst))
