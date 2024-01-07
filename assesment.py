#Question 1
def is_balanced(expression):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or char != brackets[stack.pop()]:
                return False
    return not stack

#Question 2 

def remove_duplicates(sequence):
    seen = set()
    result = []
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

#Question 3 

def word_frequency(sentence):
    frequency = {}
    words = sentence.lower().split()

    for word in words:
        cleaned_word = ''.join(filter(str.isalpha, word))
        frequency[cleaned_word] = frequency.get(cleaned_word, 0) + 1

    return frequency

