from rich import print

def TextoColorido(texto: str, isArquivo: bool):
    """Imprime o texto em azul com negrito."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    print(f"[bold blue]{conteudo}[/bold blue]")

def TextoEstilizado(texto: str, isArquivo: bool):
    """Imprime o texto em vermelho e itálico."""
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            conteudo = f.read()
    else:
        conteudo = texto

    print(f"[italic red]{conteudo}[/italic red]")
