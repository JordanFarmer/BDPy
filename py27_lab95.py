import sqlite3
connection1 = sqlite3.connect('.\\db\\lab95.sqlite')
print "open db success, try to add something later"
drop_sql = 'drop table if exists EMPLOYEE;'
create_sql = '''
CREATE TABLE EMPLOYEE
(ID INT PRIMARY KEY, 
NAME TEXT NOT NULL,
AGE INT NOT NULL,
DEPT INT, 
ADDRESS CHAR(50));
'''
drop_and_create_sql = '''
drop table if exists EMPLOYEE;
CREATE TABLE EMPLOYEE
(ID INT PRIMARY KEY, 
NAME TEXT NOT NULL,
AGE INT NOT NULL,
DEPT INT, 
ADDRESS CHAR(50));

'''
#connection1.execute(drop_sql);
#connection1.execute(create_sql);
connection1.executescript(drop_and_create_sql);
connection1.close()