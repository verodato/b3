#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import isfile
from os import listdir
import re
import datetime
from datetime import timedelta, datetime
from xml.dom import minidom
from settings import path


def xml2table():
  ''' 
  Extract selected info from xml file into a table. Save result as 
  .tsv file.
   '''
  
  # find xml file and read it
  for f in listdir(path):
      if isfile(path + f):
        xmldoc = minidom.parse(path + f)

  # get date from file
  dt = xmldoc.getElementsByTagName('CreDtAndTm')[0].childNodes[0].nodeValue
  print('date',dt)
  dt = re.sub('-','',dt[0:10])

  # open .tsv file to save results
  f = open('bvbg18601_'+ dt +'.tsv', 'w')
  
  # print file header
  f.write('TckrSymb\tOpnIntrst\tFrstPric\tMinPric\tMaxPric\tTradAvrgPric\tLastPric\n')

  # list of nodes of "PricRpt" tags
  itemlist = xmldoc.getElementsByTagName('PricRpt')
  # loop list of nodes and extract info
  for s in itemlist:
    TckrSymb = s.getElementsByTagName("TckrSymb")[0].childNodes[0].nodeValue             # ticker
    Dt = s.getElementsByTagName("Dt")[0].childNodes[0].nodeValue                         # date
    OpnIntrst = '-'
    if len(s.getElementsByTagName("OpnIntrst")) > 0:
      OpnIntrst = s.getElementsByTagName("OpnIntrst")[0].childNodes[0].nodeValue         # open interest
    if len(s.getElementsByTagName("LastPric")) > 0:
      FrstPric = s.getElementsByTagName("FrstPric")[0].childNodes[0].nodeValue           # open price
      MinPric  = s.getElementsByTagName("MinPric")[0].childNodes[0].nodeValue            # minimum price
      MaxPric  = s.getElementsByTagName("MaxPric")[0].childNodes[0].nodeValue            # maximum price
      TradAvrgPric = s.getElementsByTagName("TradAvrgPric")[0].childNodes[0].nodeValue   # trade averaged price
      LastPric = s.getElementsByTagName("LastPric")[0].childNodes[0].nodeValue           # close price
      RglrTxsQty = s.getElementsByTagName("RglrTxsQty")[0].childNodes[0].nodeValue       # number of transactions.
      # write to file
      f.write(TckrSymb+'\t'+OpnIntrst+'\t'+FrstPric+'\t'+MinPric+'\t'+MaxPric+'\t'+TradAvrgPric+'\t'+LastPric+'\n')
    else:
      f.write(TckrSymb+'\t'+OpnIntrst+'\t-\t-\t-\t-\t-\n')


if __name__ == "__main__":
  xml2table()
