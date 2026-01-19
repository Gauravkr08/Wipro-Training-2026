# Create a class Calculator that demonstrates method overriding

class Calculator:
    def calculate(self, a, b):
        return a + b


class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        return a * b


calc = Calculator()
adv_calc = AdvancedCalculator()

print(calc.calculate(4, 2))
print(adv_calc.calculate(4, 2))  