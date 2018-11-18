import time
import re
from Method_re import re_scraper
from Method_BeautifulSoup import bs_scraper
from Method_lxml import lxml_scraper
from Method_lxml import lxml_xpath_scraper

from download import download

num_iterations = 1000  # 每个爬虫测试1000次
html = download('http://example.webscraping.com/places/default/view/Australia-14')

scrapers = [('re', re_scraper), ('bs', bs_scraper), ('lxml', lxml_scraper),
            ('lxml_xpath', lxml_xpath_scraper)]

for name, scraper in scrapers:
    start_time = time.time()
    for i in range(num_iterations):
        if scraper == re_scraper:
            re.purge() #清除缓存，保证公平性
        result = scraper(html)
        # 检测结果是否为想要的
        assert result['area'] == '7,686,850 square kilometres'
    end_time = time.time()
    print("=================================================================")
    print('%s: %.2f seconds' % (name, end_time - start_time))
