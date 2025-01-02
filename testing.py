import bs4
from bs4 import BeautifulSoup
import os


def fill_template(dir):
    # directory = os.fsencode(dir)
    with open('template.html', 'rb') as f:
        html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
    
    links = []
    for file in os.listdir(dir):    
        filename = os.fsencode(file)
        filename = filename.decode("utf-8")
        filename = dir+'/'+filename
        links += [filename]
        # print(filename)
        # print(links)

    for paragraph in soup.find_all('p'):
        for link in paragraph.find_all('img'):
            alt_text = link["alt"].split()[0]
            actual_link = [x for x in links if alt_text in x ]
            # print(link, actual_link, alt_text)
            link["src"] = actual_link
            print(actual_link)
            # print(link)
        text = paragraph.get_text()
        if "Number of words" in text:
            # print(text)
            actual_file = [x for x in links if "number_of_words" in x][0]
            with open(actual_file, 'r') as f:
                number_of_words = f.readline()
            paragraph.string = text + number_of_words
            # print(paragraph.string)
        elif "Labels of the bags" in text:
            # print(text)
            actual_file = [x for x in links if "labels_of_bag" in x][0]
            with open(actual_file, 'r') as f:
                labels = f.readline()
            paragraph.string = text + labels
            # print(paragraph.string)

            


    dir = dir.split('/')
    name = dir[-2] + "_" + dir[-1] + ".html"
    with open(name, 'w') as f2:
        f2.write(str(soup))

master = "./order"
for dir in os.listdir(master):
    subfolder = master + '/' + dir
    for graph in os.listdir(subfolder):
        graph = subfolder + '/' + graph
        print(graph)
        fill_template(graph)