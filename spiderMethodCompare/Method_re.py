import re
from download import targets


def re_scraper(html):
    results = {}
    for target in targets:
        results[target] = re.search(r'<tr id="places_%s__row">.*?<td class="w2p_fw">(.*?)</td>'
                                    % target, html).groups()[0]
    return results