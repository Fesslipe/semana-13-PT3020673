import unittest
from aluno import AlunoClass
from turma import TurmaClass

class alunoTest(unittest.TestCase):
    def setUp(self):
        print(f"Inicializando o teste: {self._testMethodName}")

        # Configuração do mock do MongoDB
        self.mock_conexao = mongomock.MongoClient()
        self.mock_db = self.mock_conexao['faculdade']  # Banco de dados fictício

        # Criando objetos para os testes
        self.aluno = AlunoClass('Feslipe', 'Queiroz', 10)
        self.turma = TurmaClass()
        self.turma.cadastrarAlunos([self.aluno])

    def test_salvarAluno(self):   
        resposta = self.aluno.salvar(conexao=self.mock_db, colecao='alunos')
        self.assertEqual(True, resposta, 'Aluno não foi cadastrado corretamente!')
        print("Teste 1 (Salvar Aluno): Sucesso! Aluno cadastrado corretamente.")

    def test_salvarTurma(self):   
        resposta = self.turma.salvar(conexao=self.mock_db, colecao='turma')
        self.assertEqual(True, resposta, 'Turma cadastrada incorretamente!')
        print("Teste 2 (Salvar Turma): Sucesso! Turma cadastrada corretamente.")

    def tearDown(self):
        print(f"Finalizando o teste: {self._testMethodName}")


if __name__ == "__main__":
    unittest.main()
