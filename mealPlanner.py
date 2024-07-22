import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget
from PyQt5.QtGui import QPalette, QColor
from homePage import HomePage
from mealPlanPage import MealPlanPage
from algorithm import generate_meal_plan
from database import create_database


class MealPlanner(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Meal Planner")
        self.setGeometry(100, 100, 600, 800)
        self.setStyleSheet("QWidget { font-size: 14px; }")

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        self.setPalette(palette)

        self.stacked_widget = QStackedWidget()
        self.home_page = HomePage(self)
        self.meal_plan_page = MealPlanPage(self)

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.meal_plan_page)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

    def generate_meal_plan(self):
        dietary_type, allergies, ingredients = self.home_page.get_preferences()
        meal_plan = generate_meal_plan(dietary_type, allergies, ingredients)
        self.meal_plan_page.display_meal_plan(meal_plan)
        self.stacked_widget.setCurrentWidget(self.meal_plan_page)


if __name__ == "__main__":
    create_database()  # Create the database if it doesn't exist
    app = QApplication(sys.argv)
    meal_planner = MealPlanner()
    meal_planner.show()
    sys.exit(app.exec_())
