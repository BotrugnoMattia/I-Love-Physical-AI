from componente import Componente
class Robot:
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.applicazione = applicazione
        self.peso_massimo_componenti_kg = peso_massimo_componenti_kg
        self.stato = stato
        componenti: list[Componente]
    def aggiungi_componente(self, componente: Componente) -> None:
        if(componente.peso_kg > peso_massimo_componenti_kg | componente.codice == componenti.codice):
            componenti.append(componente)
        raise ValueError
    def peso_componenti() -> float:
        sum:int = 0
        for componente in componenti:
            sum+=componenti[i].peso_kg
    def cerca_componente(codice: str) -> Componente:
        for componente in componenti:
            if(codice == componenti.codice[i]):
                return componente
    def rimuovi_componente(codice: str) -> Optional[Componente]:
        for componente in componenti:
            if(codice == componenti.codice[i]):
                componenti.remove(componente.codice)
                return componente
            return None
    def componenti_sotto_peso(peso_massimo: float) -> list[Componente]:
        for componente in componenti:
            if(peso_massimo <= componenti.peso_kg[i]):
                return list[componente]
    