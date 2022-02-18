from django.db import models

# Create your models here.
import sys
import os


class User_Command:

    def __init__(self):
        self.user_account=0
        self.userid =2323
        self.StockSymbol = []

    def set_ADD(self, amount):
        self.user_account += amount

    def get_ADD(self, amount):
        return ("ADD,",self.userid, amount)

    def set_QUOTE(self, StockSymbol):
        self.StockSymbol.append(StockSymbol)

    def get_QUOTE(self, StockSymbol):
        return ("QUOTE,",self.userid,StockSymbol)



