# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# n=int(input())
# someStr = ""
# for i in range(n):
#     someStr = someStr + str(i+1)
#
# print(someStr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# a = "123"
# b = "4321"
# c = a + b
# print(len(c))

# def add(a, b):
#     return a+b
#
# print(add(*range(2)))

ch = {
    'I': 1
    , 'IV': 4
    , 'V': 5
    , 'IX': 9
    , 'X': 10
    , 'XL': 40
    , 'L': 50
    , 'XC': 90
    , 'C': 100
    , 'CD': 400
    , 'D': 500
    , 'CM': 900
    , 'M': 1000
}

level = {
    'I': 1
    , 'IV': 1
    , 'V': 1
    , 'IX': 1
    , 'X': 2
    , 'XL': 2
    , 'L': 2
    , 'XC': 2
    , 'C': 3
    , 'CD': 3
    , 'D': 3
    , 'CM': 3
    , 'M': 4
}

someStr = "MCMXLVII"
idx=0
result = 0
while idx < len(someStr):

    if someStr[idx:idx+2] in ch.keys():
        word_num = someStr[idx:idx+2]
        idx = idx + 2
    elif someStr[idx:idx+1] in ch.keys():
        word_num = someStr[idx:idx+1]
        idx = idx + 1
    result = result + ch[word_num]


print(result)
