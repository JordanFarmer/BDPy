import sqlite3
import time

connection1 = sqlite3.connect('.\\db\\lab95.sqlite')

employees = [{'NAME': 'Mark', 'Age': 43, 'DEPT': 1, 'ADDR': 'Hsinchu'},
             {'NAME': 'Tim', 'Age': 42, 'DEPT': 3, 'ADDR': 'Taipei'},
             {'NAME': 'Ken', 'Age': 41, 'DEPT': 1, 'ADDR': 'Taichung'},
             {'NAME': 'John', 'Age': 4, 'DEPT': 3, 'ADDR': 'Taipei'}]
sql_insert_dml = 'INSERT INTO EMPLOYEE(NAME, AGE, DEPT, ADDRESS) VALUES(?,?,?,?)'
start_time = time.time()
for i in range(100):
    for e in employees:
        connection1.execute(sql_insert_dml, (e['NAME'], e['Age'], e['DEPT'], e['ADDR']))
        # connection1.commit()
    # connection1.commit()
connection1.commit() # 0.10
print ("total --%s seconds"%(time.time()-start_time))
connection1.close()
