from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QGuiApplication

def center_window(widget: QWidget):
    screen_geometry = QGuiApplication.primaryScreen().availableGeometry()  
    widget_geometry = widget.frameGeometry()  
 
    # Align centers and move  
    widget_geometry.moveCenter(screen_geometry.center())  
    widget.move(widget_geometry.topLeft())