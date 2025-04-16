import os
import shutil

class OrganizadorArquivos:
    def __init__(self, caminho):
        self.caminho = caminho
        self.meses = {'01':'01 - JAN', '02':'02 - FEV',
                      '03':'03 - MAR', '04':'04 - ABR', 
                      '05':'05 - MAI', '06':'06 - JUN', 
                      '07':'07 - JUL', '08':'08 - AGO',
                      '09':'09 - SET', '10':'10 - OUT',
                      '11':'11 - NOV', '12':'12 - DEZ'}
        

    def organizar_arquivos(self):
        for ano in ["2024", "2025"]:
            for mes in self.meses.values():
                os.makedirs(os.path.join(self.caminho, ano, mes), exist_ok=True)

        for pasta in os.listdir(self.caminho):
            if '-' in pasta:
                partes = pasta.split('-')
                if len(partes) >= 3:
                    dia, mes, ano = partes[:3]
                    nome_mes = self.meses.get(mes)
                    if ano in ["2024", "2025"] and nome_mes:
                        origem = os.path.join(self.caminho, pasta)
                        destino = os.path.join(self.caminho, ano, nome_mes, pasta)
                        shutil.move(origem, destino)
                        print(f"Arquivo {origem} movido para {destino}")