from bs4 import BeautifulSoup
import requests
import csv
import lxml
import urllib
import re

result =  requests.get("https://www.zerozero.pt/equipa.php?id=4")
#result =  requests.get("https://www.zerozero.pt/equipa.php?id=93923&epoca_id=149")
src = result.content
soup = BeautifulSoup(src, 'lxml')

def main():

    print('Hello2')

    #LINKS

    urls = []

    for tag in soup.find_all('td', class_='vs'):
      a_tag = tag.find('a')
      urls.append(a_tag.attrs['href'])

    print(urls)

    #FIM DOS LINKS

    #DATAS E HORAS

    datas = []
    horas = []

    for tag_data in soup.find_all('tr', class_='parent'):
      a_tag_data = tag_data.find('a')
     # print(a_tag_data)
      datas.append(a_tag_data.get_text())

    #print(datas)


    #FIM DATAS E HORAS


    #EQUIPAS CASA

    equipa_casa = []

    for tag_casa in soup.find_all('td', class_='text home'):
      a_tag_casa = tag_casa.find('a')
      #print(a_tag_casa.get_text())
      Add_Casa = a_tag_casa.get_text()
      equipa_casa.append(Add_Casa)

    print(equipa_casa)



    #FIM EQUIPAS CASA

    #EQUIPAS FORA


    #FIM EQUIPAS FORA

    print(len(urls))


    #ABRIR LINK

    print('######### NOVO LINK #########')

    if len(urls)>2:
        abre_link = 'https://www.zerozero.pt'+urls[2]
        print(abre_link)
        result_link =  requests.get(abre_link)
        src_link = result_link.content
        soup2_link = BeautifulSoup(src_link, 'lxml')

        _casa = []

        #ERRO AQUI .text
        info = soup2_link.find_all('div', id='match_data')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$') 
        #print(info)
        print('-----------------------')
        exemplo = remove_html_tags(str(info))
        exemplo = exemplo[1:]
        print('-----------------------') 
        print(exemplo)
        exemplo = exemplo.split(" - ", 8)
        print(len(exemplo))
        y = len(exemplo)
        for x in range(2, 4, 1):
            print(x)
            #exemplo.pop(x)
            print('OK',x)
        #exemplo.pop(2)
        print('-----------------------') 
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$') 
        #exemplo2 = remove_html_tags(exemplo2)
        #print(exemplo2)

        print('###### HORÁRIO ######')
        print(exemplo)
        #cleantext = BeautifulSoup(info, "lxml").text
        #print(cleantext)

        print('###### EQUIPAS ######')
                
        equipas = soup2_link.title.text
        equipas = equipas[:-32]
        equipas = equipas.split("::", 1)
        equipas = equipas[0].split("vs",1)
        print(equipas)

        print('###### ESTÁDIO ######')

        url_estadio = []

        #AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
        for tag in soup2_link.find_all('div', id='stadium'):
            estadio = tag.find('a')
            print('---',estadio)
            #AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
            print('-------->', estadio)
            url_estadio.append(tag.get_text())

        print(url_estadio)
              
        exemplo2 = remove_html_tags(str(estadio)) 
            
            
        print(exemplo2)



        print('###### COMPETIÇÃO ######') 
        competicao = soup2_link.title.text
        print(competicao)
        competicao = competicao[:-32]
        competicao = competicao.split("::",1)
        print(competicao)
        competicao.pop(0) 
        print(competicao)

        print('')
        print('PRÓXIMO JOGO')
        print(equipas[0],' vs ',equipas[1])
        print('DIA: ', exemplo[0])
        print('HORA: ', exemplo[1])
        print('COMPETIÇÃO: ', competicao[0])


            #FECHAR LINK

            
    if len(urls) == 2:
        abre_link = 'https://www.zerozero.pt'+urls[2]
        print(abre_link)

    if len(urls) == 1:
        abre_link = 'https://www.zerozero.pt'+urls[2]
        print(abre_link)

    if len(urls) == 0:
        print('Não há jogos')
            

def remove_html_tags(text):
    """Remove html tags from a string"""
    print('ENTREI AQUI')
    clean = re.compile('<.*?>')
    print('',re.sub(clean, '', text))
    return re.sub(clean, '', text)
        



main()






#for i in range(0, len(equipa_casa), 1):
# print(equipa_casa[i], 'vs',equipa_fora[i])
