import pandas as pd
from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsPointXY, QgsProject
from PyQt5.QtCore import QVariant

# Función para leer las coordenadas desde el archivo Excel
def leer_coordenadas(excel_file):
    """Lee las coordenadas de latitud y longitud desde un archivo Excel.

    Args:
        excel_file (str): Ruta al archivo Excel.

    Returns:
        tuple: Tupla con las listas de latitudes y longitudes.
    """

    df = pd.read_excel(excel_file, engine='openpyxl')

    if 'latitud' not in df.columns or 'longitud' not in df.columns:
        raise ValueError("El archivo Excel debe contener las columnas 'latitud' y 'longitud'")

    return df['latitud'].values, df['longitud'].values

# Función para crear y guardar el polígono en QGIS
def crear_poligono_qgis(latitudes, longitudes, output_shapefile):
    """Crea un polígono en QGIS a partir de coordenadas y lo guarda como un shapefile.

    Args:
        latitudes (list): Lista de latitudes.
        longitudes (list): Lista de longitudes.
        output_shapefile (str): Ruta del archivo shapefile de salida.
    """

    # Crear la capa vectorial en memoria
    layer = QgsVectorLayer('Polygon?crs=EPSG:4326', 'Terreno', 'memory')
    provider = layer.dataProvider()

    # Añadir un campo ID (opcional)
    provider.addAttributes([QgsField('id', QVariant.Int)])
    layer.updateFields()

    # Crear la geometría del polígono
    puntos = [QgsPointXY(lon, lat) for lat, lon in zip(latitudes, longitudes)]
    puntos.append(puntos[0])  # Cerrar el polígono
    poligono = QgsGeometry.fromPolygonXY([puntos])

    # Crear una nueva entidad y añadirla a la capa
    feature = QgsFeature()
    feature.setGeometry(poligono)
    feature.setAttributes([1])
    provider.addFeature(feature)

    # Guardar la capa como un shapefile
    QgsVectorFileWriter.writeAsVectorFormat(layer, output_shapefile, "UTF-8", layer.crs(), "ESRI Shapefile")

    # Añadir la capa al proyecto de QGIS
    QgsProject.instance().addMapLayer(layer)
    print(f"Polígono guardado en: {output_shapefile}")

# Ruta al archivo Excel con las coordenadas
excel_file = 'C:/Users/leona/Documents/P.I. Qgis/Coordenadas Terreno 1.xlsx'

# Ruta de salida del Shapefile
output_shapefile = 'C:/Users/leona/Documents/P.I. Qgis/terreno.shp'

# Leer las coordenadas del archivo Excel
latitudes, longitudes = leer_coordenadas(excel_file)

# Crear y guardar el polígono en QGIS
crear_poligono_qgis(latitudes, longitudes, output_shapefile)
