from datetime import datetime


class Bank:
    def __init__(self, state_operation, date_operation, description_operation,
                 from_operation, to_operation,
                 amount_operation, code_operation):
        # Статус операции
        self.state_operation = state_operation
        # Дата выполнения операции
        self.date_operation = date_operation
        # Описание типа перевода
        self.description_operation = description_operation
        # Откуда сделать перевод
        self.from_operation = from_operation
        # Куда сделан перевод
        self.to_operation = to_operation
        # Сумма операции
        self.amount_operation = amount_operation
        # Валюта
        self.code_operation = code_operation

    def __str__(self):
        return f"Bank(state={self.state_operation}, date={self.date_operation}, " \
               f"description={self.description_operation}, from={self.from_operation}, to={self.to_operation}, " \
               f"amount={self.amount_operation}, code={self.code_operation})"

    # Форматирование даты в нужную форму
    def formatting_data(self):
        if self.date_operation is None:
            return "Дата отсутствует"
        date = datetime.strptime(self.date_operation, '%Y-%m-%dT%H:%M:%S.%f')
        return f"{date:%d.%m.%Y}"

    def formatting_from(self):
        if self.from_operation is None:
            return ""

        number_values_split = 4
        card_number = self.from_operation.split()[-1]
        title_card = " ".join(self.from_operation.split()[:-1])

        private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
        grouped_private_number = [private_number[i:i + number_values_split] for i in
                                  range(0, len(private_number), number_values_split)]

        return f"{title_card} {' '.join(grouped_private_number)} -> "

    def formatting_to(self):
        card_number = self.to_operation.split()[-1]
        title_card = "".join(self.to_operation.split()[:-1])
        private_number = (len(card_number[:-4]) * "*") + card_number[-4:]
        return f"{title_card} {private_number}"

    def formatting_string(self):
        if self.to_operation is None:
            return ""
        print(f"{self.formatting_data()} {self.description_operation}\n"
              f"{self.formatting_from()}{self.formatting_to()}\n"
              f"{self.amount_operation} {self.code_operation}\n")
