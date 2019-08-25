# -*- coding: utf-8 -*-
"""
@author: Ali Masoumnia
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from gsearch.googlesearch import search


x = []

#write function to append general contractor sites to list
def page(ocga_page):
    ogca_html = requests.get(ocga_page)

    soup = BeautifulSoup(ogca_html.content, 'lxml')

    for i in range(len(soup.findAll("span", {'class': 'value'}))):
        if soup.findAll("span", {'class': 'value'})[i].text[:4] == "www.":
            x.append(soup.findAll("span", {'class': 'value'})[i].text)
        else:
            pass
    return

#run function on page one and two
page("https://ogca.ca/members/member-directory/")
page("https://ogca.ca/members/member-directory/page/2/")

#put into dataframe and export for easier handling
gcs = pd.DataFrame(x[2:])
gcs.columns = ["GCs"]
gcs.to_pickle("General Contractors.p")
