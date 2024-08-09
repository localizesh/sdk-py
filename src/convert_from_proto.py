import json
from localizesh_sdk import Document


def from_proto_segment(proto_segment):
    segment = {'id': proto_segment.id,'text': proto_segment.text}

    if proto_segment.tags:
        tags = {tag_key: {'values': dict(attrs.values)} for tag_key, attrs in proto_segment.tags.items()}
        segment['tags'] = tags
    return segment

def from_proto_segments(proto_segments):
    return [from_proto_segment(proto_segment) for proto_segment in proto_segments]

def from_proto_document(proto_document):
    layout_dict = json.loads(proto_document.layout)
    metadata_dict = proto_document.metadata
    segments_list = from_proto_segments(proto_document.segments)
    document = Document(layout=layout_dict, segments=segments_list, metadata=metadata_dict)
    return document

