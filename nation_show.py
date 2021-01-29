import sys
import time
import pathlib
from PyQt5.QtWidgets import QDialog, QApplication
from nation_analyse import *
import sqlite3
import pyperclip
import collections


class band_combo_class:
    band_2G = []
    band_3G = []
    band_4G = []

    def __init__(self):
        pass

    def remove_empty_item(self, data):
        list_ret = []
        for item in data:
            if item != '':
                list_ret.append(item)
        return list_ret

    def got_band(self, str_2g, str_3g, str_4g):
        self.band_2G = []
        self.band_3G = []
        self.band_4G = []
        if len(str_2g) > 0:
            # Remove all space character
            str_2g_n = str_2g.replace(' ', '')
            self.band_2G = self.remove_empty_item(str_2g_n.rsplit(","))
        if len(str_3g) > 0:
            # Remove all space character
            str_3g_n = str_3g.replace(' ', '')
            self.band_3G = self.remove_empty_item(str_3g_n.rsplit(","))
        if len(str_4g) > 0:
            # Remove all space character
            str_4g_n = str_4g.replace(' ', '')
            self.band_4G = self.remove_empty_item(str_4g_n.rsplit(","))


class MyForm(QDialog):
    conn = None
    c = None
    band_combo = None
    band_combo_save = None
    get_all_country = True
    country_list_all = []
    country_list_2G = []
    country_list_2G_R = []
    country_list_3G = []
    country_list_3G_R = []
    country_list_4G = []
    country_list_4G_R = []
    country_list_view = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # connect to functions
        self.ui.comboBoxFilter.currentIndexChanged.connect(self.do_action)
        self.ui.pushButtonCopy.clicked.connect(self.copy_to_clipboards)
        # end functions
        # Attach Database
        self.conn = sqlite3.connect("frequency_global.db")
        self.c = self.conn.cursor()
        self.band_combo = band_combo_class()
        self.band_combo_save = band_combo_class()
        self.show()

    def do_action(self):
        # Get all countries list
        if self.get_all_country:
            self.get_all_country = False
            sql_command = "select * from Data;"
            print(sql_command)
            self.country_list_all = []
            for row in self.c.execute(sql_command):
                if row[0] not in self.country_list_all:
                    self.country_list_all.append(row[0])

        # Get band combo
        self.band_combo.got_band(self.ui.lineEdit2G.text(), self.ui.lineEdit3G.text(), self.ui.lineEdit4G.text())
        if collections.Counter(self.band_combo.band_2G) != collections.Counter(self.band_combo_save.band_2G):
            # Create sql command
            if len(self.band_combo.band_2G) != 0:
                condition_2g = ""
                for band in self.band_combo.band_2G:
                    condition_2g += "Band LIKE '%" + band + "%' or "
                sql_command = "select * from Data where Interface = 'GSM' and (" + condition_2g[
                                                                                   :len(condition_2g) - 4] + ");"
                # Recalculate country list which can work with 2G band list
                print(sql_command)
                self.country_list_2G = []
                for row in self.c.execute(sql_command):
                    if row[0] not in self.country_list_2G:
                        self.country_list_2G.append(row[0])

                # Recalculate country list which can not work with 2G band list
                self.country_list_2G_R = []
                for country in self.country_list_all:
                    if country not in self.country_list_2G:
                        self.country_list_2G_R.append(country)
            else:
                self.country_list_2G = []
                self.country_list_2G_R = self.country_list_all

            self.band_combo_save.band_2G = self.band_combo.band_2G
        if collections.Counter(self.band_combo.band_3G) != collections.Counter(self.band_combo_save.band_3G):
            # Create sql command
            if len(self.band_combo.band_3G) != 0:
                condition_3g = ""
                for band in self.band_combo.band_3G:
                    condition_3g += "Band LIKE '%" + band + "%' or "
                sql_command = "select * from Data where Interface = 'UMTS' and (" + condition_3g[
                                                                                    :len(condition_3g) - 4] + ");"
                # Recalculate country list which can work with 3G band list
                print(sql_command)
                self.country_list_3G = []
                for row in self.c.execute(sql_command):
                    if row[0] not in self.country_list_3G:
                        self.country_list_3G.append(row[0])

                # Recalculate country list which can not work with 3G band list
                self.country_list_3G_R = []
                for country in self.country_list_all:
                    if country not in self.country_list_3G:
                        self.country_list_3G_R.append(country)
            else:
                self.country_list_3G = []
                self.country_list_3G_R = self.country_list_all

            self.band_combo_save.band_3G = self.band_combo.band_3G
        if collections.Counter(self.band_combo.band_4G) != collections.Counter(self.band_combo_save.band_4G):
            # Create sql command
            if len(self.band_combo.band_4G) != 0:
                condition_4g = ""
                for band in self.band_combo.band_4G:
                    condition_4g += "Band LIKE '%" + band + "%' or "
                sql_command = "select * from Data where Interface = 'LTE' and (" + condition_4g[
                                                                                   :len(condition_4g) - 4] + ");"
                # Recalculate country list which can work with 4G band list
                print(sql_command)
                self.country_list_4G = []
                for row in self.c.execute(sql_command):
                    if row[0] not in self.country_list_4G:
                        self.country_list_4G.append(row[0])

                # Recalculate country list which can not work with 4G band list
                self.country_list_4G_R = []
                for country in self.country_list_all:
                    if country not in self.country_list_4G:
                        self.country_list_4G_R.append(country)
            else:
                self.country_list_4G = []
                self.country_list_4G_R = self.country_list_all

            self.band_combo_save.band_4G = self.band_combo.band_4G

        if self.ui.comboBoxFilter.currentIndex() == 0:  # All Countries
            self.country_list_view = self.country_list_all

        if self.ui.comboBoxFilter.currentIndex() == 1:  # 3G can work
            self.country_list_view = self.country_list_3G

        if self.ui.comboBoxFilter.currentIndex() == 2:  # 4G can work
            self.country_list_view = self.country_list_4G

        if self.ui.comboBoxFilter.currentIndex() == 3:  # 3G/4G can work
            self.country_list_view = []
            for country in self.country_list_all:
                if country in self.country_list_3G or country in self.country_list_4G:
                    self.country_list_view.append(country)

        if self.ui.comboBoxFilter.currentIndex() == 4:  # 3G and 4G can not work
            self.country_list_view = []
            for country in self.country_list_all:
                if country in self.country_list_3G_R and country in self.country_list_4G_R:
                    self.country_list_view.append(country)
        if self.ui.comboBoxFilter.currentIndex() == 5:  # 2G, 3G and 4G can not work
            self.country_list_view = []
            for country in self.country_list_all:
                if country in self.country_list_2G_R \
                        and country in self.country_list_3G_R \
                        and country in self.country_list_4G_R:
                    self.country_list_view.append(country)
        if self.ui.comboBoxFilter.currentIndex() == 6:  # 2G can not work
            self.country_list_view = self.country_list_2G_R

        self.country_list_view.sort()
        country_number = 0
        self.ui.listWidgetResult.clear()
        for country in self.country_list_view:
            self.ui.listWidgetResult.insertItem(country_number, country)
            country_number += 1
        # Update Number label
        if country_number <= 1:
            self.ui.labelResult.setText("Result: " + str(country_number) + " country")
        else:
            self.ui.labelResult.setText("Result: " + str(country_number) + " countries")

    def copy_to_clipboards(self):
        str_copy = ""
        for country in self.country_list_view:
            str_copy = str_copy + country + ", "
        print(str_copy)
        pyperclip.copy(str_copy)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.setWindowTitle("Ginno Nation Analyze Tool")
    w.show()
    sys.exit(app.exec_())
