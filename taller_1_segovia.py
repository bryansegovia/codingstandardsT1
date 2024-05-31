"""
Module that calculates the total cost of a vacation package.
Authors: Bryan Segovia Mariscal
"""


class MyClass:
    """
    Este es el docstring, lo siento por no poner más no tengo
    tiempo pero sí entendí el concepto
    """
    def __init__(self):
        self.my_fav = {'Paris': 500, 'NYC': 600}

    def get_extra_cost(self, dist):
        """
        Docstring, ahhhh me quedo sin tiempo
        """
        return self.my_fav.get(dist, 0)

    def valid_this(self, dist):
        """
        Docstring de este metodo
        """
        return isinstance(dist, str)

class Passagner:
    """
    Mi claseeeeee
    """
    def __init__(self, num):
        self.num = num

    def valid_number(self):
        """
        My docstring para este metodo
        """
        print("this working here")
        return isinstance(self.num, int) and 0 < self.num <= 80

    def for_here_discount(self):
        """
        My docstring
        """
        if 4 < self.num < 10:
            return 0.1
        elif self.num >= 10:
            return 0.2

        else:
            return 0.0

class Plane:
    """
    Doctring of this class
    """
    def __init__(self, dist, num, dur, cost_bas):
        self.my_class = MyClass()
        self.passanger = Passagner(num)
        self.total_time = TotalTime(dur, num)
        self.dist = dist
        self.seats = 200
        self.cost_bas= cost_bas

    def sum(self):
        """
        Docstring
        """
        if not self.my_class.valid_this(self.dist) or \
            not self.passanger.valid_number() or \
                not self.total_time.is_valid_total_time():
            return -1

        number_total = self.cost_bas
        number_total += self.my_class.get_extra_cost(self.dist)
        number_total += self.total_time.get_free()
        number_total -= self.total_time.get_the_best_promo_ever()

        discount = self.passanger.for_here_discount()
        number_total = number_total - (number_total * discount)

        return max(int(number_total), 0)

class TotalTime:
    """
    My Docstring by Bryan Segovia
    """
    def __init__(self, dur, num):
        self.dur = dur
        self.num = num

    def is_valid_total_time(self):
        """
        This is my Docstring
        """
        return isinstance(self.dur, int) and self.dur > 0

    def get_free(self):
        """
        This is my docstring BS
        """
        return 200 if self.dur < 7 else 0

    def get_the_best_promo_ever(self):
        """
        Docstrinnnnng
        """
        return 200 if self.dur > 30 or self.num==2 else 0

    def get_weekend(self):
        """
        This is Docstring, loviu
        """
        return 100 if self.dur > 7 else 0

class Vacation:
    """
    Docstring for this
    """
    cost_bas = 1000

    def __init__(self, dist, num, dur):
        self.my_class = MyClass()
        self.passagner = Passagner(num)
        self.total_time = TotalTime(dur, num)
        self.dist = dist

    def sum(self):
        """
        Docstring yeaaaah
        """
        #sum the cost of the vacation package here
        if not self.my_class.valid_this(self.dist) or not \
            self.passagner.valid_number() or not \
                self.total_time.is_valid_total_time():
            return -1

        #sum the total cost
        number_total = self.cost_bas
        number_total += self.my_class.get_extra_cost(self.dist)
        number_total += self.total_time.get_free()
        number_total -= self.total_time.get_the_best_promo_ever()

        discount = self.passagner.for_here_discount()
        number_total = number_total - (number_total * discount)

        return max(int(number_total), 0)

#this is main function
def main():
    """
    Docdtring for the main, this is the most important
    """
    #this are the inputs
    dist = "Paris"
    num = 6
    dur = 10

    #this are the outputs
    calculator = Vacation(dist, num, dur)
    cost = calculator.sum()

    #this will do some printing
    if cost == -1:
        print("Invalid input -1.")
    else:
        print(f"The total cost of the vacation package is: ${cost}")

#main event function
if __name__ == "__main__":
    main()
