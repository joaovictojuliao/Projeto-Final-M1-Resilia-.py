def emprestimo ():
    nomeBanco='Grupo 7'
    protocolo=8854362
#Menu principal
    opcao=5
    while opcao > 4:
        print("""\n        No empréstimo {} você encontra as melhores taxas do mercado
        
        1 - Emprestimo Consignado 
        2 - Emprestimo com garantia 
        3 - Crédito automático 
        4 - Gostaria saber um pouco mais sobre os tipos de empréstimos """.format(nomeBanco))
        opcao=int(input('\n        Digite a opcao desejada : '))
#Opção 1 do MENU - Emprestimo consignado  
    if opcao==1:
        salario1=-1
        while salario1 < 0:      
            salario1=int(input('\nDigite o seu salario para simular qual o limite de empréstimo consignado temos disponível pra você : R$ '))
        emprestimoConsignado=salario1*15
        prazo1=121
        while prazo1 > 120:
            prazo1=float(input('Digite o prazo em meses que deseja pagar (Máx 120 meses) : '))        
        parcelas1=(emprestimoConsignado/prazo1)*1.7        
        print('\nEntão o simulado ficou {:.0f} parcelas de : R$ {:.2f} '.format(prazo1, parcelas1))
        print('O valor máximo do empréstimo que foi liberado é de : R$ {:.2f} '.format(emprestimoConsignado))
        opcao1=emprestimoConsignado+1
        while opcao1 > emprestimoConsignado:
            print('\nLEMBRANDO SEU LIMITE LIBERADO É DE R$ {} '.format(emprestimoConsignado))
            opcao1=float(input('Digite o valor do emprestimo consignado que deseja : '))
        parcelas1=(opcao1/prazo1)*1.7
#Final do MENU 1 
        print("\nEmpréstimo aprovado no valor de R$ : {:.2f}".format(opcao1))
        print("Ficaram {:.0f} parcelas de R$ {:.2f} ".format(prazo1, parcelas1))
        print("Parábens seu empréstimo foi aprovado protocolo {} ".format(protocolo+3))
        print("Qualquer dúvida entre em contato com o suporte do banco {} !".format(nomeBanco))
#Opção 2 do MENU - Emprestimo garantia                   
    elif opcao==2:
        print('\nO que deseja deixar como garantia para o banco? ')
        garantia= 4
        if garantia > 3:
            garantia=int(input('\n1 - CARRO / 2 - MOTO / 3 - IMOVEL : '))
        valorGarantia=float(input('Digite o valor da garantia : '))
        prazo2=121
        while prazo2 > 120:
            prazo2=float(input('Digite o prazo em meses que deseja pagar (Máx 120 meses) : '))
        if garantia==1:
            valorEmprestimoGarantia=(valorGarantia/100)*90
        elif garantia==2:
            valorEmprestimoGarantia=(valorGarantia/100)*80
        elif garantia==3:
            valorEmprestimoGarantia=(valorGarantia/100)*95
        opcao2=valorEmprestimoGarantia+1
        while opcao2 > valorEmprestimoGarantia:
            print('O valor máximo do seu empréstimo é de R$ {}'.format(valorEmprestimoGarantia))
            opcao2=float(input('Digite o valor do empréstimo que deseja :'))
        parcelas2=(opcao2/prazo2)*1.9
#Final do MENU 2 
        print("\nEmpréstimo aprovado no valor de R$ : {:.2f}".format(opcao2))
        print("Ficaram {:.0f} parcelas de R$ {:.2f} ".format(prazo2, parcelas2))
        print("Parábens seu empréstimo foi aprovado protocolo {} ".format(protocolo+3))
        print("Qualquer dúvida entre em contato com o suporte do banco {} !".format(nomeBanco))
#Opção 3 do MENU - Crédito automático 
    elif opcao==3:
        cliente3=input("\nVocê já é cliente do Banco {} ? Digite sim ou nao : ".format(nomeBanco))
        if cliente3=='sim':
            print('\nTemos o melhor crédito com a melhor taxa de juros pra você que ja é cliente !')
            salario3=-1
            while salario3 < 0:
                salario3=float(input('Digite o seu salário para saber quanto temos disponível pra você : R$ '))
            creditoAuto=salario3*25
            prazo3=181
            while prazo3 > 180:
                prazo3=float(input('Digite o prazo em meses que deseja pagar (Máx 180 meses) : '))
            parcelas3=(creditoAuto/prazo3)*1.3
#Final do MENU 3
            print("\nEmpréstimo aprovado no valor de R$ : {:.2f}".format(creditoAuto))
            print("Ficaram {:.0f} parcelas de R$ {:.2f} ".format(prazo3, parcelas3))
            print("Parábens seu empréstimo foi aprovado protocolo {} ".format(protocolo+3))
            print("Qualquer dúvida entre em contato com o suporte do banco {} !".format(nomeBanco))
        elif cliente3=='nao':
            print('\nInfelizmente essa opção não está disponível pra você !')
#Opção 4 do MENU - Mais informações 
    elif opcao==4:
        print("""
        -----1 - Emprestimo Consignado 
        Ele é descontado diretamente no contracheque, holerite ou benefício do INSS. JUROS DE 1.7% ao mês
        -----2 - Emprestimo com garantia 
        Nele, você oferece o seu carro ou moto para dar mais segurança e conseguir um valor que toma como 
        base o preço do veículo. JUROS DE 1.9% ao mês
        -----3 - Crédito automático 
        Apenas para já clientes do banco. É uma opção de empréstimo com contratação simples e fácil 
        e para você usar como quiser. O valor solicitado é liberado na hora em sua conta corrente ou poupança.
        Prazo: Pague em até 180 meses. JUROS DE 1.3 % ao mês""")
        
#FINAL     
    print("\n---O BANCO {} AGRADECE O SEU CONTATO TENHA UM ÓTIMO DIA !---\n\n\n".format(nomeBanco))
    return 
emprestimo()

