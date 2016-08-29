from lxml import html
import requests
import re

"""An API for retreiving Cornell dining menus. Built by Sitar."""

def getOptions(meal, date, text):
    """Returns the dining rooms that are open for 'meal' on 'date'."""
    payload = {'menudates': date, 'menuperiod': meal}
    page = requests.post(
        'http://living.sas.cornell.edu/dine/whattoeat/menus.cfm#menu',
         data=payload)
    tree = html.fromstring(page.content)
    ops = tree.xpath('//*[@id="menulocations"]/option/' + ('text()' if text else '@value'))
    return ops

def getMenu(loc, meal, date):
    """Returns the menu for dining room 'loc' for 'meal' on 'date'."""
    payload = {'menudates': date, 'menuperiod': meal, 'menulocations': loc}
    page = requests.post( 
        'http://living.sas.cornell.edu/dine/whattoeat/menus.cfm#menu',
         data=payload)
    tree = html.fromstring(page.content)
    rawmenu = tree.xpath('//*[@id="CS_CCF_4430_51083"]/p[@class="menuItem"]/text()')
    menu = []
    for item in rawmenu:
        menu += [re.sub(r' +$', '', item.replace(u'\xa0', ''))]
    return menu

# Dining room codes:
# 1: Cook House Dining Room
# 2: Becker House Dining Room 
# 3: Keeton House Dining Room 
# 4: Rose House Dining Room
# 5: Hans Bethe House - Jansens Dining Room 
# 6: Robert Purcell Marketplace Eatery 
# 7: North Star
# 8: Risley Dining 
# 9: 104 West! 
# 10: Okenshields