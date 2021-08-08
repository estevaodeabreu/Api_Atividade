from flask import Flask,request
from flask_restful import Resource, Api
from models import Pessoas,Atividade,Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'Estevao': '123',
#     'Andre': '321'
# }

# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#
#     return USUARIOS.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False

    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
    @auth.login_required
    def get(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'Error',
                'mensagem': 'Pessoa nao encontrada'
            }

        return response

    def put(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return response

    def delete(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excliuda com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status':'sucesso', 'mensagem':mensagem}

class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas =Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'],idade=dados['idade'])
        pessoa.save()
        responce = {
            'nome': pessoa.nome,
            'idade': pessoa.idade,
            'id': pessoa.id
        }
        return responce

class Listaatividade(Resource):
    def get (self):
        atividade = Atividade.query.all()
        response = [{'id':i.id, 'nome':i.nome,'pessoa':i.pessoa.nome}for i in atividade]
        return response

    def post (self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividade(nome=dados['nome'],pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.id
        }
        return response




api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas,'/pessoas/')
api.add_resource(Listaatividade,'/atividades/')

if __name__ == '__main__':
    app.run(debug=True)