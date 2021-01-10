# B - Gestor Bens API
**Python, PostgreeSQL**

## Resumo
- Responsável pelo crédito do cliente. 
- Escolhido Python pois o mesmo é bastante utilizado para Inteligência artificial
- Banco de dados relacional
- Autenticação JWT  (Implementação futura)
- Compartilhar autenticação com [Sistema A](https://github.com/IVictorinoI/AGestorPessoa/) ?  (Implementação futura)
- Além dos GET, POST, PUT padrão, criar requests consolidadas para sistema de machine learning  (Implementação futura)
- A API possui swagger.

## Tabelas
- Cliente (Replicada do sistema A) (Id, Nome, Cpf, DataNascimento, Endereco) **GET**
- Bem (Id, IdCliente, Tipo{Carro, Casa}, DataAquisicao, ValorEstimado, Status{Financiado, Quitado}, ValorPago, SaldoPagar) **GET, POST, PUT, DELETE**
- Renda (Id, IdCliente, Fixo, Valor) **POST, PUT, DELETE**


## Customer
Cadastro do cliente, existe uma tabela no banco para cliente, porém ela é alimentada via sincronização.
Aqui não é permitido "cadastrar" o metodo 'PUT' recebe apenas o Cpf e faz uma request para obter os dados do [Sistema A](https://github.com/IVictorinoI/AGestorPessoa/)
![Customer](https://github.com/IVictorinoI/BGestorRendaBem/blob/main/Imagens/customer.PNG)

## Asset
Listagens de bens do cliente como Imoveis, Automoveis, etc.
![Customer](https://github.com/IVictorinoI/BGestorRendaBem/blob/main/Imagens/Asset.PNG)

## Income
Fontes de renda do cliente como, Emprego, Renda extra, aluguéis.
![Customer](https://github.com/IVictorinoI/BGestorRendaBem/blob/main/Imagens/Income.PNG)

## install:
python -m venv env
ctrl+shift+'
pip install flask
python -m pip install --upgrade pip
pip install flask-restful
pip install PyJWT

## create dependecies file
pip install -r requirements.txt
pip freeze > requirements.txt
"# BGestorRendaBem" 


Autor [Victor Matheus Mendes](https://github.com/IVictorinoI/)