data = input("Enter a quote: ")
data = data.replace(' ','')
alpha = {}
count = 0
#split the data
split = sorted(data.lower())

for i in range(len(split)):
    char = split[i]
    for j in range(len(split)):
        if char == split[j]:
            count += 1
            alpha[char] = count
    count = 0

print(alpha)
