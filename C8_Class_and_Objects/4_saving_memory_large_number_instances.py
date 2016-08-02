class Date:
    __slots__ = ['year', 'month', 'day']
    '''
    Slots are just a optimization tool.
    '''
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    '''
    You will not be able to add new attributes after using slots.
    '''
