

### Classe MesclarPDf

# metodo unir_pdf: 

 O script percorre uma diretório, buscando arquivos com extensão .pdf 
 e junta todos eles em um único para ser processado depois 

Chama o metodo PDFMERGER da lib PyPDF2, que usa os dois metodos:
1 - Append = Que adiciona os pdfs a uma fila, para posteriormente serem unidos
2 - Write = Dentro do manipulador de contexto with, faz uma junção de todos os pdf da fila