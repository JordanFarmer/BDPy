number_list = [3, 1, 5, 29, 37, 46, 8, 20, 42, 100]

over40 = sorted(i for i in number_list if i > 40)
print over40

under30 = sorted((i for i in number_list if i < 30), reverse=True)
print under30