inp = input()
arr = inp.split()
a_math = int(arr[0])
a_english = int(arr[1])

inp = input()
arr = inp.split()
b_math = int(arr[0])
b_english = int(arr[1])

if a_math > a_english and a_english > b_english :
    print(1)
else :
    print(0)