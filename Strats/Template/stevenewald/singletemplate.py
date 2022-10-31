from array import array
import time
import collections
import math

#Very simple single-stock template. We will be generating these to get started with a simple strategy, and then generalizing it outward.

class templateStrategy():
  """
  A base strategy that is used to explain how to properly develop a strategy.
  """
  
  def __init__(self, metrics, initvalues):
    """
    Metrics - the actual information you need to track. If this is a specific algorithm, you can hard-code it and remove that argument.
    Initvalues - the initial values of your arguments. 
    """
    self.data = zip(metrics,initvalues)
    self.time = time.time()
    self.orders = []
    self.ticks = 0
    self.trend = "Up"
#YOU WILL WANT A FULL SUITE OF SETTER AND GETTER METHODS!

  def getData(self):
    return self.data

  def getTime(self):
    return self.time

  def getOrders(self) -> array:
    return self.orders

  def getTicks(self) -> int:
    return self.ticks

  def getTrend(self) -> str:
    return self.trend

  def setTrend(self, trend: str) -> None:
    self.trend = trend
  
def clear_orders(self):
    """
    Clears all current orders and logs relevant information.
    """
    print(f"Trashing %d orders.", len(self.orders))
    self.orders = []
    
def update(self, data):
    """
    Will be called on every tick to update the algorithm state and output buys/sells.
    """
    self.ticks += 1
    #Ingest Data
    updates = zip(data.keys(), data.values())
    for metric, information in updates:
      self.data[metric] = information
      
    self.clear_orders()

    # retrieve data to store previous price
    prevPrice = self.getData()['price']

    # use new data to store updated price
    newPrice = data['price']

    # if the new price is ge old and we had a downward trend, reverse position
    if newPrice>=prevPrice and self.getTrend()=="Down":
      self.setTrend("Up")
      self.orders.append("BUY")
    # otherwise, if new price is less than old and our previous trend was upwards, reverse position
    elif newPrice<prevPrice and self.getTrend()=="Up":
      self.setTrend("Down")
      self.orders.append("SELL")
    return self.orders
    
