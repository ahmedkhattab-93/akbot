from ib_insync import *
import uuid 

class IbApp():
    def onBarUpdate(self, bars,hasNewBar):
        if hasNewBar:
            pass
            #print("New bar ", bars.contract.symbol)
            #print(bars)

    def __init__(self):
        self.symbols = []
        self.ib = IB()
        self.ib.setTimeout(1000)
        self.ib.connect("127.0.0.1", 7497, 123)

        self.ib.barUpdateEvent += self.onBarUpdate

        contract = Stock("FB", 'SMART', 'USD')
        l1_order = LimitOrder('BUY', 9, 300)
        l1_tp_order = LimitOrder('SELL', 9, 305)
        l1_sl_order = StopOrder("SELL", 9, 295)

        l1_tp_order.parentId = l1_order.orderId
        l1_sl_order.parentId = l1_order.orderId

        #self.ib.reqRealTimeBars(contract, 5, 'MIDPOINT', False)

        self.ib.placeOrder(contract, l1_order)

        orders = self.ib.oneCancelsAll([l1_tp_order, l1_sl_order], str(uuid.uuid1()), 2)
        for order in orders:
            self.ib.placeOrder(contract, order)

        


        # Send Order



        while True:
            self.ib.sleep(1)
            print("loop")



    

 



 


"""
for bars in ib.realtimeBars():
    ib.cancelRealTimeBars(bars)
"""



app = IbApp()