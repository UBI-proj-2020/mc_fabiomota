from bs4 import BeautifulSoup
import requests
import csv
import lxml
import urllib
import re
from app import db

from app.models import Jogador, Equipa, Jogo, Competicao
import time

jogador = Jogador.query.all()
equipa = Equipa.query.all()
jogo = Jogo.query.all()
competicao = Competicao.query.all()


def main(ids):
    #_id = input('Introduz o ID da equipa: ')
    _id = ids
    abre_link = 'https://www.zerozero.pt/equipa.php?id=' + _id
    result =  requests.get(abre_link)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    
    print('')

    print('###### NOME ######')
    nome = soup.title.text
    nome = nome.split("::", 1)
    #print(nome)
    nome_equipa_tittle = nome[0]
    nome_equipa_tittle = nome_equipa_tittle[:-1]
    print('NOME DA EQUIPA TITULO: ', nome_equipa_tittle)
    
    nome_equipa_tittle = nome_equipa_tittle.split(" - ",1)
    #print(nome_equipa_tittle)

    if(len(nome_equipa_tittle)==1):
        _modalidade = 'Futebol'
    if(len(nome_equipa_tittle)==2):
        _modalidade = nome_equipa_tittle[1]
    print('MODALIDADE: ', _modalidade)


    _nome_equipa = soup.h1.span.text
    print('NOME DA EQUIPA: ',_nome_equipa)

    try:
        stadium = soup.find_all('div', id='stadium')
        string = str(stadium)
        #print('##########COPIA###############')
        #print(string)
        
        x = string.find("sem foto")
        
        if(x == -1):
            print("-------> TEM FOTO")
            string = string.split("title",1)
            string2 = string[1]
            string2 = string2.split("vspace",1)
            _local = string2[0][2:-2]
            print('LOCAL: ', _local)
        else:
            print("------> NÃO TEM FOTO")
            string = string.split("</a></span><div class=",1)
            #print(string)
            string2 = string[0]
            #print(string2)
            _local = remove_html_tags(str(string2))
            _local = _local[11:]
            print('LOCAL: ', _local)
            
    except:
        print('LOCAL sem informação ')
        _local = ''

    print('INSERIR')
    insereequipa(_id, _nome_equipa, _modalidade,_local)
    print('INSERIU')

def remove_html_tags(text):
    """Remove html tags from a string"""
    #print('VOU REMOVER AS TAGS DA STRING')
    clean = re.compile('<.*?>')
    #print('',re.sub(clean, '', text))
    return re.sub(clean, '', text)

def insereequipa(_id, _nome, _modalidade,_local):
    e = Equipa(id=_id, nome=_nome, modalidade=_modalidade, local=_local)
    db.session.add(e)
    db.session.commit()
"""
id = ['209495','4','10508']
for x in range(0, len(id), 1):
    main(id[x])
"""

ids = ['57694','87066','7891','14912','2170','8179','20263','5678','10511','8165','14910','3688','95731','209901','233227','232124','94238','92616','10996','10508','209495','20265','64078','52620','6555','23','92774','4','20394','4369','16','12743','8194']
for x in range(0, len(ids), 1):
    time.sleep(2)
    main(ids[x])
