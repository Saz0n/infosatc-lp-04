Dados_pessoais  = {
     "id":22234,
     "nome": "rodosvaldo", 
     "cpf": 11122233344,
     "telefone": 48999220249, 
     "email": "Rodosvaldo@gmail.com",

    
}
print("Dados pessoais: ", Dados_pessoais)
print("Mostrando valor da chave id: ", Dados_pessoais["id"])
print("Mostrando valor da chave nome: ", Dados_pessoais["nome"])
print("Mostrando valor da chave cpf: ", Dados_pessoais["cpf"])
print("Mostrando valor da chave telefone: ", Dados_pessoais["telefone"])
print("Mostrando valor da chave email : ", Dados_pessoais["email"])

Dados_pessoais['sexo'] = 'Masculino'
Dados_pessoais['endereco'] = 'Rua central'
print("Mostrando valor da chave endereço : ", Dados_pessoais["endereco"])
print("Mostrando valor da chave sexo: ", Dados_pessoais["sexo"])
