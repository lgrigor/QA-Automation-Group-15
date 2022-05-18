from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from ui import Ui_Dialog
import sys
import csv
import os

class Main(Ui_Dialog):
    all = []
    index = 1

    def init_events(self):
        self.reset_btn.clicked.connect(lambda: self.reset_terminal())
        self.import_btn.clicked.connect(lambda: self.instantiate_from_csv(self.select_file_fld.text()))
        self.filter_btn.clicked.connect(lambda: self.filter_items(
            self.from_fld.text(),
            self.to_fld.text()
            )
        )
        self.add_item_btn.clicked.connect(lambda: self.add_item(
            self.name_fld.text(),
            self.price_fld.text(),
            self.quantity_fld.text()
            )
        )

    def init(self):
        Main.all = list(csv.reader(open("db.csv")))
        Main.all.pop(0)
        self.print_in_terminal(Main.all)
        self.terminal_title_lbl.setText(f'Total Items: {Main.index - 1}')

    def clear_terminal(self):
        Main.index = 1
        self.terminal_output.clear()

    def print_in_terminal(self, my_list):
        self.terminal_output.append('N\tNAME\tPRICE\tQUANTITY')
        self.terminal_output.append('-' * 80)
        for i in my_list:
            self.terminal_output.append(f'{Main.index}\t' + '\t'.join(i))
            Main.index += 1

    def filter_items(self, start, stop):
        try:
            start = int(start)
            stop = int(stop)

            my_list = []
            for each_item in Main.all:
                if stop >= int(each_item[1]) >= start and int(each_item[2]) > 0:
                    my_list.append(each_item)
            
            self.clear_terminal()
            self.print_in_terminal(my_list)
            self.terminal_title_lbl.setText(f'Total Items: {len(my_list)}')

        except:
            self.clear_terminal()
            self.terminal_output.append(f'Error:\n\t"{start}" or "{stop}" some of them are not integers!')

    def add_item(self, name, price, quantity):
        try:
            if not isinstance(name, str):
                raise Exception
            price = int(price)
            quantity = int(quantity)

            with open("db.csv", "a") as f:
                f.write(f'{name},{price},{quantity}\n')
                Main.index += 1
                self.terminal_output.append(f'{Main.index - 1}\t{name}\t{price}\t{quantity}') 
                self.terminal_title_lbl.setText(f'Total Items: {Main.index - 1}')

        except:
            self.clear_terminal()
            self.terminal_output.append(f'Error:\n\t"{price}" or "{quantity}" some of them are not integers!')
            self.terminal_output.append(f'\t Or "{name}" is not string!')

    def reset_terminal(self):
        self.clear_terminal()
        self.init()

    def instantiate_from_csv(self, csv_file):
        if not os.path.exists(csv_file):
            self.clear_terminal()
            self.terminal_output.append(f'{csv_file} not exists!') 
        else:
            reader = csv.reader(open(csv_file))
            for i in reader:
                name, price, quantity = i
                with open("db.csv", "a") as f:
                    f.write(f'{name},{price},{quantity}\n')
                    Main.index += 1
                    self.terminal_output.append(f'{Main.index}\t{name}\t{price}\t{quantity}') 
                    self.terminal_title_lbl.setText(f'Total Items: {Main.index - 1}')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    main_window = QWidget()
    main_window.show()

    ui = Main()
    ui.setupUi(main_window)
    ui.init()
    ui.init_events()

    sys.exit(app.exec_())