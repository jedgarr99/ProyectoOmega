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
        res=stub.registrar_correo(turboMessage_pb2.Correo(tema="Tarea",cuerpo="Lorem Ipsum is simply dummy text of the printing and \n typesetting industry. Lorem Ipsum has been the industry's \nstandard dummy text ever since the 1500s, when an unknown printer\n took a galley of type and scrambled it ", emisor="Jorge", receptor="Anairam"))
        print("Se pudo mandar correo : ",res)
        res=stub.registrar_correo(turboMessage_pb2.Correo(tema="Distribuidos",cuerpo="Lorem Ipsum is simply dummy text of the printing and \n typesetting industry. Lorem Ipsum has been the industry's \nstandard dummy text ever since the 1500s, when an unknown printer\n took a galley of type and scrambled it ", emisor="Jorge", receptor="Anairam"))
        print("Se pudo mandar correo : ",res)
        res=stub.registrar_correo(turboMessage_pb2.Correo(tema="Se escapo el gato",cuerpo="Lorem Ipsum is simply dummy text of the printing and \n typesetting industry. Lorem Ipsum has been the industry's \nstandard dummy text ever since the 1500s, when an unknown printer\n took a galley of type and scrambled it ", emisor="Jorge", receptor="Anairam"))
        print("Se pudo mandar correo : ",res)
        res=stub.registrar_correo(turboMessage_pb2.Correo(tema="Tarea Python",cuerpo="Lorem Ipsum is simply dummy text of the printing and \n typesetting industry. Lorem Ipsum has been the industry's \nstandard dummy text ever since the 1500s, when an unknown printer\n took a galley of type and scrambled it ", emisor="Anairam", receptor="Jorge"))
        print("Se pudo mandar correo : ",res)
        res=stub.registrar_correo(turboMessage_pb2.Correo(tema="Renta de Libro ",cuerpo="Lorem Ipsum is simply dummy text of the printing and \n typesetting industry. Lorem Ipsum has been the industry's \nstandard dummy text ever since the 1500s, when an unknown printer\n took a galley of type and scrambled it ", emisor="Anairam", receptor="Jorge"))
        print("Se pudo mandar correo : ",res)

        
     
        for usuario in stub.listado_usuarios(turboMessage_pb2.Empty()):
            print("Usuario:", usuario.username, "password: ", usuario.password , "Env: ", usuario.enviados, "Rec: ", usuario.recibidos )

        for correo in stub.listado_correos(turboMessage_pb2.Empty()):
            print("Id:", correo.id, "tema: ", correo.tema , "cuerpo: ", correo.cuerpo, "leido: ", correo.leido, "emisor: ", correo.emisor , "rec: ", correo.receptor  )

if __name__ == "__main__":
    run()