"""
Author: Eroshenkov Artem
Date: 23.03.2018
"""
from coincap import CoinCap
from binance import Binance
from time import gmtime, strftime

def main():
    my_instance = CoinCap()
    instance_binance = Binance()
    timestamp = strftime("%Y_%m_%d %H_%M_%S", gmtime())
    
    filecoincap = open("coincapio_front_" + timestamp + ".txt", "w")
    
    front_list = my_instance.get_front()
    for front_item in front_list:
        for front_item_detail in front_item:
            filecoincap.write(front_item_detail + ": " + str(front_item.get(front_item_detail)) + "\n") 
    
    filecoincap.close()

    filebinance = open("binance_klines_" + timestamp + ".txt", "w")
    
    kline = instance_binance.get_klines('BTCUSDT', '1m')
    
    filebinance.write(str(kline)) 
    
    filebinance.close()

if __name__ == "__main__":
    main()
