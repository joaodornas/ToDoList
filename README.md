# DOCUMENTACAO

Foi criado um projeto Django com uma aplicação chamada ToDoList.

# USUARIOS

O usuario administrador se chama "admin" e a senha é "password". Acessando o endpoint "admin/", da seguinte forma: http://localhost:8000/admin/, é possível cadastrar mais usuários. Foram cadastros mais dois usuários para testes. Seus usernames são: "anabela", "anaclara". A senha de cada usuário é "p@ssword123".

# AUTENTICACAO DO USUARIO

Para se autenticar, o usuario deve enviar uma requisição HTTP POST para o endpoint "api-token-auth/" com um JSON no body da requisição contendo o username e password, da seguinte forma:
    
    * { "username" : "anabela", "password": "p@ssword123" }

Caso o usuário seja autenticado corretamente, ele receberá como retorno um Token para autenticação.

# TODOLIST REST API

Foram criados três endpoints para manipular a ToDoList: "create/" (HTTP POST), "read/" (HTTP GET), "delete/id" (HTTP POST). 

O usuário somente consegue manipular os dados pelos endpoints se ele enviar uma requisição com o seu Token no cabeçalho usando o campo Authorization, da seguinte forma:

    * "{ "Authorization" : "Token e764150f45ec9eb5c2f1d8472018654205cc0bcc"}

Na requisição para o endpoint "create/", deve haver no body da requisição o texto a ser inserido na tarefa a ser criada, da seguinte forma:

    * { "task_text": "jantar" }

A tarefa é criada e registrada contendo o id do usuário que a criou.

Na requisição para o endpoint "read/", são retornadas todas as tarefas que somente o usuário, que está idenfiticado com o Token, criou. O usuário não consegue ler as tarefas de outros usuários, mas somente as dele.

Na requisição para o endpoint "delete/id", o usuário consegue apagar uma tarefa que ele criou usando o "id" da tarefa. Ele somente consegue apagar tarefas que ele criou.

# EXECUCAO

Para executar o projeto basta digitar o comando "python manage.py runserver".





