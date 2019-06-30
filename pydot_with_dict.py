import sys
import pydot

# graph = pydot.Dot(graph_type='digraph',, size="1920,1080" )
graph = pydot.Dot(graph_type='digraph', rankdir='LR')

curriculum = [{
    'Bootcamp Curriculum': [{
        'Hari 1': [{
            'Basic Python Syntaxes': [{"Sequential Code": []}, {"Branching with IF": []},
                                      {"Looping with For and While": []}],
            "Modularization - Function": [{}, {}, {}, {}],
            "Modularization - Class": [{"Encapsulation": []}, {"Inheritance": []}, {"Polymorphism": []}, {}],
            "Modularization - Package": [{}, {}, {}, {}],
            "Modularization - Study Case - Pydot Usage": [{}, {}, {}, {}],
        }],
        'Hari 2': [{
            'Motivational Talk': [],
            'Scrum Introduction and Jira Onboarding': [],
            'Database Design and Modeling': [
                {'1NF, 2NF and 3NF': []},
                {"Study Case: Courses and Member, Peminjaman Perpustakaan dan PR: Kuitansi Penjualan": []},
                {''}],

        }],
        'Hari 3': [{
            'Jira Review': [],
            'Git in Team': [],
            'Remote Work: How torow Apply to Job in Upwork': [],
            'Scrapy': [{'Airport data scraping': []}, {'Detik.com': []}],

        }],
        'Hari 4': [{
            'Remote Work: Kapan Waktu Terbaik untuk Resign?': [],
            'Membangun Blog Berbasis Flask dan Django DRF: Flask Frontend Development': [],
            'Membangun Blog Berbasis Flask dan Django DRF: Django Backend Development': [],
            'Personal Branding: artikel di medium': [],
            'Apply to remote job di remoteok.io': [],
            'BONUS MATERIAL': [{'Scrapy for Marketplace': []}, {'Dockerizing Flask and Django': []}, {'Deployment do Digital Ocean':[]}],
        }],
        'Hari 5': [{
        }],
        'Hari 6': [{
        }],
    }],
}]


def iterate(node_a=None, node_b=None, children=None):
    for data in children:
        for node_c, value in data.items():
            if node_a is not None:
                graph.add_edge(pydot.Edge(node_a, node_b))
            iterate(node_a=node_b, node_b=node_c, children=value)


iterate(children=curriculum)
graph.write_png('all_curriculum.png')
