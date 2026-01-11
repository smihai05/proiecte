from motor import Monitor
from reguli import Regula
from date import salveaza_raport

monitor = Monitor()

def alerta_cpu(date):
    return f"ALERTĂ CPU: {date['cpu']['utilizare']}%"

def alerta_ram(date):
    return f"ALERTĂ RAM: {date['ram']['utilizare']}%"

regula_cpu = Regula("CPU Mare", lambda d: d["cpu"]["utilizare"] > 70, alerta_cpu)
regula_ram = Regula("RAM Mare", lambda d: d["ram"]["utilizare"] > 80, alerta_ram)

monitor.adauga_regula(regula_cpu)
monitor.adauga_regula(regula_ram)

raport, date = monitor.genereaza_raport()

print(raport)
salveaza_raport(raport)
