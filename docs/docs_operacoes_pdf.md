# Automação de PDFs Financeiros

Este projeto realiza automações com arquivos PDF gerados por bancos, como extração de páginas específicas e mesclagem de arquivos, utilizando Python.

##  Bibliotecas

 - PyPDF2
 - pdfplumber

## Classe MesclarPDF
Classe responsável por unir múltiplos arquivos .pdf encontrados em um diretório.

Parâmetros:
diretorio - Caminho da pasta contendo os PDFs a serem mesclados.

arquivo_saida - Caminho do arquivo PDF de saída.

Método da classe:
unir_pdf(): Une todos os arquivos .pdf do diretório em um único arquivo PDF.


## Classe ProcessarPDF
Classe responsável por extrair páginas individuais de um arquivo PDF e salvá-las separadamente em pastas organizadas por data de débito, extraída do conteúdo das páginas.

Parâmetros:
caminho_pdf - Caminho do arquivo PDF a ser processado.

pasta_saida - Caminho da pasta onde os arquivos extraídos serão salvos.

Métodos:
extrair_paginas - Percorre cada página do PDF, extrai o texto e salva a página como um novo PDF.

_salvar_pagina(pdf, i, texto): Salva uma única página após extrair os dados do texto.

extrair_dados(texto): Extrai nome, valor e data do texto da página usando expressões regulares.


## Estrutura desejada após todas as operações

saida/
├── 15-04-2025/
     ├── Comprovante Banco - FORNECEDOR X - 1500.00.pdf
     └── Comprovante Banco - FORNECEDOR Y - 2300.00.pdf



Ainda estou buscando melhorias para aplicação fique a vontade para contribuir.
