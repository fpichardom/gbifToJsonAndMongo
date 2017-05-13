# gbifToJsonAndMongo

## Que es Json y Geojson

El formato json o "javascript object notation" consiste en una serie de valores en formato "key value pairs". Permite valores tanto de tipo numérico, texto, y otros objetos. Esta capacidad de poder tener otros objetos como valores le permite flexibilidad en la estructura en comparación a formatos populares como csv.

## Ejemplos json y csv

### Documento csv
pais,provincia,localidad,colectores,nombre_cientifico
República Dominicana,Santiago,"Loma La Pelona, Coordillera Central","Juan Pérez,Pancho Díaz",Pinus occidentalis

### Mismo documento en json

```javascript
{
  "pais": "República Dominicana",
  "provincia": "Santiago",
  "localidad": "Loma La Pelona, Coordillera Central",
  "collectores":"Juan Pérez, Pancho Díaz",
  "nombre_cientifico": "Pinus occidentalis"
 }
 ```
 Esto sería una conversión literal, pero no aprovechamos la flexibilidad que nos da el formato json. Por ejemplo podemos separar los nombres de los colectores para permitir búsquedas individuales:
 
 {
  "pais": "República Dominicana",
  "provincia": "Santiago",
  "localidad": "Loma La Pelona, Coordillera Central",
  "collectores":["Juan Pérez", "Pancho Díaz"],
  "especie": "Pinus occidentalis"
 }
 
 Esto se lograría en un csv añadiendo más casillas como colector1,colector2 y etc....
 Aún más el formato json nos da la posibilidad de crear más niveles dentro de cada record lo que no sería posible en csv y solo un funcionamiento similiar se lograría con una base de datos SQL.
 
 {
  "pais": "República Dominicana",
  "provincia": "Santiago",
  "localidad": "Loma La Pelona, Coordillera Central",
  "collectores": [
    {
      "nombre": "Juan",
      "apellido: "Pérez"
     },
     {
      "nombre": "Pancho",
      "apellido": "Díaz"
     }
  ],
  "especie": {
    "genero":"Pinus"
    "epitetoEspecifico": "occidentalis"
 }
 
 Este json está identado para ayudar la facilidad de lectura para los humanos, pero igual puede estar todo en una sola línea si el espacio es un problema. Pero como pueden ver cuando se abre un csv o json en un editor de texto cualquiera, json tiene la ventaja que es mucho más lejible para los humanos, claro que esto lleva la desventaja de que ocupa más espacio en disco o memoria. Pero solo debería ser de preocupación en caso de tener un json con demasiada data. Y es aquí donde entran bases de datos de tipo noSQL al rescate, pues nos permiten manejar archivos json enormes ya que por ejemplo el formato base de MongoDB es una variante muy similar de json.
 
## Geojson

Geojson es una variante de json que permite introducir data geoespacial a nuestros documentos. Lo que permite visualizarlos en programas de GIS y muchos aplicaciones web trabajan directamente con geojson para mostrar data geospacial, ya sean puntos, líneas, polígonos o una combinación de estos. Nuestro documento anterior se vería de esta forma en geojson:

{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "pais": "República Dominicana",
        "provincia": "Santiago",
        "localidad": "Loma La Pelona, Coordillera Central",
        "collectores":["Juan Pérez", "Pancho Díaz"],
        "especie": "Pinus occidentalis"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [ -71.12548828125, 19.21229162371484]
      }
    }
  ]
}

En este ejemplo
