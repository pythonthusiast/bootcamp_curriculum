import pydot

hari1 = [{
    'Mengenal Python': [{'Mengapa Python?': [{'Trend bahasa pemrograman': []},
                                             {'Keunggulan Python': []},
                                             {'Kelemahan Python': []},
                                             {'Dimana Mencari Job Remote dengan Python': []}],
                         'Python adalah interpreted language': [],
                         'Open source, dibawah Python Software Foundation': [],
                         'Ruang lingkup Python': [{'Desktop': [], 'Web': [], 'Mobile': [], 'Data Science': []}],
                         }],

    'Basic Python Syntaxis': [{"Sequential Code": []}, {"Branching with IF": []},
                              {"Looping with For and While": []}],
    'Modularization': [{
        "Function": [],
        "Class": [{"Encapsulation": []}, {"Inheritance": []}, {"Polymorphism": []}, {}],
        "Package": [{'Bagaimana mendesain packagemu sendiri?': [], 'Memperkenalkan PIP': []}],
        "Study Case": [{'Pydot Usage': []}, {'BeautifulSoup4': []}], }]
}]

hari2 = [{
    'Motivational Talk': [
        {'7 Habits untuk Remote Worker': []},
        {'Menembus, menekuni dan menjaga performa remote work': []},
        {'10 Mantra Sukses Remote Work': []},
        {'Teknik Personal Branding!!!': []},
        {'Upwork or not Upwork? That''s the question!': []},
    ],
    'Scrum Methodology': [{'Introduction to Scrum for Remote Work Project Management': [
        {'Scrum Master | Product Owner': []},
        {'Sprint | Active Sprint | Backlog': []},
        {'Backlog Grooming | Sprint Planning | Retrospective': []},
        {'Daily Standup!!!': []},
    ]},
        {'Hands-on JIRA': [
            {'Onboarding Jira for Bootcamp': []},
            {'Sprint planning: how to decide story point': []},
            {'Sprint report: Burndown chart': []},
        ]}],
    'Database Design and Modeling': [
        {'1NF, 2NF and 3NF': []},
        {"Study Case": [
            {'Courses and Member': []},
            {'Peminjaman Perpustakaan': []},
            {'PR: Kuitansi Penjualan Toko': []},
        ]}]
}]

hari3 = [{
    'Jira Review': [],
    'Git in Team': [],
    'Remote Work: How to Apply to Job in Upwork or Other Remote Work Marketplace': [],
    'Scrapy': [{'Detik.com': []}, {'Airport data scraping': []}],
}]

hari4 = [{
    'Remote Work: Kapan Waktu Terbaik untuk Resign?': [],
    'Membangun Blog Berbasis Flask dan Django DRF': [
        {'Flask Frontend Development': [], 'Django Backend Development': []}],
    'Remote Work: Teknik Personal Branding': [],
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
                graph.add_edge(pydot.Edge(parent, key))
            if val is not None or len(val) > 0:
                iterate(val, parent=key)

    if filename is not None:
        print("Writing to {}".format(filename))
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
