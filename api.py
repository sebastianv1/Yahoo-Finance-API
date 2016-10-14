import sys
import urllib.request
import json
import pprint
YAHOO_API_ENDPOINT = "https://query.yahooapis.com/v1/public/yql?q="

class Stock:
  def __init__(self, stock):
    extension = urllib.request.quote("select * from yahoo.finance.quotes where symbol in (\"" + stock + "\")")
    url_format = "&format=json&env=store://datatables.org/alltableswithkeys&callback="
    url = YAHOO_API_ENDPOINT + extension + url_format
    stock_file = urllib.request.urlopen(url)
    if stock_file.getcode() == 200:
      # Success
      json_response = json.loads(stock_file.read().decode('utf-8'))
      if json_response['query'] and json_response['query']['count'] == 1:
        self.data = json_response['query']['results']['quote']
      else:
        print("Error in query")
        self.data = None
    else:
      # Error
      self.data = None

# Used if you want to run from terminal and see output
def main(arguments):
  stock = Stock(arguments[1])
  pprint.pprint(stock.data)


if __name__ == "__main__":
  main(sys.argv)
