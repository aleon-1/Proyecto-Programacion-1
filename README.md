# Proyecto-Programacion-1
Implementación de herramientas Python para Proyectos en QGis
Código markdown
# Digitalizacion de terreno por medio de herraminetas Python-Qgis
**Autores:**
Leon Arias Armando

## Introducción
Se busca lograr la proyeccion digital de un terreno, ubicado en el poblado de Zapotitlan de Vadillo, ya que en este se pretende ser llevar a cabo proyectos para su uso como un local, negocio, etc. utilizando al maximo el area e identificar datos aproximados sin la mayor intervencion fisica en el lugar. 

## Desarrollo
El uso de software de Sistemas de Información Geográfica (SIG) como QGIS ha revolucionado la forma en que se lleva a cabo el análisis y la gestión de información geoespacial. Gracias a QGIS, los usuarios pueden proyectar regiones a través de polígonos generados a partir de coordenadas geográficas y realizar complejos análisis geográficos que permiten comprender mejor las características del territorio y tomar decisiones basadas en datos precisos. QGIS es una herramienta de código abierto que soporta diversos tipos de datos geoespaciales, tanto ráster como vectoriales. Los datos vectoriales, como los polígonos, son especialmente útiles para representar áreas geográficas de interés, como límites administrativos, áreas protegidas o zonas urbanas. Para generar estos polígonos, es necesario disponer de coordenadas geográficas que definan los vértices de la región. Estas coordenadas pueden obtenerse de diferentes fuentes, como archivos CSV con coordenadas de latitud y longitud, bases de datos geográficas o shapefiles.
Una vez que se tienen las coordenadas, el siguiente paso es proyectarlas en el sistema de referencia espacial adecuado. Es fundamental elegir un Sistema de Referencia de Coordenadas (SRC) que se ajuste a la región de análisis. Si se trabaja a nivel global, el sistema más común es el WGS 84, pero si el análisis es más local, podría ser más apropiado usar un sistema proyectado como UTM (Universal Transverse Mercator), que facilita la medición precisa en áreas pequeñas. Con las coordenadas correctamente proyectadas en el sistema adecuado, se puede proceder a la creación de polígonos en QGIS. Existen diversas maneras de hacerlo: una opción es la digitalización manual de polígonos a partir de puntos existentes, utilizando las herramientas de edición de QGIS. Si las coordenadas de los vértices ya están definidas en un archivo CSV o en otro formato, se pueden importar y luego usar la herramienta de "Puntos a Polígonos" para conectarlos automáticamente y formar las áreas deseadas. A través de este proceso, es posible representar regiones específicas en el mapa y proceder con el análisis geoespacial.

![image](https://github.com/user-attachments/assets/e9581d85-e80b-47d4-bef6-3469047aba7a)


Una de las principales ventajas de QGIS es su capacidad para realizar un análisis geográfico profundo de las regiones proyectadas. Por ejemplo, se pueden calcular áreas, longitudes y otras propiedades de los polígonos para estudiar su tamaño y características. Además, QGIS permite realizar operaciones de superposición espacial entre diferentes capas, lo que facilita el análisis de cómo se interrelacionan varias regiones, como en el caso de áreas de uso de suelo o zonas de protección ambiental. Otras herramientas útiles en el análisis geográfico son las de proximidad, como la creación de "buffers", que permiten estudiar las áreas circundantes a un polígono. También es posible realizar análisis de redes, como la conectividad de caminos o ríos, lo cual es esencial para estudios de transporte o recursos hídricos. En términos de visualización, QGIS ofrece potentes opciones para representar los resultados del análisis. Los usuarios pueden personalizar el estilo de los polígonos mediante diferentes colores, bordes y transparencias, y también pueden añadir etiquetas para mostrar información adicional, como nombres o valores asociados a cada región. Además, el software permite crear mapas temáticos que, con la adición de leyendas, escalas y otras anotaciones, facilitan la interpretación y presentación de los resultados. Una vez que se ha completado el análisis y la visualización, los resultados pueden ser exportados en diversos formatos. Los mapas generados en QGIS pueden ser guardados como imágenes o archivos vectoriales (como shapefiles o GeoJSON) que pueden ser utilizados en otros programas o compartidos con otros usuarios. También es posible exportar los datos de análisis a archivos CSV o bases de datos para su uso en otras aplicaciones o para su integración con sistemas de información.

## Manejo de Datos

QGIS es una herramienta efectiva para realizar análisis de datos geoespaciales, especialmente cuando se trabaja con coordenadas geográficas y polígonos. En este caso, supongamos que tenemos un conjunto de coordenadas extraídas de Google Maps que definen los vértices de un polígono, y queremos analizar esas coordenadas en QGIS. Primero, debemos obtener las coordenadas desde Google Maps, que generalmente se presentan en formato de latitud y longitud. Estas coordenadas pueden ser extraídas haciendo clic derecho sobre un área específica en Google Maps y seleccionando "¿Qué hay aquí?" para obtener las coordenadas exactas. Una vez que tenemos las coordenadas, el siguiente paso es ingresar estos puntos en QGIS. Si las coordenadas están en un archivo CSV, podemos importarlas en QGIS seleccionando Capa -> Añadir capa -> Añadir capa de texto delimitado, asegurándonos de que las columnas de latitud y longitud sean correctamente reconocidas. Después de importar los puntos, QGIS ofrece herramientas para convertirlos en un polígono. Para esto, se puede utilizar la herramienta "Puntos a Polígonos", que une los puntos en el orden adecuado para formar un polígono cerrado que represente la región de interés. Una vez creado el polígono, es crucial asegurarnos de que los datos estén proyectados correctamente. QGIS permite trabajar con diferentes sistemas de referencia espacial (SRC), por lo que si las coordenadas fueron obtenidas en WGS 84, por ejemplo, debemos asegurarnos de que el SRC del proyecto esté configurado correctamente, para evitar errores en el análisis. Si es necesario, podemos reproyectar las capas a otro SRC adecuado para el análisis.


Con el polígono ya creado y proyectado, podemos empezar a analizar sus propiedades espaciales. QGIS permite realizar una serie de análisis geoespaciales, como el cálculo del área y el perímetro del polígono. Estas métricas son útiles para estudios de planificación territorial, gestión de recursos naturales y otras aplicaciones donde el tamaño y la forma de las áreas son importantes. Para calcular el área y el perímetro, se puede utilizar la herramienta de Calculadora de Campos en QGIS, donde se pueden generar nuevos campos que calculen automáticamente estos valores mediante expresiones como $area o $perimeter. Además del cálculo de áreas, QGIS permite realizar análisis de superposición espacial, lo que significa que podemos comparar el polígono con otras capas geográficas, como áreas de uso de suelo, cuerpos de agua o infraestructura. Esto es útil para identificar intersecciones entre el polígono y otras áreas de interés. Por ejemplo, si estamos analizando un polígono que representa una zona agrícola, podemos superponerlo con una capa que muestre áreas protegidas para identificar si existen solapamientos entre las dos. Otra herramienta útil en QGIS es la creación de buffers, que permite generar zonas de influencia alrededor de un polígono. Esto es particularmente útil en el análisis de proximidad. Por ejemplo, si queremos saber qué áreas se encuentran a una distancia específica de una carretera o un parque, podemos usar la herramienta de Buffer para crear una zona de influencia de 100 metros alrededor de un polígono y analizar qué otras características geográficas caen dentro de esa área. Además, QGIS permite realizar análisis de redes, lo que es útil si el polígono forma parte de una red, como una red de caminos, ríos o servicios. Se pueden analizar rutas, conectividad y otros aspectos relacionados con la estructura de la red en función de las características del polígono. Una vez completado el análisis, QGIS ofrece herramientas avanzadas para la visualización de los resultados. Podemos personalizar el estilo de los polígonos, aplicando colores, bordes y transparencias, para facilitar la interpretación de los datos. Además, es posible generar mapas temáticos que muestran los resultados del análisis de manera clara y efectiva, y exportarlos a formatos como imágenes o PDFs para su presentación.

## Codigo y su funcionamiento.


¿Cómo funciona el código?
El código lee las coordenadas de latitud y longitud de un archivo Excel, el archivo debe tener columnas específicamente llamadas latitud y longitud, si no están de esta manera, el código generará un error. Con las coordenadas leídas, el código utiliza las funciones de QGIS para crear una capa vectorial en memoria. Las coordenadas se convierten en puntos que forman un polígono. Este polígono se cierra automáticamente añadiendo el primer punto al final. Por ultimo se guarda como un archivo Shapefile en la ruta indicada, y también se agrega a la vista de QGIS, lo que permite visualizarlo directamente en el software.

Explicacion Paso a paso

1. Importación de librerías:
 
import pandas as pd                                                                                                                                                                                                 
from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsPointXY, QgsProject                                                                                                                     
from PyQt5.QtCore import QVariant

pandas: Se usa para leer el archivo Excel que contiene las coordenadas de latitud y longitud.                                                                                                                       
qgis.core: Proporciona las herramientas necesarias de QGIS para crear y manejar capas vectoriales, geometrías y otros objetos espaciales.                                                                           
PyQt5.QtCore: Se usa para manejar tipos de datos (en este caso, QVariant), que son necesarios para las funcionalidades de QGIS.

2. Función leer_coordenadas(excel_file):                                                                                                                                                                            
Propósito: Lee las coordenadas desde un archivo Excel.                                                                                                                                                              
Parámetros:                                                                                                                                                                                                         
excel_file: La ruta al archivo Excel que contiene las coordenadas.
Funcionamiento:                                                                                                                                                                                                     
Usa pandas.read_excel() para leer el archivo Excel.
Se asegura de que el archivo tenga las columnas latitud y longitud (de lo contrario, lanza un error).
Devuelve dos listas: una con las latitudes y otra con las longitudes de las coordenadas en el archivo Excel.

4. Función crear_poligono_qgis(latitudes, longitudes, output_shapefile):                                                                                                                                            
Propósito: Crea un polígono en QGIS a partir de las coordenadas de latitud y longitud y lo guarda como un archivo Shapefile.                                                                                        
Parámetros:                                                                                                                                                                                                         
latitudes: Lista de latitudes.                                                                                                                                                                                      
longitudes: Lista de longitudes.                                                                                                                                                                                    
output_shapefile: Ruta de salida para guardar el archivo Shapefile.                                                                                                                                                 
Funcionamiento:                                                                                                                                                                                                     
-Crea una capa vectorial en memoria para almacenar el polígono.                                                                                                                                                      
-Añade un campo opcional id a la capa, que se usará para almacenar un valor único (en este caso, 1).                                                                                                                 
-Crea la geometría del polígono utilizando las coordenadas de latitudes y longitudes, asegurándose de que el polígono se cierre (es decir, el primer punto se repite como el último).                                
-Añade el polígono como una nueva "entidad" (o feature) en la capa.                                                                                                                                                  
-Guarda la capa como un archivo Shapefile en la ubicación especificada.                                                                                                                                              
-Añade la capa creada al proyecto de QGIS en ejecución, de modo que sea visible en el mapa de QGIS.                                                                                                                  
5. Ejecución del código:                                                                                                                                                                                            
excel_file = 'C:/Users/su/ruta/al archivo/de Coordenadas.xlsx'                                                                                                                                                      
Se define la ruta del archivo Excel (excel_file) y la ruta de salida para el Shapefile (output_shapefile).                                                                                                          
Luego, se llama a la función leer_coordenadas para leer las coordenadas desde el archivo Excel.                                                                                                                     
Finalmente, se llama a la función crear_poligono_qgis para generar el polígono en QGIS y guardarlo como un archivo Shapefile en la ruta especificada.


## Resultados
QGis y Google Maps
Se extrajeron datos desde google maps, coordenadas de la region que necesitamos en este caso es nuestro lote, el cual tiene solo cuatro coordenadas, para ello las ingresamos a un archivo excel con el formato longitud y latitud, es de esta manera por que es una manera sencilla en el que el sofware puede leerlos sin problema, el codigo a utilizar funciona de tal manera que necesita de libreriapara prcesar datos de los cuales son leidos para genearr un archivo shape que contiene esta cordenadas y generra un poligono el cual tiene propiedades que podemos analizar, area y perimetro en nnuestro caso son las que necesitaremos.
QGIS es una herramienta avanzada para realizar análisis geoestadístico utilizando datos geoespaciales, como los que se encuentran en archivos SHP (Shapefiles). Estos archivos contienen configuraciones del terreno que permiten obtener información detallada sobre características geográficas, como la altitud, la pendiente o la cobertura del suelo, a partir de datos espaciales.

![image](https://github.com/user-attachments/assets/456ffa39-1625-4445-9fd8-f601eeff16eb)

Para realizar un análisis geoestadístico en QGIS, primero se deben cargar los archivos SHP que contienen las configuraciones del terreno. Es fundamental asegurarse de que el sistema de referencia espacial (SRC) esté correctamente configurado para garantizar la precisión de los análisis. QGIS permite trabajar con una variedad de capas geoespaciales, como polígonos, líneas y puntos, que pueden representar diferentes características del terreno. Uno de los análisis clave en geoestadística es la interpolación espacial, que predice valores desconocidos en ubicaciones no muestreadas basándose en datos cercanos. Usando herramientas como la interpolación Kriging o el método de Distancia Inversa (IDW), QGIS puede generar superficies continuas, como un modelo digital de elevación (DEM), que proporciona una representación detallada de la variabilidad del terreno. Otro análisis común es el de estadísticas zonales, que permite calcular características estadísticas dentro de zonas definidas, como la media, la desviación estándar o el máximo de valores en una capa ráster dentro de un polígono. Este análisis es útil para evaluar, por ejemplo, la pendiente promedio de diferentes parcelas de terreno o la cantidad de cobertura forestal en diferentes áreas. El análisis de patrones espaciales en QGIS también permite estudiar cómo se distribuyen fenómenos en el espacio, como la ubicación de estaciones meteorológicas o recursos naturales. Técnicas como el análisis de la distribución de puntos ayudan a identificar patrones espaciales en función de la cercanía y agrupamiento de los puntos, lo cual es clave en estudios de distribución de recursos o riesgos ambientales.
QGIS permite modelar superficies para analizar variaciones topográficas del terreno. Las herramientas de modelado de elevación digital, como el análisis de pendiente o exposición, ofrecen representaciones detalladas de la geografía de la región, fundamentales para el diseño de infraestructuras, estudios hidrológicos o planificación territorial. La visualización de estos resultados es fundamental. QGIS ofrece diversas opciones para estilizar las capas y crear mapas temáticos que faciliten la interpretación de los análisis. Los resultados, además, pueden ser exportados a otros formatos, como TIFF, GeoJSON o KML, para su integración con otras plataformas o su presentación en informes.

![image](https://github.com/user-attachments/assets/9b3e6ac8-74ab-458e-ac1f-fa3fa9b2f372)
![image](https://github.com/user-attachments/assets/0ab2c1b1-272a-47ac-aee8-312a6f49393b)

Datos recolectados en QGis 

![image](https://github.com/user-attachments/assets/2019cf10-e12a-4982-af8a-85e09967bdcd)

## Analisis.

INEGI ofrece datos geoespaciales detallados sobre límites administrativos, uso de suelo, áreas naturales protegidas, y más, en formatos como SHP (Shapefile). A través de este análisis, se puede obtener información clave sobre el territorio y realizar evaluaciones espaciales que apoyen la planificación, la gestión y el desarrollo de proyectos.

![Captura de pantalla 2024-12-07 173815](https://github.com/user-attachments/assets/6f78eafc-3aa7-45fb-acac-bad0a4ed3cf5)

Una vez realizados los análisis espaciales, QGIS permite crear mapas temáticos que representan visualmente los resultados obtenidos. Estos mapas temáticos pueden incluir diferentes colores o símbolos para representar distintas categorías o valores de los atributos analizados, como diferentes tipos de uso de suelo o áreas con diferentes características geográficas. Estos mapas son útiles para presentar los resultados de forma clara y accesible, facilitando la interpretación y la comunicación de los resultados.

## Codigo y su funcionamiento

## Conclusiones
El objetivo principal del proyecto se centró en crear una rutina que facilite la proyección y el análisis geoespacial, permitiendo realizar trabajos de forma más eficiente y accesible. Esta herramienta busca simplificar los procesos complejos involucrados en la manipulación y análisis de datos geoespaciales, proporcionándole al usuario una manera más directa y rápida de generar los resultados necesarios. Los beneficios de contar con una rutina automatizada radican en la capacidad de representar de manera más precisa y fiel las características del terreno en cuestión, ya que se utilizan datos más específicos y detallados para crear las proyecciones y análisis. Al estar basado en una rutina programada, el sistema tiene la flexibilidad de adaptarse a distintos escenarios y necesidades. La libertad que ofrece el código permite modificar, ajustar y extender la funcionalidad del programa según los requerimientos del usuario. Esta capacidad de personalización es una de las grandes ventajas, ya que no se limita a un conjunto rígido de características, sino que puede evolucionar y ajustarse continuamente a medida que se presentan nuevas demandas o se identifican mejoras necesarias. Los usuarios tienen la oportunidad de explorar de manera profunda los datos, agregar nuevos códigos y funcionalidades, y modificar los existentes para optimizar el análisis o incluir nuevos elementos que mejoren la precisión o la relevancia de los resultados obtenidos. Esto convierte al proyecto no solo en una herramienta útil, sino en una plataforma flexible y escalable que puede adaptarse a una amplia gama de necesidades geoespaciales, independientemente del nivel de complejidad o especificidad requerido.
