from db.database import Db
from spelldb import SpellDb
class WordCheck:
    def __init__(self, db):
        self.db = db
    
    def check_valid(self, word):
        '''
            check if is a valid word
        '''
        return True
    
    def suggest(self, word):
        '''
            suggest based on the word
        '''
        pass
    
    def smart_suggest(self, word, start, length=-1, end=''):
        pass
    
db = Db()
spdb = SpellDb(db)
spellcheck = WordCheck(spdb)