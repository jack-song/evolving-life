CREATE TABLE tempx(x integer);
CREATE TABLE tempy(y integer);

INSERT INTO tempx (x)
SELECT *
FROM generate_series(0,100);

INSERT INTO tempy (y)
SELECT *
FROM generate_series(0,100);

INSERT INTO evolvinglife_geographypoint(x, y, geography)
SELECT tempx.x, tempy.y, evolvinglife_geography.id
FROM tempx CROSS JOIN tempy INNER JOIN evolvinglife_geography on evolvinglife_geography.category = 'land';

DROP TABLE tempx;
DROP TABLE tempy;