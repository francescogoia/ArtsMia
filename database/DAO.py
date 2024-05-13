from database.DB_connect import DBConnect
from model.artObject import ArtObject
from model.connsessioni import Connessione


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_all_objects():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from objects o """
        cursor.execute(query)

        for row in cursor:
            result.append(ArtObject(**row))         ## se il nome del campo del dizionario è lo stesso dell'oggetto
                                                    ## posso fare così per non dover sccrivere tutti i campi


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_connessioni(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select eo1.object_id as o1, eo2.object_id as o2, count(*) as peso
                    from exhibition_objects eo1, exhibition_objects eo2
                    where eo1.exhibition_id = eo2.exhibition_id
                        and  eo1.object_id < eo2.object_id 
                    group by eo1.object_id, eo2.object_id 
                    order by peso desc """
        cursor.execute(query)

        for row in cursor:
            result.append(Connessione(idMap[row["o1"]],
                                      idMap[row["o2"]],
                                      row["peso"]))
        cursor.close()
        conn.close()
        return result



if __name__ == "__main__":
    d = DAO()
    d.get_all_objects()
