#Function to execute MySQL query where query = "YOUR SQL QUERY GOES HERE"
def ExecuteMySQL(query):
    import mysql.connector
    from mysql.connector import Error
    #Create connection to MySQL DB
    conn = mysql.connector.connect(host='localhost',
                                database='DATABASE_NAME',
                                user='root')
    cursor = conn.cursor(buffered=True)

    #Set some configuration settings of MySQL
    cursor.execute("SET SQL_SAFE_UPDATES = 0;")
    cursor.execute("SET AUTOCOMMIT = 1;")
    cursor.execute("UNLOCK TABLES;")
    conn.commit()
    #Exectue your SQL query
    try:
        cursor.execute(query)
        conn.commit()
        print("[!] Your executed SQL Query:" + query)
        print("")
        print(cursor.rowcount, "record(s) affected")
        if cursor.description is not None:
            try:
                result = cursor.fetchall()
                print(result)
            except Error as error1:
                print(error1)
                pass
    except Error as error:
        print("[!] Error in this code")
        print(error)

#Function to fetch the name and job title from the GUI widget form
def button_click(name_str, job_str):
    #Print the name and job title
    print(name_str + ' is a ' + job_str)
    #Enter the name and job title records in to a MySQL database
    query = "WRITE YOUR SQL QUERY TO INSERT NAME AND JOB TITLE IN TO A MySQL DATABASE"
    try:
        ExecuteMySQL(query)
    except:
        print("[!] An error happened while executing the ExecuteMySQL(query) function")
    
#Creating the GUI widget form
import tkinter as tk
window = tk.Tk()
tk.Label(window, text='Name').grid(row=0)
tk.Label(window, text='Job Title').grid(row=1)
name = tk.Entry(window)
name.grid(row=0,column=1)
job = tk.Entry(window)
job.grid(row=1,column=1)
tk.Button(window, text='Cancel', command=window.destroy).grid(row=2, column=3)
#Notice there are no () in destroy (above). If there were, the function would
#be called instantly – and not when clicked
tk.Button(window, text='Ok', command=lambda:button_click(name.get(), job.get())).grid(row=2, column=1)
window.mainloop()
