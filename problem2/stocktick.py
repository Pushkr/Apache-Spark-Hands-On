class StockTick:
   def __init__(self, text_line=None, date="", time="", price=0.0, bid=0.0, ask=0.0, units=0):
      if text_line != None:
         tokens = text_line.split(",")
         self.date = tokens[0]
         self.time = tokens[1]
         try:
            self.price = float(tokens[2])
            self.bid = float(tokens[3])
            self.ask = float(tokens[4])
            self.units = int(tokens[5])
         except:
            self.price = 0.0
            self.bid = 0.0
            self.ask = 0.0
            self.units = 0
      else:
         self.date = date
         self.time = time
         self.price = price
         self.bid = bid
         self.ask = ask
         self.units = units
