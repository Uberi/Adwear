#!/usr/bin/env python

import random, os
from os import path

ads_path = path.join(path.dirname(path.abspath(__file__)), "ads")

ads = []
while True:
    if len(ads) == 0:
        ads = os.listdir(ads_path)
        random.shuffle(ads)
    ad = ads.pop()
    os.system("python '{}'".format(path.join(ads_path, ad)))
