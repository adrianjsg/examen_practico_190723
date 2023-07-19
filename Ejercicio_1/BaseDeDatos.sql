#Crea las siguientes consultas SQL:
#Obtener el id del usuario que su nombre es Juan.

SELECT id FROM nombre_de_la_tabla WHERE nombre = 'Juan';

#en nombre_de_la_tabla, tienes que poner el nombre de la tabla donde está el usuario que buscas


#Inserta en la base de datos, el usuario Juan, con nombre, apellido y correo. La tabla tiene auto númerico.

INSERT INTO nombre_de_la_tabla (nombre, apellido, correo) VALUES ('Juan', 'Garcia', 'juan.garcia@gmail.com');


#Actualizar el campo edad de Juan a 60 años.

UPDATE nombre_de_la_tabla SET edad = 60 WHERE nombre = 'Juan';
