shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(id(shopping_list))
print(id(another_list))

print(another_list)

a = b = c = d = e = f = another_list
print(f)
b.append("cream")
print(c)
