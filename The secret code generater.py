
print('\nWelcome to secret code generator!\n')

message = input("Enter the message : ")
tipe = input("Enter whether you want to Code or Decode : ").lower()
words = message.split(' ')

if tipe == 'code':
    newwords = []
    for word in words:
        if (len(word) >= 3):
            rc = 'dfg'
            rc1 = 'jkl'
            code = rc + word[1:] + word[0] + rc1
            newwords.append(code)
        elif (len(word) < 3):
            newwords.append(word[::-1])
    coded = " ".join(newwords)
    print(f"\nThe message in coded language is : {coded}")

elif tipe == 'decode':
    newwords = []
    for word in words:
        if (len(word) >= 3):
            decode = word[3:-3]
            decode = decode[-1] + decode[:-1]
            newwords.append(decode)
        elif (len(word) < 3):
            newwords.append(word[::-1])
    decoded = " ".join(newwords)
    print(f"\nThe original message is : {decoded}")

