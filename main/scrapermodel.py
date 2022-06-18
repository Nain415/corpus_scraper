#!/usr/bin/python

import re, convokit, os, random
from datetime import datetime
from convokit import Corpus, download
from openpyxl import Workbook

subreddits = ["subreddit-UBC", "subreddit-vancouver", "subreddit-canada"]

class Scraper:
    def __init__(self, subReddit=""):
        self._startIndex = 0
        self._endIndex = 5*(10**5)
        self._startDate = 2007
        self._endDate = 2018
        self._target = subReddit
        if self._target != "": Corpus(filename=download(self._target), utterance_start_index=self._startIndex, utterance_end_index=self._endIndex)
    def set_subreddit(self, subReddit):
        self._target = subReddit
        self._corpus = Corpus(filename=download(self._target), utterance_start_index=self._startIndex, utterance_end_index=self._endIndex)
        
    def get_subReddit(self):
        return(self._target)

    def set_indices(self, startIndex, endIndex):
        self._startIndex = int(startIndex)
        self._endIndex = int(endIndex)

    def set_dates(self, startDate, endDate):
        self._startDate = int(startDate)
        self._endDate = int(endDate)

    def get_dates(self):
        return (self._startDate, self._endDate)

    def get_indices(self):
        return (self._startIndex, self._endIndex)
    
    def search(self, pattern):
        self.search_date(pattern, True, True, True)
        #expects self._target to be defined

    def search_date(self, pattern, yyyy1, yyyy2, *num):
        #expects self._target to be defined
  
        wb = Workbook()
        ws = wb.active
        ws.append(["Speaker", "Utterance", "Date", "Function"])
        
        start, end = self.get_indices()
        subreddit = self.get_subReddit()
        corpus = self._corpus
        
        words = []
        r = re.compile(pattern)


        for i in corpus.iter_utterances():
            matches = r.findall(i.text)
            year = datetime.fromtimestamp(i.timestamp).year
            if matches != [] and (yyyy1 <= year and year <= yyyy2 or yyyy1 == True):
                matches.append((i.speaker.id, datetime.fromtimestamp(i.timestamp), i.text))
                words.append(matches)

        #randomize
        if len(num) > 0:
            if num[0] <= len(words): words = random.sample(words,num[0])
            else: words = random.sample(words,len(words))

        for listofwords in words:
            speaker_info = listofwords.pop()
            ws.append(["{0}".format(speaker_info[0]), "{0}".format(speaker_info[2]), "{0}".format(speaker_info[1])])

        path = "./output"
        if not os.path.exists(path): os.makedirs(path)

        dest_filename = str(start) + pattern + "_" + subreddit + '_results_' + str(yyyy1) + '-' + str(yyyy2) + '.xlsx'
        wb.save(os.path.join(path, dest_filename))


        #os.system(str(end) + pattern + "_" + subreddit + '_results_' + str(yyyy1) + '-' + str(yyyy2) + '.xlsx')
        
