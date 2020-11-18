import os, json, re
os.system("clear")

from flask import Flask, request
app = Flask(__name__)

import pandas as pd
import numpy as np


@app.route('/')  # route localhost:5000
def index():
   return "Ceci est la page d'accueil.<a href=\"/contact\">contact</a>"

@app.route('/hello/<phrase>')
def hello(phrase):
   return "Bonjour "+phrase

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    lignes = []
    chain = ""
    
    if request.method == 'POST':
        df = pd.read_csv('../t.csv', ";")
        fd = open("../t.csv")
        for ligne in fd.readlines() :
            #res1 = re.search( ???? , ligne)
            res2 = re.search(""+request.form['msg'], ligne)
            if res2 :
                lignes.append(ligne)
                chain += str(ligne)

        chain2 = ""
        tab = []
        #convertire le tableau lignes en tableau de deux dimensions
        #c'est a dire ligne colonne
        chain2 += "<table>"
        chain2 += "<tr>"
        for x in df.columns:
            chain2 += "<th>"+x+"</th>"
        chain2 += "<tr>"
        for i in lignes:
            chain2 += "<tr>"
            t = i.split(";")
            tab.append(t)
            for e in t:#parcour chaue colonne de la ligne i
                chain2 += "<td>"+e+"</rd>"
            chain2 += "<tr>"
        chain2 += "<table>"



        #df2 est un dataframe permettant de sortie un fichier csv
        df2 = pd.DataFrame(np.array(tab), columns=df.columns)
        #sort le fichier csv
        df2.to_csv("out_file.csv", sep=";")#fichier de sortie .csv

        return chain2
        #return "Vous avez envoyé : {msg}".format(msg=request.form['msg'])
    return '<form action="" method="post"><input type="text" name="msg" /><input type="submit" value="Envoyer" /></form>'


app.run()

