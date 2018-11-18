from bs4 import BeautifulSoup
from download import targets

def bs_scraper(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = {}
    for target in targets:
        results[target] = soup.find('table').find('tr', id='places_%s__row' % target) \
            .find('td', class_="w2p_fw").text
    return results