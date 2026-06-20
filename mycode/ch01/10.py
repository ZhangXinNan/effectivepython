
def make_lemonade(count):
    print(f"make lemonade {count}")

def out_of_stock():
    print("out of stock")

fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5,
}

count = fresh_fruit.get('lemon', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()


