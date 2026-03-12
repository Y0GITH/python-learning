names = ['bruce', 'clark', 'arther']
heros = ['batman(H)', 'superman(H)', 'joker(V)']

# I want a dict {name:hero} for each name, hero in zip(name,heros)

# my_dect = {}
# for name,hero in zip(names,heros):
#     my_dect[name.title()]=hero.replace('man','-Man').title()
# print(my_dect)    

my_dect_h = {name.title():hero.replace('man','-Man').title() for name,hero in zip(names,heros) if hero.endswith('(H)')}
my_dect_v = {name.title():hero.replace('man','-Man').title() for name,hero in zip(names,heros) if hero.endswith('(V)')}
print(my_dect_h)    
print(my_dect_v)    
