# Automação de diretórios
Este script realiza a criação de pastas e organização de arquivos dentro de diretório
##  Bibliotecas

 - os
 - shutil

## Classe organizadorArquivos
Classe responsável por criar duas pastas [2024 , 2025] e 12 subpastas correspondentes aos meses de cada ano. Após a criação, organizar dentro delas todos os comprovantes de pagamentos que tenham a correspondências com as pastas criadas, exemplo:

├── 2025/
     ├── 01 - Jan
           └── Comprovante Banco - FORNECEDOR Y - 2300.00.pdf 

Parâmetros:
diretorio - Para criar das pastas e subpastas.


Método da classe:
organizar_arquivos(): Após a criação das pastas e subpastas, todos os PDFs correspondentes são movidos e organizados.