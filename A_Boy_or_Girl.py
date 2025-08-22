name = input()

distinct_name = set(name)

if len(distinct_name) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")