# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nullabletypes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='nullabletypes.proto',
  package='xbospb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13nullabletypes.proto\x12\x06xbospb\"\x16\n\x05Int32\x12\r\n\x05value\x18\x01 \x01(\x05\"\x16\n\x05Int64\x12\r\n\x05value\x18\x01 \x01(\x03\"\x17\n\x06\x44ouble\x12\r\n\x05value\x18\x01 \x01(\x01\"\x15\n\x04\x42ool\x12\r\n\x05value\x18\x01 \x01(\x08\x62\x06proto3')
)




_INT32 = _descriptor.Descriptor(
  name='Int32',
  full_name='xbospb.Int32',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='xbospb.Int32.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=53,
)


_INT64 = _descriptor.Descriptor(
  name='Int64',
  full_name='xbospb.Int64',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='xbospb.Int64.value', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=77,
)


_DOUBLE = _descriptor.Descriptor(
  name='Double',
  full_name='xbospb.Double',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='xbospb.Double.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=102,
)


_BOOL = _descriptor.Descriptor(
  name='Bool',
  full_name='xbospb.Bool',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='xbospb.Bool.value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['Int32'] = _INT32
DESCRIPTOR.message_types_by_name['Int64'] = _INT64
DESCRIPTOR.message_types_by_name['Double'] = _DOUBLE
DESCRIPTOR.message_types_by_name['Bool'] = _BOOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Int32 = _reflection.GeneratedProtocolMessageType('Int32', (_message.Message,), dict(
  DESCRIPTOR = _INT32,
  __module__ = 'nullabletypes_pb2'
  # @@protoc_insertion_point(class_scope:xbospb.Int32)
  ))
_sym_db.RegisterMessage(Int32)

Int64 = _reflection.GeneratedProtocolMessageType('Int64', (_message.Message,), dict(
  DESCRIPTOR = _INT64,
  __module__ = 'nullabletypes_pb2'
  # @@protoc_insertion_point(class_scope:xbospb.Int64)
  ))
_sym_db.RegisterMessage(Int64)

Double = _reflection.GeneratedProtocolMessageType('Double', (_message.Message,), dict(
  DESCRIPTOR = _DOUBLE,
  __module__ = 'nullabletypes_pb2'
  # @@protoc_insertion_point(class_scope:xbospb.Double)
  ))
_sym_db.RegisterMessage(Double)

Bool = _reflection.GeneratedProtocolMessageType('Bool', (_message.Message,), dict(
  DESCRIPTOR = _BOOL,
  __module__ = 'nullabletypes_pb2'
  # @@protoc_insertion_point(class_scope:xbospb.Bool)
  ))
_sym_db.RegisterMessage(Bool)


# @@protoc_insertion_point(module_scope)