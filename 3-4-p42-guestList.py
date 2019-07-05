# 3-4 guest list

guests = ['uncle frank', 'shihan holck', 'helio gracie', 'bruce lee']

for g in range(len(guests)):
    print(f'It would be an honor to have you join us for dinner, {guests[g].title()}')

# 3-5 changing guest list
working = ('bruce lee')
notAvail = guests.remove(working)
print(guests)

print(f'\n{working.title()} is busy working and cannot attend')

newGuest1 = 'choki motobu'
# print(newGuest1.title())
guests.append(newGuest1)
print(guests)

g2 = len(guests)

for l in range(g2):
    print(f'The date has changed. I hope you can still attend, {guests[l].title()}-san')

guests.insert(0, 'Miyamoto Mushashi')

g3 = int(len(guests) / 2 + 1)
guests.insert(g3, 'Angel Cabales')

guests.append('William Chow')

for t in range(len(guests)):
    print(f'Looking forward to seeing you, {guests[t].title()}-sama')

print('\nNow I can only invite 2 people.')

while len(guests) > 2:
    popped = guests.pop()
    popped = popped.title()
    print(f'Gomenesai, {popped}-dono, the table is not big enough.')

for f in range(len(guests)):
    xGuest = guests[f].title()
    print(f'{xGuest}, you are still invited.')

while len(guests) > 0:
    del guests[0]

print(guests)
