from flask import Flask, request

app = Flask(__name__)


@app.route('/phones/create/')
def phones_create():
    name = request.args['name']
    name = request.args['name']
    phone = request.args['phone']

    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    print(1111111111111111)
    # Create table
    sql = f'''
    INSERT INTO phones (name, phone)
    VALUES ('{name}', '{phone}');
    '''
    cur.execute(sql)
    con.commit()
    con.close()
    return 'OK'


@app.route('/phones/read/')
def phones_read():
    id_ = request.args.get('id')

    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    # Create table
    if id_:
        sql = f'''SELECT * FROM phones WHERE id={id_};'''
    else:
        sql = f'''SELECT * FROM phones;'''
    cur.execute(sql)
    results = cur.fetchall()
    con.close()
    return str(results)


@app.route('/phones/update/')
def phones_update():
    id_ = request.args['id']
    name = request.args['name']

    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    # Create table
    sql = f'''UPDATE phones SET name='{name}' WHERE id={id_};'''
    cur.execute(sql)
    con.commit()
    con.close()
    return 'OK'


@app.route('/phones/delete/')
def phones_delete():
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    # Create table
    sql = f'''DELETE FROM phones;'''
    cur.execute(sql)
    con.commit()
    con.close()
    print('HELLO2222222')
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

'''
VCS
version control system GIT
'''
