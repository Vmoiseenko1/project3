# Individual Project №3
# Developer: Moiseenko Victoria
# The idea: find the number of different words that can be composed by rearranging the letters of the given word with
# symbols from a to e.

word = str(input(''))  # Enter your word with only a-e letters
d = dict.fromkeys(word, 0)

for a in word:  # Counting the num of a letters
    count = {}
    if count[a] == 1:
        f1 = 1
    print(count[a], f1)
else:
    count[a] += 1
    f1 = 1
    for i in range(2, count[a] + 1):
        f1 *= i
    print(count[a], f1)
for b in word:  # Counting the num of b letters
    count = {}
    if count[b] == 1:
        f2 = 1
        print(count[b], f2)
    else:
        count[b] += 1
        f2 = 1
        for i in range(2, count[b] + 1):
            f2 *= i
        print(count[b], f2)
for c in word:  # Counting the num of c letters
    count = {}
    if count[c] == 1:
        f3 = 1
        print(count[c], f3)
    else:
        count[c] += 1
        f3 = 1

        for i in range(2, count[c] + 1):
            f3 *= i
        print(count[c], f3)
for d in word:  # Counting the num of d letters
    count = {}
    if count[d] == 1:
        f4 = 1
        print(count[d], f4)
    else:
        count[d] += 1

        f4 = 1

        for i in range(2, count[d] + 1):
            f4 *= i
        print(count[d], f4)
for e in word:  # Counting the num of e letters
    count = {}
    if count[e] == 1:
        f5 = 1
        print(count[e])
    else:
        count[e] += 1

        f5 = 1

        for i in range(2, count[e] + 1):
            f5 *= i
        print(count[e], f5)

length = len(word)  # Counting the factorial of total num of outcomes
factorial = 1

for i in range(2, length + 1):
    factorial *= i
print(factorial)

p = factorial / f1 * f2 * f3 * f4 * f5  # The num of different words
print(p)
