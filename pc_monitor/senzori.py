import psutil

def citeste_cpu():
    return {
        "utilizare": psutil.cpu_percent(interval=1),
        "frecventa": psutil.cpu_freq().current
    }

def citeste_ram():
    mem = psutil.virtual_memory()
    return {
        "utilizare": mem.percent,
        "total": mem.total,
        "disponibil": mem.available
    }
