import random

for i in range(100):
    with open("myrandfile"+str(i)+".txt", "wb") as file:
        file.write(bytes([random.randint(0,255) for _ in range(random.randint(50,70))]))
