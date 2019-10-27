import pymysql

class SQLHelper:

    #链接数据库
    def __init__(self, Address, UserName, Password, Database):
        try:
            self._db = pymysql.connect(host=Address, user=UserName, password=Password, database=Database, charset='utf8')
            self._cursor = self._db.cursor()
            print('数据库连接成功')
        except Exception as e:
            print('连接数据库失败！', str(e))
    #对象销毁关闭连接
    def __del__(self):
        self._cursor.close()
        self._db.close()
#private variable:

#public variable:

#private function:

#public function:
    #执行单挑sql语句
    def ExecuteSQL(self, Command, Para):
        self._cursor.execute(Command, Para)
        self._db.commit()
    #执行多条sql语句
    def ExecuteSQLMany(self, Command, ParaList):
        self._cursor.executemany(Command, ParaList)
        self._db.commit()
    #查询单条数据
    def Query(self, Command, Para):
        self._cursor.execute(Command, Para)
        return self._db.cursor().fetchone()
    #查询多行数据
    def QueryMuilt(self, Command, *Para):
        try:
            self._cursor.execute(Command, Para)
            Res = self._cursor.fetchall()
            return Res
        except:
            print("查询失败")
