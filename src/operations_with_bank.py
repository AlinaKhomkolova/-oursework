from datetime import datetime


class Bank:
    def __init__(self, state_operation: str, date_operation: str | None, description_operation: str,
                 from_operation: str | None, to_operation: str | None,
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
        if self.date_operation:
            date = datetime.strptime(self.date_operation, '%Y-%m-%dT%H:%M:%S.%f')
            return f"{date:%d.%m.%Y}"
        # Если строка с датой пустая, то вернуть пустую строу
        return ""

    def formatting_payment(self, payment_data: str):
        """
        Форматирует информацию об отправителе операции.
        :return: Строка с информацией об отправителе операции.
        """
        if payment_data:
            # Количество цифр для группировки
            number_values_split = 4
            card_number = payment_data.split()[-1]
            title_card = " ".join(payment_data.split()[:-1])
            # Шифрование счета
            if title_card == "Счет":
                private_number_to = f"**{card_number[-4:]}"
                return f"{title_card} {private_number_to}"
            # Шифрование номера карты
            else:
                private_number_from = (
                    f"{card_number[:4]}{card_number[6:8]}******{card_number[-4:]}"
                )
                grouped_private_number = [private_number_from[i:i + number_values_split] for i in
                                          range(0, len(private_number_from), number_values_split)]

                return f"{title_card} {' '.join(grouped_private_number)}"
        # Если строка со счетом пустая, то вернуть пустую строу
        return ""

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
        if self.from_operation:
            return (f"{self.formatting_date()} {self.description_operation}\n"
                    f"{self.formatting_payment(self.from_operation)} -> {self.formatting_payment(self.to_operation)}\n"
                    f"{self.amount_operation} {self.currency_name}\n")
        return (f"{self.formatting_date()} {self.description_operation}\n"
                f"{self.formatting_payment(self.from_operation)}{self.formatting_payment(self.to_operation)}\n"
                f"{self.amount_operation} {self.currency_name}\n")
