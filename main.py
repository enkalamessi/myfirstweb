import os
from Website import create_app


app = create_app()

if __name__ == "__main__":
    # Get the port from the environment, default to 5000 if not set
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
