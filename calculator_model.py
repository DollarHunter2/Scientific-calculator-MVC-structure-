import math

class CalculatorModel:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, char):
        self.expression += str(char)
        return self.expression

    def clear_all(self):
        self.expression = ""
        self.result=""
        return self.expression

    def delete_last(self):
        self.expression = self.expression[:-1]
        return self.expression

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    def factorial(self):
        try:
            value = int(self.expression)
            result = str(math.factorial(value))
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    def trig_sin(self):
        return self._trig_func(math.sin)

    def trig_cos(self):
        return self._trig_func(math.cos)

    def trig_tan(self):
        return self._trig_func(math.tan)

    def trig_cot(self):
        try:
            val = math.radians(float(self.expression))
            result = str(1 / math.tan(val))
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    def _trig_func(self, func):
        try:
            val = math.radians(float(self.expression))
            result = str(func(val))
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    def square_root(self):
        return self._root_func(2)

    def cube_root(self):
        return self._root_func(3)

    def _root_func(self, n):
        try:
            val = float(self.expression)
            if val < 0:
                raise ValueError
            result = str(val ** (1 / n))
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    def change_sign(self):
        if self.expression.startswith('-'):
            self.expression = self.expression[1:]
        else:
            self.expression = '-' + self.expression
        return self.expression

    def percent(self):
        try:
            result = str(float(self.expression) / 100)
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    def celsius_to_kelvin(self):
        try:
            val = float(self.expression)
            result = str(val + 273.15)
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"

    def kelvin_to_celsius(self):
        try:
            val = float(self.expression)
            result = str(val - 273.15)
            self.expression = result
            return result
        except Exception:
            self.expression = ""
            return "ERROR"
