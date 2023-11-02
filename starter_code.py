'''
Before you can run this code, please do the following:
    Fill up the information in line 23 below "connStr = "host='cmpstudb-01.cmp.uea.ac.uk' dbname= '' user='' password = " + pw"
    using the Russell Smith's provided credentials', add your password in the pw.txt file.
    
    Get connected to VPN (https://my.uea.ac.uk/divisions/it-and-computing-services/service-catalogue/network-and-telephony-services/vpn) if you are running this code from an off-campus location.
    
    Get the server running in https://pgadmin.cmp.uea.ac.uk/ by log into the server. 
    
'''

import psycopg2
import pandas as pd

def getConn():
    #function to retrieve the password, construct
    #the connection string, make a connection and return it.
    #The pw.txt file will have the password to access the PGAdmin given to you by Russell Smith
    pwFile = open("pw.txt", "r")
    pw = pwFile.read();
    pwFile.close()
    # Fill up the following information from the Russell Smith's email.
    connStr = "host='cmpstudb-01.cmp.uea.ac.uk' \
               dbname= '' user='' password = " + pw
    #connStr=("dbname='studentdb' user='dbuser' password= 'dbPassword' " )
    conn=psycopg2.connect(connStr)      
    return  conn

def clearOutput():
    with open("output.txt", "w") as clearfile:
        clearfile.write('')
        
def writeOutput(output):
    with open("output.txt", "a") as myfile:
        myfile.write(output)
         
try:
    conn=None   
    conn=getConn()
    # All the sql statement once run will be autocommited
    conn.autocommit=True
    cur = conn.cursor()
    
    f = open("input.txt", "r")
    clearOutput()
    for x in f:
        print(x)
        if(x[0] == 'A'):
            raw = x.split("#",1)
            raw[1]=raw[1].strip()
            data = raw[1].split("#")   
            # Statement to insert data into the student table
            try:
                cur.execute("SET SEARCH_PATH TO demo, public;");
                # The SQL statement can be a INSERT statement
                #sql="INSERT INTO student(sno,sname,semail) values ('{}','{}','{}');".format(data[0],data[1],data[2]);
                sql = "Select * from emp where emp_id = {};". format (data[0]);
                writeOutput("TASK "+x[0]+"\n")            
                cur.execute(sql)
                writeOutput(cur.statusmessage+"\n")
                table_df=pd.read_sql_query(sql, conn)
                # Converting dataframe to string so that it can be written to text file.
                table_str=table_df.to_string()
                writeOutput(table_str+"\n")
            except Exception as e:
                writeOutput(str(e)+"\n")

            
            try:
                cur.execute("SET SEARCH_PATH TO demo, public;");
                sql="SELECT * FROM emp;"
                # Sending the query and connection object to read_sql_query method of pandas pd. It reurns table as dataframe.
                table_df=pd.read_sql_query(sql, conn)
                # Converting dataframe to string so that it can be written to text file.
                table_str=table_df.to_string()
                writeOutput(table_str+"\n")
            except Exception as e:
                print (e)

        if(x[0] == 'B'):
            raw = x.split("#",1)
            raw[1]=raw[1].strip()
            data = raw[1].split("#")  
            # Statement to insert data into the student table
            try:
                cur.execute("SET SEARCH_PATH TO demo, public;");
                #sql="INSERT INTO student(sno,sname,semail) values ('{}','{}','{}');".format(data[0],data[1],data[2]);
                sql = "Select * from emp where emp_id = {} or emp_id = {};". format (data[0], data[1]);
                writeOutput("TASK "+x[0]+"\n")            
                cur.execute(sql)
                writeOutput(cur.statusmessage+"\n")
                table_df=pd.read_sql_query(sql, conn)
                # Converting dataframe to string so that it can be written to text file.
                table_str=table_df.to_string()
                writeOutput(table_str+"\n")
            except Exception as e:
                writeOutput(str(e)+"\n")

                
            try:
                cur.execute("SET SEARCH_PATH TO demo, public;");
                sql="SELECT * FROM emp;"
                # Sending the query and connection object to read_sql_query method of pandas pd. It reurns table as dataframe.
                table_df=pd.read_sql_query(sql, conn)
                # Converting dataframe to string so that it can be written to text file.
                table_str=table_df.to_string()
                writeOutput(table_str+"\n")
            except Exception as e:
                print (e)
        elif(x[0] == 'X'):
            print("Exit {}".format(x[0]))
            writeOutput("\n\nExit program!")
except Exception as e:
    print (e)               