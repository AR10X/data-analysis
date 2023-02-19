select *
from weather_dataset_v2;

-- Q1

SELECT COUNT(*)
FROM (SELECT Date, Temperature, 
             LAG(Temperature) OVER (ORDER BY Date) AS prev_temp
      FROM weather_dataset_v2) t
WHERE temperature < prev_temp;

-- Q3

SELECT Date, Temperature
FROM (
  SELECT Date, Temperature,
         SUM(CASE WHEN Temperature < 30 THEN 1 ELSE 0 END) 
           OVER (ORDER BY Date ROWS BETWEEN 3 PRECEDING AND CURRENT ROW) AS below_30_count
  FROM weather_dataset_v2
) t
WHERE below_30_count = 4;

-- Q5

select avg(avg_humidity) as avg_of_avg_hum
from
(select Date,avg(`Average humidity (%)`) as avg_humidity
	from weather_dataset_v2
    group by Date) as derivedtable;

-- Q9

Select count(Date)
from(select Date,Temperature
	from weather_dataset_v2
    where Temperature<0) as dp;

-- Q10

alter table weather_dataset_v2
add column id int Auto_increment primary key first;
create table weatherapp(
id int auto_increment primary key,
dataID int NOT NULL,
foreign key (dataID) references weather_dataset_v2(id));
