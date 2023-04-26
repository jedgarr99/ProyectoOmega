from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Correo(_message.Message):
    __slots__ = ["cuerpo", "emisor", "emisorRespaldo", "id", "leido", "receptor", "receptorRespaldo", "tema"]
    CUERPO_FIELD_NUMBER: _ClassVar[int]
    EMISORRESPALDO_FIELD_NUMBER: _ClassVar[int]
    EMISOR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEIDO_FIELD_NUMBER: _ClassVar[int]
    RECEPTORRESPALDO_FIELD_NUMBER: _ClassVar[int]
    RECEPTOR_FIELD_NUMBER: _ClassVar[int]
    TEMA_FIELD_NUMBER: _ClassVar[int]
    cuerpo: str
    emisor: str
    emisorRespaldo: str
    id: int
    leido: bool
    receptor: str
    receptorRespaldo: str
    tema: str
    def __init__(self, id: _Optional[int] = ..., tema: _Optional[str] = ..., cuerpo: _Optional[str] = ..., leido: bool = ..., emisor: _Optional[str] = ..., receptor: _Optional[str] = ..., emisorRespaldo: _Optional[str] = ..., receptorRespaldo: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Mensaje(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class Usuario(_message.Message):
    __slots__ = ["enviados", "password", "recibidos", "username"]
    ENVIADOS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    RECIBIDOS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    enviados: int
    password: str
    recibidos: int
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., enviados: _Optional[int] = ..., recibidos: _Optional[int] = ...) -> None: ...
