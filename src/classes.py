class Bank:
    def __init__(self, id_operation, state_operation, date_operation, description_operation,
                 from_operation, to_operation,
                 amount_operation, code_operation):
        self.id_operation = id_operation
        self.state_operation = state_operation
        self.date_operation = date_operation
        self.description_operation = description_operation
        self.from_operation = from_operation
        self.to_operation = to_operation
        self.amount_operation = amount_operation
        self.code_operation = code_operation

    def print_init(self):
        for i in range(2):
            print(self.id_operation, self.state_operation, self.date_operation,
                  self.from_operation, self.to_operation,
                  self.amount_operation, self.code_operation)

