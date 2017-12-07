import sys
from itertools import filterfalse


class Entry(object):
    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = weight
        self.children = list()
        if children:
            self.children.extend(children)

    def __repr__(self):
        return "{} ({}) -> {}".format(self.name, self.weight, self.children)


def build_tree(filename):
    tree = dict()
    with open(filename, 'r') as f:
        for line in f:
            name, weight, *rest = line.split()
            weight = int(weight.strip('()'))
            children = None
            if rest:
                children = [r.strip(',') for r in rest[1:]]
            tree[name] = Entry(name, weight, children)

    return tree


def find_root(tree):
    all_children = list()
    for e in tree:
        all_children.extend(tree[e].children)
    names = set(tree.keys())
    kids = set(all_children)
    return (names - kids).pop()


def total_weight(tree, root):
    if tree[root].children:
        return tree[root].weight + sum([total_weight(tree, child) for child in tree[root].children])
    else:
        return tree[root].weight


def weigh_subtrees(tree, root):
    if not tree[root].children:
        return
    return {child: total_weight(tree, child) for child in tree[root].children}


def part2(tree, root):
    subtree_weights = weigh_subtrees(tree, root)
    v = list(subtree_weights.values())
    print("{} subtree weights: {}".format(root, subtree_weights))

    unbalanced = next(filterfalse(lambda x: v.count(subtree_weights[x]) != 1, subtree_weights))
    v.remove(subtree_weights[unbalanced])
    target_weight = v[0]

    return find_unbalanced(tree, unbalanced, target_weight)


def find_unbalanced(tree, root, target):
    print("{} weighs {}, target is {}".format(root, tree[root].weight, target))
    subtree_weights = weigh_subtrees(tree, root)
    if not subtree_weights:
        return root, target

    v = list(subtree_weights.values())
    print("{} subtree weights: {}".format(root, subtree_weights))
    unbalanced = list(filterfalse(lambda x: v.count(subtree_weights[x]) != 1, subtree_weights))
    if not unbalanced:
        print("Balanced tree, must be this node: {}({})".format(root, tree[root].weight))
        return root, target-sum(v)
    unbalanced = unbalanced[0]
    v.remove(subtree_weights[unbalanced])
    target_weight = v[0]
    return find_unbalanced(tree, unbalanced, target_weight)


if __name__ == '__main__':
    tree = build_tree(sys.argv[1])
    root_name = find_root(tree)
    print("root is {}".format(root_name))
    print("total weight of tree is {}".format(total_weight(tree, root_name)))

    print(part2(tree, root_name))
