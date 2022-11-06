from inputtreeclass import InputTree

c = [
  "Agua",
  "Agua 0",
  "Agua 1",
  "Agua 2",
  "Agua 3",
  "Agua 4",
  "Agua 5",
  "Agua 6",
  "Agua 7",
  "Banana",
  "Alcornoque",
  "Alcornoque",
  "Alcornoque",
  "Alcornoque A",
  "Alcornoque B",
  "             Alcornoque C      ",
  "Alcornoque D",
  "Alcornoque E",
  "Alcornoque",
  "Batidora",
  "Docena",
  "Dulce",
  "Ejercicio",
  "Esmero",
  "Frenadol",
  "Gaita",
  "Carcabuey",
  "3j3jj2",
  "mmemrwe",
  "88j23j4",

]

a = InputTree(tree=3).input(c)

print("Choice: %s" % a)
