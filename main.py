def JahJaEiKüsimus(question):
  JahJaEiVastus = input(question).upper()
  if JahJaEiVastus == "JAH" or JahJaEiVastus == "EI":
     return JahJaEiVastus
  else:
     return JahJaEiKüsimus(question)
height  = float(input("Pange oma pikkus:")) 
cm = (height) 
vastus = JahJaEiKüsimus("Kas teil on pilet?")
vastus1 = JahJaEiKüsimus("Kas teil on kaelakaart?")
if height <=170:
    print("Kahjuks te ei pääse kosmoselennule.")
elif vastus1 == "JAH":
  print("Palju õnne, pääsete kosmoselennule.") 
elif vastus == "JAH":
    print("Palju õnne, pääsete kosmoselennule.")
else:
    print("Kahjuks te ei pääse kosmoselennule.")        