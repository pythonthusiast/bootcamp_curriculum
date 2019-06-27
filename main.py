import sys
import pydot

# graph = pydot.Dot(graph_type='digraph',, size="1920,1080" )
graph = pydot.Dot(graph_type='digraph', rankdir='LR')

root = 'Curriculum'
days = ['Hari 1', 'Hari 2', 'Hari 3', 'Hari 4', 'Hari 5', 'Hari 6']
for day in days:
    graph.add_edge(pydot.Edge(root, day))

day1 = ["Basic Python Syntaxes",
        "Modularization - Function",
        "Modularization - Class",
        "Modularization - Package",
        "Modularization - Study Case - Pydot Usage"]

for d1 in day1:
    graph.add_edge(pydot.Edge(days[0], d1))

day1_basic = [
    "Sequential Code",
    "Branching with IF",
    "Looping with For and While"
]

for day2 in day1_basic:
    graph.add_edge(pydot.Edge(day1[0], day2))

day1_class = [
    "Encapsulation",
    "Inheritance",
    "Polymorphism"
]

for d2c in day1_class:
    graph.add_edge(pydot.Edge(day1[2], d2c))

graph.write_png('curriculum.png')
