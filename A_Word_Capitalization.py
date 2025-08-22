inp = input()

if inp[0].islower():
    lowering = inp[0].upper()
    print(lowering+inp[1:])
else:
    print(inp)
