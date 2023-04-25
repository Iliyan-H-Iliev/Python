from collections import deque

parentheses = deque(list(input()))
opened_parentheses = []
closed_parentheses = []

while parentheses:
    par = parentheses.popleft()

    if par == "{" or par == "(" or par == "[":
        opened_parentheses.append(par)
    else:
        if opened_parentheses:
            opened_par = opened_parentheses[-1]
            if opened_par == "{" and par == "}" \
                    or opened_par == "(" and par == ")" \
                    or opened_par == "[" and par == "]":
                opened_parentheses.pop()
        else:
            closed_parentheses.append(par)

if opened_parentheses or closed_parentheses:
    print("NO")
else:
    print("YES")
