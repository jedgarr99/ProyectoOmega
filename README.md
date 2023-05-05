# Turbo Message
## _Sistemas Distribuidos: Proyecto Omega_



"Turbo Message" es un servicio de mensajería que replica la funcionalidad de un servidor de correo electrónico con ciertas restricciones. El proyecto implementa todas sus comunicaciones utilizando gRPC y Protocol Buffers. Los usuarios pueden interactuar con TurboMessage a través de una interfaz de consola que ofrece un menú de opciones para acceder a todas las funcionalidades del sistema. 


##### ¿Qué puede hacer un usuario de Turbo Message"?

- Los usuarios pueden registrarse de forma persistente en TurboMessage creando un nombre de usuario y una contraseña. Con sus credenciales, los usuarios pueden enviar y consultar correos electrónicos. Sin embargo, un usuario no puede tener más de 5 correos en su bandeja de entrada o salida, lo que significa que si alguien intenta enviar un correo electrónico a un usuario cuya bandeja de entrada está llena, recibirá un mensaje de error.
- Los usuarios pueden enviar y recibir correos electrónicos a otros usuarios existentes siempre que el nombre de usuario del destinatario exista en el sistema. Un correo electrónico tiene un identificador, un tema, un emisor, un destinatario y un cuerpo de mensaje. Los correos electrónicos tienen estados de no leído y leído, y dichos estados deben ser persistentes.

##### ¿Cómo se comunican el servidor y los clientes?

- La arquitectura de TurboMessage está diseñada para cumplir con los requisitos de rendimiento, escalabilidad y persistencia del servicio de mensajería. El sistema se compone de dos elementos principales: el **cliente** y el **servidor** 
- El cliente es una interfaz de consola que permite a los usuarios interactuar con el servidor. Los usuarios pueden registrarse en el sistema, enviar y recibir correos electrónicos, y realizar otras acciones típicas de un servicio de mensajería. La interfaz de consola utiliza gRPC para comunicarse con el servidor.
- El servidor es responsable de gestionar todas las solicitudes de los clientes y proporcionar los servicios de correo electrónico. El servidor utiliza gRPC y Protocol Buffers para la comunicación entre el cliente y el servidor. Además, el servidor mantiene una conexión persistente y se tienen diccionarios en donde estamos guardando la información, similar a lo que sería una base de datos, lo que permite que los correos electrónicos sean persistentes.


##### ¿Cómo funciona la interfaz del cliente?

La interfaz del cliente se maneja desde la consola. Cada sección incluye diferentes opciones, que el usuario elige escribiendo en la consola el número de la opción que desea.
- Menu de inicio:
El menu cuenta con 3 opciones, la primera para registrarse (si es que aún no tiene una cuenta), la segunda para iniciar sesión (con su usuario y contraseña) y la tercera para cerrrar la aplicación.

![Interfaz de Menu](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/1MenuInicio.png)
*Imagen 1. Interfaz Menu*


![Interfaz de registro](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/2Registro.png)
*Imagen 2. Opción para registrarse*

![Interfaz de login](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/3InicioSesion.png)
*Imagen 3. Opción para hacer login*

- Menu de correo:
En el menu de correo se tienen las diferentes opciones para ue el usuario se comunique. Primero, la opción para escribir correo, segundo para ver los correos recibidos y tercero opción para ver los correos enviados. Adicionalmente está lac cuarta opción para regresar el menú de inicio y la quinta para cerrar la aplicación.

![Interfaz de menu correo](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/4VerMailRecibido.png)
*Imagen 4. Menu de correo*

![Ver mails recibidos](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/4VerMailRecibido.png)
*Imagen 5. Opción ver mails recibidos*

Se incluye una función para que el usuario vea si ya ha leído el correo en cuestión. Los correos leídos aparecen con una palomita mientras que los correos no leídos tienen una cruz.

![Correos leídos ](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/5CorreoLeido.png)
*Imagen 6. Notificación de leído*

Se incluye una función para eliminar correos de la bandeja de enviados y de la bandeja de recibidos. Así se libera el espacio de la bandeja puesto que hay un limite en correos enviados y recibidos de 5 correos.

![ELiminar correo ](https://github.com/jedgarr99/ProyectoOmega/blob/master/imgs/7BorrarCoreo.png)
*Imagen 7. Eliminar correo*

##### Objetos
Para cumplir con los requerimientos del proyecto,  se definieron en el .proto los objetos utilizados por el cliente y el servidor. Los objetos utilizados fueron:
  
  
Se agrega para aquellas funciones que no devuelven nada o no reciben nada
    message Empty {} 

Devuelve el status de un método para saber si su ejecución fue satisfactoria u ocurrió una falla
    message Status {
        optional bool success = 1; 
    }

Devuelve mensajes del resultado de ejecución de mandar un mensaje 
    message Mensaje {
        optional string message = 1; 
    }

  
Contiene la información principal de nuestros usuarios   
    message Usuario {
        optional string username = 1; 
        optional string password = 2; 
        optional int32 enviados = 3;
        optional int32 recibidos = 4;
    }

Contiene la información principal de nuestros correos
    message Correo {
        optional int32 id = 1;
        optional string tema = 2;
        optional string cuerpo = 3;
        optional bool leido = 4; 
        optional string emisor = 5;
        optional string receptor = 6;
        optional string emisorRespaldo = 7;
        optional string receptorRespaldo = 8;

    }


##### Métodos
Para cumplir con los requerimientos del proyecto se utilizaron los siguientes métodos. Primero, los definimos en el .proto para después utilizarlos en nuestro servidor. Además, para evitar la condición de carrera se utilizaron candados con la implementación del siguiente código.

    ServidorTurboMessage.lock_registro.acquire()
    
El propósito principal de utilizar candados en el código es garantizar la integridad de los datos y prevenir situaciones en las que múltiples hilos o procesos accedan a la misma sección crítica al mismo tiempo, lo que puede generar problemas como la corrupción de datos o condiciones de carrera.

Así, se logra controlar el acceso a las zonas críticas del código, como variables compartidas y los diccionarios de almacenamiento. Además con esto logramos proteger la lógica del funcionamiento del servidor. Por ejemplo, en el método de registrar usuario, dos usuarios podrían tratar de registrarse al mismo tiempo con el mismo username y si no se pone un candado podríamos encontrarnos con dos usernames iguales.

    rpc registrar_usuario (Usuario) returns (Status){}; #Para registrar un usuario checamos que no exista uno con el mismo username porque es un identificador único
    rpc registrar_correo (Correo) returns (Mensaje){};  #Checamos que el emisor tiene menos de 5 enviados y que el receptor tiene menos de 5 recibidos pues es uno de nuestros límites.

    rpc inicio_sesion(Usuario) returns (Status); #Checamos que el username y la password coincidan con lo que tenemos guardado en el servidor

    rpc borrar_correo_recibido(Correo) returns (Status); #Se utiliza una bandera para que si el emisor y el receptor eliminan el mensaje este sea eliminado del servidor también
    rpc borrar_correo_enviado (Correo) returns (Status); #Se utiliza una bandera para que si el emisor y el receptor eliminan el mensaje este sea eliminado del servidor también
    rpc marcar_leido(Correo) returns (Status); #Se actualiza el atributo leído del objeto correo

    #Los siguientes métodos se utilizan para poder visualizar la información almacenada en el servidor
    rpc listado_correos_enviados (Usuario) returns (stream Correo) {};
    rpc listado_correos_recibidos (Usuario) returns (stream Correo) {};
    rpc listado_usuarios (Empty) returns (stream Usuario) {};
    rpc listado_correos (Empty) returns (stream Correo) {};

##### Conclusiones

Turbo Message es un servidor que simula un e-mail con ciertas restricciones entre las cuales están: 
- Un máximo de 5 correos enviados y recibidos
- Manejarse con comunicación GRPC y ProtocolBuffers
- Contar con una interfaz para el cliente
- Realizar funciones similares a las de un correo normal (enviar, recibir, eliminar mensajes. Leído no leído)

Turbo Message es un proyecto interesante que permite a los usuarios enviar y recibir correos electrónicos de manera limitada, pero con la ventaja de tener una arquitectura diseñada para garantizar la escalabilidad, el rendimiento y la persistencia del servicio de mensajería. GRPC nos pareció una tecnología con mucha lógica e intuitiva para el desarrollador. Este proyecto nos hizo preguntarnos como se deben realizar las funciones básicas para uno de los servicios que utilizamos día a día y nos permitió comprender la lógica detrás de estros procesos. Además consideramos positivo el hecho de que algunos procesos los realizamos de una manera diferente a la de un correo convencional de tal forma que el sistema fuera de nuestro total agrado.



