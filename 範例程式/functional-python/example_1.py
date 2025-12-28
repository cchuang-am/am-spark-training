

CHOCO = ["七七乳加", "義美葡萄乾巧克力", "小七小雷神"]
TOTAL = 30
PRICE = {
    "七七乳加": 25,
    "義美葡萄乾巧克力": 30,
    "小七小雷神": 35
}

ITEMS = TOTAL // len(CHOCO)
sum = 0

for choco in CHOCO:
    for i in range(ITEMS):
        sum = sum + PRICE[choco]


print("總花費: ", sum)