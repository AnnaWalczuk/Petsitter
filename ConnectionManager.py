import pymysql

class DBCOnnectManager:
    def __init__(self, host = "localhost", user = "ania", password = "ania", db_name = "petsitter", charset  = "utf8", port = 3306):


        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db_name = db_name
        self.charset  = charset

        try:

            self.connection = pymysql.connect(host = self.host,
                                              port = self.port,
                                              user =  self.user,
                                              password = self.password,
                                              database = self.db_name,
                                              charset = self.charset)
            print("Petsitter")

        except Exception as e:
            print (e)
            print("Connection not established")


