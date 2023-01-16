from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MinMax(_message.Message):
    __slots__ = ["maximum", "minimum"]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    maximum: int
    minimum: int
    def __init__(self, minimum: _Optional[int] = ..., maximum: _Optional[int] = ...) -> None: ...

class RandNum(_message.Message):
    __slots__ = ["num"]
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...
