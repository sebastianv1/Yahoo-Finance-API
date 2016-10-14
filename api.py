import sys
import urllib.request
import json
import pprint

YAHOO_API_ENDPOINT = "https://query.yahooapis.com/v1/public/yql?q="

class Stock:
  def __init__(self, stock, start_date=None, end_date=None):
    query = "select * from yahoo.finance.quotes where symbol = \"" + stock + "\""
    if start_date and end_date:
      query = "select * from yahoo.finance.historicaldata where symbol = \"" + stock + "\" and startDate = \"" + start_date + "\" and endDate = \"" + end_date + "\""
    if start_date and not end_date:
      query = "select * from yahoo.finance.historicaldata where symbol = \"" + stock + "\" and startDate = \"" + start_date + "\" and endDate = \"" + start_date + "\""
    query_url = urllib.request.quote(query)
    url_extension = "&format=json&env=store://datatables.org/alltableswithkeys&callback="
    url = YAHOO_API_ENDPOINT + query_url + url_extension
    stock_file = urllib.request.urlopen(url)
    if stock_file.getcode() == 200:
      # Success
      json_response = json.loads(stock_file.read().decode('utf-8'))
      if json_response['query'] and json_response['query']['count'] >= 1:
        self.data = json_response['query']['results']['quote']
      else:
        print("Error in query")
        self.data = None
    else:
      # Error
      self.data = None

# Used if you want to run from terminal and see output
def main(arguments):
  if len(arguments) < 4:
    while len(arguments) < 4:
      arguments.append(None)
  stock = Stock(arguments[1], arguments[2], arguments[3])
  pprint.pprint(stock.data)


if __name__ == "__main__":
  main(sys.argv)
