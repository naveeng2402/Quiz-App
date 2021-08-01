from PyQt5.QtWidgets import QLayout, QLineEdit, QSizePolicy, QWidget
from PyQt5.QtCore import Qt

def set_size_policy(horizontal:QSizePolicy.Policy, vertical:QSizePolicy.Policy)->QSizePolicy:
    
    sizePolicy = QSizePolicy(horizontal, vertical)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(True)

    return sizePolicy


def line_edit_gen(parent:QWidget, layout:QLayout, obj_name:str = None, accessible_name:str = None, sizePolicy:QSizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)) -> QLineEdit:
    
    line_edit = QLineEdit(parent)
    
    if obj_name:
        line_edit.setObjectName(obj_name)
    line_edit.setAccessibleName(accessible_name)
    
    line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    line_edit.setSizePolicy(sizePolicy)
    
    layout.addWidget(line_edit)

    return line_edit