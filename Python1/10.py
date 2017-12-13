black_dir=dict()
black_dir[" i "]=" oraz "
black_dir[" oraz "]=" i "
black_dir[" dlaczego "]=" czemu "
black_dir[" nigdy "]=" prawie nigdy "

str= "Wiesz dlaczego nigdy się nie śpieszę i jestem spokojny? Lubie auta oraz samochody."
for key,value in black_dir.iteritems():
    str=str.replace(key,value)


