import time
from rich.progress import track



def ProgressoRapido(texto: str, isArquivo: bool):
    """Mostra a barra de progresso com menor tempo(5 segundos)"""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    for _ in track(range(5), description="Analisando arquivo rapidamente..."):
        time.sleep(1)
    
    print(f"[blue]{conteudo}")

def ProgressoLento(texto: str, isArquivo: bool):
    """Mostra a barra de progresso com maior tempo(10 segundos)"""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    for _ in track(range(10), description="Analisando arquivo lentamente..."):
        time.sleep(1)
    
    print(f"[black]{conteudo}")