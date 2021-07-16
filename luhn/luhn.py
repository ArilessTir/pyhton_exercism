class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    @property
    def valid(self):
        # length 1 or less
        if len(self.card_num.replace(' ', '')) <= 1:
            return False

        # Special digits
        try:
            int(self.card_num.replace(' ', ''))
        except ValueError:
            return False

        # Good Length
        if len(self.card_num) > 1:
            tab = []
            num = self.card_num.replace(' ', '')
            for digits in num:
                tab.append(int(digits))

            for i in range(len(tab) % 2, len(tab), 2):
                if tab[i] * 2 > 9:
                    tab[i] = tab[i] * 2 - 9
                else:
                    tab[i] = tab[i] * 2

            if sum(tab) % 10 == 0:
                return True
            else:
                return False
