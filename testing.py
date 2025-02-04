import bs4
from bs4 import BeautifulSoup
import os


def fill_template(dir):
    # directory = os.fsencode(dir)
    with open('template.html', 'rb') as f:
        html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')

    rel_dir = '.'+dir[12:]
    '''    
    links = []
    for file in os.listdir(dir):    
        filename = os.fsencode(file)
        filename = filename.decode("utf-8")
        filename = dir+'/'+filename
        links += [filename]
        # print(filename)
        # print(links)'''
    
    main_info = soup.find(class_ = 'original-graph')
    main_graph_img = main_info.find("img")
    main_graph_img["src"] = rel_dir + '/' + "original.png"

    main_graph_words = main_info.find("p", class_="no-of-words")
    with open(dir + '/' + 'number_of_words.txt', 'r') as f:
        no_of_words = f.readline()
    main_graph_words.string += no_of_words

    modular_decomp = soup.find(class_="modular-decomp")
    modular_decomp_img = modular_decomp.find("img")
    modular_decomp_img["src"] = rel_dir + '/' + 'modular_decomposition.png'

    split_decomp = soup.find(class_="split-decomp")
    split_decomp_img = split_decomp.find("img")
    split_decomp_img["src"] = rel_dir + '/' + 'split_decomp.png'
    with open(dir + '/' + 'labels_of_bags.txt', 'r') as f:
        labels = f.readline()
    split_decomp_labels = split_decomp.find("p", class_="labels-split-decomp")
    split_decomp_labels.string += labels

    interlace_one = soup.find(class_="Interlace-one-var")
    interlace_one_img = interlace_one.find("img")
    interlace_one_img["src"] = rel_dir + '/' + 'interlace_roots.png'

    with open(dir + '/' + 'interlace_polynomial.txt', 'rt') as f:
        poly = f.readline()
        roots = f.readline()
    interlace_one_poly = interlace_one.find(class_="one-var-poly")
    interlace_one_poly.string += poly
    interlace_one_roots = interlace_one.find(class_="one-var-roots")
    interlace_one_roots.string += roots

    interlace_two = soup.find(class_="Interlace-two-var")
    interlace_two_img = interlace_two.find("img")
    interlace_two_img["src"] = rel_dir + '/' + 'two_interlace_polynomial.png'

    with open(dir + '/' + 'interlace_poly_two_var.txt', 'rt') as f:
        poly = f.readline()

    interlace_two_poly = interlace_two.find(class_="two-var-poly")
    interlace_two_poly.string += poly

    characteristic_poly = soup.find(class_="characteristic")
    characteristic_img = characteristic_poly.find("img")
    characteristic_img["src"] = rel_dir + '/' + 'characteristic_roots.png'

    with open(dir + '/' + 'characteristic_polynomial.txt', 'rt') as f:
        poly = f.readline()
    with open(dir + '/' + 'characteristic_polynomial_factored.txt', 'rt') as f:
        factored = f.readline()
    characteristic_poly_string = characteristic_poly.find(class_="characteristic-poly")
    characteristic_poly_string.string += poly
    interlace_one_roots = characteristic_poly.find(class_="characteristic-poly-factors")
    interlace_one_roots.string += factored

    chromatic = soup.find(class_="chromatic")
    chromatic_img = chromatic.find("img")
    chromatic_img["src"] = rel_dir + '/' + 'chromatic_roots.png'

    with open(dir + '/' + 'chromatic_polynomial.txt', 'rt') as f:
        poly = f.readline()

    chromatic_poly = chromatic.find(class_="chromatic-poly")
    chromatic_poly.string += poly

    
    dir = dir.split('/')
    name = dir[-2] + "_" + dir[-1] + ".html"
    with open("./html_files/"+name, 'w') as f2:
        f2.write(str(soup))

master = "./html_files/order"
for dir in os.listdir(master):
    subfolder = master + '/' + dir
    for graph in os.listdir(subfolder):
        graph = subfolder + '/' + graph
        print(graph)
        fill_template(graph)