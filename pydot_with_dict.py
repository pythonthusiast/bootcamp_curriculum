import pydot


hari1 = [{
    'Basic Python Syntaxes': [{"Sequential Code": []}, {"Branching with IF": []},
                              {"Looping with For and While": []}],
    "Modularization - Function": [{}, {}, {}, {}],
    "Modularization - Class": [{"Encapsulation": []}, {"Inheritance": []}, {"Polymorphism": []}, {}],
    "Modularization - Package": [{}, {}, {}, {}],
    "Modularization - Study Case - Pydot Usage": [{}, {}, {}, {}],
}]
hari2 = [{
    'Motivational Talk': [],
    'Scrum Introduction and Jira Onboarding': [],
    'Database Design and Modeling': [
        {'1NF, 2NF and 3NF': []},
        {"Study Case: Courses and Member, Peminjaman Perpustakaan dan PR: Kuitansi Penjualan": []},
    ],

}]
hari3 = [{
    'Jira Review': [],
    'Git in Team': [],
    'Remote Work: How torow Apply to Job in Upwork': [],
    'Scrapy': [{'Airport data scraping': []}, {'Detik.com': []}],

}]
hari4 = [{
    'Remote Work: Kapan Waktu Terbaik untuk Resign?': [],
    'Membangun Blog Berbasis Flask dan Django DRF: Flask Frontend Development': [],
    'Membangun Blog Berbasis Flask dan Django DRF: Django Backend Development': [],
    'Personal Branding: artikel di medium': [],
    'Apply to remote job di remoteok.io': [],
    'BONUS MATERIAL': [{'Scrapy for Marketplace': []}, {'Dockerizing Flask and Django': []},
                       {'Deployment do Digital Ocean': []}],
}]

curriculum = [{
    'Bootcamp Curriculum': [{
        'Hari 1': hari1,
        'Hari 2': hari2,
        'Hari 3': hari3,
        'Hari 4': hari4,
    }],
}]


def iterate(course_list, parent=None, filename=None):
    for c in course_list:
        for key, val in c.items():
            if parent is not None:
                print(parent, key)
                graph.add_edge(pydot.Edge(parent, key))
            if val is not None or len(val) > 0:
                iterate(val, parent=key)

    if filename is not None:
        graph.write_png(filename)

graph = pydot.Dot(graph_type='digraph', rankdir='LR')
iterate(curriculum, parent=None, filename='all_curriculum.png')

graph = pydot.Dot(graph_type='digraph', rankdir='LR')
iterate(hari1, parent='Hari 1', filename='bootcamp_hari1.png')

graph = pydot.Dot(graph_type='digraph', rankdir='LR')
iterate(hari2, parent='Hari 2', filename='bootcamp_hari2.png')

graph = pydot.Dot(graph_type='digraph', rankdir='LR')
iterate(hari3, parent='Hari 3', filename='bootcamp_hari3.png')

graph = pydot.Dot(graph_type='digraph', rankdir='LR')
iterate(hari4, parent='Hari 4', filename='bootcamp_hari4.png')


