from lxml import html
import requests

page = requests.get('http://biblehub.com/interlinear/genesis/1.htm')
tree = htnl.fromstring(page.text)


