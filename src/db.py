from psycopg2.extras import DictCursor, NamedTupleCursor

from settings import get_umk_connection, get_auth_connection


def get_data_from_db(connection, sql, data=None, many=True):
    with connection.cursor(cursor_factory=NamedTupleCursor) as cursor:
        cursor.execute(sql, data)
        if many:
            for row in cursor:
                yield row
        else:
            yield cursor.fetchone()


class FtstReader:
    def __init__(self):
        self.__connection = get_umk_connection()

    def getMaxRv(self):
        # GetMaxFtstRv

        sql = """
            SELECT MAX(rv) AS max_rv
            FROM ftst
        """
        result_it = get_data_from_db(self.__connection, sql, many=False)
        return next(result_it)[0]

    def readFromDate(self, start_time):
        # ReadFromDate

        sql = """
            SELECT * 
            FROM ftst
            WHERE rv > %s
        """
        result_it = get_data_from_db(self.__connection, sql, (start_time,), many=True)
        yield from result_it

    def __getDataExt(self, sql):
        # GetDataExt

        result_it = get_data_from_db(self.__connection, sql, many=False)
        return next(result_it)

    def getTestDataExt(self, test_id):
        # GetTestDataExt

        

    def getGroupDataExt(self, group_id):
        # GetGroupDataExt
        pass

    def getDocumentDataExt(self, document_id):
        # GetDocumentDataExt
        pass

    def getSid(self, user_id):
        # GetSid
        pass


class AuthReader:
    def __init__(self):
        self.__connection = get_auth_connection()

    def getUserDataExt(self, sid):
        # GetUserDataExt
        pass


print("1: ", FtstReader().getMaxRv())
from datetime import datetime, timedelta
print("2: ", next(FtstReader().readFromDate(datetime.today() - timedelta(days=365))))
