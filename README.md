@MIAGUILA
@FERNANDO TIBANA 
@AGOSTO-2020

TRIPS

Breve explicacion:

1. se crear base de datos tripss en postgres, Se crea una carga de trips.json en postgreSQL
2. Se agrega id para identificar registro para edicion y eliminacion
3. se crea proyecto en python, se insatala psycopg2, posteriormente se configura coinexion a base de datos
4. se realiza migracion a base de datos desde python 
5. se intala django framework
6. se instala rest_framework_suagger para documentacion
7. se generan las vistas para request

para ejecutar

1. Se debe iniciar el proyecto por terminal, se debe validar la configuracion DATABASES en settings.py 
2. Organizar migracion  para generar tablas y campos en la base de datos:
    python manage.py makemigrations 
    python manage migrate
3. poblar tablas
4. correr servidor local
    python runserver 8080

5. llamar desde afuera para validar funciones

se pouede usar postman para generar las peticiones 
la direccion es
localhost:8080/trips

documentacion 
localhost:8080/doc


Para Crear un endpoint que reciba una posición geográfica y que basado en el histórico de viajes genere un multiplicador para tarifas dinámicas. 

se realiza operacion de dejar todas las coordenadas hasta el decimal 3, redondeando con esto se logra ubicar mas o menos en un rqango de 500 a 1000 metros a la redonda, luego de esto se agrupan y se cuentan, las coordenadas y se realiza un count quedando asi

punto           CANTIDAD    multiplicador

-74.142,4.698	14          2.3
-76.388,3.545	11          1.5
-75.428,6.171	13          1.7
-74.119,4.684	45          2.0


Teniendo en cuanta esto y al ingresar la coordenada se deja de 3 decimales se redondea y se valida con la informacion anterior si no coincide la coordenada, se deja sin multiplicador

la consulta desde postgres es 

SELECT PUNTO,CANTIDAD AS CANT
FROM(
SELECT  
 --data->'start'->'pickup_location'->'coordinates' AS inicio
concat(  round(substring(data->'start'->'pickup_location'->>'coordinates',2,position (',' in data->'start'->'pickup_location'->>'coordinates' )-2)::numeric,3) 
  ,',',round(substring(data->'start'->'pickup_location'->>'coordinates',position (',' in data->'start'->'pickup_location'->>'coordinates')+2,position (']' in data->'start'->'pickup_location'->>'coordinates')-(position (',' in data->'start'->'pickup_location'->>'coordinates')+2))::numeric,3)) as punto
  ,count(concat(  round(substring(data->'start'->'pickup_location'->>'coordinates',2,position (',' in data->'start'->'pickup_location'->>'coordinates' )-2)::numeric,3) 
  ,',',round(substring(data->'start'->'pickup_location'->>'coordinates',position (',' in data->'start'->'pickup_location'->>'coordinates')+2,position (']' in data->'start'->'pickup_location'->>'coordinates')-(position (',' in data->'start'->'pickup_location'->>'coordinates')+2))::numeric,3)) ) as cantidad
FROM trips
 

  group by concat(  round(substring(data->'start'->'pickup_location'->>'coordinates',2,position (',' in data->'start'->'pickup_location'->>'coordinates' )-2)::numeric,3) 
  ,',',round(substring(data->'start'->'pickup_location'->>'coordinates',position (',' in data->'start'->'pickup_location'->>'coordinates')+2,position (']' in data->'start'->'pickup_location'->>'coordinates')-(position (',' in data->'start'->'pickup_location'->>'coordinates')+2))::numeric,3))
)  AS X

where cantidad>10