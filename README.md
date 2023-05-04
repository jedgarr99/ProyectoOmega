# Turbo Message
## _Sistemas Distribuidos: Proyecto Omega_



"Turbo Message" es un servicio de mensajería que replica la funcionalidad de un servidor de correo electrónico con ciertas restricciones. El proyecto debe implementar todas sus comunicaciones utilizando gRPC y Protocol Buffers. Los usuarios pueden interactuar con TurboMessage a través de una interfaz de consola que ofrece un menú de opciones para acceder a todas las funcionalidades del sistema. 


##### ¿Cómo se puede utilizar Turbo Message"?

- Los usuarios pueden registrarse de forma persistente en TurboMessage creando un nombre de usuario y una contraseña. Con sus credenciales, los usuarios pueden enviar y consultar correos electrónicos. Sin embargo, un usuario no puede tener más de 5 correos en su bandeja de entrada o salida, lo que significa que si alguien intenta enviar un correo electrónico a un usuario cuya bandeja de entrada está llena, recibirá un mensaje de error.
- Los usuarios pueden enviar y recibir correos electrónicos a otros usuarios existentes siempre que el nombre de usuario del destinatario exista en el sistema. Un correo electrónico tiene un identificador, un tema, un emisor, un destinatario y un cuerpo de mensaje. Los correos electrónicos tienen estados de no leído y leído, y dichos estados deben ser persistentes.

##### ¿Cómo se comunican el servidor y los clientes?

- La arquitectura de TurboMessage está diseñada para cumplir con los requisitos de rendimiento, escalabilidad y persistencia del servicio de mensajería. El sistema se compone de dos componentes principales: el cliente y el servidor 
-El cliente es una interfaz de consola que permite a los usuarios interactuar con el servidor. Los usuarios pueden registrarse en el sistema, enviar y recibir correos electrónicos, y realizar otras acciones típicas de un servicio de mensajería. La interfaz de consola utiliza gRPC para comunicarse con el servidor.
-El servidor es responsable de gestionar todas las solicitudes de los clientes y proporcionar los servicios de correo electrónico. El servidor utiliza gRPC y Protocol Buffers para la comunicación entre el cliente y el servidor. Además, el servidor mantiene una conexión persistente con la base de datos, lo que permite que los correos electrónicos sean persistentes.


##### ¿Cómo funciona la interfaz del cliente?

La interfaz del cliente se maneja desde la consola. Para cada sección incluye diferentes opciones y el usuario escribe en la consola el número con la opción que desea.
- Menu de inicio:
el menu cuenta con 3 opciones, la primera para registrarse (si es que aún no tiene una cuenta), la segunda para iniciar sesión (con su usuario y contraseña) y la tercera para cerrrar la aplicación.

![Interfaz de Menu](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/1MenuInicio.png). 
  
*Imagen 1. Interfaz Menu*
![Interfaz de registro](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/2Registro.png). 
  
*Imagen 2. Opción para registrarse*

![Interfaz de login](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/3InicioSesion.png). 
  
*Imagen 3. Opción para hacer login*

- Menu de correo:
En el menu de correo se tienen las diferentes opciones para ue el usuario se comunique. Primero, la opción para escribir correo, segundo para ver los correos recibidos y tercero opción para ver los correos enviados. Adicionalmente está lac cuarta opción para regresar el menú de inicio y la quinta para cerrar la aplicación.

![Interfaz de menu correo](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/4VerMailRecibido.png). 
  
*Imagen 4. Menu de correo*

![Ver mails recibidos](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/4VerMailRecibido.png). 
  
*Imagen 5. Opción ver mails recibidos*

Se incluye una función para que el usuario vea si ya ha leído el correo en cuestión. Los correos leídos aparecen con una palomita mientras que los correos no leídos tienen una cruz.

![Correos leídos ](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/5CorreoLeido.png). 
  
*Imagen 6. Notificación de leído*

Se incluye una función para eliminar correos de la bandeja de enviados y de la bandeja de recibidos. Así se libera el espacio de la bandeja puesto que hay un limite en correos enviados y recibidos de 5 correos.

![ELiminar correo ](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/7BorrarCoreo.png). 
  
*Imagen 7. Eliminar correo*


##### Conclusiones





