def even_odd_filter(**kwargs):
    res = {}
    for k, v in kwargs.items():
        if k in kwargs:
            if k == "even":
                res[k] = [x for x in v if x % 2 == 0]
            elif k == "odd":
                res[k] = [x for x in v if x % 2 != 0]

    return sorted(res.items(), key=lambda x: x[0])


print(even_odd_filter(
        odd=[1, 2, 3, 4, 10, 5],
        even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
