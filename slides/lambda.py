data = [[345, 4.5, 4, 40.95], [987, 6.7, 5, 56.80],[772, 8.2, 3, 32.95], 
[881, 10.2, 3, 24.99]]
min_product = 100.0
my_list = list(map(lambda x: x if x[1]>min_product else (x[0], x[1]+10.0), 
               map(lambda x: (x[0], x[2]*x[3]), data)))
print(my_list)
