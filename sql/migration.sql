-- create the table variables
CREATE TABLE IF NOT EXISTS public.variables
(
    instalacion varchar,
 	equipo varchar,
    id_equipo int,
    descripcion varchar,
    id_variable int,
    PRIMARY KEY (instalacion, equipo, id_variable)
);

-- create the table registros
CREATE TABLE IF NOT EXISTS public.registros
(
    instalacion varchar,
 	fecha timestamp,
    variable varchar,
    valor float,
    PRIMARY KEY (instalacion, fecha, variable)
);


-- Data