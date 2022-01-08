import urllib.request

def get_qqq_holdings():
    req = urllib.request.Request(
      url=r"https://www.zacks.com/funds/etf/QQQ/holding",
      headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    handler = urllib.request.urlopen(req)
    fdata = handler.read().decode("utf-8") 
    fdata = fdata.split('etf_holdings.formatted_data')[1].split('etf_holdings.table_header')[0].split('[')[2:]
    tickers = []
    for d in fdata:
        loc = d.find('rel')
        this_data = d[loc:].split('\\"')[1].split('\\"')[0]
        tickers.append(this_data)
    return tickers

if __name__ == '__main__':
    holdings = get_qqq_holdings()
    print(holdings)

