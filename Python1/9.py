str= "Wiesz dlaczego nigdy się nie śpieszę i jestem spokojny? Lubie auta oraz samochody."
black_list=[" nigdy "," się "," oraz ", " dlaczego "," i "]
for word in black_list:
    str=str.replace(word," ")


