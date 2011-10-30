"""
tsol.py - TL m1 timetable module
Copyright 2011, Andrew Watson, Adrien Beraud
Licensed under GPL 3.0
"""
from urllib import urlencode
import urllib, re

def tsol(arret, dir):
    dir = dir.lower();
    if not dir in ['a', 'r']:
        dir = 'a'

    directions = {'a':'L', 'r':'R'}

    base_url = 'http://www.t-l.ch/htr.php?'
    payload = dict(ligne='70', sens=dir, arret=arret+'_'+directions[dir])
    socket = urllib.urlopen( base_url + urlencode(payload))
    content = socket.read()
    socket.close()

    table_re = re.compile('<table\s[^>]*id=\"htr_param_table\"[^>]*>(.*)<\/table>', re.I|re.M|re.S)
    time_re = re.compile('<td\s[^>]*><span\s[^>]*>([^<]*)<\/span>[^<]*<\/td>', re.I|re.M|re.S)
    table = table_re.findall(content)
    if len(table) == 0:
        return []
    elements = time_re.findall(table[0])

    return elements
