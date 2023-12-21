#!/usr/bin/python3
'''Another comment'''
import mysql.connector
import unittest
from os import getenv

class Test_db(unittest.TestCase):
    """This thing start today"""
    
    def setUp(self):
        # Set up code that runs before each test
        self.host = getenv("HBNB_MYSQL_HOST")
        self.user = getenv("HBNB_MYSQL_USER")
        self.password = getenv("HBNB_MYSQL_PWD")
        self.database = getenv("HBNB_MYSQL_DB")

    def test_dbs(self):
        if not all([self.host, self.user, self.password, self.database]):
            self.skipTest("Missing requirement")
        con = mysql.connector.connect(host=self.host,
                                          port=3306,
                                          user=self.host,
                                          passwd=self.password,
                                          db=self.database,
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
