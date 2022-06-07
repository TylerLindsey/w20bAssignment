from dbcreds import *
import mariadb

def connect_db():
  conn=None
  cursor=None
  
  try:
    conn= mariadb.connect(host=host,port=port,database=database,user=user, password=password)
    cursor = conn.cursor()
    return(conn,cursor)
    
  except mariadb.OperationalError as e:
    print("You got an operational error")
    if("Access denied" in e.msg):
      print('failed to login')
    disconnect_db()

def disconnect_db(conn,cursor):
  if (cursor != None):
    cursor.close()
  if (cursor != None):
    conn.rollback()
    conn.close()
# *************************************************************************

def run_query(statement, args=None):
  # args None is so we dont HAVE to pass an argument in our query. It can be set to an value
  # if arguments not passed, set arguements to none
  try:
    (conn, cursor) = connect_db()
    # below is if it is a select, then just execute, other wise it is going to change the database AND it will make a commit
    if statement.startswith('SELECT'):
      cursor.execute(statement, args)
    else:
      cursor.execute(statement,args)
      conn.commit
  #########  # # cursor.execute("INSERT INTO exploits (content, user_id) VALUES (?,?)", ['injection protection number x',5])
  #########  # cursor.execute('SELECT * from exploits WHERE user_id=?', [1])
  #########  # # cursor.execute("INSERT INTO exploits (content, user_id) VALUES ('hello3', 2)") works as hard code
  #########  # # conn.commit()
  #########  # # tried to commit without having something to commit
  #########  # print('The select was successful')
    
  except mariadb.OperationalError as e:
    print("You got an operational error")
    if("Access denied" in e.msg):
      print('failed to login')
      
  except mariadb.IntegrityError as e:
    print('Integrity error')
    if ('Duplicate entry' in e.msg):
      print('That user is already in the DB')
      # this is where I could do an elif for constraints from the DB
    else:
      print(e.msg)
    
  except mariadb.ProgrammingError as e:
    if ("SQL syntax" in e.msg):
      print("There is a programming error. You might have a typo")
    else:
      print("Got a programming error that is not syntax related")
    print(e.msg)
    
  except RuntimeError as e:
    print('There was a Runtime error')
    e.with_traceback

  except Exception as e:
    # This line above makes the Exception alias e for short hand
    # Always have a catch all at the end with an alias
    print(e.with_traceback)
      # with_traceback -> Whenever the code gets an exception, the traceback will give the information about what went wrong in the code. -> https://www.geeksforgeeks.org/python-traceback/
    print(e.msg)
  
  finally:
    disconnect_db(conn, cursor)
  
hacks = run_query('SELECT * from exploits')

# hacks = run_query('SELECT * from exploits WHERE user_id=?',[1])

        

    
    
    
    
    
    
    
    
    
    
    
    