from datetime import datetime

def salveaza_raport(text):
    with open("raport_pc.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()}\n{text}\n\n")
