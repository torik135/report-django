import uuid

def generate_code():
    code = str(uuid.uuid4()).replace('-', 'CODE')[:12]
    return code
