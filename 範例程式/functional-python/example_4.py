

CHOCO = ["七七乳加", "義美葡萄乾巧克力", "小七小雷神"]
TOTAL = 30
PRICE = {
    "七七乳加": 25,
    "義美葡萄乾巧克力": 30,
    "小七小雷神": 35
}

MAX_PRICE = 30
# ITEMS = TOTAL // len(CHOCO)

def count_price(price, item_count):
    return price * item_count

def sum_price(choco_price_list):
    sum = 0

    for price in choco_price_list:
        sum = sum + price

    return sum

cheap_choco_list = []
for choco in CHOCO:
    if PRICE[choco] <= MAX_PRICE:
        cheap_choco_list.append(choco)

choco_price_list = []
for choco in cheap_choco_list:
    price = PRICE[choco]
    choco_price_list.append(count_price(price, TOTAL //  len(cheap_choco_list)))

sum = sum_price(choco_price_list)

print("總花費: ", sum)
