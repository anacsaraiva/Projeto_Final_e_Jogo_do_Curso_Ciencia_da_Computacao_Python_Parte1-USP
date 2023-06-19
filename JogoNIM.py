def computador_escolhe_jogada(n,m):

    i = 1

    while i<=m and i<=n:

        if (n-i)%(m+1)==0:
            break
        else:
            if i < m and i < n:
                i +=1
            elif i == m:
                break

    return i

def usuario_escolhe_jogada(n,m):

    jogada = False
    
    while not(jogada):

        p = int(input("\nQuantas peças você vai tirar?"))
        
        if p <= m and p >0 and p <= n:
            
            jogada = True
            
        else:
            print('Oops ! Jogada Inválida! Tente de novo.')

    return p
              
def partida():


    print("Bem-Vindo ao jogo do NIM! Escolha:")

    escolha = int(input("\n1 - para jogar uma partida isolada""\n2 - para jogar um campeonato\n\n"))

    if escolha == 1:
        
        print("\nVoce escolheu uma partida isolada!")

        n_digitado = int(input("\nQuantas peças? "))
        m_digitado = int(input("Limite de peças por jogada? "))

        if n_digitado % (m_digitado+1) == 0:

            print("Você começa!")

            while n_digitado >= 0:

                tirou = usuario_escolhe_jogada(n_digitado,m_digitado)
                n_digitado -= tirou

                print("Você tirou",tirou,"peças.")

                if n_digitado == 0:
                    print("Fim de jogo! Você ganhou!")
                    break
                else:
                    
                    print("Agora restam apenas",n_digitado,"peças no tabuleiro.")
                    
                    tirou = computador_escolhe_jogada(n_digitado,m_digitado)
                    n_digitado -= tirou

                    print("\nO computador tirou",tirou,"peças.")

                    if n_digitado == 0:
                        print("Fim do jogo! O computador ganhou!")
                        break
                    else:
                        print("Agora restam apenas",n_digitado,"peças no tabuleiro.")
        else:

            print("Computador começa!")

            while n_digitado >= 0:

                tirou = computador_escolhe_jogada(n_digitado,m_digitado)
                n_digitado -= tirou

                print("O computador tirou",tirou,"peças.")

                if n_digitado == 0:
                    print("Fim de jogo! O computador ganhou!")
                    break
                else:
                    
                    print("Agora restam apenas",n_digitado,"peças no tabuleiro.")
                    
                    tirou = usuario_escolhe_jogada(n_digitado,m_digitado)
                    n_digitado -= tirou

                    print("\nVocê tirou",tirou,"peças.")

                    if n_digitado == 0:
                        print("Fim do jogo! Você ganhou!")
                        break
                    else:
                        print("Agora restam apenas",n_digitado,"peças no tabuleiro.")
        
    elif escolha == 2:
        
        print("\nVoce escolheu um campeonato!")
        
        rodada = 1
        comp_ganhou = 0
        jog_ganhou = 0

        while rodada <=3:

            print("\n**** Rodada",rodada,"****")

            n_digitado = int(input("\nQuantas peças? "))
            m_digitado = int(input("Limite de peças por jogada? "))

            if n_digitado % (m_digitado+1) == 0:

                print("Você começa!")

                while n_digitado >= 0:

                    tirou = usuario_escolhe_jogada(n_digitado,m_digitado)
                    n_digitado -= tirou

                    print("Você tirou",tirou,"peças.")

                    if n_digitado == 0:
                        print("Fim de jogo! Você ganhou!")
                        rodada +=1
                        jog_ganhou += 1
                        break
                    else:
                    
                        print("Agora restam apenas",n_digitado,"peças no tabuleiro.")
                    
                        tirou = computador_escolhe_jogada(n_digitado,m_digitado)
                        n_digitado -= tirou

                        print("\nO computador tirou",tirou,"peças.")

                        if n_digitado == 0:
                            print("Fim do jogo! O computador ganhou!")
                            rodada +=1
                            comp_ganhou +=1
                            break
                        else:
                            print("Agora restam apenas",n_digitado,"peças no tabuleiro.")
            else:

                print("Computador começa!")

                while n_digitado >= 0:

                    tirou = computador_escolhe_jogada(n_digitado,m_digitado)
                    n_digitado -= tirou

                    print("O computador tirou",tirou,"peças.")

                    if n_digitado == 0:
                        print("Fim de jogo! O computador ganhou!")
                        rodada += 1
                        comp_ganhou += 1
                        break
                    else:
                    
                        print("Agora restam apenas",n_digitado,"peças no tabuleiro.")
                    
                        tirou = usuario_escolhe_jogada(n_digitado,m_digitado)
                        n_digitado -= tirou

                        print("\nVocê tirou",tirou,"peças.")

                        if n_digitado == 0:
                            print("Fim do jogo! Você ganhou!")
                            rodada +=1
                            jog_ganhou += 1
                            break
                        else:
                            print("Agora restam apenas",n_digitado,"peças no tabuleiro.")
                
        print("\n**** Final do campeonato! ****")
        print("\n Placar: Você",jog_ganhou,"X",comp_ganhou,"Computador")


                
partida()

    
            
        


    
    
