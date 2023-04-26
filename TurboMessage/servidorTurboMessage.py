from concurrent import futures
import grpc
import turboMessage_pb2
import turboMessage_pb2_grpc
import threading 

class ServidorTurboMessage (turboMessage_pb2_grpc.TurboMessageServicer):

    folio_correo = 0


    usuarios = {}
    correos = {}

    lock_registro=threading.Lock()

    def registrar_usuario(self, request, context):
        statusUsuario = False 
        ServidorTurboMessage.lock_registro.acquire()

        if request.username not in ServidorTurboMessage.usuarios:

            ServidorTurboMessage.usuarios[request.username]= turboMessage_pb2.Usuario(username=request.username, password=request.password, enviados=0,recibidos=0)
            for usuario in ServidorTurboMessage.usuarios.values(): 
                print(len(ServidorTurboMessage.usuarios.values()), type(usuario), usuario)

            
            statusUsuario = True 
        ServidorTurboMessage.lock_registro.release()
        return turboMessage_pb2.Status(success=statusUsuario)
    
    def registrar_correo (self, request, context):
        statusCorreo = "El receptor no existe" 

        ServidorTurboMessage.lock_registro.acquire()

        ServidorTurboMessage.folio_correo+=1
        if request.receptor in ServidorTurboMessage.usuarios and request.emisor in ServidorTurboMessage.usuarios:
            rec=ServidorTurboMessage.usuarios[request.receptor]
            cantRecibidos=rec.recibidos
            em=ServidorTurboMessage.usuarios[request.emisor]
            cantEnviados=em.enviados
            statusCorreo = "Tu bandeja de enviados esta llena" 

            if cantEnviados <5 :
                    statusCorreo = "La bandeja de entrada del receptor esta llena" 
                    
                    if cantRecibidos<5:
                        
                        em.enviados=em.enviados+1
                        rec.recibidos=rec.recibidos+1

                        ServidorTurboMessage.correos[ServidorTurboMessage.folio_correo]= turboMessage_pb2.Correo(
                            id=ServidorTurboMessage.folio_correo, tema=request.tema, cuerpo=request.cuerpo,leido=False, emisor=request.emisor, receptor=request.receptor,emisorRespaldo=request.emisor,receptorRespaldo=request.receptor)
                        
                        for correo in ServidorTurboMessage.correos.values(): 
                            print(len(ServidorTurboMessage.correos.values()), type(correo), correo)

                        

                        statusCorreo = "Envio Exitoso" 

        ServidorTurboMessage.lock_registro.release()
        return turboMessage_pb2.Mensaje(message=statusCorreo)

    def inicio_sesion (self, request, context):
        statusUsuario = False

        if request.username in ServidorTurboMessage.usuarios:
            user=ServidorTurboMessage.usuarios[request.username]
            if user.password == request.password:
                statusUsuario=True

        return turboMessage_pb2.Status(success=statusUsuario)
    
    def borrar_correo_recibido(self, request, context):
        #sacar del front 
        statusCorreo=False
        if request.id in ServidorTurboMessage.correos:
            esteCorreo=ServidorTurboMessage.correos[request.id]
            usuario = esteCorreo.receptor
            if usuario in ServidorTurboMessage.usuarios:
                objetoUsuario=ServidorTurboMessage.usuarios[usuario]
                objetoUsuario.recibidos=objetoUsuario.recibidos-1
                esteCorreo.receptor="-"

                if esteCorreo.emisor=="-":
                    ServidorTurboMessage.correos.pop(request.id, None)
                statusCorreo=True

        return turboMessage_pb2.Status(success=statusCorreo)
    
    def borrar_correo_enviado(self, request, context):
        #sacar del front 
        statusCorreo=False
        ServidorTurboMessage.lock_registro.acquire()
        if request.id in ServidorTurboMessage.correos:
            esteCorreo=ServidorTurboMessage.correos[request.id]

            usuario = esteCorreo.emisor  #Checar que no busque ralla
            if usuario in ServidorTurboMessage.usuarios:
                objetoUsuario=ServidorTurboMessage.usuarios[usuario]
                objetoUsuario.enviados=objetoUsuario.enviados-1
                esteCorreo.emisor="-"

                if esteCorreo.receptor=="-":
                    ServidorTurboMessage.correos.pop(request.id, None)
                statusCorreo=True
        ServidorTurboMessage.lock_registro.release()
        return turboMessage_pb2.Status(success=statusCorreo)
    
    def marcar_leido(self, request, context):
        statusLeido=False
        if request.id in ServidorTurboMessage.correos:
            esteCorreo=ServidorTurboMessage.correos[request.id]
            esteCorreo.leido=True
            statusLeido=True

        return turboMessage_pb2.Status(success=statusLeido)
    
    def listado_usuarios (self, request, context): # (Empty)   
        for usuario in ServidorTurboMessage.usuarios.values():
            yield usuario

 
    def listado_correos (self, request, context): # (Empty)   
        for correo in ServidorTurboMessage.correos.values():
            yield correo

    def listado_correos_enviados (self, request, context): # (Empty)  
        usuario=request.username

        for correo in ServidorTurboMessage.correos.values():
            if correo.emisor == usuario:
                yield correo

    def listado_correos_recibidos (self, request, context): # (Empty)  
        usuario=request.username

        for correo in ServidorTurboMessage.correos.values():
            if correo.receptor == usuario:
                yield correo
    
   


def ofrece_servicios():
    puerto = "50051"
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    turboMessage_pb2_grpc.add_TurboMessageServicer_to_server(ServidorTurboMessage(),servidor)
    servidor.add_insecure_port("[::]:" + puerto)
    servidor.start()
    servidor.wait_for_termination()

if __name__ == "__main__":
    print("Ofreciendo servicios de correos")
    ofrece_servicios()