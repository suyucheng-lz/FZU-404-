class error(Exception):
        def __init__(self, ErrorInfo):
            super().__init__(self)
            self.errorinfo = ErrorInfo
        def __str__(self):
            return self.errorinfo
if __name__ == '__main__':
    try:
        raise error('客户异常')
    except error as e:
        print(e)
