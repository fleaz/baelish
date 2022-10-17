class Amount:
    """An amount of SIFRP currency represented in Gold Dragons (gd), Silver Stags (ss) and Copper Pennies (cp)."""

    def __init__(self, gd=0, ss=0, cp=0):
        self._goldDragons = Coin("Gold Dragons", "GD", gd)
        self._silverStags = Coin("Silver Stags", "SS", ss)
        self._copperPennies = Coin("Copper Pennies", "CP", cp)

    def __repr__(self):
        return "<Amount: {}, {}, {}>".format(self._goldDragons, self._silverStags, self._copperPennies)

    def __str__(self, useLongUnits=False, format_specifier=".2f"):
        output=[]

        if self._goldDragons != 0:
            output.append(self._goldDragons.__str__(useLongUnits, format_specifier))

        if self._silverStags != 0:
            output.append(self._silverStags.__str__(useLongUnits, format_specifier))

        if self._copperPennies != 0 or (self._goldDragons == 0 and self._silverStags == 0):
            output.append(self._copperPennies.__str__(useLongUnits, format_specifier))

        return ", ".join(output)

    def __int__(self):
        return int(self.in_cp)

    def __float__(self):
        return float(self.in_cp)

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __eq__(self, other):
        return float(self) == float(other)

    def __ne__(self, other):
        return float(self) != float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    @property
    def gd(self):
        return self._goldDragons

    @gd.setter
    def gd(self, value):
        self._goldDragons = Coin("Gold Dragons", "GD", value)

    @property
    def in_gd(self):
        return Coin("Gold Dragons", "GD", self.in_ss / 210)

    @property
    def ss(self):
        return self._silverStags

    @ss.setter
    def ss(self, value):
        self._silverStags = Coin("Silver Stags", "SS", value)

    @property
    def in_ss(self):
        return Coin("Silver Stags", "SS", self.in_cp / 56)

    @property
    def cp(self):
        return self._copperPennies

    @cp.setter
    def cp(self, value):
        self._copperPennies = Coin("Copper Pennies", "CP", value)

    @property
    def in_cp(self):
        value = (((self._goldDragons * 210) + self._silverStags) * 56) + self._copperPennies
        return Coin("Copper Pennies", "CP", value)

    @property
    def minimized(self):
        original = self.in_cp

        if self < 0:
            original = original * -1
        
        diff = original % (210 * 56)
        goldDragons = (original - diff) / (210 * 56)

        original = diff
        diff = original % 56
        
        silverStags = (original - diff) / 56
        copperPennies = diff

        if self < 0:
            goldDragons = goldDragons * -1
            silverStags = silverStags * -1
            copperPennies = copperPennies * -1

        return Amount(goldDragons, silverStags, copperPennies)