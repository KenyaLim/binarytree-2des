def plus_minus(self):
    ganjil = []
    genap = []
    level_map = {}
    stack = [(self.root, 0)]

    while stack:
        node, level = stack.pop()
        if node is not None:
            if level not in level_map:
                level_map[level] = []
            level_map[level].append(node.data)
            stack.append((node.right, level + 1))
            stack.append((node.left, level + 1))

    for i in level_map:
        if i % 2 == 0:
            for j in level_map[i]:
                genap.append(j)  # Fix: Even level adds to genap
        else:
            for j in level_map[i]:
                ganjil.append(j)  # Fix: Odd level adds to ganjil

    ganjill = 0
    for e in ganjil:
        ganjill += e

    genapp = 0
    for o in genap:
        genapp += o
    return genapp - ganjill  # Fix: Subtract ganjil from genap