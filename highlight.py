import re
import sys

print('Enter Highlights and CTRL+Z + ENTER when done')
s = sys.stdin.readlines()

# Format Highlights/remove unwanted info
h = []

for i in range(len(s)):
    if 'Yellow highlight' in s[i]:
        continue
    elif s[i] == '' or s[i] == '                \n' or s[i] == '\n':
        continue
    elif 'Note:' in s[i]:
        h.pop()
        h.append(s[i-2] + ', ' + s[i])
    else:
        h.append(s[i])

# strip remaining \n
for i in range(len(h)):
    h[i] = re.sub(r'[\n]','',h[i])

# Format Noted highlights
def notes():
    n = [] # noted HLs
    for i in h:
        if 'Note:' in i:
            n.append(i)
    for i in n:
        print(i + '\n')

# Format Word HLs
def words():
    w = [] # word HLs
    for i in h:
        if len(i.split(' ')) == 1:
            w.append(re.sub(r'[^\w\s]','',i)) # remove unnecessary punctuation
    for i in w:
        print(i + '\n')

# Format Quote HLs
def quotes():
    q = [] # quoted HLs
    for i in h:
        if len(i.split(' ')) >= 2 and 'Note:' not in i.split(' ')[1]:
            q.append(i)
    for i in q:
        print(i + '\n')

# Print Notes
print('Notes:')
notes()

# Print Words
print('Words:')
words()

# Print Quotes
print('Quotes:')
quotes()
