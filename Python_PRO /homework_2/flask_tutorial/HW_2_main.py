from utils import generate_password, open_file, generator, finder
from flask import Flask, request

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/password")
def password():

    length = request.args.get('length', '10')

    if length.isdigit():
        length = int(length)
        MAX_PASS_VALUE = 100

        if length > MAX_PASS_VALUE:
            return f"Length should be less than {MAX_PASS_VALUE}"
        return generate_password(length)

    return f"Invalid values: {length}, please enter valid int amount!"

@app.route("/requirements")
def open_files() -> str:
    contents = open_file()
    return contents

@app.route("/generate-users")
def generate() -> str:
    amount = request.args.get('amount', '5')

    if amount.isdigit():
        amount = int(amount)
        # MIN_AMOUNT = 5
        MAX_AMOUNT = 100

        if amount > MAX_AMOUNT:
            return f"Amount should be less than {MAX_AMOUNT} "
        return generator(amount)

    return f"Invalid values: {amount}, please enter valid int amount!"

@app.route("/space")
def find_amount_of_cosmonauts() -> str:
    result = finder()
    return str(f"The number of astronauts at the moment: {result}")




if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001)









