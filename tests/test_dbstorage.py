#!/usr/bin/python3
'''Another comment'''
import MySQLdb
import unittest
from os import getenv

class Test_db(unittest.TestCase):
    """This thing start today"""
    def test_dbs(self):
        con = MySQLdb.connect(host=getenv("HBNB_MYSQL_HOST"),
                                          port=3306,
                                          user=getenv("hbnb_test"),
                                          passwd=getenv("hbnb_test_pwd"),
                                          db=getenv("hbnb_test_db"),
                                          charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT * FROM states")
        query_row = cur.fetchall();
        cur_state = len(query_row)

        cur.execute("INSERT INTO states (name) VALUES ('California')")
        new_query = cur.fetchall();
        new_state = len(new_query)
        cur.close()
        conn.close()
        return self.assertEqual(cur_state + 1, new_state)
