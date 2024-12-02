def plus_minus(self):
    even = []
    odd = []
    level_map = {}
    stack = [(self.root, 0)]  # Stack for manual traversal with levels

    while stack:  # Manual traversal
        node, level = stack.pop()
        if node is not None:
            if level not in level_map:
                level_map[level] = []
            level_map[level].append(node.data)
            stack.append((node.right, level + 1))
            stack.append((node.left, level + 1))

    for l in level_map:
        if l % 2 == 0:
            for v in level_map[l]:
                even.append(v)
        else:
            for v in level_map[l]:
                odd.append(v)

    total_even = 0
    for e in even:
        total_even += e

    total_odd = 0
    for o in odd:
        total_odd += o

    result = total_even - total_odd
    return result