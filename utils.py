from models import Pessoas,Usuarios


# Insere dados na tabela pessoas
def insere_pessoas():
    pessoas = Pessoas(nome='Andre', idade=36)
    print(pessoas)
    pessoas.save()

# Consulta dados na tabela pessoas
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Andre').first()
    print(pessoa.idade)

# Altera dados na tabela pessoas
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Andre').first()
    pessoa.nome = 'Leonardo'
    pessoa.save()

# Exclui dados na tabela pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Leonardo').first()
    pessoa.delete()


def insere_usuario(login,senha):
    usuario = Usuarios(login=login,senha=senha)
    usuario.save()

def consulta_todo_usuarios():
    usuarios = Usuarios.query.all()


if __name__ == '__main__':
    #insere_usuario('Estevao','789')
    #consulta_todo_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()