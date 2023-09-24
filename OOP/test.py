def myXOR(x, y):
    res = 0  # Initialize result

    # Assuming 32-bit Integer
    for i in range(31, -1, -1):

        # Find current bits in x and y
        b1 = x & (1 << i)
        b2 = y & (1 << i)
        b1 = min(b1, 1)
        b2 = min(b2, 1)

        # If both are 1 then 0
        # else xor is same as OR

        xoredBit = 0
        if (b1 & b2):
            xoredBit = 0
        else:
            xoredBit = (b1 | b2)

        # Update result
        res <<= 1;
        res |= xoredBit
    return res


# Driver Code
x = 95
y = 74
print("XOR is", myXOR(x, y))