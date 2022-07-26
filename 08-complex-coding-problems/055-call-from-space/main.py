signal="RZ VMZ WMDIBDIB VGG AJMXZN OJ EJDI RDOC XGZJKVOMV OJ YZAZVO OCZ ZIZHT LPZZI VO OCZ IDGZ YZGOV"
signal=signal.lower()
shift = 1
for shift in range(0,26):
    print(shift)
    for letter in signal:
        if (letter != " "):
            print(chr(97+(ord(letter)+shift-97)%26),end="")
        else:
            print(end=" ")
    print()
print()