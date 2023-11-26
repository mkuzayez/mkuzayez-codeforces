def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False


def perfect_year(x):
    x = str(x)
    y = []
    for i in x:
        y.append(i)
    x = int(x)
    while has_duplicates(y):
        x += 1
        y = str(x)
    print(x)


perfect_year(int(input()) + 1)
