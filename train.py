# TASK - V

def countChars(text):

    result = {}

    for char in text:

        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result


print(countChars("hello"))





# TASK - T


# def mergeSortedArrays(arr1, arr2):

#     merged = arr1 + arr2

#     merged.sort()

#     return merged


# print(
#     mergeSortedArrays(
#         [0, 3, 4],
#         [4, 6]
#     )
# )

# print(mergeSortedArrays)




# TASK - S

# def missingNumber(numbers):
    
#     numbers.sort()
    
#     for i in range(len(numbers)):
#         if numbers[i] != i:
#             return i

# print(missingNumber([3, 0, 1]))






# TASK - R


# def calculate(text):
#     parts = text.split()
    
#     num1 = int(parts[0])

#     operator = parts[1]

#     num2 = int(parts[2])
    
#     if operator == "+":
#         return num1 + num2
 
# print(calculate("1 + 3"))



# TASK - Q

# def hasProperty(obj, prop):

#     return prop in obj


# print(
#     hasProperty(
#         {"name": "BMW"},
#         "name"
#     )
# )


# TASK - P

# def objectToArray(obj):

#     result = []

#     for key, value in obj.items():

#         result.append([key, value])

#     return result


# result = objectToArray({
#     "a": 10,
#     "b": 20
# })

# print(result)


# TASK - O

# def calculateSumOfNumbers(arr):

#     total = 0

#     for item in arr:

#         if type(item) == int and type(item) != bool:
#             total += item

#     return total


# result = calculateSumOfNumbers([10, "10", {"son": 10}, True, 35])

# print(result)


# TASK - N

# def palindromCheck(text):
#     reversed_text = text[::-1]
#     return text == reversed_text

# print(palindromCheck("dad"))

# TASK-M

# def getSquareNumbers(numbers):
#     result = []
#     for number in numbers:
#         obj = {
#            "number": number,
#            "square": number ** 2
#         }
#         result.append(obj)

#     return result

# print(getSquareNumbers([1, 2, 3]))


# TASK-l


# def reverseSentence(text):
#     words = text.split()
#     new_words = []


#     for word in words:
#         reversed_word = word[::-1]
#         new_words.append(reversed_word)
#     return " ".join(new_words)

# result = reverseSentence("we like coding!")

# print(result)
