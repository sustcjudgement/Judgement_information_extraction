class TimeBean:
    def __init__(self, judgement_id=0,time=''):
        self._judgement_id = judgement_id
        self._time = time

    @property
    def judgement_id(self):
        return int(self.judgement_id)

    @judgement_id.setter
    def judgement_id(self, id):
        self._judgement_id = id

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time):
        self._time=time