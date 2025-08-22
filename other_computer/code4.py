import pandas as pd 

sales = pd.Series([781, 650, 705, 406, 580, 450, 550, 640], 
                  index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
print("1. Sales Series")
print(sales)

print('\n2. Lenght of Sales')
print(sales)

print("\n3. Sales of Second Team Index")
print(sales.iloc[1])

print("\n4. Sales of Team F")
print(sales.loc['F'], sales['F'])

print("\n5. Sales of 3rd to Fifth teams based on index")
print(sales.iloc[2:5]) 

print('\n6. Sales of Team A, B, D')
print(sales[['A', 'B', 'D']])

print('\n7. Team with (sales < 500) | (sales > 700) ')
print(sales[(sales > 500) | (sales < 700)])

print('\n8. Name and Score > Team B')
print(sales[sales > sales['B']])

print('\n9. Sales less than 600')
print(sales[sales < 600 ].index)

print('\n10. Teams < 600 increased 20%: ')
inc20 = (sales[sales < 600]* 1.2).round(0).astype(int)
print(inc20) 

print('\n11. Mean, Sum, std')
print('Mean: ', sales.mean(), 'Sum: ', sales.sum(), 'STD: ', sales.std())

print('\n12. After Changing Value ')
sales_mod = sales.copy()
sales_mod.loc[['A','C']] = [810, 820]
print(sales_mod[['A', 'C']])

print('\n 13. After editing J team')
sales_mod.loc['J'] = 400
print(sales_mod)

print('\n14. delete team j')
sales_mod = sales_mod.drop('J')
print(sales_mod)

print('\n15. Compare sales vs sales2')
sales2 = sales.copy()
sales2 = sales + 500
print('Sales', sales)
print('Sales2', sales2)