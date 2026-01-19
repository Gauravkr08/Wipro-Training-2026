class Calculator:
    def calculate(self, a, b):
        return a + b


class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        return a * b


calc = Calculator()
adv_calc = AdvancedCalculator()

print(calc.calculate(3, 2))
print(adv_calc.calculate(3, 2))  