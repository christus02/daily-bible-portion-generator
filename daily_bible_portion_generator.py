#!/usr/bin/env python3
'''
Description: To Generate a Daily Bible Portion from Bible
'''

import json
import copy
import urllib.request

BIBLE_INDEX = 'https://raw.githubusercontent.com/christus02/daily-bible-portion-generator/main/resources/bible-index.json'

def readBibleIndex(url):
    '''
    Function to get the JSON file from GitHub
    '''
    headers = {'Content-Type': 'application/json'}
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    return response.read()

def parseJson(jsonContent):
    '''
    Function to parse the json to Python Datastructure
    '''
    return json.loads(jsonContent)

jsonBibleIndex = readBibleIndex(BIBLE_INDEX)
BIBLE_DATA = parseJson(jsonBibleIndex)

def recontructData():
    '''
    Function to recontruct the data for convenience
    '''
    data = {}
    data['allBooks'] = []
    i = 0
    for book in BIBLE_DATA:
        i = i + 1
        data[book['book']] = {}
        data[book['book']]['index'] = i
        data['allBooks'].append(book['book'])
        data[book['book']]['chaptersCount'] = len(book['chapters'])
        data[book['book']]['chapters'] = book['chapters']
    return data

ORGANISED_DATA = recontructData()

def getBibleBooks():
    '''
    Function to return all the books of the Bible
    '''
    return ORGANISED_DATA['allBooks']

def getIndexOfBook(bookName):
    '''
    Function to return the index of the Book in the Bible
    '''
    return ORGANISED_DATA[bookName]['index']

def getChaptersOfBook(book="Romans"):
    '''
    Function to get the number of Chapters from the specified book of Bible
    '''
    return ORGANISED_DATA[book]['chaptersCount']

def getBiblePortionFromBook(book, fromChapter=1):
    chapters = getChaptersOfBook(book)
    ret = []
    for i in range(fromChapter, chapters+1):
        ret.extend(getBiblePortionFromChapter(book=book, chapter=i))
    return ret

def getBiblePortionFromChapter(book="Romans", chapter=6):
    '''
    Function to return a list of Bible portion from a chapter
    The logic is that, it will allocate 10 verses per day and 
    if the last chapter has more than 7 verses, then the last 7+ verses
    would be spilled over to the next day
    '''
    dailyVerseCount = 10
    spillover = 7 # spillover to next day if it's greater than this variable

    versesCount = int(ORGANISED_DATA[book]['chapters'][chapter-1]['verses'])

    days = versesCount // 10 # Python3 :) 
    remainder = versesCount % 10

    start_verse = 1
    end_verse = dailyVerseCount
    verses = []
    
    for i in range(days):
        verses.append({"start":start_verse, "end":end_verse})
        start_verse = end_verse + 1
        end_verse = end_verse + dailyVerseCount

    if remainder > spillover:
        verses.append({"start":verses[-1]["end"]+1, "end":verses[-1]["end"]+remainder})
    else:
        verses[-1]["end"] = verses[-1]["end"]+remainder

    return _writeToString(book, chapter, verses)

def _writeToString(book, chapter, verses):

    STRING_TEMPLATE = "*Personal Bible study* - Read:\n*" + book + " Chapter " + str(chapter) + ":" + "START" + " to " + str(chapter) + ":" + "END*\nGod bless you."
    ret = []
    for daily in verses:
        copied_string_template = copy.deepcopy(STRING_TEMPLATE)
        copied_string_template = copied_string_template.replace("START", str(daily['start']))
        copied_string_template = copied_string_template.replace("END", str(daily['end']))
        ret.append(copied_string_template)
    return ret


if __name__ == "__main__":
    for portion in getBiblePortionFromBook("Romans", fromChapter=6):
        print (portion)


#*************************************#
__author__ = "Raghul Christus"
__version__ = "1.0.0"
__maintainer__ = "Raghul Christus"
#*************************************#
