class InMemoryDB:
    def __init__(self):
        self.database = {}
        self.transaction = None

    def get(self, key):
        if self.transaction is not None and key in self.transaction:
            return self.transaction[key]
        return self.database.get(key, None)

    def put(self, key, value):
        if self.transaction is None:
            raise Exception("No transaction in progress")
        self.transaction[key] = value

    def begin_transaction(self):
        if self.transaction is not None:
            raise Exception("A transaction is already in progress")
        self.transaction = {}

    def commit(self):
        if self.transaction is None:
            raise Exception("No transaction in progress")
        for key, value in self.transaction.items():
            self.database[key] = value
        self.transaction = None

    def rollback(self):
        if self.transaction is None:
            raise Exception("No transaction in progress")
        self.transaction = None
