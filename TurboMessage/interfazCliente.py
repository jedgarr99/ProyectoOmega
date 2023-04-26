import grpc
import turboMessage_pb2
import turboMessage_pb2_grpc
from colorama import Fore, Back, Style

def menuDeInicio(opcionActual):
    usuarioActual=""
    
    print(Style.RESET_ALL)
    print(Back.YELLOW + '\n')
    print(Back.YELLOW + "1. Inicio de Sesión")
    print(Back.YELLOW + "2. Registrarse")
    print(Back.YELLOW + "3. Cerrar Aplicacion")
    print(Back.GREEN + '\n')
    opcionIngresada = input(Back.GREEN + 'Ingrese el numero de la opcion deseada: ')
    #print(Back.GREEN + '\n')
    print(Style.RESET_ALL)

    if opcionIngresada=="1":
        print(Fore.GREEN+"Usted ingresó 1. Inicio de Sesión")
        opcionActual=opcionIngresada
    elif opcionIngresada=="2":
        print(Fore.GREEN+"Usted ingresó 2. Registrarse")
        opcionActual=opcionIngresada
    elif opcionIngresada=="3":
        print(Fore.GREEN+"3. Cerrar Aplicacion")
        opcionActual=opcionIngresada

    else:
        print(Fore.RED+"Usted ingresó un mensaje invalido")

    print(Style.RESET_ALL)
    return opcionActual,usuarioActual

def menuInicioDeSesion(opcionActual,stub):
    usuarioActual=""
    print(Style.RESET_ALL)
    print(Back.GREEN + '\n')
    usuarioIngresado=  input(Back.GREEN + "Ingrese su usuario: ")
    passwordIngresado=  input(Back.GREEN + "Ingrese su contraseña: ")

    status=stub.inicio_sesion(turboMessage_pb2.Usuario(username=usuarioIngresado,password=passwordIngresado))
    usuarioValido=status.success


    if usuarioValido:
        print(Style.RESET_ALL)
        print(Fore.GREEN+"Hola ",usuarioIngresado, "  ",passwordIngresado)
        print(Style.RESET_ALL)
        usuarioActual=usuarioIngresado
        opcionActual="MenuPrincipal"
    else:
        print(Style.RESET_ALL)
        print(Fore.RED+"Usuario Invalido, intente de nuevo")
        print(Style.RESET_ALL)
        opcionActual="0"

    return opcionActual,usuarioActual

def menuRegistro(opcionActual,stub):


    print(Style.RESET_ALL)
    print(Back.GREEN + '\n')
    usuarioIngresado=  input(Back.GREEN + "Ingrese su nuevo  usuario: ")
    passwordIngresado=  input(Back.GREEN + "Ingrese su nueva contraseña: ")

    status=stub.registrar_usuario(turboMessage_pb2.Usuario(username=usuarioIngresado,password=passwordIngresado))
    usuarioValido=status.success


    if usuarioValido:
        print(Style.RESET_ALL)
        print(Fore.GREEN+"Hola ",usuarioIngresado, "Tu contraseña es: ",passwordIngresado)
        print(Style.RESET_ALL)
        opcionActual="99999"
    else:
        print(Style.RESET_ALL)
        print(Fore.RED+"Usuario ya existe, intente de nuevo ")
        print(Style.RESET_ALL)
        opcionActual="0"

    return opcionActual

def menuPrincipal(opcionActual):
    print(Style.RESET_ALL)
    print(Back.YELLOW + '\n')
    print(Back.YELLOW + "1. Escribir Correo")
    print(Back.YELLOW + "2. Ver Mails Recibidos")
    print(Back.YELLOW + "3. Ver Mails Enviados")
    print(Back.YELLOW + "4. Regresar a menu de Inicio")
    print(Back.YELLOW + "5. Cerrar Aplicacion")
    
    print(Back.GREEN + '\n')
    opcionIngresada = input(Back.GREEN + 'Ingrese el numero de la opcion deseada: ')
    print(Style.RESET_ALL)
    if opcionIngresada=="1":
        print(Fore.GREEN+"Usted ingresó 1. Escribir Correo")
        opcionActual="EscribirCorreo"

    elif opcionIngresada=="2":
        print(Fore.GREEN+"Usted ingresó 2. Ver Mails Recibidos")
        opcionActual="MailsRecibidos"
    elif opcionIngresada=="3":
        print(Fore.GREEN+"3. Ver Mails Enviados")
        opcionActual="MailsEnviados"

    elif opcionIngresada=="4":
        print(Fore.GREEN+"4.Regresar a menu de Inicio")
        opcionActual="0"

    elif opcionIngresada=="5":
        print(Fore.GREEN+"5.Cerrar Aplicacion")
        opcionActual="3"

    else:
        print(Fore.RED+"Usted ingresó un mensaje invalido")

    print(Style.RESET_ALL)
    return opcionActual

def menuEscribirCoreo(stub,usuarioActual):
    print(Style.RESET_ALL)
    print(Back.YELLOW + '\n')
    print(Back.YELLOW + "Mandar Correo")
    print(Style.RESET_ALL)
    print(Back.GREEN + '\n')
    destinatarioIngresado = input(Back.GREEN + 'Ingrese el usuario al que se le enviará el correo: ')
    temaIngresado = input(Back.GREEN + 'Ingrese el tema del correo: ')
    cuerpoIngresado = input(Back.GREEN + 'Ingrese el cuerpo del correo: ')
    print(temaIngresado,"  ",cuerpoIngresado ," usAct: ",usuarioActual,"  ",destinatarioIngresado)
    status=stub.registrar_correo(turboMessage_pb2.Correo(tema=temaIngresado,cuerpo=cuerpoIngresado, emisor=usuarioActual, receptor=destinatarioIngresado, emisorRespaldo=usuarioActual,receptorRespaldo=destinatarioIngresado)) 
    mensajeServidor=status.message

    if mensajeServidor=="Envio Exitoso" :
        print(Style.RESET_ALL)
        print(Fore.GREEN+mensajeServidor)
        print(Style.RESET_ALL)
    else:
        print(Style.RESET_ALL)
        print(Fore.RED+mensajeServidor)
        print(Style.RESET_ALL)

    return "MenuPrincipal"

def menuMailsRecibidos(stub,usuarioActual):
    print(Style.RESET_ALL)
    print(Back.YELLOW+"  #  ",Back.RED+"Leido",Back.BLUE+"       Tema        ",Back.MAGENTA+" Emisor         ",Style.RESET_ALL)
    print(Style.RESET_ALL)
    correosActuales={}
    folioCorreo=0

    for correo in stub.listado_correos_recibidos(turboMessage_pb2.Usuario(username=usuarioActual)):
            
            folioCorreo=folioCorreo+1
            correosActuales[folioCorreo]=(correo.id,correo.tema ,correo.cuerpo,correo.leido,  correo.emisorRespaldo ,correo.receptorRespaldo )
          

            if correo.leido:
                print(Fore.YELLOW+str(folioCorreo),Fore.GREEN+"  ✓  ",Fore.BLUE+correo.tema,Fore.MAGENTA+correo.emisorRespaldo)
            else:
                print(Fore.YELLOW+str(folioCorreo),Fore.RED+"  X  ",Fore.BLUE+correo.tema,Fore.MAGENTA+correo.emisorRespaldo)
                
    print(Style.RESET_ALL)

    correoIngresado="nadaAun"

    correoIngresado=input(Back.GREEN + "Ingrese el numero del correo que desea ver o 0 para regresar al menu anterior: ")
    print(Back.GREEN + '\n')
    print(Style.RESET_ALL)

    if correoIngresado!="0":
        try:
            esteCorreo=correosActuales[int(correoIngresado)]
            stub.marcar_leido(turboMessage_pb2.Correo(id=int(esteCorreo[0])))
            desplegarCorreo(esteCorreo[1],esteCorreo[4],esteCorreo[5],esteCorreo[2])
            opcionIngresada="0"
            print(Back.GREEN + '\n')
            opcionIngresada = input(Back.GREEN + 'Ingrese 1 para borrar este correo o enter para continuar: ')
            print(Back.GREEN + '\n')
            #print(Back.GREEN + '\n')
            print(Style.RESET_ALL)
            if opcionIngresada=="1":
                
                status=stub.borrar_correo_recibido(turboMessage_pb2.Correo(id=int(esteCorreo[0])))
                if status.success:
                    print(Fore.GREEN + 'Correo Borrado exitosamente')
                else:
                    print(Fore.RED+"No se pudo borrar el correo")




            print(Style.RESET_ALL)
        except:
            print(Fore.RED+"Usted ingresó un mensaje invalido")
            print(Style.RESET_ALL)
        
    return "MenuPrincipal"

def menuMailsEnviados(stub,usuarioActual):
    print(Style.RESET_ALL)
    print(Back.YELLOW+"  #  ",Back.RED+"Leido",Back.BLUE+"       Tema        ",Back.MAGENTA+" Receptor         ",Style.RESET_ALL)
    print(Style.RESET_ALL)
    correosActuales={}
    folioCorreo=0
    #print("us Act:",usuarioActual)
    for correo in stub.listado_correos_enviados(turboMessage_pb2.Usuario(username=usuarioActual)):
            
            folioCorreo=folioCorreo+1
            correosActuales[folioCorreo]=(correo.id,correo.tema ,correo.cuerpo,correo.leido,  correo.emisorRespaldo ,correo.receptorRespaldo )
            #print("Id:", correo.id, "tema: ", correo.tema , "cuerpo: ", correo.cuerpo, "leido: ", correo.leido, "emisor: ", correo.emisor , "rec: ", correo.receptor  )

            if correo.leido:
                print(Fore.YELLOW+str(folioCorreo),Fore.GREEN+"  ✓  ",Fore.BLUE+correo.tema,Fore.MAGENTA+correo.receptorRespaldo)
            else:
                print(Fore.YELLOW+str(folioCorreo),Fore.RED+"  X  ",Fore.BLUE+correo.tema,Fore.MAGENTA+correo.receptorRespaldo)
                
    print(Style.RESET_ALL)

    correoIngresado="nadaAun"

    correoIngresado=input(Back.GREEN + "Ingrese el numero del correo que desea ver o 0 para regresar al menu anterior: ")
    print(Back.GREEN + '\n')
    print(Style.RESET_ALL)

    if correoIngresado!="0":
        try:
            esteCorreo=correosActuales[int(correoIngresado)]

            desplegarCorreo(esteCorreo[1],esteCorreo[4],esteCorreo[5],esteCorreo[2])

            opcionIngresada="0"
            print(Back.GREEN + '\n')
            opcionIngresada = input(Back.GREEN + 'Ingrese 1 para borrar este correo o enter para continuar: ')
            print(Back.GREEN + '\n')
            #print(Back.GREEN + '\n')
            print(Style.RESET_ALL)
            if opcionIngresada=="1":
                
                status=stub.borrar_correo_enviado(turboMessage_pb2.Correo(id=int(esteCorreo[0])))
                if status.success:
                    print(Fore.GREEN + 'Correo Borrado exitosamente')
                else:
                    print(Fore.RED+"No se pudo borrar el correo")


        except:
            print(Fore.RED+"Usted ingresó un mensaje invalido")
            print(Style.RESET_ALL)
    return "MenuPrincipal"

def desplegarCorreo(Tema, Emisor, Receptor,Cuerpo):
    print(Style.RESET_ALL)
    print(Back.LIGHTBLUE_EX+"\n")
    print(Back.LIGHTBLUE_EX+"DE: ",Emisor)
    print("PARA: ",Receptor)
    print(Style.RESET_ALL)
    print(Fore.MAGENTA+"TEMA: ",Tema,Style.RESET_ALL)
    print("\n")
    print(Fore.BLUE+Cuerpo)
    print(Style.RESET_ALL)

if __name__ == "__main__":
    print("Arrancando cliente")    
    with grpc.insecure_channel("localhost:50051") as channel:

       
        stub=turboMessage_pb2_grpc.TurboMessageStub(channel)
        opcionActual="0"
        continuar=True 
        usuarioActual=""

        print(Style.RESET_ALL)
        while continuar:

            if opcionActual=="0":
                opcionActual,usuarioActual=menuDeInicio(opcionActual)
            elif opcionActual=="1":
                opcionActual,usuarioActual=menuInicioDeSesion(opcionActual,stub)
            elif opcionActual=="2":
                opcionActual=menuRegistro(opcionActual,stub)
            elif opcionActual=="3":
                break
            elif opcionActual=="MenuPrincipal":
                opcionActual=menuPrincipal(opcionActual)
            elif opcionActual=="EscribirCorreo":
                opcionActual=menuEscribirCoreo(stub,usuarioActual)
            elif opcionActual=="MailsRecibidos":
                opcionActual=menuMailsRecibidos(stub,usuarioActual)
            elif opcionActual=="MailsEnviados":
                opcionActual=menuMailsEnviados(stub,usuarioActual)
            else:
                opcionActual="0"
            