from Dispencer.cash_dispencer import CashDispencer
from Dispencer.note_dispencer_10 import NoteDispencer10
from Dispencer.note_dispencer_100 import NoteDispencer100
from Dispencer.note_dispencer_50 import NoteDispencer50
from BankService.account import Account
from BankService.bank import Bank
from BankService.card import Card
from atm import ATM


class AtmDemo:
    
    @staticmethod
    def main():
        note100 = NoteDispencer100(50)
        note10 = NoteDispencer10(10)
        note50 = NoteDispencer50(5)
        note100.set_next_dispencer(note50)
        note50.set_next_dispencer(note10)
        cash_dispencer = CashDispencer(note100)
        bank = Bank("k-456","SBI")
        account = Account("m-4563",1000)
        card = Card("c-87462","8215","m-4563")
        bank.add_account(account)
        account.add_card(card)
        
        atm = ATM("y-765",bank,cash_dispencer)
        
        atm.insert_card(card)
           
        
AtmDemo.main()