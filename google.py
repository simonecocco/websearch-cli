import argparse
import webbrowser
import sys
from urllib.parse import quote

def search(text):
    tab = ''
    query = ''
    qtext = text.get('text', None)
    if qtext is not None:
        around = text.get('around')
        if around is not None:
            around = f' AROUND({around[0]}) '
        else:
            around = ' '
        query = around.join([' '.join(x) for x in qtext])
    strict_words = text.get('strict', None)
    if strict_words is not None:
        for w1 in strict_words:
            for w in w1:
                query += f' "{w}"'
    prohibited_words = text.get('no_word', None)
    if prohibited_words is not None:
        for w1 in prohibited_words:
            for w in w1:
                query += f' -{w}'
    interval = text.get('fromto', None)
    if interval is not None:
        query += ' (' + ' OR '.join([f'{interval[i]}..{interval[i+1]}' for i in range(0, len(interval), 2)]) + ')'
    price = text.get('price', None)
    if price is not None:
        query += f' {"€" if "EUR" in price else "$"}'
        tab = '&tbm=shop'
    usernames = text.get('username', None)
    if usernames is not None:
        query += f' (' + ' OR '.join([f'@{u}' for u in usernames]) + ')'
    hashtag = text.get('hashtag', None)
    if hashtag is not None:
        query += ' '
        query += '(' + ' OR '.join([('(' + ' AND '.join([f'#{y}' for y in x]) + ')') for x in hashtag]) + ')'
    convert = text.get('convert', None)
    if convert is not None:
        query += f' {convert[0]} in {convert[1]}'
    sites = text.get('site', None)
    if sites is not None:
        query += ' ' + ' OR '.join(f'site:{x}' for x in sites)
    no_sites = text.get('no_site', None)
    if no_sites is not None:
        query += ' ' + ' AND '.join(f'-site:{x}' for x in no_sites)
    cache = text.get('cache', None)
    if cache is not None:
        query += f' cache:{cache[0]}'
    t = text.get('type', None)
    if t is not None:
        query += f' filetype:{t[0]}'
    d = text.get('define', None)
    if d is not None:
        query += f' define:{d[0]}'
    w = text.get('weather', None)
    if w is not None:
        query += f' weather:{w[0]}'
    m = text.get('map', None)
    if m is not None:
        query += f' map:{m[0]}'
    in_text = text['in_text']
    if in_text is not None:
        query += f' (intext:{" ".join(in_text)})'
    in_url = text['in_url']
    if in_url is not None:
        query += f' (inurl:{" ".join(in_url)})'
    in_title = text['in_title']
    if in_title is not None:
        query += f' (intitle:{" ".join(in_title)})'
    url_string = f'https://google.com/search?q={tab}{quote(query)}'
    webbrowser.open_new_tab(url_string)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='google', description='Search in google from CLI')
    parser.add_argument('-q', dest='text', metavar='QUERY', type=str, nargs='+', action='append', help='Search query')
    parser.add_argument('-s', '--strict', dest='strict', type=str, nargs='+', action='append', help='Set strict mode for words')
    parser.add_argument('-n', '--no-word', dest='no_word', type=str, nargs='+', action='append', help='Prohibite words')
    parser.add_argument('--from-to', dest='fromto', type=str, nargs='+', action='append', help='Define an interval')
    parser.add_argument('-p', '--price', choices=['EUR', 'USD'], dest='price', type=str, nargs=1, help='Show price of product in USD or EUR')
    parser.add_argument('-u', '--username', dest='username', type=str, nargs='+', help='Search username')
    parser.add_argument('-H', '--hashtag', dest='hashtag', type=str, nargs='+', action='append', help='Find almost one of the hashtag')
    parser.add_argument('-c', '--convert', dest='convert', type=str, nargs='+', help='Convert a misure into another')
    parser.add_argument('-S', '--in-site', dest='site', type=str, nargs='+', help='Search in a site')
    parser.add_argument('-nS', '--no-site', dest='no_site', type=str, nargs='+', help='Don\'t search on that site')
    parser.add_argument('-C', '--cache', dest='cache', type=str, nargs=1, help='Search inside the website cache')
    parser.add_argument('-f', '--filetype', dest='type', type=str, nargs=1, help='Specify the file type')
    parser.add_argument('-d', '--define', dest='define', type=str, nargs=1, help='Define a word')
    parser.add_argument('-w', '--weather', dest='weather', type=str, nargs=1, help='Search for the weather in a specified city')
    parser.add_argument('-m', '--map', dest='map', type=str, nargs=1, help='Search for a locality')
    parser.add_argument('-a', '--query-around', dest='around', type=str, nargs=1, help='Set the around value for query')
    parser.add_argument('-qt', '--in-text', dest='in_text', type=str, nargs='+', help='Search a word or a phrase into sites text')
    parser.add_argument('-qT', '--in-title', dest='in_title', type=str, nargs='+', help='Search a word or a phrase into sites url')
    parser.add_argument('-qu', '--in-url', dest='in_url', type=str, nargs='+', help='Search a word or a phrase into sites url')
    args = vars(parser.parse_args())
    if len(list(filter(lambda x: x is not None, args.values()))) <= 1:
        query = sys.stdin.readline()
        url_string = f'https://google.com/search?q={quote(query)}'
        webbrowser.open_new_tab(url_string)
    else:
        search(args)