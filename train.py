# TASK - O

def calculateSumOfNumbers(arr):

    total = 0

    for item in arr:

        if type(item) == int and type(item) != bool:
            total += item

    return total


result = calculateSumOfNumbers([10, "10", {"son": 10}, True, 35])

print(result)




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
