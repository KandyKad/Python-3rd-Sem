counts = dict()
words = input().split(" ")
words.sort()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
