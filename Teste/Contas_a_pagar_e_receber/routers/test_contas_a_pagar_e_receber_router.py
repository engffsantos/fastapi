from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_deve_listar_contas_a_pagar_e_receber():
    response = client.get('/contas-a-pagar-e-receber')
    assert response.status_code ==200
    assert response.json() == [
        {'id': 1, 'descricao':'Aluguel','valor':33.65,'tipo':'PAGAR'},
        {'id': 2, 'descricao':'Salario','valor':1233.65,'tipo':'RECEBER'}
    ]

def test_deve_criar_contas_a_pagar_e_receber():
    nova_conta = {
        'descricao':'Luz',
        'valor':11.65,
        'tipo':'PAGAR'
    }
    nova_conta_copy = nova_conta.copy()
    nova_conta_copy['id'] = 3
    response = client.post('/contas-a-pagar-e-receber',json=nova_conta)
    assert response.status_code ==201
    assert response.json() == nova_conta_copy