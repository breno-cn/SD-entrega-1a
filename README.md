# SD-entrega-1a

## Instruções

### Dotenv

Esse projeto utiliza a biblioteca dotenv do python, que pode ser instalada por `sudo pip install python-dotenv`, ou por `sudo pip install -r requirements.txt`

### Servidor

Para executar o projeto, primeiro será necessário criar na raiz do repositório um arquivo de ambiente `.env`

Nele, será necessário definir duas variáveis:

* TCP_SERVER_PORT
* GRPC_SERVER_PORT

Essas duas variáveis irão definir a porta que o servidor de TCP socket e o servidor de GRPC irá ouvir, e também a porta o qual seus respectivos clientes irão se conectar.

Feito isso, o servidor sobre com um comando de `python Server.py`

Para encerrar o servidor, uma interrupção do teclado CTRL-C o encerra.

### Clientes

Feito isso, os clientes TCP e GRPC são criados respectivamente com 

`python TcpClient.py`

`python GrpcClient.py`

