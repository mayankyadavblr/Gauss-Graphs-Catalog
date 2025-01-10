import bs4
from bs4 import BeautifulSoup
import os

# Loading all html files's relative paths in one list
master = './html_files'
all_files = os.listdir(master)
all_files = [x for x in all_files if x.split('.')[-1] == 'html']
# all_files = ['./html_files/' + x for x in all_files]
all_files.sort()
total_length = len(all_files)

print(all_files)
for i in range(0, total_length):
    site = "./html_files/" + all_files[i]

    # Open html file
    with open(site, 'rb') as f:
        html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
    pointers = soup.find_all('a')
    
    # Backward linking (corner case of first graph)
    if i == 0:
        pointers[0]['href'] = "../index.html"
        pointers[0]['target'] = "homepage"
    else:
        pointers[0]['href'] = all_files[i-1]

    # Forward linking (corner case of last graph)
    if i == len(all_files) - 1:
        pointers[1]['href'] = "../index.html"
        pointers[1]['target'] = "homepage"
    else:
        pointers[1]['href'] = all_files[i+1]
    
    # Write to html file and close
    with open(site, 'w') as f1:
        f1.write(str(soup))
