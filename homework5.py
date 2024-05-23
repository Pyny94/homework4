#immutable_var = 1, 2, True, "Vladislav"
#print(immutable_var)
#immutable_var[0] = 100
#rint(immutable_var) - нельзя заменить значение переменной в кортеже, если только в кортеже не будет [], там значение можно изменить.
mutable_list= [1, 2, True, "Vladislav"]
mutable_list[3] = 'Egor'
mutable_list[0] = 5
mutable_list[1] = False
print(mutable_list)