# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import turboMessage_pb2 as turboMessage__pb2


class TurboMessageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.registrar_usuario = channel.unary_unary(
                '/TurboMessage.TurboMessage/registrar_usuario',
                request_serializer=turboMessage__pb2.Usuario.SerializeToString,
                response_deserializer=turboMessage__pb2.Status.FromString,
                )
        self.registrar_correo = channel.unary_unary(
                '/TurboMessage.TurboMessage/registrar_correo',
                request_serializer=turboMessage__pb2.Correo.SerializeToString,
                response_deserializer=turboMessage__pb2.Mensaje.FromString,
                )
        self.inicio_sesion = channel.unary_unary(
                '/TurboMessage.TurboMessage/inicio_sesion',
                request_serializer=turboMessage__pb2.Usuario.SerializeToString,
                response_deserializer=turboMessage__pb2.Status.FromString,
                )
        self.borrar_correo_recibido = channel.unary_unary(
                '/TurboMessage.TurboMessage/borrar_correo_recibido',
                request_serializer=turboMessage__pb2.Correo.SerializeToString,
                response_deserializer=turboMessage__pb2.Status.FromString,
                )
        self.borrar_correo_enviado = channel.unary_unary(
                '/TurboMessage.TurboMessage/borrar_correo_enviado',
                request_serializer=turboMessage__pb2.Correo.SerializeToString,
                response_deserializer=turboMessage__pb2.Status.FromString,
                )
        self.marcar_leido = channel.unary_unary(
                '/TurboMessage.TurboMessage/marcar_leido',
                request_serializer=turboMessage__pb2.Correo.SerializeToString,
                response_deserializer=turboMessage__pb2.Status.FromString,
                )
        self.listado_correos_enviados = channel.unary_stream(
                '/TurboMessage.TurboMessage/listado_correos_enviados',
                request_serializer=turboMessage__pb2.Usuario.SerializeToString,
                response_deserializer=turboMessage__pb2.Correo.FromString,
                )
        self.listado_correos_recibidos = channel.unary_stream(
                '/TurboMessage.TurboMessage/listado_correos_recibidos',
                request_serializer=turboMessage__pb2.Usuario.SerializeToString,
                response_deserializer=turboMessage__pb2.Correo.FromString,
                )
        self.listado_usuarios = channel.unary_stream(
                '/TurboMessage.TurboMessage/listado_usuarios',
                request_serializer=turboMessage__pb2.Empty.SerializeToString,
                response_deserializer=turboMessage__pb2.Usuario.FromString,
                )
        self.listado_correos = channel.unary_stream(
                '/TurboMessage.TurboMessage/listado_correos',
                request_serializer=turboMessage__pb2.Empty.SerializeToString,
                response_deserializer=turboMessage__pb2.Correo.FromString,
                )


class TurboMessageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def registrar_usuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def registrar_correo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def inicio_sesion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def borrar_correo_recibido(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def borrar_correo_enviado(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def marcar_leido(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listado_correos_enviados(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listado_correos_recibidos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listado_usuarios(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listado_correos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TurboMessageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'registrar_usuario': grpc.unary_unary_rpc_method_handler(
                    servicer.registrar_usuario,
                    request_deserializer=turboMessage__pb2.Usuario.FromString,
                    response_serializer=turboMessage__pb2.Status.SerializeToString,
            ),
            'registrar_correo': grpc.unary_unary_rpc_method_handler(
                    servicer.registrar_correo,
                    request_deserializer=turboMessage__pb2.Correo.FromString,
                    response_serializer=turboMessage__pb2.Mensaje.SerializeToString,
            ),
            'inicio_sesion': grpc.unary_unary_rpc_method_handler(
                    servicer.inicio_sesion,
                    request_deserializer=turboMessage__pb2.Usuario.FromString,
                    response_serializer=turboMessage__pb2.Status.SerializeToString,
            ),
            'borrar_correo_recibido': grpc.unary_unary_rpc_method_handler(
                    servicer.borrar_correo_recibido,
                    request_deserializer=turboMessage__pb2.Correo.FromString,
                    response_serializer=turboMessage__pb2.Status.SerializeToString,
            ),
            'borrar_correo_enviado': grpc.unary_unary_rpc_method_handler(
                    servicer.borrar_correo_enviado,
                    request_deserializer=turboMessage__pb2.Correo.FromString,
                    response_serializer=turboMessage__pb2.Status.SerializeToString,
            ),
            'marcar_leido': grpc.unary_unary_rpc_method_handler(
                    servicer.marcar_leido,
                    request_deserializer=turboMessage__pb2.Correo.FromString,
                    response_serializer=turboMessage__pb2.Status.SerializeToString,
            ),
            'listado_correos_enviados': grpc.unary_stream_rpc_method_handler(
                    servicer.listado_correos_enviados,
                    request_deserializer=turboMessage__pb2.Usuario.FromString,
                    response_serializer=turboMessage__pb2.Correo.SerializeToString,
            ),
            'listado_correos_recibidos': grpc.unary_stream_rpc_method_handler(
                    servicer.listado_correos_recibidos,
                    request_deserializer=turboMessage__pb2.Usuario.FromString,
                    response_serializer=turboMessage__pb2.Correo.SerializeToString,
            ),
            'listado_usuarios': grpc.unary_stream_rpc_method_handler(
                    servicer.listado_usuarios,
                    request_deserializer=turboMessage__pb2.Empty.FromString,
                    response_serializer=turboMessage__pb2.Usuario.SerializeToString,
            ),
            'listado_correos': grpc.unary_stream_rpc_method_handler(
                    servicer.listado_correos,
                    request_deserializer=turboMessage__pb2.Empty.FromString,
                    response_serializer=turboMessage__pb2.Correo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TurboMessage.TurboMessage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TurboMessage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def registrar_usuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TurboMessage.TurboMessage/registrar_usuario',
            turboMessage__pb2.Usuario.SerializeToString,
            turboMessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def registrar_correo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TurboMessage.TurboMessage/registrar_correo',
            turboMessage__pb2.Correo.SerializeToString,
            turboMessage__pb2.Mensaje.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def inicio_sesion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TurboMessage.TurboMessage/inicio_sesion',
            turboMessage__pb2.Usuario.SerializeToString,
            turboMessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def borrar_correo_recibido(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TurboMessage.TurboMessage/borrar_correo_recibido',
            turboMessage__pb2.Correo.SerializeToString,
            turboMessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def borrar_correo_enviado(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TurboMessage.TurboMessage/borrar_correo_enviado',
            turboMessage__pb2.Correo.SerializeToString,
            turboMessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def marcar_leido(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/TurboMessage.TurboMessage/marcar_leido',
            turboMessage__pb2.Correo.SerializeToString,
            turboMessage__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listado_correos_enviados(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/TurboMessage.TurboMessage/listado_correos_enviados',
            turboMessage__pb2.Usuario.SerializeToString,
            turboMessage__pb2.Correo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listado_correos_recibidos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/TurboMessage.TurboMessage/listado_correos_recibidos',
            turboMessage__pb2.Usuario.SerializeToString,
            turboMessage__pb2.Correo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listado_usuarios(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/TurboMessage.TurboMessage/listado_usuarios',
            turboMessage__pb2.Empty.SerializeToString,
            turboMessage__pb2.Usuario.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listado_correos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/TurboMessage.TurboMessage/listado_correos',
            turboMessage__pb2.Empty.SerializeToString,
            turboMessage__pb2.Correo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
