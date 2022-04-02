import os, random

count = 0
score = 0

file1 = open('english.txt', 'r')
file2 = open('hebrew.txt', 'r')
file3 = open('heb-phonetic.txt', 'r')

f1content = file1.readlines()
f2content = file2.readlines()
f3content = file3.readlines()

# StackOverflow # Hebrew unicode in Python 
def reverse(s):
    heb = []
    g = ""
    s = s.decode('UTF-8')
    for i in range(len(s)):
        c = s[i]
        heb.append(c)
    for i in range(len(heb)):
        g += heb.pop()
    return g

while count < 10:
    os.system('clear')

    wordnum = random.randint(0, len(f1content)-1)

    print 'Word:', f1content[wordnum], ''

    options = [random.randint(0, len(f2content)-1),
            random.randint(0, len(f2content)-1),
            random.randint(0, len(f2content)-1)]

    options[random.randint(0, 2)] = wordnum

    #print num - reverse hebrew leters then remove the \n at the beginning
    print '1 -', reverse(f2content[options[0]]).lstrip()
    print '2 -', reverse(f2content[options[1]]).lstrip()
    print '3 -', reverse(f2content[options[2]]).lstrip()

    answers = input('\nyour choice: ')

    if options[answers-1] == wordnum:
        # print the phonetic spelling
        print ' ', f3content[wordnum]
        raw_input('\nCorrect! Hit Enter...')
        score = score + 1
    else:
        raw_input('\nWrong! Hit Enter...')
    count = count + 1
print '\nYour score is:', score
