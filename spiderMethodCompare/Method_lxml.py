import re

from download import targets
from lxml.html import fromstring


def lxml_scraper(html):
    tree = fromstring(html)
    results = {}
    for target in targets:
        results[target] = tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % target)[0].text_content()
    return results


def lxml_xpath_scraper(html):
    tree = fromstring(html)
    results = {}
    for target in targets:
        results[target] = tree.xpath('//tr[@id="places_%s__row"]/td[@class="w2p_fw"]' % target)[0].text_content()
    return results