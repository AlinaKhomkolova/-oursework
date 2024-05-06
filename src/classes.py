from datetime import datetime


class Bank:
    def __init__(self, state_operation, date_operation, description_operation,
                 from_operation, to_operation,
                 amount_operation, code_operation):
        self.state_operation = state_operation
        self.date_operation = date_operation
        self.description_operation = description_operation
        self.from_operation = from_operation
        self.to_operation = to_operation
        self.amount_operation = amount_operation
        self.code_operation = code_operation
        state = False

    def __str__(self):
        return f"Bank(state={self.state_operation}, date={self.date_operation}, " \
               f"description={self.description_operation}, from={self.from_operation}, to={self.to_operation}, " \
               f"amount={self.amount_operation}, code={self.code_operation})"

    def check_state(self):
        if self.state_operation == "EXECUTED":
            state = True

    def formatting_data(self):
        if self.date_operation is None:
            return "Дата отсутствует"
        date = datetime.strptime(self.date_operation, '%Y-%m-%dT%H:%M:%S.%f')
        return f"{date:%d.%m.%Y}"

    def formatting_from(self):
        pass

    def formatting_string(self):
        print(f"{self.formatting_data()} {self.description_operation}")

    # def print_init(self):
    #     for i in range(1):
    #         # print(self.formatting_data())
    #         print(self.state_operation, self.date_operation, self.description_operation,
    #               self.from_operation, self.to_operation,
    #               self.amount_operation, self.code_operation)
