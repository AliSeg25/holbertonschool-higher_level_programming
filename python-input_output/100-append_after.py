def modify_list(lst):
    print("Avant modification :", lst)
    lst.append(1)
    print("Après modification :", lst)

def modify_string(string):
    print("Avant modification :", string)
    string = string + " modifié"
    print("Après modification :", string)

my_list = [2, 3, 4]
modify_list(my_list)
print("Liste après la fonction :", my_list)

my_string = "Chaine de caractères"
modify_string(my_string)
print("Chaine de caractères après la fonction :", my_string)

#Objet Mutable 
#Avant modification : [2, 3, 4]
#Après modification : [2, 3, 4, 1]
#Liste après la fonction : [2, 3, 4, 1]

#Objet Immutable
#Avant modification : Chaine de caractères
#Après modification : Chaine de caractères modifié
#Chaine de caractères après la fonction : Chaine de caractères