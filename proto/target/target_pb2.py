# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/target/target.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.openconfig.gnmi.proto.gnmi import gnmi_pb2 as github_dot_com_dot_openconfig_dot_gnmi_dot_proto_dot_gnmi_dot_gnmi__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19proto/target/target.proto\x12\x06target\x1a\x30github.com/openconfig/gnmi/proto/gnmi/gnmi.proto\"\x85\x03\n\rConfiguration\x12\x33\n\x07request\x18\x01 \x03(\x0b\x32\".target.Configuration.RequestEntry\x12\x31\n\x06target\x18\x02 \x03(\x0b\x32!.target.Configuration.TargetEntry\x12\x13\n\x0binstance_id\x18\x03 \x01(\t\x12-\n\x04meta\x18\x04 \x03(\x0b\x32\x1f.target.Configuration.MetaEntry\x12\x14\n\x08revision\x18\xff\xff\xff\xff\x01 \x01(\x03\x1a\x46\n\x0cRequestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.gnmi.SubscribeRequest:\x02\x38\x01\x1a=\n\x0bTargetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.target.Target:\x02\x38\x01\x1a+\n\tMetaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xbb\x01\n\x06Target\x12\x11\n\taddresses\x18\x01 \x03(\t\x12(\n\x0b\x63redentials\x18\x02 \x01(\x0b\x32\x13.target.Credentials\x12\x0f\n\x07request\x18\x03 \x01(\t\x12&\n\x04meta\x18\x04 \x03(\x0b\x32\x18.target.Target.MetaEntry\x12\x0e\n\x06\x64ialer\x18\x05 \x01(\t\x1a+\n\tMetaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"F\n\x0b\x43redentials\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x13\n\x0bpassword_id\x18\x03 \x01(\tB)Z\'github.com/openconfig/gnmi/proto/targetb\x06proto3')



_CONFIGURATION = DESCRIPTOR.message_types_by_name['Configuration']
_CONFIGURATION_REQUESTENTRY = _CONFIGURATION.nested_types_by_name['RequestEntry']
_CONFIGURATION_TARGETENTRY = _CONFIGURATION.nested_types_by_name['TargetEntry']
_CONFIGURATION_METAENTRY = _CONFIGURATION.nested_types_by_name['MetaEntry']
_TARGET = DESCRIPTOR.message_types_by_name['Target']
_TARGET_METAENTRY = _TARGET.nested_types_by_name['MetaEntry']
_CREDENTIALS = DESCRIPTOR.message_types_by_name['Credentials']
Configuration = _reflection.GeneratedProtocolMessageType('Configuration', (_message.Message,), {

  'RequestEntry' : _reflection.GeneratedProtocolMessageType('RequestEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGURATION_REQUESTENTRY,
    '__module__' : 'proto.target.target_pb2'
    # @@protoc_insertion_point(class_scope:target.Configuration.RequestEntry)
    })
  ,

  'TargetEntry' : _reflection.GeneratedProtocolMessageType('TargetEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGURATION_TARGETENTRY,
    '__module__' : 'proto.target.target_pb2'
    # @@protoc_insertion_point(class_scope:target.Configuration.TargetEntry)
    })
  ,

  'MetaEntry' : _reflection.GeneratedProtocolMessageType('MetaEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGURATION_METAENTRY,
    '__module__' : 'proto.target.target_pb2'
    # @@protoc_insertion_point(class_scope:target.Configuration.MetaEntry)
    })
  ,
  'DESCRIPTOR' : _CONFIGURATION,
  '__module__' : 'proto.target.target_pb2'
  # @@protoc_insertion_point(class_scope:target.Configuration)
  })
_sym_db.RegisterMessage(Configuration)
_sym_db.RegisterMessage(Configuration.RequestEntry)
_sym_db.RegisterMessage(Configuration.TargetEntry)
_sym_db.RegisterMessage(Configuration.MetaEntry)

Target = _reflection.GeneratedProtocolMessageType('Target', (_message.Message,), {

  'MetaEntry' : _reflection.GeneratedProtocolMessageType('MetaEntry', (_message.Message,), {
    'DESCRIPTOR' : _TARGET_METAENTRY,
    '__module__' : 'proto.target.target_pb2'
    # @@protoc_insertion_point(class_scope:target.Target.MetaEntry)
    })
  ,
  'DESCRIPTOR' : _TARGET,
  '__module__' : 'proto.target.target_pb2'
  # @@protoc_insertion_point(class_scope:target.Target)
  })
_sym_db.RegisterMessage(Target)
_sym_db.RegisterMessage(Target.MetaEntry)

Credentials = _reflection.GeneratedProtocolMessageType('Credentials', (_message.Message,), {
  'DESCRIPTOR' : _CREDENTIALS,
  '__module__' : 'proto.target.target_pb2'
  # @@protoc_insertion_point(class_scope:target.Credentials)
  })
_sym_db.RegisterMessage(Credentials)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\'github.com/openconfig/gnmi/proto/target'
  _CONFIGURATION_REQUESTENTRY._options = None
  _CONFIGURATION_REQUESTENTRY._serialized_options = b'8\001'
  _CONFIGURATION_TARGETENTRY._options = None
  _CONFIGURATION_TARGETENTRY._serialized_options = b'8\001'
  _CONFIGURATION_METAENTRY._options = None
  _CONFIGURATION_METAENTRY._serialized_options = b'8\001'
  _TARGET_METAENTRY._options = None
  _TARGET_METAENTRY._serialized_options = b'8\001'
  _CONFIGURATION._serialized_start=88
  _CONFIGURATION._serialized_end=477
  _CONFIGURATION_REQUESTENTRY._serialized_start=299
  _CONFIGURATION_REQUESTENTRY._serialized_end=369
  _CONFIGURATION_TARGETENTRY._serialized_start=371
  _CONFIGURATION_TARGETENTRY._serialized_end=432
  _CONFIGURATION_METAENTRY._serialized_start=434
  _CONFIGURATION_METAENTRY._serialized_end=477
  _TARGET._serialized_start=480
  _TARGET._serialized_end=667
  _TARGET_METAENTRY._serialized_start=434
  _TARGET_METAENTRY._serialized_end=477
  _CREDENTIALS._serialized_start=669
  _CREDENTIALS._serialized_end=739
# @@protoc_insertion_point(module_scope)
