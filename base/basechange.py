
def convertBase(number, base):

    newnumber = []
    while number != 0:

        remainder = number%base
        number //= base
        newnumber.append(str(remainder))

    return ''.join(newnumber[::-1])


base = 10
number = 10011001

print(convertBase(number, base))