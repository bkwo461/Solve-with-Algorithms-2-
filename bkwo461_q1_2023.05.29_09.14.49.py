import sys

lines = sys.stdin.readlines()

def solve(tree,op,idx):

    # if the value of list is not symbol then return the number
    if op[idx] not in ['*','+']:
        return int(op[idx])

    if op[idx] == '+':
        ans = 0
    elif op[idx] == '*':
        ans = 1
    for i in range(len(tree[idx])):
        # print(idx,i)
        if op[idx] == '+':
            ans = ans + solve(tree,op,tree[idx][i])
        elif op[idx] == '*':
            ans = ans * solve(tree,op,tree[idx][i])

    # print(ans)
    return ans

for i in range(len(lines)//2):
    tree = list()
    a = lines[2*i].strip().split(',')
    b = lines[2*i+1].strip().split(',')
    a = [int(x) for x in a] # input is string, converting them to integers

    for j in range(len(a)):
        tree.append(list())

    root = 0
    for j in range(len(a)):
        if a[j] != -1:
            tree[a[j]].append(j) # creating adjacency list
        else:
            root = j
    # print(tree)
    print(solve(tree,b,root))