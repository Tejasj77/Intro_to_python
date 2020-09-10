# Unicode values of symbols
symbols = '$%&@#'
x = [ord(symbol) for symbol in symbols]
#print(x)

#Code to prepare a list of symbols whose Unicode value is greater than 50
#2 ways
# 1. List Comprehension way
symbols = '%^*@#?>:}{'
list_final = [ord(symbol) for symbol in symbols if ord(symbol)>50]
print(list_final)

# 2. Map-Filter way
final_list = list(filter(lambda c:c>50,map(ord,symbols)))
print(final_list)