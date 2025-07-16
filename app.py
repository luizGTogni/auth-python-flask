from os import getenv
from src import app

if __name__ == "__main__":
    is_development = getenv("MODE") == "development"
    app.run(debug=is_development)