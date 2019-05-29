class AgeBean:
    def __init__(self, judgement_id=0,
                 age=''):
        self._judgement_id = judgement_id
        self._age = age


    @property
    def judgement_id(self):
        return int(self.judgement_id)

    @judgement_id.setter
    def judgement_id(self, id):
        self._judgement_id = id

    @property
    def age(self):
        return str(self._age)

    @age.setter
    def age(self, age):
        self._age = age