
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
def main(x):
    return x%2!=0

print(list(filter(main, list1)))