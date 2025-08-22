inp_nums = int(input())
stones = input().strip()

count = 0
for inp_num in range(inp_nums-1):
    if stones[inp_num] == stones[inp_num+1]:
        count += 1
print(count)