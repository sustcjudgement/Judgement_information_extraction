class MoneyBean:
    def __init__(self, judgement_id=0, money=''):
        self._judgement_id = judgement_id
        self._money = money

    @property
    def judgement_id(self):
        return int(self.judgement_id)

    @judgement_id.setter
    def judgement_id(self, id):
        self._judgement_id = id

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money=money
