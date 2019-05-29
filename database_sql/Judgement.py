class JudgementBean:
    def __init__(self, judgement_id=0, area='',
                 job='',age='',time='',money=''):
        self._judgement_id = judgement_id
        self._area = area
        self._job = job
        self._age = age
        self._time = time
        self._money = money

    @property
    def judgement_id(self):
        return int(self.judgement_id)

    @judgement_id.setter
    def judgement_id(self, id):
        self._judgement_id = id

    @property
    def area(self):
        return str(self._area)

    @area.setter
    def area(self, area):
        self._area = area

    @property
    def job(self):
        return str(self._job)

    @job.setter
    def job(self,job):
        self._job=job

    @property
    def age(self):
        return str(self._age)

    @age.setter
    def age(self, age):
        self._age=age

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time=time

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        self._money=money

