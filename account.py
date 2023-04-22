class Account:
    """
    A class representing actions on an account object
    """
    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of account object
        :param name: name the account is tied to
        """
        self.__account_name = name
        self.__account_balance = 0.00

    def deposit(self, amount: int or float) -> bool:
        """
        Method to increment amount to the account balance
        :param amount: amount to be incremented
        :return: True/False based on success or failure of transaction
        """
        if amount <= 0.00:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: int or float) -> bool:
        """
        Method to decrement amount to the account balance
        :param amount: amount to be decremented
        :return: True/False based on success or failure of transaction
        """
        if amount <= 0.00:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to obtain current balance
        :return: account balance amount
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to obtain name on account
        :return: Name
        """
        return self.__account_name
