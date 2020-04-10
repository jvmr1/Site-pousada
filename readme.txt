Nosso site feito para uma pequena pousada que possui 4 quartos diferentes, o site oferece um sistema de gerenciamento de reservas

Para abrir o site: 
	Abrir o terminal na pasta "flask"
	Dar o comando "$ python3 run.py runserver"
	Abrir a url "http://127.0.0.1:5000/" no navegador

Ao entrar no site, o usuário tem as opções de criar uma conta, caso não possua, ou de entrar na sua conta, caso já possua.

Se optou por criar conta, no final, é redirecionado para a página de login

Ao logar, é direcionado para a página de quartos, onde poderá ver os 4 quartos que possuímos na pousada

O usuário pode reservar um quarto. Ele só será reservado se não estiver já reservado, caso já esteja reservado, aparecerá uma mensagem avisando.

No banco de dados são armazenadas informações sobre os quartos, os usuários e suas reservas

O framework empregado foi o flask, e a linguagem python.

Para a criação do banco de dados foi utilizada a extensão do flask SQLAlchemy, que gera as tabelas automaticamente

