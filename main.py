import sys

def digitsToBase2IntMethod(x):
    base2 = [False] * sys.getsizeof(x)
    i = 0

    while x > 0:
        base2[i] = bool(x % 2)
        x //= 2
        i += 1
    
    start = 0
    end = i - 1
    while start < end:
        temp = base2[start]
        base2[start] = base2[end]
        base2[end] = temp
        start += 1
        end -= 1

    res = 0
    mult = 1
    j = i - 1
    while j >= 0:
        res += int(base2[j]) * mult
        mult *= 10
        j -= 1

    return res

def digitsToBase2StrMethod(x):
    base2 = [False] * sys.getsizeof(x)
    i = 0

    while x > 0:
        base2[i] = bool(x % 2)
        x //= 2
        i += 1

    res = ""
    j = i - 1
    while j >= 0:
        res += str(int(base2[j])) 
        j -= 1

    return res

x = int(input("Enter num: "))

print("Str Method: " + digitsToBase2StrMethod(x))
print("Int Method: " + str(digitsToBase2IntMethod(x)))

print("Size of input value(" + str(x) + "): " + str(sys.getsizeof(x)))

print("Size of Str with base2 num: " + str(sys.getsizeof(digitsToBase2StrMethod(x))))
print("Size of Int with base2 num: " + str(sys.getsizeof(digitsToBase2IntMethod(x))))


base2 = [False] * sys.getsizeof(x)
base2Int = [0] * sys.getsizeof(x)

print("Size of bool array: " + str(sys.getsizeof(base2)))
print("Size of int array: " + str(sys.getsizeof(base2Int)))
print("Int Array: " + str(base2Int))