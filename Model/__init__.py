#from mysql import connector

class Model:
    def __init__(self):
        self.cnx = None
        self.open_conection()

    def open_conection(self):
        pass
        #self.cnx = connector.connect(user='root', password='brn123789', host='localhost', database='os')

    def close_conection(self):
        self.cnx.close()

    def get_nru_parans(self):
        return dict()
