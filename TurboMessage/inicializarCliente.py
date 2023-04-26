import grpc
import turboMessage_pb2
import turboMessage_pb2_grpc

def run():
    print("Inicializando cliente")
    with grpc.insecure_channel("localhost:50051") as channel:

       
        stub=turboMessage_pb2_grpc.TurboMessageStub(channel)
        print("Vamo a registrar")
        res=stub.registrar_usuario(turboMessage_pb2.Usuario(username="Anairam",password="Anairam"))
        print("Se pudo registrar usuario : ",res)
        res=stub.registrar_usuario(turboMessage_pb2.Usuario(username="Jorge",password="Jorge"))
        print("Se pudo registrar usuario : ",res)


        #Agregar estado
        res=stub.registrar_correo(turboMessage_pb2.Correo(tema="Te amo 1 ",cuerpo="para siempre", emisor="Jorge", receptor="Anairam"))
        print("Se pudo mandar correo : ",res)
        res=stub.registrar_correo(turboMessage_pb2.Correo(tema="Te amo 2 ",cuerpo="para siempre", emisor="Jorge", receptor="Anairam"))
        print("Se pudo mandar correo : ",res)
        res=stub.registrar_correo(turboMessage_pb2.Correo(tema="Te amo 3 ",cuerpo="para siempre", emisor="Jorge", receptor="Anairam"))
        print("Se pudo mandar correo : ",res)
        res=stub.registrar_correo(turboMessage_pb2.Correo(tema="Te amordido el perro 1 ",cuerpo="para siempre", emisor="Anairam", receptor="Jorge"))
        print("Se pudo mandar correo : ",res)
        res=stub.registrar_correo(turboMessage_pb2.Correo(tema="Te amordido el perro 2 ",cuerpo="para siempre", emisor="Anairam", receptor="Jorge"))
        print("Se pudo mandar correo : ",res)

        
     
        for usuario in stub.listado_usuarios(turboMessage_pb2.Empty()):
            print("Usuario:", usuario.username, "password: ", usuario.password , "Env: ", usuario.enviados, "Rec: ", usuario.recibidos )

        for correo in stub.listado_correos(turboMessage_pb2.Empty()):
            print("Id:", correo.id, "tema: ", correo.tema , "cuerpo: ", correo.cuerpo, "leido: ", correo.leido, "emisor: ", correo.emisor , "rec: ", correo.receptor  )

if __name__ == "__main__":
    run()