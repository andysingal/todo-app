from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML,'html.parser')

def find_title():
  h1_tag = simple_soup.find('h1')
  print(h1_tag.string)

def list_items():
    list_items = simple_soup.find_all('li')
    list_content = [e for e in list_items]
    print(list_content)

def find_subtitle():
    para = simple_soup.find('p',{'class':'subtitle'})
    print(para.string)

def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    print(paragraphs)
    list_para = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class',[])]
    print(list_para[0].string)

find_title()
list_items()
find_subtitle()
find_other_paragraph()
