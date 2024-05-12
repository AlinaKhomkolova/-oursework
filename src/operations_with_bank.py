from datetime import datetime


class Bank:
    def __init__(self, state_operation: str, date_operation: str, description_operation: str,
                 from_operation: str | None, to_operation: str,
                 amount_operation: str, currency_name: str):
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
        self.currency_name = currency_name

    def formatting_date(self) -> str:
        """
        Форматирует дату операции в нужный формат.
        :return: Строка с отформатированной датой операции.
        """
        date = datetime.strptime(self.date_operation, '%Y-%m-%dT%H:%M:%S.%f')
        return f"{date:%d.%m.%Y}"

    def formatting_from(self):
        """
        Форматирует информацию об отправителе операции.
        :return: Строка с информацией об отправителе операции.
        """
        if self.from_operation:
            number_values_split = 4
            card_number = self.from_operation.split()[-1]
            title_card = " ".join(self.from_operation.split()[:-1])

            private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
            grouped_private_number = [private_number[i:i + number_values_split] for i in
                                      range(0, len(private_number), number_values_split)]

            return f"{title_card} {' '.join(grouped_private_number)} -> "
        return ""

    def formatting_to(self):
        """
        Форматирует информацию о получателе операции.
        :return: Строка с информацией о получателе операции.
        """
        card_number = self.to_operation.split()[-1]
        title_card = "".join(self.to_operation.split()[:-1])
        private_number = (len(card_number[:-4]) * "*") + card_number[-4:]
        return f"{title_card} {private_number}"

    def __lt__(self, other):
        """
        Определяет поведение оператора меньше (<) для объектов Bank по дате операции.
        :param other: Объект Bank.
        :return: Результат сравнения по дате операции.
        """
        return self.date_operation < other.date_operation

    def __gt__(self, other):
        """
        Определяет поведение оператора больше (>) для объектов Bank по дате операции.
        :param other: Объект Bank.
        :return: Результат сравнения по дате операции.
        """
        return self.date_operation > other.date_operation

    def __str__(self):
        """
        Возвращает строковое представление объекта Bank.
        :return: Строковое представление объекта Bank.
        """
        return (f"{self.formatting_date()} {self.description_operation}\n"
                f"{self.formatting_from()}{self.formatting_to()}\n"
                f"{self.amount_operation} {self.currency_name}\n")
