import argparse
from personalizador import progresso, painel, layout, estilo

modulos = {
    "layout": {"de_cima": layout.LayoutDeCima, "de_lado": layout.LayoutDeLado},
    "painel": {"verde": painel.PainelVerde, "amarelo": painel.PainelAmarelo},
    "progresso": {"rapido": progresso.ProgressoRapido, "lento": progresso.ProgressoLento},
    "estilo": {"colorido": estilo.TextoColorido, "estilizado": estilo.TextoEstilizado},
}

parser = argparse.ArgumentParser(description="Imprime textos usando o pacote personalizador com Rich")

parser.add_argument("texto", type=str, help="Texto ou caminho do arquivo a ser impresso")
parser.add_argument("-a", "--arquivo", action="store_true", help="Ativa se o argumento 'texto' for um arquivo")
parser.add_argument("-m", "--modulo", choices=modulos.keys(), required=True, help=f"Escolha o módulo ({', '.join(modulos.keys())})")
parser.add_argument("-f", "--funcao", required=True, help="Escolha a função do módulo (verifique os nomes disponíveis)")

args = parser.parse_args()

funcoes_do_modulo = modulos[args.modulo]

if args.funcao not in funcoes_do_modulo:
    print(f"Função '{args.funcao}' não encontrada no módulo '{args.modulo}'. Opções: {', '.join(funcoes_do_modulo.keys())}")
else:
    funcoes_do_modulo[args.funcao](args.texto, args.arquivo)