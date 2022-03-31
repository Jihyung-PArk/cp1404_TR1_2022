 
 products = [["phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
 # on_sale_products = []
 #
 # for i in range(0, len(products)):
 #     if products[i][2] == True:
 #         on_sale_products.append(products[i])
 #
 # print(on_sale_products)
 
 on_sale_product = [product for product in products if product[2]]
 
 print(on_sale_product)




    
p = Person("Joanne", 20)
print("My name is", p.name)
pring("my age is", p.age)






