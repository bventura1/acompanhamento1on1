from pydantic import BaseModel
from typing import Optional, List
from model.colaboradores import Colaboradores


class ColaboradoresSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str = "Marcar Reunião"
    cargo: str = "Alberto"
    

class ColaboradoresBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    nome: str = "Bruno"


class ListagemColaboradoresSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    colaboradores:List[ColaboradoresSchema]


def apresenta_colaboradores(colaboradoress: List[Colaboradores]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for colaboradores in colaboradoress:
        result.append({
        "nome": colaboradores.nome,
            "cargo": colaboradores.cargo
        })

    return {"colaboradores": result}


def apresenta_colaboradores(atividades: Colaboradores):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "nome": colaboradores.nome,
        "cargo": colaboradores.cargo,
    }
