import bs4
from bs4 import BeautifulSoup
import os


with open('template.html', 'rb') as f:
    html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
def fill_template(dir):
    # directory = os.fsencode(dir)
    
    links = []
    for file in os.listdir(dir):    
        filename = os.fsencode(file)
        filename = filename.decode("utf-8")
        filename = dir+'/'+filename
        links += [filename]
        # print(filename)

    for paragraph in soup.find_all('p'):
        for link in paragraph.find_all('img'):
            alt_text = link["alt"].split()[0]
            actual_link = [x for x in links if alt_text in x ]
            print(link, actual_link, alt_text)
            link["src"] = actual_link
            # print(link)


    dir = dir.split('/')
    name = dir[-2] + "_" + dir[-1] + ".html"
    with open(name, 'w') as f2:
        f2.write(str(soup))

master = "./order"
for dir in os.listdir(master):
    subfolder = master + '/' + dir
    for graph in os.listdir(subfolder):
        print(graph)
        graph = subfolder + '/' + graph
        fill_template(graph)