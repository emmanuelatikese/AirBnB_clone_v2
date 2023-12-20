#!/usr/bin/python3
'''Another comment'''
import mysql.connector
import unittest
from os import getenv

class Test_db(unittest.TestCase):
    """This thing start today"""
    def test_dbs(self):
        con = mysql.connector.connect(host=getenv("HBNB_MYSQL_HOST"),
                                          port=3306,
                                          user=getenv("HBNB_MYSQL_USER"),
                                          passwd=getenv("HBNB_MYSQL_PWD"),
                                          db=getenv("HBNB_MYSQL_DB"),
                                          charset="utf8")
        cur = con.cursor()
        cur.execute("SELECT * FROM states")
        query_row = cur.fetchall();
        cur_state = len(query_row)

        cur.execute("INSERT INTO states (name) VALUES ('California')")
        con.commit()

        cur.execute("SELECT * FROM states")
        new_query = cur.fetchall();
        new_state = len(new_query)
        cur.close()
        con.close()
        return self.assertEqual(cur_state + 1, new_state)
if __name__ == "__main__":
    unittest.main()
