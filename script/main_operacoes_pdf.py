from operacoes_pdf import MesclarPDF, ProcessarPDF


if __name__ == "__main__":

    mesclar_pdf = MesclarPDF("diretorio", "arquivo_saida")

    mesclar_pdf.unir_pdf()

    processar_pdf = ProcessarPDF("caminho_pdf", "pasta_saida")

    processar_pdf.extrair_paginas()