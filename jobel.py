#declaration de variable 
#Exemple de différents type de variable //: int:a=12 ; double/float :b=2,5; bool c=True or False ;String d="Bonjour" ;char  e="d"
#exemple de cas d'utilisation : je m'appelle jobel et j'ai 12 ans


"""
1ere methode: methode statique
a="jobel"
b=12
print("je m'appelle",a," et j'ai",b,"ans")  
print(f"je m'appelle {a} et j'ai {b} ans")
"""
"""
#2eme methode : methode dynamique
a=input("veuiller saisir votre prénom :")
b=int(input("veuiller saisir votre age :"))
print("je m'appelle",a," et j'ai",b,"ans")
"""
#3eme methode : boucle for
""""
for i in range(10):
    print("je m'appelle jobel et j'ai 12 ans")  
"""
#4eme methode : boucle while
"""
i=0 
while i<10:
    print("je m'appelle jobel et j'ai 12 ans")
    i+=1/i=i+1 : incrementation
    """
#5eme methode : structure conditionnelle if/else
"""
i=0
if i<10 :
   print("je m'appelle jobel et j'ai 12 ans")

elif i==10 :
   print("je m'appelle jobel ")
else:
   print("je ne m'appelle pas jobel")   
"""
#6eme methode : fonction
"""
def sum(a,b):
   return a+b
print(sum(5,6))  #appel de la fonction avec 2 argument
"""
#*********************************
def sum(a,b):
   return a+b
a=int(input("veuiller saisir le premier nombre :"))
b=int(input("veuiller saisir le deuxième nombre :"))
print(sum(a,b))

# Git/Github