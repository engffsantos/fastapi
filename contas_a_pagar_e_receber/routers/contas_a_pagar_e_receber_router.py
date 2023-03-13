from _decimal import Decimal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix='/contas-a-pagar-e-receber')

class ContaPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str #PAGAR ou Receber

class ContaPagarReceberrequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: str #PAGAR ou Receber


@router.get('/')
def lista_contas():
    return [ContaPagarReceberResponse
            (id=1,
             descricao='Aluguel',
             valor=33.65,
             tipo='PAGAR'),
            ContaPagarReceberResponse(id=1,
            descricao='Salario',
            valor=1233.65,
            tipo='RECEBER')
    ]

@router.post('/', response_model=ContaPagarReceberResponse, status_code=201)
def criar_conta(conta: ContaPagarReceberrequest):
    return ContaPagarReceberResponse(
        id=3,
        descricao=conta.descricao,
        valor= conta.valor,
        tipo= conta.tipo  # PAGAR ou Receber
    )