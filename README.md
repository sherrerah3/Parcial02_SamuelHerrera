# Parcial 02 - Arquitectura de Software

 **¿Cómo modificaría su diseño si este microservicio tuviera que comunicarse con otro servicio que almacena el historial de cálculos en una base de datos externa.?**

Si el microservicio debe comunicarse con otro que almacena el historial de calculos, lo que yo haria es agregar un POST al terminar el cálculo para enviar los datos que estamos mostrando en este momento (número, factorial y etiqueta) al segundo servicio, y este los guarda en una base de datos.

Para correr este programa, ejecutamos en consola ``flask run`` y la url a modificar sera http://127.0.0.1:5000/int, luego al ingresar a esta url y cambia ``<int>`` por algun numero, veremos el JSON.

Hecho por Samuel Herrera Hoyos
