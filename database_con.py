import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='12081996Nn1996',
    database='python_user_reg'
)

mycursor=mydb.cursor()

def save_new_user(username,password):
    sql="INSERT INTO User(username,password)VALUES(%s,%s)"
    user=(username,password)
    mycursor.execute(sql,user)
    mydb.commit()
    # return 'USer with username as {} and password{} as been saved Successfully'.format(username,password)

