file_1="""apple
banana
pineapple
orange
raspberry"""
file_2 = """potato
cucumber
apple"""
file_3 = """orange
watermelon"""

def count_duplicates():

    files = {'file_1' : file_1, 'file_2' : file_2, 'file_3': file_3}
    result = {}
    for k, v in files.items():
        for line in v.split('\n'):
            if line not in result:
                result[line] = [k]
            else:
                result[line].append(k)
    print()

if __name__ == "__main__":
    count_duplicates()