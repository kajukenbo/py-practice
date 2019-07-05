# http://openbookproject.net/courses/python4fun/spellcheck.html
# Simple spell check to filter output

# watch for case sensitivity
# default matches whole string, need to break it up

# We can get this into a list in memory with the following
words = open("spell.words").readlines()

# remove newlines
words = [word.strip() for word in words]

# use python dict for speed
hash = {}
for w in words:
    hash[w] = True

SEARCH='this or that other'

#for i in range(100000):
#    found = 'zygotic' in hash

#if 'dragon' in hash:
#if 'ccwdrdfaghghgofn' in hash:
if SEARCH in hash:
    print ('FOUND A MATCH!')

#print(words)

print('finished')

# https://www.tutorialspoint.com/python/python_spelling_check.htm
# actually a pip module for this...
