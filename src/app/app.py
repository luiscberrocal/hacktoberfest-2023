from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def main_end_point():
    return {'hello': 'world', "payload": "test",
            'dynamic333': True,
            "new_content" : "KKK"
            }
