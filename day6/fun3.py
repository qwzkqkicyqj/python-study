def dis_price(price, discount):
    return price - (price * discount / 100)

#a상품: 10000원 / 할인율: 10%
price_a=dis_price(10000, 10)
print(f"a상품의 할인된 가격: {price_a}")

#a상품: 50000원 / 할인율: 20%
price_b=dis_price(50000, 20)
print(f"b상품의 할인된 가격: {price_b}")