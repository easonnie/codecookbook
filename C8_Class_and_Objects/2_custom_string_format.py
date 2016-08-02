_format = {
    'ymd': '{date.year}-{date.month}-{date.day}',
    'mdy': '{date.month}/{date.day}/{date.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec=''):
        if not format_spec:
            format_spec = 'ymd'
        fm = _format[format_spec]
        return fm.format(date=self)

if __name__ == '__main__':
    d = Date(2016, 8, 2)
    print(format(d))
    print(format(d, 'mdy'))
    print('Today is {0}'.format(d))
    '''
    Watch this usage and learn.
    '''
    print('Today is {0:mdy}'.format(d))