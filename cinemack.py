filme1=[[0]*50,[0]*50]
filme2=[[0]*40,[0]*40]
filme3=[[0]*30,[0]*30]

avaliacao=[0,0,0] #avaliaçao = [filme1,filme2,filme3]
qtd_avaliacao=[0,0,0]

filme1_ingressos = [[0,0,0],[0,0,0]] # => meia/1=inteira/2=vip
filme2_ingressos = [[0,0,0],[0,0,0]]
filme3_ingressos = [[0,0,0],[0,0,0]]

def menu():
    opc = 0
    while True:
        print("\nMENU PRINCIPAL")
        print("Digite:")
        print("1 - Comprar ingressos para Filme 1 - Sessão 1")
        print("2 - Comprar ingressos para Filme 1 - Sessão 2")
        print("3 - Comprar ingressos para Filme 2 - Sessão 1")
        print("4 - Comprar ingressos para Filme 2 - Sessão 2")
        print("5 - Comprar ingressos para Filme 3 - Sessão 1")
        print("6 - Comprar ingressos para Filme 3 - Sessão 2")
        print("7 - Avaliar um filme")
        print("8 - Encerrar o dia e exibir o relatório")
        print("9 - cancelar ingresso")
        
        opc = int(input("Digite o número inteiro correspondente: "))
        if opc == 8:
            relatorio()
            break
        else:
            match opc:
                case 1:
                    disp = assentos_disponiveis(1,1)
                    print(f"\nFilme 1 - sessão 1: {disp} lugares disponíveis\n")
                    if disp == 0:
                        print('\nSessão Lotada!\n')
                    else:
                        menu_compra_ingresso(1,1)
                case 2:
                    disp = assentos_disponiveis(1,2)
                    print(f"\nFilme 1 - sessão 2: {disp} lugares disponíveis\n")
                    if disp == 0:
                        print('\nSessão Lotada!\n')
                    else:
                        menu_compra_ingresso(1,2)
                case 3:
                    disp = assentos_disponiveis(2,1)
                    print(f"\nFilme 2 - sessão 1: {disp} lugares disponíveis\n")
                    if disp == 0:
                        print('\nSessão Lotada!\n')
                    else:
                        menu_compra_ingresso(2,1)
                case 4:
                    disp = assentos_disponiveis(2,2)
                    print(f"\nFilme 2 - sessão 2: {disp} lugares disponíveis\n")
                    if disp == 0:
                        print('\nSessão Lotada!\n')
                    else:
                        menu_compra_ingresso(2,2)
                case 5:
                    disp = assentos_disponiveis(3,1)
                    print(f"\nFilme 3 - sessão 1: {disp} lugares disponíveis\n")
                    if disp == 0:
                        print('\nSessão Lotada!\n')
                    else:
                        menu_compra_ingresso(3,1)
                case 6:
                    disp = assentos_disponiveis(3,2)
                    print(f"\nFilme 3 - sessão 2: {disp} lugares disponíveis\n")
                    if disp == 0:
                        print('\nSessão Lotada!\n')
                    else:
                        menu_compra_ingresso(3,2)
                case 7:
                    while True:
                        print("\nDigite...")
                        print("1 - Filme 1")
                        print("2 - Filme 2")
                        print("3 - Filme 3")
                        filme = int(input("Digite o número correspondente ao filme: "))
                        if filme<1 or filme>3:
                            print("Número não correspondente!")
                            continue
                        else:
                            while True:
                                avaliacao = int(input("De 0 a 5 estrelas, com quantas estrelas você avalia esse filme? "))
                                if avaliacao<0 or avaliacao>5:
                                    print("Número de estrelas inválido!")
                                    continue
                                else:
                                    avaliar(filme,avaliacao)
                                    break
                            
                            break
                case 9:
                    menu_cancelar_ingressos()
                       
                case _:
                    print("Opção inválida")
                    continue

def avaliar(filme,estrelas):
    avaliacao[filme-1]+=estrelas
    qtd_avaliacao[filme-1]+=1
    
    print("\nAvaliação registrada!")
    

def cancelar_ingressos(qtd_ingressos,tipo,filme,sessao):
    i=0
    j=0
    if filme == 1:
        while j<qtd_ingressos:
            if filme1[sessao-1][i]==1:
                filme1[sessao-1][i] = 0
                j+=1
            i+=1
        for k in range(qtd_ingressos):
                filme1_ingressos[sessao-1][tipo-1] -=1
                
    elif filme == 2:
        while j<qtd_ingressos:
            if filme2[sessao-1][i]==1:
                filme2[sessao-1][i] = 0
                j+=1
            i+=1
        for k in range(qtd_ingressos):
                filme2_ingressos[sessao-1][tipo-1] -=1
    else:
        while j<qtd_ingressos:
            if filme3[sessao-1][i]==1:
                filme3[sessao-1][i] = 0
                j+=1
            i+=1
        for k in range(qtd_ingressos):
                filme3_ingressos[sessao-1][tipo-1] -=1
    
    print('\nCancelamento de ingresso realizado!')

def menu_cancelar_ingressos():
    print("\nVocê deseja cancelar...")
    print("1 - Ingressos para Filme 1 - Sessão 1")
    print("2 - Ingressos para Filme 1 - Sessão 2")
    print("3 - Ingressos para Filme 2 - Sessão 1")
    print("4 - Ingressos para Filme 2 - Sessão 2")
    print("5 - Ingressos para Filme 3 - Sessão 1")
    print("6 - Ingressos para Filme 3 - Sessão 2")
    print("7 - Voltar")
    while True:
        num = int(input("Digite o valor correspondente: "))
        if num <1 or num>7:
            print("Valor não correspondente!")
            continue
        else:
            if num == 7:
                menu()
                break
            else:
                print("DIGITE QUAL TIPO DE INGRESSO DESEJA CANCELAR:")
                print("1 - meia")
                print("2 - inteira")
                print("3 - vip")
                while True:
                    tipo = int(input("Insira o número correspondente: "))
                    if tipo<1 or tipo>3:
                        print("Número não correspondente!")
                        continue
                    else:
                        while True:
                            qtd_ingressos = int(input("Digite quantos ingressos deseja cancelar ou 0 para voltar: "))
                            if qtd_ingressos ==0:
                                break                            
                            match num:
                                case 1:
                                    cancelavel = qtd_ingressos<=filme1_ingressos[0][tipo-1]
                                    if cancelavel == False:
                                        print("Não existem tantos ingressos desse tipo reservados!")
                                        continue
                                    cancelar_ingressos(qtd_ingressos,tipo,1,1)
                                case 2:
                                    cancelavel = qtd_ingressos<=filme1_ingressos[1][tipo-1]
                                    if cancelavel == False:
                                        print("Não existem tantos ingressos desse tipo reservados!")
                                        continue
                                    cancelar_ingressos(qtd_ingressos,tipo,1,2)

                                case 3:
                                    cancelavel = qtd_ingressos<=filme2_ingressos[0][tipo-1]
                                    if cancelavel == False:
                                        print("Não existem tantos ingressos desse tipo reservados!")
                                        continue
                                    cancelar_ingressos(qtd_ingressos,tipo,2,1)

                                case 4:
                                    cancelavel = qtd_ingressos<=filme2_ingressos[1][tipo-1]
                                    if cancelavel == False:
                                        print("Não existem tantos ingressos desse tipo reservados!")
                                        continue
                                    cancelar_ingressos(qtd_ingressos,tipo,2,2)

                                case 5:
                                    cancelavel = qtd_ingressos<=filme3_ingressos[0][tipo-1]
                                    if cancelavel == False:
                                        print("Não existem tantos ingressos desse tipo reservados!")
                                        continue
                                    cancelar_ingressos(qtd_ingressos,tipo,3,1)

                                case 6:
                                    cancelavel = qtd_ingressos<=filme3_ingressos[1][tipo-1]
                                    if cancelavel == False:
                                        print("Não existem tantos ingressos desse tipo reservados!")
                                        continue
                                    cancelar_ingressos(qtd_ingressos,tipo,3,2)

                                case _:
                                    print("Opção inválida")
                                    continue
                            break
                    break
        break
    
def assentos_disponiveis(filme,sessao):
    disponivel = 0
    if filme ==1:
        for i in range(len(filme1[sessao-1])):
            if filme1[sessao-1][i]==0:
                disponivel +=1
                
    elif filme ==2:
        for i in range(len(filme2[sessao-1])):
            if filme2[sessao-1][i]==0:
                disponivel +=1
    else:      
        for i in range(len(filme3[sessao-1])):
            if filme3[sessao-1][i]==0:
                disponivel +=1
        
    return disponivel

def menu_compra_ingresso(filme,sessao):
    print("DIGITE QUAL TIPO DE INGRESSO DESEJA COMPRAR:")
    print("1 - meia")
    print("2 - inteira")
    print("3 - vip")
    print("4 - voltar")

    while True:
        tipo = int(input("Digite o valor correspondente à opção: "))
        
        if tipo < 1 or tipo > 4:
            print("Valor não correspondente!")
            continue
        elif tipo == 4:
            menu()
            break
        else:
            while True:
                qtd_ingressos = int(input("Quantos ingressos deseja comprar? "))
                if qtd_ingressos < 1:
                    print("O valor deve ser positivo e não nulo!")
                    continue
                else:
                    if qtd_ingressos>assentos_disponiveis(filme,sessao):
                        print("Quantidade excedente de ingressos!")
                        continue
                    else:
                        comprar_ingresso(qtd_ingressos,tipo,filme,sessao)
                        break
                            
                        
            break
                

def comprar_ingresso(qtd_ingressos,tipo,filme,sessao):
    i=0
    j=0
    if filme == 1:
        while j<qtd_ingressos:
            if filme1[sessao-1][i]==0:
                filme1[sessao-1][i] = 1
                j+=1
            i+=1
        for k in range(qtd_ingressos):
                filme1_ingressos[sessao-1][tipo-1] +=1
                
    elif filme == 2:
        while j<qtd_ingressos:
            if filme2[sessao-1][i]==0:
                filme2[sessao-1][i] = 1
                j+=1
            i+=1
        for k in range(qtd_ingressos):
                filme2_ingressos[sessao-1][tipo-1] +=1
    elif filme ==3:
        while j<qtd_ingressos:
            if filme3[sessao-1][i]==0:
                filme3[sessao-1][i] = 1
                j+=1
            i+=1
        for k in range(qtd_ingressos):
                filme3_ingressos[sessao-1][tipo-1] +=1

    print('\nCompra realizada!')

def relatorio():
    print("============================| RELATÓRIO FINAL |============================")

    f1s1_int = filme1_ingressos[0][1]*20
    f1s1_meia = filme1_ingressos[0][0]*20*0.5
    f1s1_vip = filme1_ingressos[0][2]*20*1.5
    
    print("Filme 1 - Sessão 1")
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira: {filme1_ingressos[0][1]}")
    print(f"Meia: {filme1_ingressos[0][0]}")
    print(f"Vip: {filme1_ingressos[0][2]}")
    
    print("Receita por tipo:")
    print(f"Inteira: R$ {f1s1_int:.2f}")
    print(f"Meia: R$ {f1s1_meia:.2f}")
    print(f"Vip: R$ {f1s1_vip:.2f}")

    print("===================================================")
    
    #----------------

    f1s2_int = filme1_ingressos[1][1]*20
    f1s2_meia = filme1_ingressos[1][0]*20*0.5
    f1s2_vip = filme1_ingressos[1][2]*20*1.5
    
    print("Filme 1 - Sessão 2")
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira: {filme1_ingressos[1][1]}")
    print(f"Meia: {filme1_ingressos[1][0]}")
    print(f"Vip: {filme1_ingressos[1][2]}")

    print("Receita por tipo:")
    print(f"Inteira: R$ {f1s2_int:.2f}")
    print(f"Meia: R$ {f1s2_meia:.2f}")
    print(f"Vip: R$ {f1s2_vip:.2f}")

    print("===================================================")

    #----------------

    f2s1_int = filme2_ingressos[0][1]*15
    f2s1_meia = filme2_ingressos[0][0]*15*0.5
    f2s1_vip = filme2_ingressos[0][2]*15*1.5

    print("Filme 2 - Sessão 1")
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira: {filme2_ingressos[0][1]}")
    print(f"Meia: {filme2_ingressos[0][0]}")
    print(f"Vip: {filme2_ingressos[0][2]}")

    print("Receita por tipo:")
    print(f"Inteira: R$ {f2s1_int:.2f}")
    print(f"Meia: R$ {f2s1_meia:.2f}")
    print(f"Vip: R$ {f2s1_vip:.2f}")

    print("===================================================")

    #----------------

    f2s2_int = filme2_ingressos[1][1]*15
    f2s2_meia = filme2_ingressos[1][0]*15*0.5
    f2s2_vip = filme2_ingressos[1][2]*15*1.5

    print("Filme 2 - Sessão 2")
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira: {filme2_ingressos[1][1]}")
    print(f"Meia: {filme2_ingressos[1][0]}")
    print(f"Vip: {filme2_ingressos[1][2]}")

    print("Receita por tipo:")
    print(f"Inteira: R$ {f2s2_int:.2f}")
    print(f"Meia: R$ {f2s2_meia:.2f}")
    print(f"Vip: R$ {f2s2_vip:.2f}")

    print("===================================================")

    #----------------

    f3s1_int = filme3_ingressos[0][1]*10
    f3s1_meia = filme3_ingressos[0][0]*10*0.5
    f3s1_vip = filme3_ingressos[0][2]*10*1.5

    print("Filme 3 - Sessão 1")
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira: {filme3_ingressos[0][1]}")
    print(f"Meia: {filme3_ingressos[0][0]}")
    print(f"Vip: {filme3_ingressos[0][2]}")

    print("Receita por tipo:")
    print(f"Inteira: R$ {f3s1_int:.2f}")
    print(f"Meia: R$ {f3s1_meia:.2f}")
    print(f"Vip: R$ {f3s1_vip:.2f}")

    print("===================================================")

    #----------------

    f3s2_int = filme3_ingressos[1][1]*10
    f3s2_meia = filme3_ingressos[1][0]*10*0.5
    f3s2_vip = filme3_ingressos[1][2]*10*1.5

    print("Filme 3 - Sessão 2")
    print("Quantidade de ingressos vendidos:")
    print(f"Inteira: {filme3_ingressos[1][1]}")
    print(f"Meia: {filme3_ingressos[1][0]}")
    print(f"Vip: {filme3_ingressos[1][2]}")

    print("Receita por tipo:")
    print(f"Inteira: R$ {f3s2_int:.2f}")
    print(f"Meia: R$ {f3s2_meia:.2f}")
    print(f"Vip: R$ {f3s2_vip:.2f}")

    print("===================================================")

    #----------------
    total_f1_meia =0
    total_f1_int =0
    total_f1_vip =0
    total_f2_meia =0
    total_f2_int =0
    total_f2_vip =0
    total_f3_meia =0
    total_f3_int =0
    total_f3_vip =0
    
    for i in range(2):
        total_f1_meia += filme1_ingressos[i][0]
        total_f1_int += filme1_ingressos[i][1]
        total_f1_vip += filme1_ingressos[i][2]
        total_f2_meia += filme2_ingressos[i][0]
        total_f2_int += filme2_ingressos[i][1]
        total_f2_vip += filme2_ingressos[i][2]
        total_f3_meia += filme3_ingressos[i][0]
        total_f3_int += filme3_ingressos[i][1]
        total_f3_vip += filme3_ingressos[i][2]

    total_ingressos = total_f1_meia+total_f1_int+total_f1_vip+total_f2_meia+total_f2_int+total_f2_vip+total_f3_meia+total_f3_int+total_f3_vip
        
    total_f1_meia = total_f1_meia*20*0.5
    total_f1_int = total_f1_int*20
    total_f1_vip = total_f1_vip*20*1.5
    total_f1 = total_f1_meia +total_f1_int+total_f1_vip

    total_f2_meia = total_f2_meia*15*0.5
    total_f2_int = total_f2_int*15
    total_f2_vip = total_f2_vip*15*1.5
    total_f2 = total_f2_meia +total_f2_int+total_f2_vip


    total_f3_meia = total_f3_meia*10*0.5
    total_f3_int = total_f3_int*10
    total_f3_vip = total_f3_vip*10*1.5
    total_f3 = total_f3_meia +total_f3_int+total_f3_vip

    total_monetario = total_f1+total_f2+total_f3


    print(f"Total de ingressos vendidos: {total_ingressos}")
    print(f"Receita total do dia: R$ {total_monetario:.2f}")

    if qtd_avaliacao[0] == 0:#para não dividir por 0
        qtd_avaliacao[0]=1
    if qtd_avaliacao[1] == 0:
        qtd_avaliacao[1]=1
    if qtd_avaliacao[2] == 0:
        qtd_avaliacao[2]=1
    

    media_f1 = avaliacao[0]/qtd_avaliacao[0]
    media_f2 = avaliacao[1]/qtd_avaliacao[1]
    media_f3 = avaliacao[2]/qtd_avaliacao[2]

    print("Média de avaliações:")
    print(f"Filme 1: {media_f1:.2f}")
    print(f"Filme 2: {media_f2:.2f}")
    print(f"Filme 3: {media_f3:.2f}")

#INÍCIO DO CÓDIGO ============
menu()
    


    




