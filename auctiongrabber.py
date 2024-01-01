"""
Author: Mike AND Vincent
Date: 14/01/2023
"""
#V1.0

import requests
import time

###################################################
stat = ["Skin", "Dye", "[Lvl","Mixin","Drill Engine","'Burning Kuudra Core","Plasma","Coffin","◆ Smokey Rune I","Surfboard","Ruby-polished Drill Engine"]
purse= 54276615
minprofit=1000000
###################################################


# parts to remove
STARS_and_other = ['✪', '✪✪', '✪✪✪', '✪✪✪✪', '✪✪✪✪✪', '✪✪✪✪✪➊', '✪✪✪✪✪➋', '✪✪✪✪✪➌', '✪✪✪✪✪➍', '✪✪✪✪✪➎', '✪', '✪✪', '✪✪✪', '✪✪✪✪',
                   '✪✪✪✪✪', '✪✪✪✪✪➊', '✪✪✪✪✪➋', '✪✪✪✪✪➌', '✪✪✪✪✪➍', '✪✪✪✪✪➎', '✿', '✦', '⚚', '[§7', '§f[', '§a[', '§9[', '§5[', '§6[',
                   'Withered', 'Fabled', 'Gilded', 'Warped', 'Jaded', 'Loving', 'Renowned', 'Giant', 'Ancient', 'Spiritual', 'Submerged', 'Giant',
                   'Auspicious', 'Glistening', 'Skin', 'Gentle', 'Odd', 'Fast', 'Fair', 'Epic', 'Sharp', 'Heroic', 'Spicy', 'Legendary', 'Dirty',
                   'Suspicious', 'Bulky', 'Deadly', 'Fine', 'Grand', 'Hasty', 'Neat', 'Rapid', 'Unreal', 'Awkward', 'Rich', 'Headstrong', 'Precise',
                   'Clean', 'Fierce', 'Heavy', 'Light', 'Mythic', 'Pure', 'Smart', 'Titanic', 'Wise', 'Perfect', 'Necrotic', 'Spiked', 'Cubic', 'Hyper',
                   'Reinforced', 'Ridiculous', 'Empowered', 'Very', 'Highly', 'Extremely', 'NotSo', 'Thicc', 'Absolutely', 'EvenMore', 'Strong', 'Shiny',
                   'Stiff', 'Lucky', "Jerry's", 'Stellar', 'Heated', 'Ambered', 'Fruitful', 'Magnetic', 'Fleet', 'Mithraic', 'Auspicious', 'Refined', 'Moil',
                   'Blessed', 'Toil', 'Bountiful', 'Sweet', 'Silky', 'Bloody', 'Shaded', 'Bizarre', 'Itchy', 'Ominous', 'Pleasant', 'Pretty', 'Simple', 'Strange',
                   'Vivid', 'Godly', 'Demonic', 'Forceful', 'Hurtful', 'Keen', 'Unpleasant', 'Zealous', 'Double-Bit', "Lumberjack's", 'Great', 'Rugged', 'Lush',
                   'GreenThumb', "Peasant's", 'Robust', 'Zooming', 'Unyielding', "Prospector's", 'Excellent', 'Sturdy', 'Fortunate', 'Strengthened', 'Fortified',
                   'Waxed', 'Glistening', 'Treacherous', 'Salty', 'Candied', 'Reforged', "Pitchin'"]


def Auction_housse(stats: list, profit_recherche: int,purse: int):
    """
    Print les flips les plus intéressant ayant 1m de profit
    :param stats: chose que l'on veux renlever
    :param profit_recherche: profit que l'on veux se faire
    :return: None
    """
    # Prend toute les enchères possible
    buffer=""
    liste_auctions = []
    for i in range (80):
        try:
            data = requests.get (f"https://api.hypixel.net/skyblock/auctions?page={i}").json ( )
            liste_auctions += [data ["auctions"]]
        except:
            break

    # simplement pour annoncer le depart de la recherche et que toute les auctions ont ete recuperer
    print(" ")
    print("__________________Starting__________________")
    print (" ")

    itemold = []


    # Prends les auctions recents
    # gets in json
    data = requests.get("https://api.hypixel.net/skyblock/auctions?page=0").json()
    # gets the auctions
    auctions = data["auctions"]
    items = []
    # adds the auction that is a bin et pas un pet
    for auction in auctions:
        try:
            for word in STARS_and_other:                              #enleve les stars
                auction["item_name"] = auction["item_name"].replace(str(word), "")
            if auction["bin"]:
                items.append([auction["item_name"], auction["starting_bid"], auction["uuid"]])
        except KeyError:
            pass
    # sorts by the prices, use items.sort(key=lambda x:x[1], reverse=True) for highest prices first
    items.sort(key=lambda x:x[1])

    # Print seulement les flip intérressant
    copy = 0
    comptage_item_remove = 0
    print("________________ALERT_________________")           
    for j in items:
        average_price = search_lowest_bin_average(j[0], j[2], liste_auctions)
        profit = (average_price//100)*2+average_price - int(j[1])
        if profit > profit_recherche:       #trouve le flip
            # A partir de la tri les items de façon qu'il n'y a plus que des items clean
            var_trie = False
            for i in stats:
                for word in j[0].split(" "):
                    if i == word:
                        var_trie = True
                        comptage_item_remove += 1
                        break
            # Renvoie l'item qui est clean
            if var_trie != True:
                profit = str(profit)[::-1]
                profit2 = ""
                for i in range(len(profit)):
                    if i%3 == 0:
                        profit2 += " " + profit[i]
                    else:
                        profit2 += profit[i]
                profit2 = profit2[::-1]
                if j[1]<purse:
                    buffer+="SUIVANT ::" + str(j) + ", Profit: " + profit2 + "\r\n"
                    copy=(average_price//100)*2+average_price - int(j[1])
    return(buffer)

 


def search_lowest_bin_average(item_name: str, item_uuid: str, liste_auction: list):
    """
    Renvoie le prix moyen d'un item
    :param item_name: Nom de l'item  que l'on veux flip, type str
    :param item_uuid: uuid de l'item  que l'on veux flip, type str
    :param liste_auction: liste recent de tou les auctions, type list
    :return: Renvoie le lowest bin average de l'item
    """
    prices = []
    for auction1 in liste_auction:
        for auction in auction1:
            try:
                if auction ["bin"] and auction["item_name"] == item_name and auction["uuid"] != item_uuid :
                    prices.append (int(auction ["starting_bid"]))
            except KeyError:
                pass

    if len(prices) < 10:
        return -999999999999999999999
    else:
        prices.sort ()
        average_bin = 0
        for i in range(5):
            average_bin += prices[i]
        return average_bin//5

