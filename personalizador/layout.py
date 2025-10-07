from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

console = Console()

def LayoutDeCima(texto: str, isArquivo: bool):
    """Mostra o Layout com a leitura do arquivo de cima"""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    layout = Layout()
    layout.split_column(
        Layout(Panel("o conteúdo de 'texto' é:")),
        Layout(Panel(conteudo))
    )

    console.print(layout)

def LayoutDeLado(texto: str, isArquivo: bool):
    """Mostra o Layout com a leitura do arquivo de lado"""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    layout = Layout()
    layout.split_row(
        Layout(Panel("o conteúdo de 'texto' é:")),
        Layout(Panel(conteudo))
    )

    console.print(layout)
