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

result =  requests.get("https://www.zerozero.pt/equipa.php?id=4")
src = result.content
soup = BeautifulSoup(src, 'lxml')

def main():
    urls = []
    for tag in soup.find_all('td', class_='vs'):
      a_tag = tag.find('a')
      urls.append(a_tag.attrs['href'])
    print(len(urls),' URLs : ', (urls))

    #ABRIR LINK
    print('######### NOVO LINK #########')
    #INVERTE A ORDEM DO ARRAY PARA O PRÓXIMO JOGO ESTAR NA POSIÇÃO 0
    urls.reverse()
    print(urls)
    #abre_link = 'https://www.zerozero.pt'+urls[0]
    abre_link = 'https://www.zerozero.pt/jogo.php?id=7003810'
    print(abre_link)
    result_link =  requests.get(abre_link)
    src_link = result_link.content
    soup2_link = BeautifulSoup(src_link, 'lxml')
    print('')

    print('###### ID ######')
    _idjogo = urls[0]
    print(_idjogo[13:])
    _idjogofinal = _idjogo[13:]
    print('')
    
    print('###### DIA E HORA ######')
    #OBTER A INFO
    info = soup2_link.find_all('div', id='match_data')
    #print(info)
    print('----------------------------------------------')
    dia_hora = remove_html_tags(str(info))
    dia_hora = dia_hora[1:]
    print('----------------------------------------------')
    #print(dia_hora)
    dia_hora = dia_hora.split(" - ", 8)
    #print('DEPOIS DO SPLIT: ',dia_hora)
    #print(len(dia_hora))
    _dia = dia_hora[0]
    _hora = dia_hora[1]
    print('DIA: ',_dia,' // HORA: ',_hora)
    print('')

    print('###### EQUIPAS ######')
    equipas = soup2_link.title.text
    equipas = equipas[:-32]
    equipas = equipas.split("::", 1)
    equipas = equipas[0].split("vs",1)
    _equipacasa = equipas[0]
    _equipafora = equipas[1]
    print('EQUIPA CASA: ', _equipacasa, 'EQUIPA FORA: ', _equipafora)
    print('')

    print('###### COMPETIÇÃO ######') 
    array_competicao = soup2_link.title.text
    #print(array_competicao)
    array_competicao = array_competicao[:-32]
    array_competicao = array_competicao.split("::",1)
    #print(array_competicao)
    array_competicao.pop(0) 
    print(array_competicao)
    _competicao = array_competicao[0]
    print('')


    print('###### ESTÁDIO ######')
    stadium = soup2_link.find_all('div', id='stadium')
    print(stadium)
    string = str(stadium)
    string = string.split("title",1)
    print(' -------------------------> ', string[1])
    print('')
    print('TESTE COM SUCESSO: ', string[1])
    print('')
    string2 = string[1]

    print("STRING2:",string2)

    string2 = string2.split("vspace",1)

    print(string2[0])
    
    _local = string2[0][2:-2]

    print('')
    print(_local)


    print('###### FASE ######')
    fase = soup2_link.find_all('div', id='matchedition')
    print(fase)
    string = str(fase)
    string = string.split("Fase",1)
    print(' -------------------------> ', string[1])
    print('')
    string2 = string[1]
    string2 = string2.split("color:rgb(",4)
    print(string2)
    string2.pop(0)
    print(string2)

    fase = string2[0][15:-46]
    print('FASE: ', fase)
    print('')

    jornada_eliminatoria_grupo = string2[2][15:-32]
    print('JORNADA / ELIMINATORIA / GRUPO : ', jornada_eliminatoria_grupo)
    print('')


    

    """
    print('TESTE COM SUCESSO: ', string[1])
    print('')
    string2 = string[1]

    print("STRING2:",string2)

    string2 = string2.split("vspace",1)

    print(string2[0])
    
    _local = string2[0][2:-2]

    print('')
    print(_local)
    """




    print('PRÓXIMO JOGO')
    print('ID: ', _idjogofinal)
    print(_equipacasa,' vs ',_equipafora)
    print('DIA: ', _dia)
    print('HORA: ', _hora)
    print('COMPETIÇÃO: ', _competicao)
    print('LOCAL: ', _local)
    print('FASE: ', fase)
    print('JORNADA/ELIMINATÓRIA/GRUPO: ', jornada_eliminatoria_grupo)

    #INSERIR O JOGO NA BASE DE DADOS
    time.sleep( 2 )
    #inserejogo(_idjogofinal, equipas[0], equipas[1], dia_hora[0],dia_hora[1],_competicao[0])
    
def remove_html_tags(text):
    """Remove html tags from a string"""
    print('VOU REMOVER AS TAGS DA STRING')
    clean = re.compile('<.*?>')
    print('',re.sub(clean, '', text))
    return re.sub(clean, '', text)

def inserejogo(_id, _equipa_casa, _equipa_fora, _data, _hora, _competicao):
    j = Jogo(id=_id, equipa_casa= _equipa_casa, equipa_fora=_equipa_fora, data=_data, hora=_hora, competicao=_competicao)
    db.session.add(j)
    db.session.commit()

main()