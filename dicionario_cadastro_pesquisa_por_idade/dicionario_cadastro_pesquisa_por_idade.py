
id = 1
dic = {}
while(1):
	op = input("-------\nMenu:\n0 para sair\n1 para cadastro\n2 para consulta\n-------\nDigite um valor: ")
	if(op=='0'):
		break
	if(op=='1'):
		cadastro = []
		cadastro.append(input("Digite o nome: "))
		cadastro.append(input("Digite a idade: "))
		cadastro.append(input("Digite o sexo (M ou F): "))
		cadastro.append(input("Digite a altura: "))
		dic[id]=cadastro
		id+=1
	
	elif(op=='2'):
		flag = 0
		idade = input("Qual a idade para pessoa(as) que deseja a con1sulta? ")
		print(end='\n')
		for i in dic:
			if idade==dic[i][1]:
				print('Cadastro de id: ',i)
				print('Nome: ',dic[i][0])
				print('Idade: ',dic[i][1])
				print('Sexo: ',dic[i][2])
				print('Altura: ',dic[i][3],end='\n\n')
				flag=1
		if(flag==0):
			print("\nLamento, nao foi encontrada nenhuma pessoa com esta idade.")
	




