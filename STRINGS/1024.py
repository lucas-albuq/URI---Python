n = int(input())
for x in range(n):
    string = input()
    str2 = ''
    for x in string:
        if x.isalpha() == True:
            str2 += chr(ord(x) + 3)
        else:
            str2 += x
    str2 = ''.join(reversed(str2))
    metade = len(str2)//2
    str3 = ''
    for x in str2:
      if len(str3) >= metade:
        str3 += chr(ord(x) - 1)
      else:
        str3 += x
    print(str3)
