

def init_db():
    import sqlite3  # Importar diretamente dentro da função
    conn = sqlite3.connect('home_food.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_order(name, quantity):
    import sqlite3
    conn = sqlite3.connect('home_food.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO orders (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    conn.close()

def get_orders():
    import sqlite3
    conn = sqlite3.connect('home_food.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    conn.close()
    return orders
