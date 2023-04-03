import pandas as pd

from bs4 import BeautifulSoup
from urllib import request

response = request.urlopen('https://www.python.org/').read()
soup = BeautifulSoup(response, features="html.parser")

raw_text = soup.get_text()
text = ''.join(text.strip().replace(' ', '') for text in raw_text.split('\n'))

pd.set_option('display.max_rows', 100)
res = str(pd.Series(list(text)).value_counts())

with open('./output.txt', 'w') as file:
    file.write(res)
