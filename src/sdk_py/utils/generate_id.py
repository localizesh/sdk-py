import hashlib
import json

class IdGenerator:
    def __init__(self, context):
        self.context = context
        self.content_map = {}

    def generate_id(self, text="", tags=None):
        key = text + (json.dumps(tags) if tags else "")
        
        if key in self.content_map:
            self.content_map[key] += 1
        else:
            self.content_map[key] = 1
        
        content = {
            "context": self.context,
            "text": text,
            "tags": tags,
            "index": self.content_map[key]
        }
        
        content_str = json.dumps(content)
        return hashlib.sha256(content_str.encode()).hexdigest()