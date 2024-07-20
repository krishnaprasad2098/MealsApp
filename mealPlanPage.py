from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MealPlanPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(20)

        title = QLabel("Your Weekly Meal Plan")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 18, QFont.Bold))
        layout.addWidget(title)

        self.meal_plan_display = QTextEdit()
        self.meal_plan_display.setReadOnly(True)
        self.meal_plan_display.setStyleSheet(
            "QTextEdit { background-color: #f0f0f0; padding: 10px; }"
        )
        layout.addWidget(self.meal_plan_display)

        back_button = QPushButton("Back to Preferences")
        back_button.clicked.connect(self.go_back)
        back_button.setStyleSheet(
            "QPushButton { padding: 10px; background-color: #008CBA; color: white; }"
        )
        layout.addWidget(back_button)

        self.setLayout(layout)

    def display_meal_plan(self, meal_plan):
        self.meal_plan_display.clear()
        if not meal_plan:
            self.meal_plan_display.append(
                "Sorry, no suitable meals found based on your preferences and available ingredients."
            )
            return

        for i, meal in enumerate(meal_plan, 1):
            meal_name, ingredients, _ = meal
            self.meal_plan_display.append(f"<b>Day {i}: {meal_name}</b>")
            self.meal_plan_display.append(f"Ingredients: {ingredients}\n")

        if len(meal_plan) < 7:
            self.meal_plan_display.append(
                "\n<i>Note: We couldn't find 7 different meals that match your preferences and ingredients. "
                "Consider adding more ingredients or adjusting your preferences for more variety.</i>"
            )

    def go_back(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.home_page)
