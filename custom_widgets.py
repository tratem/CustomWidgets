from PyQt5.QtWidgets import QPushButton, QComboBox, QLabel, QLineEdit, QSizePolicy, QLayout

TEXT_SIZE = 12

def create_button(text: str = "", 
                  text_color: str = "black", 
                  background_color: str = "white",
                  text_size: int = TEXT_SIZE,
                  height: int = None,
                  width: int = None,
                  border_radius_px: int = 5) -> QPushButton:
    button = QPushButton(text)
    style = f"""
        color: {text_color};
        background-color: {background_color};
        font-size: {text_size}px;
        border-radius: {border_radius_px}px;
    """
    button.setStyleSheet(style)

    if height is not None:
        button.setFixedHeight(height)
    else:
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    if width is not None:
        button.setFixedWidth(width)
    else:
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    
    return button

def create_combo_box(items: list = [],
                     height: int = None,
                     width: int = None) -> QComboBox:
    combo = QComboBox()
    combo.addItems(items)

    if height is not None:
        combo.setFixedHeight(height)
    else:
        combo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    if width is not None:
        combo.setFixedWidth(width)
    else:
        combo.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    return combo

def create_label(text: str = "",
                 text_color: str = "black",
                 text_size: int = TEXT_SIZE,
                 height: int = None,
                 width: int = None) -> QLabel:
    label = QLabel(text)
    style = f"""
        color: {text_color};
        font-size: {text_size}px;
    """
    label.setStyleSheet(style)

    if height is not None:
        label.setFixedHeight(height)
    else:
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    if width is not None:
        label.setFixedWidth(width)
    else:
        label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    return label

def create_line_edit(placeholder: str = "",
                     text_color: str = "black",
                     background_color: str = "white",
                     text_size: int = TEXT_SIZE,
                     height: int = None,
                     width: int = None,
                     border_radius_px: int = 5) -> QLineEdit:
    line_edit = QLineEdit()
    line_edit.setPlaceholderText(placeholder)

    style = f"""
        color: {text_color};
        background-color: {background_color};
        font-size: {text_size}px;
        border-radius: {border_radius_px}px;
    """
    line_edit.setStyleSheet(style)

    if height is not None:
        line_edit.setFixedHeight(height)
    else:
        line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

    if width is not None:
        line_edit.setFixedWidth(width)
    else:
        line_edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    return line_edit

def clear_layout(layout: QLayout):
    if layout is None:
        return

    while layout.count():
        item = layout.takeAt(0)

        if item.layout():
            clear_layout(item.layout())

        if item.widget():
            widget = item.widget()
            widget.setParent(None)
            widget.deleteLater()