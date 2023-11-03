

def create_table():
    import sqlite3
    con = sqlite3.connect('HW_3.db')
    cur = con.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS Phones (
    PhoneId INTEGER PRIMARY KEY,
    PhoneValue varchar(255)
    );
    """
    cur.execute(sql)

    con.commit()
    con.close()
