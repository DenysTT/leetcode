def reverse_int(i):
    if not i:
        return False
    reversed_int = ""
    negative = False
    for i, c in enumerate(str(i)):
        if i == 0 and c == '-':
            negative = True 
            continue       
        reversed_int = c + reversed_int
    print(reversed_int if not negative else '-' + reversed_int)


if __name__ == "__main__":
    reverse_int(-24)