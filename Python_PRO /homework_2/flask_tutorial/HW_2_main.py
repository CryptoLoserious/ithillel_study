from utils import generate_password, open_file, generator, finder, commit_sql
from flask import Flask, request
from create_table import create_table

app = Flask(__name__)

# @app.route("/hello")
# def hello_world():
#     return "<p>Hello, World!</p>"
#
# @app.route("/password")
# def password():
#
#     length = request.args.get('length', '10')
#
#     if length.isdigit():
#         length = int(length)
#
#         MAX_PASS_VALUE = 100
#
#         if length > MAX_PASS_VALUE:
#             return f"Length should be less than {MAX_PASS_VALUE}"
#         return generate_password(length)
#
#     return f"Invalid values: {length}, please enter valid int amount!"
#
# @app.route("/requirements")
# def open_files() -> str:
#     contents = open_file()
#     return contents
#
# @app.route("/generate-users")
# def generate():
#     amount = request.args.get('amount', '5')
#
#     if amount.isdigit():
#         amount = int(amount)
#         MIN_AMOUNT = 5
#         MAX_AMOUNT = 100
#
#         if amount > MAX_AMOUNT or amount < MIN_AMOUNT:
#             return f"Amount should be less than {MAX_AMOUNT} and {MIN_AMOUNT}"
#         return generator(amount)
#
#     return f"Invalid values: {amount}, please enter valid int amount!"
#
# @app.route("/space")
# def find_amount_of_cosmonauts() -> str:
#     result = finder()
#     return str(f"The number of astronauts at the moment: {result}")



"""  _____________________________________________homework_3___________________________________________"""

@app.route("/phone/create")
def phones_create():
    phone_value = request.args.get('phone', '0')

    sql = f"""
    INSERT INTO Phones (PhoneValue)
    VALUES ({phone_value});
    """
    commit_sql(sql)

    return 'phones_create'

@app.route("/phone/read")
def phones_read():
    import sqlite3
    con = sqlite3.connect('HW_3.db')
    cur = con.cursor()

    sql = """
    SELECT * FROM Phones;  
    """
    cur.execute(sql)

    result = cur.fetchall()
    con.close()
    return result

@app.route("/phone/update")
def phones_update():
    phone_value = request.args['phone']
    phone_id = request.args['id']

    sql = f"""
    UPDATE Phones
    SET PhoneValue = '{phone_value}'
    WHERE PhoneID = {phone_id};
    """
    commit_sql(sql)

    return "phones_update"

@app.route("/phone/delete")
def phones_delete():
    phone_id = request.args['id']

    sql = f"""
    DELETE FROM Phones
    WHERE PhoneID = {phone_id};
    """
    commit_sql(sql)

    return "phones delete"





if __name__=='__main__':
    create_table()
    app.run(host='0.0.0.0', port=5001)









