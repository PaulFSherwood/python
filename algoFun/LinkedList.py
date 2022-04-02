#introduction to Binary search and complexity analysis with python
import math

print(math.factorial(5))

print(math.sqrt(25))
x = 0
while x < 10:
    print(math.sqrt(10*x))
    x = x + 1

### Systematic strategy for problem solving
# 1> State the problem clearly.  Identify the input & output formats.
# 2> Come up with some example inputs & outputs.  Try to cover all edge cases.
# 3> Come up with a correct solution for the problem.  State it in plain English.
# 4> Implement the solution and test it using example inputs.  Fix bugs, if any.
# 5> Analyze the algoritym's complexity and identify inefficiencies, if any.
# 6> Apply the right technique to overcome the inefficiency. Repetat steps 3 to 6.



# step 2 example input
cards = [13, 11, 10, 7, 4, 2, 1, 0]
query = 7
output = 3

# use discriptive function names and variable names
def locate_card(cards, query):
    pass

print("bacon")

result = locate_card(cards, query)
print(result)


# dictionary
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}
## reference whole dictionary with **
print(locate_card(**test['input']) == test['output'])

# list out scenarios
# 1. The number query occours somewhere in the middle of the list cards
# 2. query is the first element in cards
# 3. query is the last eleent in cards
# 4. the list cards contains just one element, which is query
# 5. The list cards does not contain number query
# 6. The list cards is empty.
# 7. The list cards contains repeating numbers.
# 8. The number query occurs at more than one position in cards.
# 9. (can you think of more variations?)


# edge cases

tests = []

# query occurs in the middle
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query occurs in the first element
tests.append(test)

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query contains just one element, query
tests.append(test)

tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0
})

# cards don't contain the query
tests.append(test)

tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# card is empty
tests.append(test)

tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

print(tests)