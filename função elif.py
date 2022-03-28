temperatura = (int(input("Temperatura: ")))
if temperatura<10:
   print("congelando")
elif 11 <= temperatura <=20:    
    print("frio")
elif 21 <= temperatura <=25:    
    print ("normal")
elif 26 <= temperatura <=35:    
    print ("quente")
else:
    print("muito quente")
    
