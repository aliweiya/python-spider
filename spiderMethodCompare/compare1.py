import time
import re

from Method_re import re_scraper
from Method_BeautifulSoup import bs_scraper
from Method_lxml import lxml_scraper
from Method_lxml import lxml_xpath_scraper

#from chp2_all_scrapers import re_scraper, bs_scraper, lxml_scraper, lxml_xpath_scraper
from download import download


scrapers = [('re', re_scraper), ('bs',bs_scraper), ('lxml', lxml_scraper), ('lxml_xpath',lxml_xpath_scraper)]
html = download('http://example.webscraping.com/places/default/view/Australia-14')
for name, scraper in scrapers:
    print(name,"=================================================================")
    result = scraper(html)
    print(result)