import re

def main():

    string = '[<div id="stadium"><div class="content"><div class="photo"><a href="/estadio.php?id=12"><img alt="Estádio do Sport Lisboa e Benfica (Luz)" border="0" height="100" hspace="0" src="/img/estadios/101/389101_estadio_do_sport_lisboa_e_benfica_luz_.jpg.jpg" title="Estádio do Sport Lisboa e Benfica (Luz)" vspace="0" width="150"/></a></div><div class="wrapper"><div class="name"><span><a href="/estadio.php?id=12">Estádio do Sport Lisboa e Benfica (Luz)</a></span><div class="micrologo_and_text"><div class="image"><a href="/pais.php?id=1"><img alt="Portugal" height="10" src="https://static-img.zz.pt/bandeiras/flag_1_por_30x20.png" style="vertical-align:middle;margin-top:0px;" title="Portugal" width="14"/></a></div><div class="text">Lisboa</div></div></div></div><div class="information">Lotação<span>64 642</span></div><div class="information">Medidas<span>105x68m</span></div><div class="information">Inauguração<span>2003</span></div></div></div>]'

    string = string.split("title=",1)
    print(string)

    print('')
    print('TESTE COM SUCESSO: ', string[1])
    print('')
    string2 = string[1]

    print("STRING2:",string2)

    string2 = string2.split("vspace",1)

    print(string2[0])
    
    _local = string2[0][1:-2]

    print('')
    print(_local)

main()