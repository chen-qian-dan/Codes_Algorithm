class Dot:
    """
      black: haven't reached yet;
      red: discovered;
      blue: finished;
    """
    def __init__(self, name):
        self.name = name
        self.color = 'black'
        self.neighbors = list()
        self.discoveryTime = 0
        self.finishTime = 0

    def add_neighbor(self, strDotName):
        if strDotName not in self.neighbors:
            self.neighbors.append(strDotName)
            self.neighbors.sort()


class Graph:
    # because dot name should be unique, so better use dictionary
    dots = dict()
    time = 0

    def add_dot(self, dot: Dot) -> bool:
        if dot.name not in self.dots:
            self.dots[dot.name] = dot
            return True
        else:
            return False

    def add_edge(self, strDotU, strDotV) -> bool:
        if strDotU in self.dots and strDotV in self.dots:
            for key, value in self.dots.items():
                if key == strDotU:
                    value.add_neighbor(strDotV)
                elif key == strDotV:
                    value.add_neighbor(strDotU)
            return True
        else:
            return False

    def print(self):
        for k in sorted(self.dots.keys()):
            print(k + str(self.dots[k].neighbors) + " " + str(self.dots[k].discoveryTime))


    def _dfs(self, dot: Dot):
        global time
        dot.discoveryTime = time
        dot.color = 'red'
        time += 1
        print( dot.neighbors)
        for n in dot.neighbors:
            if self.dots[n].color == 'black':
                self._dfs(self.dots[n])
                dot.color = 'blue'
                dot.finishTime = time
                time += 1


    def dfs(self, dot):
        global time
        time = 1
        self._dfs(dot)


g = Graph()

for i in range(ord('A'), ord('K')):
    g.add_dot(Dot(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[0], edge[1])

g.dfs(g.dots['A'])
g.print()








