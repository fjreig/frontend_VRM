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

-- Data