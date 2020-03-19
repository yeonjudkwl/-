inputs = list(map(int, input().split()))

for i in range(7):
    if inputs[i] + 1 == inputs[i+1]:
        rst = 'ascending'
    elif inputs[i] - 1 == inputs[i+1]:
        rst = 'descending'
    else:
        rst = 'mixed'
        break
print(rst)