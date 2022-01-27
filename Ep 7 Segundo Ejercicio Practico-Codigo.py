class EjercicioPractico2(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2021, 1, 1)  # Set Start Date
        self.SetEndDate(2021,12,31)
        self.SetCash(100000)  # Set Strategy Cash
        
        self.btc = self.AddCrypto("BTCUSD",Resolution.Daily).Symbol
        
        self.stopLoss = None
        self.takeProfit = None
        
        self.PreviousPrice = 100000000

    
    def OnData(self, data):
        price = data[self.btc].Close
        if not(self.Portfolio.Invested and self.Transactions.GetOpenOrders):
            self.MarketOrder(self.btc,1)
            self.takeProfit = self.LimitOrder(self.btc,-1,price *1.03)
            self.stopLoss = self.StopMarketOrder(self.btc,-1,price *0.97) 
        elif(price > self.PreviousPrice):
            self.stopLoss.UpdateStopPrice(price*0.97)
        
        self.PreviousPrice = price
        
    def OnOrderEvent(self, orderEvent):
        order = self.Transactions.GetOrderById(orderEvent.OrderId)
        
        if(orderEvent.Status != OrderStatus.Filled):
            return
        if(self.stopLoss == None or self.takeProfit == None):
            return
        if(order.Id == self.takeProfit.OrderId):
            self.stopLoss.Cancel()
            return
        if(order.Id == self.stopLoss.OrderId):
            self.takeProfit.Cancel()
            return
        
        