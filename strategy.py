from fastquant import CustomStrategy, BaseStrategy
from fastquant.indicators import MACD, CrossOver 
from fastquant.indicators.custom import CustomIndicator
import backtrader as bt


class MAMAStrategy(BaseStrategy):
    
    params = (  
        ("buy_prop", 1),
        ("sell_prop", 1),
        ("commission", 0),
        ("stop_loss", 0),
        ("stop_trail", 0),
        ("take_profit", 0),
        ("sb" , 30),
        ("ss", 70)
    )

    def __init__(self):
        # Initialize global variables
        super().__init__()
        
        self.Stochastic = bt.indicators.Stochastic(self.data)
        self.EMA = bt.indicators.EMA(self.data.close, period=14)
        self.sb = self.params.sb
        self.ss = self.params.ss
        

    # Buy when the custom indicator is below the lower limit, and sell when it's above the upper limit
    def buy_signal(self):
        sto_buy =  self.Stochastic[0] < self.sb   # Close is above ALMA
        ema_buy = self.EMA[0] > self.data.close       # MACD crosses signal line upward
        
        
        return sto_buy and ema_buy 
    def sell_signal(self):
        sto_sell = self.ss < self.Stochastic[0]
        ema_sell = self.EMA[0] < self.data.close

        return sto_sell and ema_sell 
