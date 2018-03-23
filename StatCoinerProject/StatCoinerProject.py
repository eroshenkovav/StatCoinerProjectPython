"""
Author: Eroshenkov Artem
Date: 23.03.2018
"""
from coincap import CoinCap
from time import gmtime, strftime

def main():
    my_instance = CoinCap()
    timestamp = strftime("%Y_%m_%d %H_%M_%S", gmtime())
    
    file = open("coincapio_front_" + timestamp + ".txt", "w")
    
    front_list = my_instance.get_front()
    for front_item in front_list:
        for front_item_detail in front_item:
            file.write(front_item_detail + ": " + str(front_item.get(front_item_detail)) + "\n") 
    
    file.close()

if __name__ == "__main__":
    main()
