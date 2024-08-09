import json
from localize.segment_pb2 import Segment as ProtoSegment
from localize.document_pb2 import Document as ProtoDocument
from google.protobuf import struct_pb2


def to_proto_segment(segment):
    proto_segment = ProtoSegment(id=segment['id'], text=segment['text'])
    if 'tags' in segment:
        for tag_key, attrs in segment['tags'].items():
            proto_segment.tags[tag_key].values.update(attrs['values'])
    return proto_segment

def to_proto_segments(segments):
    return [to_proto_segment(segment) for segment in segments]

def to_proto_document(document):
    proto_document = ProtoDocument(layout=json.dumps(document.layout))
    proto_document.segments.extend(to_proto_segments(document.segments))
    metadata = struct_pb2.Struct()
    metadata.update(document.metadata)
    proto_document.metadata.CopyFrom(metadata)
    return proto_document