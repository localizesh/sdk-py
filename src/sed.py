ROW_TO_DELETE = 'from localize import segment_pb2 as localize_dot_segment__pb2'
FILE_PATH = 'src/protos/localize/document_pb2.py'

with open(FILE_PATH, "r") as f:
    old_data = f.read()

new_data = old_data.replace(ROW_TO_DELETE, '')

with open(FILE_PATH, 'w') as f:
    f.write(new_data)


