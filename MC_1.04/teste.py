import re, time
"""
minha_string = "teste benfica sporting teste"
print(minha_string)
print("==============================")

minha_string = minha_string.replace('benfica', 'sporting', '')
print(minha_string)
"""

"""
string = '<div id="stadium"><div class="content"><div class="photo">(sem foto)</div><div class="wrapper"><div class="name"><span><a href="/estadio.php?id=4251">Pavilhão Gimnodesportivo Municipal Do Ladoeiro</a></span><div class="micrologo_and_text"><div class="image"><a href="/pais.php?id=1"><img src="https://static-img.zz.pt/bandeiras/flag_1_por_30x20.png" width="14" height="10" alt="Portugal" title="Portugal" style="vertical-align:middle;margin-top:0px;"></a></div><div class="text">Ladoeiro, Idanha-a-nova</div></div></div></div><div class="information">Lotação<span>300</span></div><div class="information">Medidas<span>40x20</span></div><div class="information">Inauguração<span>0</span></div></div></div>'

x = string.find("sem foto")

print(x)
"""

"""
def main():
    stringcomestadio= '<div id="stadium"><div class="content"><div class="photo"><a href="/estadio.php?id=2521"><img src="/img/estadios/521/2521_pavilhao_desportivo_universitario_de_gualtar.jpg" width="150" height="100" border="0" alt="Pavilhão Desportivo Universitário de Gualtar" title="Pavilhão Desportivo Universitário de Gualtar" hspace="0" vspace="0"></a></div><div class="wrapper"><div class="name"><span><a href="/estadio.php?id=2521">Pavilhão Desportivo Universitário de Gualtar</a></span><div class="micrologo_and_text"><div class="image"><a href="/pais.php?id=1"><img src="https://static-img.zz.pt/bandeiras/flag_1_por_30x20.png" width="14" height="10" alt="Portugal" title="Portugal" style="vertical-align:middle;margin-top:0px;"></a></div><div class="text">Gualtar - Braga</div></div></div></div><div class="information">Lotação<span>1000</span></div><div class="information">Medidas<span>40x20</span></div><div class="information">Inauguração<span>1993</span></div></div></div>'
    string = '<div id="stadium"><div class="content"><div class="photo">(sem foto)</div><div class="wrapper"><div class="name"><span><a href="/estadio.php?id=21587">PalaBianchini</a></span><div class="micrologo_and_text"><div class="image"><a href="/pais.php?id=18"><img alt="Itália" height="10" src="https://static-img.zz.pt/bandeiras/flag_18_ita_30x20.png" style="vertical-align:middle;margin-top:0px;" title="Itália" width="14"/></a></div><div class="text">Latina</div></div></div></div><div class="information">Lotação<span>2500</span></div><div class="information">Medidas<span>-</span></div><div class="information">Inauguração<span>1975</span></div></div></div>]'
    string = string.split("</a></span><div class=",1)
    print(string)
    string2 = string[0]
    print(string2)
    _local = remove_html_tags(str(string2))
    _local = _local[10:]
    print(_local)

def remove_html_tags(text):
    print('VOU REMOVER AS TAGS DA STRING')
    clean = re.compile('<.*?>')
    print('',re.sub(clean, '', text))
    return re.sub(clean, '', text)


main()

"""

print('HELLO')
time.sleep(2)
print('HELLO 2')