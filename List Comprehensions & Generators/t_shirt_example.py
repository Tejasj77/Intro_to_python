# Printing different types of t-shirts using list comprehensions and generator expressions
colors = ['black','blue','red']
sizes = ['L','XL','XXL']

# 1. List Comprehension Way
# final = [f'{color} {size}' for color in colors for size in sizes]
final = [(color,size) for color in colors for size in sizes]
#print(final)

# 2. Generator Expression Way

for gen_final in ((color,size) for color in colors for size in sizes):
    print(gen_final)
gen = list(((color,size) for color in colors for size in sizes))
print(gen)
