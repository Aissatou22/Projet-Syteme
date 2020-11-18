#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys, os, json, requests

reponse = requests.get("http://localhost:5000/recherche/"+sys.argv[1])
lignes = reponse.json()
"""
os.system("curl localhost:5000/recherche/"+sys.argv[1]+" > resultat")
fd = open("resultat")
lignes = json.loads(fd.readline())
"""

for ligne in lignes :
    print(ligne)
    print("--------------------")
