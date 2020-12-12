def part1(graph):
    shiny_gold_bag = graph.get_node("shiny gold bag")

    num_bags = 0
    open_list = [shiny_gold_bag]
    closed_list = []

    while len(open_list) > 0:
        current = open_list.pop(0)
        closed_list.append(current.identifier)

        for x in current.back_links:
            if x in closed_list or current.back_links[x].from_node in open_list:
                continue

            num_bags += 1
            open_list.append(current.back_links[x].from_node)
    
    return num_bags

def part2(graph):
    shiny_gold_bag = graph.get_node("shiny gold bag")

    return shiny_gold_bag.weight()

class Link:
    def __init__(self, weight, from_node, to_node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.links = {}
        self.back_links = {}

    def link(self, node, weight):
        self.links[node.identifier] = Link(weight, self, node)
        node.back_links[self.identifier] = self.links[node.identifier]

    def weight(self):
        weight = 0

        for x in self.links:
            weight += self.links[x].weight * self.links[x].to_node.weight() + self.links[x].weight
        
        return weight

class Graph:
    def __init__(self):
        self.nodes = {}

    def has_node(self, identifier):
        return identifier in self.nodes

    def get_node(self, identifier, create = False):
        if not create and not self.has_node(identifier):
            return None
        
        if not self.has_node(identifier):
            node = Node(identifier)
            self.nodes[identifier] = node
        else:
            node = self.nodes[identifier]

        return node

    def link(self, identifier, link_identifier, weight):
        if identifier == link_identifier or weight == 0:
            return
        
        from_node = self.get_node(identifier, True)
        to_node = self.get_node(link_identifier, True)

        from_node.link(to_node, weight)

def create_graph(input):
    graph = Graph()

    for line in input:
        identifier, children = line.split("contain")

        identifier = identifier.strip().rstrip("s.")
        children = [x.strip().split(" ", 1) for x in children.split(",")]

        if children[0][0] == "no":
            continue

        children = [[int(x[0]), x[1].strip().rstrip("s.")] for x in children]
        
        for child in children:
            weight, link = child

            graph.link(identifier, link, weight)

    return graph

input = [x.rstrip("\n") for x in open("input.txt", "r").readlines()]
graph = create_graph(input)

print(part1(graph))
print(part2(graph))