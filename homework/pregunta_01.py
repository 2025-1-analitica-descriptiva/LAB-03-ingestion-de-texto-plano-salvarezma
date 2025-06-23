"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re
from pathlib import Path

def pregunta_01():
  file_path = Path("files/input/clusters_report.txt")

  f = open(file_path, encoding="utf-8")
  lines = f.readlines()
  f.close()

  start_idx = next(i for i, ln in enumerate(lines) if ln.strip().startswith('---')) + 1
  data_lines = lines[start_idx:]

  registros = []
  i = 0
  while i < len(data_lines):
      if re.match(r'\s+\d+', data_lines[i]):
          cluster = int(data_lines[i][:5].strip())
          cantidad = int(data_lines[i][5:20].strip())
          porcentaje = float(
              data_lines[i][20:40].strip().replace('%', '').replace(',', '.')
          )

          palabras_partes = [data_lines[i][40:].rstrip("\n")]
          j = i + 1
          while j < len(data_lines) and not re.match(r'\s+\d+', data_lines[j]):
              palabras_partes.append(data_lines[j].rstrip("\n"))
              j += 1

          palabras = ' '.join(palabras_partes)
          palabras = re.sub(r'\s+', ' ', palabras).strip().rstrip('.')
          palabras = re.sub(r'\s*,\s*', ', ', palabras)

          registros.append({
              'cluster': cluster,
              'cantidad_de_palabras_clave': cantidad,
              'porcentaje_de_palabras_clave': porcentaje,
              'principales_palabras_clave': palabras,
          })
          i = j
      else:
          i += 1

  return pd.DataFrame(registros)  
  
  
  
    # """
    # Construya y retorne un dataframe de Pandas a partir del archivo
    # 'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    # - El dataframe tiene la misma estructura que el archivo original.
    # - Los nombres de las columnas deben ser en minusculas, reemplazando los
    #   espacios por guiones bajos.
    # - Las palabras clave deben estar separadas por coma y con un solo
    #   espacio entre palabra y palabra.


    # """
