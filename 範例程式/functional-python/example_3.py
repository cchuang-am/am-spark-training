

CHOCO = ["七七乳加", "義美葡萄乾巧克力", "小七小雷神"]
TOTAL = 30
PRICE = {
    "七七乳加": 25,
    "義美葡萄乾巧克力": 30,
    "小七小雷神": 35
}

ITEMS = TOTAL // len(CHOCO)

def count_price(price, item_count):
    return item_count * price

def sum_price(choco_price_list):
    sum = 0

    for price in choco_price_list:
        sum = sum + price

    return sum


choco_price_list = []
for choco in CHOCO:
    price = PRICE[choco]
    choco_price_list.append(count_price(price, ITEMS))

sum = sum_price(choco_price_list)

print("總花費: ", sum)
