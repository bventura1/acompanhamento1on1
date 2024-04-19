from pydantic import BaseModel
from typing import Optional, List
from model.atividades import Atividades


class AtividadesSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    id: int = 1
    tarefa: str = "Marcar Reunião"
    colaborador: str = "Alberto"
    status: str = "Finalizado"


class AtividadesBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
    colaborador: str = "Bruno"




class ListagemAtividadesSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    atividades:List[AtividadesSchema]


def apresenta_atividades(atividadess: List[Atividades]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for atividades in atividadess:
        result.append({
        "id": atividades.id,
            "tarefa": atividades.tarefa,
            "colaborador": atividades.colaborador,
            "status": atividades.status
        })

    return {"atividades": result}


class AtividadesViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    tarefa: str = "Marcar reunião"
    colaborador: str = "Alberto"
    status: str = "Status"
#    total_cometarios: int = 1
 #   comentarios:List[ComentarioSchema]


class AtividadesDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_atividades(atividades: Atividades):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": atividades.id,
        "tarefa": atividades.tarefa,
        "colaborador": atividades.colaborador,
        "status": atividades.status
        #"total_cometarios": len(atividades.comentarios),
        #"comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }
