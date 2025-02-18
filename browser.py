#!/bin/env python3

import re,sys
from PyQt5.QtCore import QUrl, QDir, QFileInfo
from PyQt5.QtWidgets import QFileDialog
from time import sleep
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineDownloadItem
from PyQt5.QtWebEngineWidgets import QWebEngineProfile as profile

from PyQt5.QtWidgets import QApplication, QVBoxLayout,QMainWindow, QWidget, QLineEdit

class Browser(QMainWindow):
    def __init__(self):
        super(Browser,self).__init__()

        filters = make_filters()
        self.initUI(filters)

    def initUI(self,filters):
        profile.defaultProfile().downloadRequested.connect(self.download_file)
        self.webEngineView = QWebEngineView(self)
        # self.webEngineView.setUrl(QUrl("https://$institution.instructure.com"))
        self.webEngineView.setUrl(QUrl("https://www.wikipedia.org"))
        self.setWindowTitle('Web Browser')
        self.setGeometry(100, 100, 800, 600)
        self.filters = filters
        layout = QVBoxLayout(self)

        self.setCentralWidget(self.webEngineView)
        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)
        self.webEngineView.page().urlChanged.connect(self.urlChanged)
        self.webEngineView.page()
        self.show()

    def urlChanged(self, url):
        newurl = self.webEngineView.page().url().toString()
        self.urlFilter(newurl);

    def urlFilter(self, url):
        url = self.webEngineView.page().url().toString()
        match = False
        for domain in self.filters:
            if re.search(domain,url):
                match = True
                #print("checking: ", domain):
                print(domain, " is allowed")
        if not match:
            self.webEngineView.page().triggerAction(QWebEnginePage.Back)
            print("bounced for: ", url)

    def download_file(self, download:QWebEngineDownloadItem):
        assert download and download.state() == QWebEngineDownloadItem.DownloadRequested
        path, _ = QFileDialog.getSaveFileName(self, "Save as", QDir(download.downloadDirectory()).filePath(download.downloadFileName()))

        # File Not Selected close the progress
        if path == None:
            return

        # Set download directory and file name
        download.setDownloadDirectory(QFileInfo(path).path())
        download.setDownloadFileName(QFileInfo(path).fileName())

        # Start Download the file
        download.accept()

def make_filters():
    filters = {}
    # allowed = ["login.microsoft.com", "$institution.instructure.com", "login.microsoftonline.com"]
    allowed = ["wikipedia.org"]
    for domain in allowed:
        filters[domain] = re.compile(".*" + domain + ".*")
    return filters

app = QApplication(sys.argv)
browser = Browser()

sys.exit(app.exec_())
