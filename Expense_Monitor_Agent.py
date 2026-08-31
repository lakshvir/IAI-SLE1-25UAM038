class MonthlyExpenseMonitor:
    def __init__(self):
        self.income = 0
        self.expenses = {}

    # Take income and expense details from user
    def get_user_data(self):
        print("===== MONTHLY EXPENSE MONITOR =====")

        self.income = float(input("Enter your monthly income: ₹"))

        categories = [
            "Food",
            "Travel",
            "Shopping",
            "Entertainment",
            "Education",
            "Bills",
            "Other"
        ]

        print("\nEnter your monthly expenses:")

        for category in categories:
            amount = float(input(f"{category}: ₹"))
            self.expenses[category] = amount

    # Calculate total expense
    def calculate_total(self):
        return sum(self.expenses.values())

    # Find category with highest expense
    def highest_expense(self):
        return max(self.expenses, key=self.expenses.get)

    # Ask user questions
    def ask_questions(self):
        print("\n===== QUICK QUESTIONS =====")

        food_outside = input(
            "Do you frequently eat outside? (yes/no): "
        ).lower()

        unnecessary_shopping = input(
            "Do you buy things that you don't really need? (yes/no): "
        ).lower()

        unnecessary_travel = input(
            "Do you frequently spend money on unnecessary travel? (yes/no): "
        ).lower()

        entertainment = input(
            "Do you spend a lot on entertainment/subscriptions? (yes/no): "
        ).lower()

        return {
            "food_outside": food_outside,
            "unnecessary_shopping": unnecessary_shopping,
            "unnecessary_travel": unnecessary_travel,
            "entertainment": entertainment
        }

    # Give recommendations
    def give_advice(self, answers):

        total = self.calculate_total()
        remaining = self.income - total
        highest = self.highest_expense()

        print("\n===== AI EXPENSE ANALYSIS =====")

        print(f"Total Income     : ₹{self.income:.2f}")
        print(f"Total Expenses   : ₹{total:.2f}")
        print(f"Money Remaining  : ₹{remaining:.2f}")

        print("\n===== EXPENSE BREAKDOWN =====")

        for category, amount in self.expenses.items():
            percentage = (amount / self.income) * 100

            print(
                f"{category}: ₹{amount:.2f} "
                f"({percentage:.1f}% of income)"
            )

        print(f"\nHighest Expense Category: {highest}")

        print("\n===== AI RECOMMENDATIONS =====")

        # Food recommendation
        if answers["food_outside"] == "yes":
            print("• Food: You eat outside frequently. "
                  "Try reducing outside food and save more money.")

        # Shopping recommendation
        if answers["unnecessary_shopping"] == "yes":
            print("• Shopping: Avoid unnecessary purchases. "
                  "Make a list before buying anything.")

        # Travel recommendation
        if answers["unnecessary_travel"] == "yes":
            print("• Travel: Reduce unnecessary trips or use "
                  "public transport when possible.")

        # Entertainment recommendation
        if answers["entertainment"] == "yes":
            print("• Entertainment: Review your subscriptions "
                  "and cancel services you don't use.")

        # Category based advice
        if highest == "Food" and self.expenses["Food"] > self.income * 0.20:
            print("• Your food expense is relatively high. "
                  "Try setting a monthly food budget.")

        if highest == "Travel" and self.expenses["Travel"] > self.income * 0.15:
            print("• Your travel expense is relatively high. "
                  "Try planning trips and using cheaper transport.")

        if highest == "Shopping" and self.expenses["Shopping"] > self.income * 0.15:
            print("• Your shopping expense is relatively high. "
                  "Consider delaying non-essential purchases.")

        # Saving advice
        if remaining <= 0:
            print("\n⚠️ You are spending as much as or more than your income.")
            print("Try reducing unnecessary expenses immediately.")

        elif remaining < self.income * 0.10:
            print("\n⚠️ Your savings are quite low.")
            print("Try to save at least a small fixed amount every month.")

        else:
            print("\n✓ Your expenses are within your income.")
            print(f"Try to save ₹{remaining:.2f} or more next month.")


# Main program
agent = MonthlyExpenseMonitor()

agent.get_user_data()

answers = agent.ask_questions()

agent.give_advice(answers)
