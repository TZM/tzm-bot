#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from trello import TrelloClient
import os
import urllib2
import BeautifulSoup
import csv
import re

user_agent = ('Mozilla/5.0 (X11; U; Linux i686)'
                'Gecko/20071127 Firefox/2.0.0.11')
auth = TrelloClient(os.environ['TRELLO_API_KEY'], os.environ['TRELLO_TOKEN'])

gca_board = auth.get_board('4f199b088ab038761f17b066')

gca_lists = gca_board.all_lists()

chapters_to_check = []
chapters_with_web_sites = []
for gca_list in gca_lists:
    #print gca_list.id, gca_list.name
    # we get the 'Chapters to Check' list
    # with id '4f199b088ab038761f17b06b'
    if gca_list.id == '4f199b088ab038761f17b06b':
        # get the cards
        cards = gca_list.list_cards()
        print len(cards)
        for c in cards:
            # do something with the description and try to extract the website address
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', c.description)
            
            if urls != []:
                chapter_data = {'name': c.name, 'urls': urls}
                chapters_with_web_sites.append(chapter_data)
                #print chapter_data
            
    else:
        pass

print chapters_with_web_sites


