import json

#Elementos={}
#Elementos['nombre']=[]
#Elementos['nombre']=[{'estrategia':'self.estrategia','localizador':'self.localizador'}]

#with open('Elementos.json', 'w') as file:
#    json.dump(Elementos, file, indent=4)

with open('Elementos.JSON') as file:
    Elementos = json.load(file)
Elementos[nombre] = [{'estrategia': self.estrategia, 'localizador': self.localizador}]
with open('Elementos.json', 'w') as file:
    json.dump(Elementos, file, indent=4)
file.close()
