from dotenv import load_dotenv
load_dotenv()
from app import create_app

server = create_app()

if __name__ == '__main__':
    server.run(debug=True,host="0.0.0.0")