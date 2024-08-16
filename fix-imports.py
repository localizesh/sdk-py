FILE_PATH = 'src/protos/localize/document_pb2.py'

with open(FILE_PATH, "r") as f:
    data = f.read()

data = data.replace('from localize', 'from .')

with open(FILE_PATH, 'w') as f:
    f.write(data)
