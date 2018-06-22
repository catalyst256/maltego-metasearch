#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
import json
from settings import BaseConfig as settings
from MaltegoTransform import *


def metasearch(query):
    m = MaltegoTransform()
    for page in range(1, settings.MAX_PAGES):
        url = '{0}{1}&format=json&pageno={2}'.format(
            settings.SEARX, query, page)
        response = requests.post(url).json()
        for r in response['results']:
            ent = m.addEntity('maltego.URL', r['url'])
            ent.addAdditionalFields('url', 'URL', True, r['url'])
            if r.get('title'):
                ent.addAdditionalFields(
                    'title', 'Title', True, r['title'])
            if r.get('content'):
                ent.addAdditionalFields(
                    'content', 'Content', True, r['content'])
    m.returnOutput()


if __name__ == '__main__':
    metasearch(sys.argv[1])
