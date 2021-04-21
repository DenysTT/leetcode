def reverse_word(my_str):
    rev_str = ""
    for c in list(my_str):
        rev_str = c + rev_str
    return rev_str

def reverse_word_different(my_str):
    for i,c in enumerate(list(my_str)):
        my_str[i], my_str[len(my_str) - 1]  =  my_str[len(my_str) - 1], my_str[i]
    print(my_str)


def reverse_line(line):
    res_line = ""
    print(' '.join(reverse_word(l) for l in line.split(' ')))
    return res_line

if __name__ == "__main__":
    line = 'cmon go'
    reverse_word_different("khekhe")
    reverse_line(line)