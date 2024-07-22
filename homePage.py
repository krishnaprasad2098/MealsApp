from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QListWidget,
    QScrollArea,
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class HomePage(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.allergies = []
        self.ingredients = []
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        title = QLabel("Welcome to Meal Planner")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 18, QFont.Bold))
        layout.addWidget(title)

        # Dietary Type
        layout.addWidget(QLabel("Select your dietary type:"))
        self.dietary_type_combo = QComboBox()
        self.dietary_type_combo.addItems(
            ["vegetarian", "vegan", "pescatarian", "non-vegetarian"]
        )
        self.dietary_type_combo.setStyleSheet("QComboBox { padding: 5px; }")
        layout.addWidget(self.dietary_type_combo)

        # Allergies
        layout.addWidget(QLabel("Add your allergies:"))
        allergy_layout = QHBoxLayout()
        self.allergy_input = QLineEdit()
        self.allergy_input.setPlaceholderText("Enter an allergy")
        allergy_layout.addWidget(self.allergy_input)
        add_allergy_btn = QPushButton("Add")
        add_allergy_btn.clicked.connect(self.add_allergy)
        allergy_layout.addWidget(add_allergy_btn)
        layout.addLayout(allergy_layout)

        self.allergy_list = QListWidget()
        self.allergy_list.setStyleSheet("QListWidget { border: 1px solid gray; }")
        layout.addWidget(self.allergy_list)

        delete_allergy_btn = QPushButton("Delete Selected")
        delete_allergy_btn.clicked.connect(self.delete_allergy)
        layout.addWidget(delete_allergy_btn)

        # Ingredients
        layout.addWidget(QLabel("Add your available ingredients:"))
        ingredient_layout = QHBoxLayout()
        self.ingredient_input = QLineEdit()
        self.ingredient_input.setPlaceholderText("Enter an ingredient")
        ingredient_layout.addWidget(self.ingredient_input)
        add_ingredient_btn = QPushButton("Add")
        add_ingredient_btn.clicked.connect(self.add_ingredient)
        ingredient_layout.addWidget(add_ingredient_btn)
        layout.addLayout(ingredient_layout)

        self.ingredient_list = QListWidget()
        self.ingredient_list.setStyleSheet("QListWidget { border: 1px solid gray; }")
        layout.addWidget(self.ingredient_list)

        # Generate Button
        generate_button = QPushButton("Generate Meal Plan")
        generate_button.clicked.connect(self.parent.generate_meal_plan)
        generate_button.setStyleSheet(
            "QPushButton { padding: 10px; background-color: #4CAF50; color: white; }"
        )
        layout.addWidget(generate_button)

        # Wrap everything in a scroll area
        scroll = QScrollArea()
        container = QWidget()
        container.setLayout(layout)
        scroll.setWidget(container)
        scroll.setWidgetResizable(True)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll)

    def add_allergy(self):
        allergy = self.allergy_input.text().strip()
        if allergy and allergy not in self.allergies:
            self.allergies.append(allergy)
            # item = QListWidget(allergy)
            self.allergy_list.addItem(allergy)
            # self.allergy_list.addItem(item)
            self.allergy_input.clear()

    def delete_allergy(self):
        selected_items = self.allergy_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            allergy = item.text()
            self.allergies.remove(allergy)
            self.allergy_list.takeItem(self.allergy_list.row(item))

    def add_ingredient(self):
        ingredient = self.ingredient_input.text().strip()
        if ingredient and ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
            self.ingredient_list.addItem(ingredient)
            self.ingredient_input.clear()

    def get_preferences(self):
        dietary_type = self.dietary_type_combo.currentText()
        return dietary_type, self.allergies, self.ingredients
