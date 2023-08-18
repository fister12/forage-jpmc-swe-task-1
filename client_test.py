import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        expected_price = (bid_price + ask_price) / 2  # Calculate expected price
        
        self.assertEqual(stock, quote['stock'])
        self.assertEqual(bid_price, quote['top_bid']['price'])
        self.assertEqual(ask_price, quote['top_ask']['price'])
        self.assertEqual(price, expected_price)
    """ ------------ Add the assertion below ------------ """


  """ ------------ Add more unit tests ------------ """
    

def getRatio(price_a , price_b):
    if price_b==0:
        return
    return price_a/price_b

def test_getRatio(self):
    # Test division by zero case
    ratio = getRatio(100, 0)
    self.assertEqual(ratio, float('inf'))

    # Test division by zero with reversed values
    ratio = getRatio(0, 100)
    self.assertEqual(ratio, 0.0)

    # Test positive values
    ratio = getRatio(10, 5)
    self.assertEqual(ratio, 2.0)

    # Test negative values
    ratio = getRatio(-10, -5)
    self.assertEqual(ratio, 2.0)


if __name__ == '__main__':
    unittest.main()

