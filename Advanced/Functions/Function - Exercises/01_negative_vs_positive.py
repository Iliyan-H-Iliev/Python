def negative_vs_positive(args):
    positive = []
    negative = []
    for el in args:
        if el > 0:
            positive.append(el)
        else:
            negative.append(el)

    result = f"{sum(negative)}\n{sum(positive)}\n"
    result += "The negatives are stronger than the positives"\
        if abs(sum(negative)) > sum(positive) else\
        "The positives are stronger than the negatives"
    return result


numb = [int(x) for x in input().split()]

print(negative_vs_positive(numb))
