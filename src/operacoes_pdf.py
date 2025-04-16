import os
import re
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter, PdfMerger



class MesclarPDF:
    def __init__(self, diretorio, arquivo_saida):
        self.diretorio = diretorio
        self.arquivo_saida = arquivo_saida

    def unir_pdf(self):   
        escrever_pdf = PdfMerger()
        pdfs = [f for f in os.listdir(self.diretorio) if f.endswith(".pdf") or f.endswith(".PDF")]

        for pdf in pdfs:
            caminho_pdf = os.path.join(self.diretorio, pdf)
            #metodo append() adiciona um pdf ao final da fila
            escrever_pdf.append(caminho_pdf)                 

        with open(self.arquivo_saida, "wb") as f:
            escrever_pdf.write(f)
        print(f"PDFs unidos com sucesso em: {self.arquivo_saida}")    


class ProcessarPDF:
    def __init__(self, caminho_pdf, pasta_saida):
        self.caminho_pdf = caminho_pdf
        self.pasta_saida = pasta_saida
        os.makedirs(self.pasta_saida, exist_ok=True)

    def extrair_paginas(self):
        with open(self.caminho_pdf, "rb") as arquivo:
            pdf = PdfReader(arquivo)
            num_paginas = len(pdf.pages)
            print(f"Número de páginas: {num_paginas}")

            with pdfplumber.open(self.caminho_pdf) as pdf_plumber:
                for i in range(num_paginas):
                    texto = pdf_plumber.pages[i].extract_text()
                    self._salvar_pagina(pdf, i, texto)

    def _salvar_pagina(self, pdf, i, texto):
        pagina = pdf.pages[pagina]
        nome, valor, data_debito = self.__extrair_dados(texto)
        pasta_data = os.path.join(self.pasta_saida, data_debito)
        os.makedirs(pasta_data, exist_ok=True)

        nome_arquivo = f"Comprovante Bradesco - {nome} - {valor}.pdf"

        nome_arquivo = re.sub(r'[\/:*?"<>|]', "", nome_arquivo)
        caminho_arquivo = os.path.join(pasta_data, nome_arquivo)

        contador = 1                    
        while os.path.exists(caminho_arquivo):
            nome_arquivo = f"Comprovante Bradesco - {nome} - {valor} ({contador}).pdf"
            nome_arquivo = re.sub(r'[\/:*?"<>|]', "", nome_arquivo)
            caminho_arquivo = os.path.join(pasta_data, nome_arquivo)
            contador += 1

        criando_pdf = PdfWriter()
        criando_pdf.add_page(pagina)

        with open(caminho_arquivo, "wb") as f:
            criando_pdf.write(f)

        print(f"Página {i} salva em: {caminho_arquivo}")      
        

    def extrair_dados(self, texto):

        nome_arquivo = re.compile(r"(Fornecedor:|Beneficiário:)\s*(.{0,17})", flags=re.IGNORECASE)    
        valor_arquivo = re.compile(r"(Valor \(R\$\):|Valor total:)\s*(.*)", flags=re.IGNORECASE)    
        data_arquivo = re.compile(r"(Data de debito:)\s*(\d{2}/\d{2}/\d{4})")

        # Conjunto de expressão regular usada para documentos comprovantes tipo Manual
        nome_manual = re.compile(r"(Fornecedor:|Razão Social)\s*(.{0,17})", flags=re.IGNORECASE)    
        valor_manual = re.compile(r"(Valor R\$|Valor total:)\s*(.*)", flags=re.IGNORECASE)    
        data_manual = re.compile(r"(Data de debito:)\s*(\d{2}/\d{2}/\d{4})")

        nome = nome_arquivo.search(texto)
        valor = valor_arquivo.search(texto)
        data = data_arquivo.search(texto)

        nome = nome.group(2).strip().upper() if nome else "Nome_nao_encontrado"
        valor = valor.group(2).strip() if valor else "Valor_nao_encontrado"
        data_debito = data.group(2).replace("/", "-") if data else "Data_nao_encontrada"   

        return nome, valor, data_debito