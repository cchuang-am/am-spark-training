

CHOCO = ["七七乳加", "義美葡萄乾巧克力", "小七小雷神"]
TOTAL = 30
PRICE = {
    "七七乳加": 25,
    "義美葡萄乾巧克力": 30,
    "小七小雷神": 35
}

ITEMS = TOTAL // len(CHOCO)
sum = 0

def count_price(price, item_count):
    return price * item_count

for choco in CHOCO:
    price = PRICE[choco]
    sum = sum + count_price(price, ITEMS)


print("總花費: ", sum)
