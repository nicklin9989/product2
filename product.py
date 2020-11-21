products = []
while  True:
    name = input('prease enter product name: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    products.append([name,price])
print(products)

print(products[0][0])