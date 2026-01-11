class Regula:
    def __init__(self, nume, conditie, actiune_text):
        self.nume = nume
        self.conditie = conditie
        self.actiune_text = actiune_text

    def verifica(self, date):
        if self.conditie(date):
            return self.actiune_text(date)
        return None
