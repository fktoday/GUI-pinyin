import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from pypinyin import pinyin, Style
import images

class PinyinConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('汉语拼音转换器v1.0.1 by:欠文')
        self.setWindowIcon(QIcon(':/ico1.ico'))
        self.resize(400, 200)

        # 创建控件
        self.input_label = QLabel('请输入要转换的汉字:')
        self.input_edit = QLineEdit()
        self.output_label = QLabel('转换后的拼音:')
        self.output_edit = QLineEdit()
        self.output_edit.setReadOnly(True)
        self.convert_btn = QPushButton('转换')
        self.copy_btn = QPushButton('复制')

        # 添加布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.input_label)
        vbox.addWidget(self.input_edit)
        vbox.addWidget(self.output_label)
        vbox.addWidget(self.output_edit)
        hbox = QHBoxLayout()
        hbox.addWidget(self.convert_btn)
        hbox.addWidget(self.copy_btn)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # 添加事件
        self.convert_btn.clicked.connect(self.convert)
        self.copy_btn.clicked.connect(self.copy_output)

    def convert(self):
        text = self.input_edit.text()
        pinyin_list = pinyin(text, style=Style.TONE)
        pinyin_str = ' '.join(p[0] for p in pinyin_list)
        self.output_edit.setText(pinyin_str)

    def copy_output(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_edit.text())
        QMessageBox.information(self, '复制成功', '已成功复制到剪贴板！')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = PinyinConverter()
    converter.show()
    sys.exit(app.exec_())
