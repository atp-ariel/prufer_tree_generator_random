from random import randint

def build_prufer(n: int) -> list:
    prufer = []
    for _ in range(n):
        prufer.append(randint(0, n-1))
    return prufer 

def __build_degree(prufer: list) -> list:
    n = len(prufer)
    degree = [1] * (n + 2)
    for i in range(n):
        degree[prufer[i]] += 1
    return degree

def build_tree( prufer: list) -> list:
    degree = __build_degree(prufer)
    n =  len(prufer)
    tree = [[] for _ in range(len(degree))]
    for i in range(n):
        j = __get_deg_1(degree)
        tree[j].append(prufer[i])
        tree[prufer[i]].append(j)
        degree[prufer[i]] -= 1
    j = __get_deg_1(degree)
    j1 = __get_deg_1(degree)
    tree[j].append(j1)
    tree[j1].append(j)
    return tree

def __get_deg_1(degree: list) -> int:
    j = 0
    while not degree[j] == 1:
        j += 1
    degree[j] -= 1
    return j

if __name__ == "__main__":
    print("Write the number of nodes on the tree")
    print("n = ", end="")

    line = input().split()
    
    prufer = build_prufer(int(line[0]) - 2)

    tree = build_tree(prufer)

    print("The tree is:")
    print(tree)
