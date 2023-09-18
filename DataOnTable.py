from tabulate import tabulate

data = [['name', 'age', 'city'],
       ['Alice', 24, 'Toronto'],
       ['Bob', 19, 'Waterloo'],
       ['Charlie', 28, 'Toronto'],
       ['Dave', 32, 'Waterloo'],]

table = tabulate(data,headers='firstrow',tablefmt='fancy_gridpppp')
print(table)