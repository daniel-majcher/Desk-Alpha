from array import array
import time
import collections
import math

#Very simple single-stock template. We will be generating these to get started with a simple strategy, and then generalizing it outward.

class templateStrategy():
  """
  A base strategy that is used to explain how to properly develop a strategy.
  """
  
  def __init__(self, stockInfo):
    """
    stockInfo - dictionary of stock prices
    """
    self.data = stockInfo
    self.time = time.time()
    self.orders = []
    self.ticks = 0
    self.trends = {}
    for stock in self.data:
      self.trends[stock] = "Up"
#YOU WILL WANT A FULL SUITE OF SETTER AND GETTER METHODS!

  def getPrice(self, stock) -> dict:
    return self.data[stock]['price']

  def getTime(self) -> time:
    return self.time

  def getOrders(self) -> array:
    return self.orders

  def getTicks(self) -> int:
    return self.ticks

  def getTrend(self, stock) -> str:
    return self.trends[stock]

  def setStock(self, stock, info) -> None:
    self.data[stock] = info

  def setTrend(self, stock, trend: str) -> None:
    self.trends[stock] = trend
  
def clear_orders(self):
    """
    Clears all current orders and logs relevant information.
    """
    print(f"Trashing %d orders.", len(self.orders))
    self.orders = []
    
def update(self, updatedData):
    """
    Will be called on every tick to update the algorithm state and output buys/sells.
    """
    self.ticks += 1
    self.clear_orders()
    #Ingest Data
    for stock in updatedData:
      # retrieve data to store previous price
      prevPrice = self.getPrice(stock)

      # Update new stock info
      self.setStock(stock, updatedData)

      # use new data to store updated price
      newPrice = updatedData[stock]['price']

      # if the new price is ge old and we had a downward trend, reverse position
      if newPrice>=prevPrice and self.getTrend(stock)=="Down":
        self.setTrend(stock, "Up")
        self.orders.append((stock, "BUY"))
      # otherwise, if new price is less than old and our previous trend was upwards, reverse position
      elif newPrice<prevPrice and self.getTrend(stock)=="Up":
        self.setTrend(stock, "Down")
        self.orders.append((stock, "SELL"))
    return self.orders
    
