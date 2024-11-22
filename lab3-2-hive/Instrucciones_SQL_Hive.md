```sql
--Crear la Tabla HDI en HDFS utilizando Hive
CREATE DATABASE IF NOT EXISTS usernamedb;
USE usernamedb;
CREATE TABLE HDI (
    id INT,
    country STRING,
    hdi FLOAT,
    lifeex INT,
    mysch INT,
    eysch INT,
    gni INT
) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE;
LOAD DATA INPATH '/user/hadoop/datasets/onu/hdi-data.csv' INTO TABLE HDI; --Cargar los datos de hdi-data.csv en la tabla HDI
--Consultas en la Tabla HDI
SHOW TABLES;
DESCRIBE HDI;
SELECT * FROM HDI;
SELECT country, gni FROM HDI WHERE gni > 2000;

--Ejecutar un Join en Hive

--Crear la Tabla EXPO
CREATE EXTERNAL TABLE EXPO (
    country STRING,
    expct FLOAT
) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE
LOCATION 's3://sbetancurb/onu/export/';
LOAD DATA INPATH '/user/hadoop/datasets/onu/export-data.csv' INTO TABLE EXPO; --Cargar los datos de export-data.csv en la tabla EXPO
--Consultas en la Tabla EXPO
SHOW TABLES;
DESCRIBE EXPO;
SELECT * FROM EXPO;

--Realizar el Join entre las Tablas HDI y EXPO
SELECT h.country, h.gni, e.expct 
FROM HDI h 
JOIN EXPO e 
ON (h.country = e.country) 
WHERE h.gni > 2000;

--WordCount en Hive

--Crear la Tabla docs con alternativa HDFS
CREATE EXTERNAL TABLE docs (line STRING) 
STORED AS TEXTFILE 
LOCATION '/user/hadoop/datasets/gutenberg-small/';

--Orden por palabra
SELECT word, COUNT(1) AS count 
FROM (
    SELECT explode(split(line, ' ')) AS word 
    FROM docs
) w 
GROUP BY word 
ORDER BY word DESC 
LIMIT 10;

--Orden por frecuencia de menor a mayor
SELECT word, COUNT(1) AS count 
FROM (
    SELECT explode(split(line, ' ')) AS word 
    FROM docs
) w 
GROUP BY word 
ORDER BY count DESC 
LIMIT 10;

--Reto: Almacenar Resultados en una Tabla

--Crear una tabla para almacenar resultados
CREATE TABLE wordcount_result (
    word STRING,
    count INT
)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ',' 
STORED AS TEXTFILE;

--Insertar resultados del WordCount
INSERT INTO wordcount_result 
SELECT word, COUNT(1) AS count 
FROM (
    SELECT explode(split(line, ' ')) AS word 
    FROM docs
) w 
GROUP BY word;

--Verificar los datos
SELECT * FROM wordcount_result;
```
