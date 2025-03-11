class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getPass(self, login):
        sql = """select pass from mainmenu where login = ?""", (login,)
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchone()
            if res:
                return res
            print(res)
        except:
            print("Ошибка паса")
        return []

    def addlog(self, login, password):
        sql = """insert into mainmenu valuse = (NULL, ?, ?)""", (login, password)
        try:
            self.__cur.execute(sql)
        except:
            print("Ошибка")
        self.__db.commit()