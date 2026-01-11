from senzori import citeste_cpu, citeste_ram
from reguli import Regula

class Monitor:
    def __init__(self):
        self.reguli = []

    def adauga_regula(self, regula):
        self.reguli.append(regula)

    def genereaza_raport(self):
        date = {
            "cpu": citeste_cpu(),
            "ram": citeste_ram()
        }
        texte_alerta = []
        for regula in self.reguli:
            rezultat = regula.verifica(date)
            if rezultat:
                texte_alerta.append(rezultat)
        if not texte_alerta:
            texte_alerta.append("Toate valorile sunt normale")
        raport = self._formateaza_raport(date, texte_alerta)
        return raport, date

    def _formateaza_raport(self, date, texte_alerta):
        raport = f"=== Raport Monitorizare PC ===\n"
        raport += f"CPU: {date['cpu']['utilizare']}% | Frecventa: {date['cpu']['frecventa']} MHz\n"
        raport += f"RAM: {date['ram']['utilizare']}% | Total: {date['ram']['total']//(1024**3)} GB | Disponibil: {date['ram']['disponibil']//(1024**3)} GB\n"
        raport += "--- Alertă ---\n"
        for t in texte_alerta:
            raport += t + "\n"
        return raport
