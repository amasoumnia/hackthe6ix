# -*- coding: utf-8 -*-
"""
@author: Ali Masoumnia
"""
from bs4 import BeautifulSoup
import html2text
import requests
import pandas as pd
import re
import time

#open dataframe array of general contractor sites
df = pd.read_pickle("General Contractors.p")
df.columns = ["GCs"]

#obtains all text from html links for each file
for x in range(len(df)):

  url = "http://" + df["GCs"][x]
  f = html2text.HTML2Text() #sets various conditions for text conversion
  f.ignore_links = True
  f.ignore_anchors = True
  f.ignore_images = True
  f.ignore_emphasis = True
  f.skip_internal_links = True

  try:
    r = requests.get(url)
    r.raise_for_status()
  except:
    time.sleep(3)
    try:
      r = requests.get(url)
      r.raise_for_status()
    except:
      pass

  soup = str(BeautifulSoup(r.content, "html.parser").prettify())

#converts and cleans html into text
  rendered_content = f.handle(soup) 
  rendered_content = re.sub(r'{{.+?}}', '', rendered_content) #removes unnecessary new lines and conversion errors
  rendered_content = rendered_content.replace("*", "").replace("#", "").replace("_", "").replace("\n\n\n\n", "\n").replace("\n\n\n", "\n\n")
  rendered_content = ''.join(c for c in rendered_content if 0 < ord(c) < 200) #removes non ASCI characters                    

#exports to text files in the corpus                                             
  file_name = 'corpus/' + df["GCs"][x].replace("www.", "").split(".")[0] + ".txt" #appends all sites as text files to build corpus
  f = open(file_name, "w", encoding="utf-8")
  f.write(rendered_content)
  f.close()