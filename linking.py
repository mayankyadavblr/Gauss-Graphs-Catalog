import bs4
from bs4 import BeautifulSoup
import os




master = './'
all_files = os.listdir(master)
all_files = [x for x in all_files if x.split('.')[-1] == 'html']
all_files = [x for x in all_files if "template" not in x]
all_files = [x for x in all_files if "index" not in x]
total_length = len(all_files)
print(all_files)
for i in range(1, total_length-1):
    site = all_files[i]
    if "template" not in site or "index" not in site:
        with open(site, 'rb') as f:
            html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')

        pointers = soup.find_all('a')
        pointers[0]['href'] = all_files[i-1]
        pointers[1]['href'] = all_files[i+1]

        with open(site, 'w') as f1:
            f1.write(str(soup))
