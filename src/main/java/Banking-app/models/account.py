import sqlite3
from models.db import get_connection

def create_account(name, initial_balance=0):
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, initial_balance))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False, "Account already exists"
    conn.close()
    return True, "Account created"

def get_accounts():
    conn = get_connection()
    accounts = conn.execute("SELECT * FROM accounts").fetchall()
    conn.close()
    return [dict(a) for a in accounts]

def get_balance(name):
    conn = get_connection()
    row = conn.execute("SELECT balance FROM accounts WHERE name = ?", (name,)).fetchone()
    conn.close()
    return row["balance"] if row else None

def deposit(name, amount):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, name))
    c.execute("INSERT INTO transactions (sender, receiver, amount, type) VALUES (?, ?, ?, ?)", ("-", name, amount, "Deposit"))
    conn.commit()
    conn.close()
    return True

def withdraw(name, amount):
    balance = get_balance(name)
    if balance is None:
        return False, "Account does not exist"
    if balance < amount:
        return False, "Insufficient funds"
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, name))
    c.execute("INSERT INTO transactions (sender, receiver, amount, type) VALUES (?, ?, ?, ?)", (name, "-", amount, "Withdraw"))
    conn.commit()
    conn.close()
    return True, "Withdraw successful"

def transfer(sender, receiver, amount):
    balance = get_balance(sender)
    if balance is None:
        return False, "Sender does not exist"
    if balance < amount:
        return False, "Insufficient funds"
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, sender))
    c.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, receiver))
    c.execute("INSERT INTO transactions (sender, receiver, amount, type) VALUES (?, ?, ?, ?)", (sender, receiver, amount, "Transfer"))
    conn.commit()
    conn.close()
    return True, "Transfer successful"

def get_transactions():
    conn = get_connection()
    transactions = conn.execute("SELECT * FROM transactions ORDER BY timestamp DESC").fetchall()
    conn.close()
    return [dict(t) for t in transactions]
