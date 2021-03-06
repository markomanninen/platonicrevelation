#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# file: heb.py

import re
from collections import OrderedDict
from .romanizer import romanizer

has_capitals = False

data = OrderedDict()

"""

Data mapping between hebrew letters and their linguistic components

http://en.wikipedia.org/wiki/Hebrew_alphabet

Segments:
- vowel
- consonant

Four vowels: א ה ו י (a e w i)

Transliteration: http://baytephraim.com/mobile_site/Hebrew.html

"""

# letters from א to ט (1 to 9)
# alef:http://en.wiktionary.org/wiki/
data['alef'] = dict(letter=[u'א'], name=u'אָלֶף', segment='vowel', subsegment='', transliteration=u'a', order=1)
# beth:http://en.wiktionary.org/wiki/
data['beth'] = dict(letter=[u'ב'], name=u'בֵּית', segment='consonant', subsegment='', transliteration=u'b', order=2)
# gimel:http://en.wiktionary.org/wiki/
data['gimel'] = dict(letter=[u'ג'], name=u'גִּימל', segment='consonant', subsegment='', transliteration=u'c', order=3)
# daleth:http://en.wiktionary.org/wiki/
data['daleth'] = dict(letter=[u'ד'], name=u'דָּלֶת', segment='consonant', subsegment='', transliteration=u'd', order=4)
# he:http://en.wiktionary.org/wiki/
data['he'] = dict(letter=[u'ה'], name=u'הי', segment='vowel', subsegment='', transliteration=u'e', order=5)
# vau:http://en.wikipedia.org/wiki/
data['vau'] = dict(letter=[u'ו'], name=u'ויו', segment='vowel', subsegment='', transliteration=u'f', order=6)
# zayin:http://en.wiktionary.org/wiki/
data['zayin'] = dict(letter=[u'ז'], name=u'זַיִן', segment='consonant', subsegment='', transliteration=u'z', order=7)
# heth:http://en.wiktionary.org/wiki/
data['heth'] = dict(letter=[u'ח'], name=u'חֵית', segment='consonant', subsegment='', transliteration=u'h', order=8)
# teth:http://en.wiktionary.org/wiki/
data['teth'] = dict(letter=[u'ט'], name=u'טֵית', segment='consonant', subsegment='', transliteration=u'u', order=9)

# letters from י to צ (10 to 90)
# yod:http://en.wiktionary.org/wiki/
data['yod'] = dict(letter=[u'י'], name=u'יוֹד', segment='vowel', subsegment='', transliteration=u'i', order=10)
# kaph:http://en.wiktionary.org/wiki/
data['kaph'] = dict(letter=[u'כ'], name=u'כַּף', segment='consonant', subsegment='', transliteration=u'k', order=11)
# lamed:http://en.wiktionary.org/wiki/
data['lamed'] = dict(letter=[u'ל'], name=u'לָמֶד', segment='consonant', subsegment='', transliteration=u'l', order=12)
# mem:http://en.wiktionary.org/wiki/
data['mem'] = dict(letter=[u'מ'], name=u'מֵם', segment='consonant', subsegment='', transliteration=u'm', order=13)
# num:http://en.wiktionary.org/wiki/
data['num'] = dict(letter=[u'נ'], name=u'נוּן', segment='consonant', subsegment='', transliteration=u'n', order=14)
# samekh:http://en.wiktionary.org/wiki/
data['samekh'] = dict(letter=[u'ס'], name=u'סָמֶך', segment='consonant', subsegment='', transliteration=u'x', order=15)
# ayin:http://en.wiktionary.org/wiki/
data['ayin'] = dict(letter=[u'ע'], name=u'עַיִן', segment='consonant', subsegment='', transliteration=u'o', order=16)
# pe:http://en.wiktionary.org/wiki/π
data['pe'] = dict(letter=[u'פ'], name=u'פה', segment='consonant', subsegment='', transliteration=u'p', order=17)
# tsade:http://en.wikipedia.org/wiki/Tsade
data['tsade'] = dict(letter=[u'צ'], name=u'צדיק', segment='consonant', subsegment='', transliteration=u'y', order=18)

# letters from ק to ץ (100 to 900)
# qoph:http://en.wiktionary.org/wiki/
data['qoph'] = dict(letter=[u'ק'], name=u'קוֹף', segment='consonant', subsegment='', transliteration=u'q', order=19)
# resh:http://en.wiktionary.org/wiki/
data['resh'] = dict(letter=[u'ר'], name=u'רֵישׂ', segment='consonant', subsegment='', transliteration=u'r', order=20)
# shin:http://en.wiktionary.org/wiki/
data['shin'] = dict(letter=[u'ש'], name=u'שִׁין', segment='consonant', subsegment='', transliteration=u's', order=21)
# tau:http://en.wiktionary.org/wiki/
data['tau'] = dict(letter=[u'ת'], name=u'תו', segment='consonant', subsegment='', transliteration=u't', order=22)
# final_kaph:http://en.wiktionary.org/wiki/
data['final_kaph'] = dict(letter=[u'ך'], name=u'כַף סוֹפִית', segment='consonant', subsegment='', transliteration=u'K', order=23)
# final_mem, chi:http://en.wiktionary.org/wiki/
data['final_mem'] = dict(letter=[u'ם'], name=u'מֵם סוֹפִית', segment='consonant', subsegment='', transliteration=u'M', order=24)
# final_nun:http://en.wiktionary.org/wiki/
data['final_nun'] = dict(letter=[u'ן'], name=u'נוּן סוֹפִית', segment='consonant', subsegment='', transliteration=u'N', order=25)
# final_pe:http://en.wiktionary.org/wiki/
data['final_pe'] = dict(letter=[u'ף'], name=u'פה סופית', segment='consonant', subsegment='', transliteration=u'P', order=26)
# final_tsade:http://en.wiktionary.org/wiki/Tsade
data['final_tsade'] = dict(letter=[u'ץ'], name=u'צדיק סופית', segment='consonant', subsegment='', transliteration=u'Y', order=27)

r = romanizer(data, False)

# collect hebrew and transliteration letters from data dictionary for preprocessing function
letters = ''.join([''.join(d['letter'])+d['transliteration'] for key, d in data.items()])
regex = re.compile('[^%s ]+' % letters)

def preprocess(string):
    """
    Preprocess string to transform all diacritics and remove other special characters than appropriate
    
    :param string:
    :return:
    """
    return regex.sub('', string)

def convert(string, sanitize=False):
    """
    Swap characters from script to transliterated version and vice versa.
    Optionally sanitize string by using preprocess function.

    :param sanitize:
    :param string:
    :return:
    """
    return r.convert(string, (preprocess if sanitize else False))

