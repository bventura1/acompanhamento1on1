from pydantic import BaseModel
from typing import Optional, List
from model.atividades import Atividades


class AtividadesSchema(BaseModel):
    """ Define como uma nova atividade a ser inserido deve ser representada
    """
    id: int = 1
    tarefa: str = "Marcar Reunião"
    colaborador: str = "Alberto"
    status: str = "Finalizado"


class AtividadesBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do colaborador.
    """
    colaborador: str = "Bruno"




class ListagemAtividadesSchema(BaseModel):
    """ Define como uma listagem de atividades será retornada.
    """
    atividades:List[AtividadesSchema]


def apresenta_atividades(atividadess: List[Atividades]):
    """ Retorna uma representação de atividades seguindo o schema definido em
        AtividadesViewSchema.
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
    """ Define como atividades serão retornadas
    """
    id: int = 1
    tarefa: str = "Marcar reunião"
    colaborador: str = "Alberto"
    status: str = "Status"


class AtividadesDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_atividades(atividades: Atividades):
    """ Retorna uma representação de atividades seguindo o schema definido em
        AtividadesViewSchema.
    """
    return {
        "id": atividades.id,
        "tarefa": atividades.tarefa,
        "colaborador": atividades.colaborador,
        "status": atividades.status
        #"total_cometarios": len(atividades.comentarios),
        #"comentarios": [{"texto": c.texto} for c in produto.comentarios]
    }
