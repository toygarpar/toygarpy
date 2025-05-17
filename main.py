import module

result = module.num

print(result)



result2 = module.nums

print(result2)



result3 = module.products

print(result3)
print(module.products["product_name"])
print(module.products["product_price"])
print(module.products["product_colors"])
print(module.toplam(1,2))


import module as m

print(m.nums)



from module import num, nums, products

x = num
print(num)

y = nums
print(y)

z = products
print(products)




from module import *

print(toplam(5, 7))
