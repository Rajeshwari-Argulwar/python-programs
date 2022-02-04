my_list=[12,45,26,47,48,52,19]
result =list(filter(lambda X: (X%13==0),my_list))
print(result)