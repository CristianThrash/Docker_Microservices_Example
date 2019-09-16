# Docker-Microservices-Example

Ejemplo de una calculadora web convirtiendo las operaciones de suma, resta, multiplicación y división en microservicios, usando Docker y el framework Flask.

Se lanzan 6 servicios:

	front: interfaz de usuario web. Puerto 5000.
	gateway: busca el microservicio requerido por el cliente y retorna el resultado. Puerto 5005.
	serv_suma: realiza una suma y retorna el resultado. Puerto 5001
	serv_resta: realiza una resta y retorna el resultado. Puerto 5002
    serv_mult: realiza una multiplicación y retorna el resultado. Puerto 5003
    serv_div: realiza una división y retorna el resultado. Puerto 5004

# Autores

Jairo Andrés Romero

Cristian Manuel Bernal

# Requisitos de instalacion

git y docker con docker-compose instalados.

# Instalación en Linux

Situarse en la ubicación de preferencia y ejecutar en una terminal los comandos

	git clone https://github.com/CristianThrash/Docker-Microservices-Example.git
	cd Docker-Microservices-Example
	docker-compose up

Nota: Puede agregar la opción -d en el último comando para no bloquear la consola.

Una vez que los contenedores docker hayan terminado de construirse se lanzarán los 6 servicios. Cuando eso ocurra ingrese en el navegador

	localhost:5000

Con lo cual podrá probar la aplicación. 

Nota: Una vez que los servicios se hayan lanzado en una máquina, puede acceder a ellos desde cualquier otra máquina en la red local escribiendo en el navegador

	dirección_ip_del_servidor:5000
