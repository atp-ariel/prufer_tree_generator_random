import random
def build_prufer(n: int):
    prufer = []
    for _ in range(n):
        prufer.append(random.randint(0, n-1))
    return prufer 
def build_degree(prufer: list):
    n = len(prufer)
    degree = [1] * (n + 2)
    for i in range(n):
        degree[prufer[i]] += 1
    return degree

def build_tree(degree: list, prufer: list):
    n =  len(prufer)
    tree = [[] for _ in range(len(degree))]
    for i in range(n):
        j = get_deg_1(degree)
        tree[j].append(prufer[i])
        tree[prufer[i]].append(j)
        degree[prufer[i]] -= 1
    j = get_deg_1(degree)
    j1 = get_deg_1(degree)
    tree[j].append(j1)
    tree[j1].append(j)
    return tree

def get_deg_1(degree: list):
    j = 0
    while not degree[j] == 1:
        j += 1
    degree[j] -= 1
    return j
line = input().split()
prufer = build_prufer(int(line[0]))
print(prufer)
print(build_tree(build_degree(prufer), prufer))
