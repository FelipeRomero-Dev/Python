lista_alunos = ["mauricio","felipe"]
condicao = "sim" 
while condicao =="sim":
        
    nome = input("informe seu nome: ")

    if nome=="mauricio":
        print ("usuario logado ")

        nota1 = 8
        nota2 = 7
        nota3 = 6
        
        while True:

            nota1mauricio = int(input("favor inserir nota 1: "))
            if nota1mauricio == nota1:
                print ("nota 1 ok")
                break
            else :
                print("favor inserir nota correta")
                
        while True:
            
            nota2mauricio = int(input("favor inserir nota 2: "))    
            if nota2mauricio ==nota2:
                print ("nota2 ok")
                break
            else :
                    print("favor inserir nota correta")    
        while True:
            
            nota3mauricio = int(input("favor inserir nota 3: "))
            if nota3mauricio ==nota3:
                print ("nota3 ok")
                break
            else :
                    print("favor inserir nota correta")
            
        media = (nota1+nota2+nota3) /3
        print("media : ",media)
        
    elif nome=="felipe":
        print (" usuario logado ")

        nota1 = 10
        nota2 = 9
        nota3 = 5
        
        while True: 
            nota1felipe = int(input("favor inserir a nota 1: "))
            if nota1felipe ==nota1:
                print ("nota 1 ok")
                break 
            else :
                print("favor inserir nota correta")

        while True:         
            nota2felipe = int(input("favor inserir nota 2: "))
            if nota2felipe ==nota2:
                print ("nota 2 ok")
                break
            else :
                print("favor inserir nota correta")
                
        while True:     
            nota3felipe = int(input("favor inserir nota 3: "))
            if nota3felipe ==nota3:
                print ("nota 3 ok")
                break
            else :
                print("favor inserir nota correta")
                
        media = (nota1+nota2+nota3) /3
        print("media : ",media)

    else:
        print("acesso negado")
        condicao = str(input("deseja continuar ? sim ou não "))
                




    
            

    
