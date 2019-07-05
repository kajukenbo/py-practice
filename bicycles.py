bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())

num_bikes = len(bicycles)
print(num_bikes)

for b in range(num_bikes):
    print(bicycles[b].title())

print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)