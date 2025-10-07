from rich import print
from rich.panel import Panel


def PainelVerde(texto: str, isArquivo: bool):
    """Mostra o Painel com o texto em verde"""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    print(Panel(f"o conteúdo é [green]{conteudo}"))

def PainelAmarelo(texto: str, isArquivo: bool):
    """Mostra o Painel com texto em amarelo"""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    print(Panel(f"o conteúdo é [yellow]{conteudo}"))