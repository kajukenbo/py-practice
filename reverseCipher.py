# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = 'Three can keep a secret, if two of them are dead.'
# message = input('Enter message: ')
 
translated = ''
print('Length is:', len(message))

i = len(message) - 1
# indexes start at zero, so we are minus one from the len

while i >= 0:
    translated = translated + message[i]
    # print('i is:', i, ', message[i] is:', message[i], ', translated is', translated)
    i = i - 1
    
print(translated)
