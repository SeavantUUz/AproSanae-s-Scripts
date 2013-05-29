import sys
class Parser(object):
    def __init__(self):
        ##self.stdin = (c for c in raw_input('\n### '))
        ##self.lookhead = self.stdin.next()
        ##self.lookhead = sys.stdin.read(1)
        self.stdin = [c for c in raw_input('\n###')]
        self.index = 0
        self.lookhead = self.stdin[self.index]
    def expr(self):
        print '\n>>>',
        self.term()
        while True:
            if self.lookhead == '+':
                self.match('+')
                self.term()
                sys.stdout.write('+')
            elif self.lookhead == '-':
                self.match('-')
                self.term()
                sys.stdout.write('-')
            else:
                return

    def match(self,symbol):
        if self.lookhead == symbol:
            try:
                ##self.lookhead = self.stdin.next()
                ##self.lookhead = sys.stdin.read(1)
                self.index += 1
                self.lookhead = self.stdin[self.index] 
            #except StopIteration:
            except IndexError:
                self.lookhead = ''
                #sys.exit(0)
        else:
            raise SyntaxError

    def term(self):
        if self.lookhead.isdigit():
            ##peek = self.stdin.next()
            ##try:
            ##    while peek.isdigit():
            ##        self.lookhead += peek
            ##        peek = self.stdin.next() 
            ##except StopIteration:
            ##    pass
            ##peek = sys.stdin.read(1)
            self.index += 1
            peek = self.stdin[self.index]
            try:
                while peek.isdigit():
                    self.lookhead += peek
                    ##peek = sys.stdin.read(1)
                    self.index += 1
                    peek = self.stdin[self.index]
                ##sys.stdin.write(peek)
            except IndexError:
                pass
            sys.stdout.write(self.lookhead)
            self.index -=1
            self.match(self.lookhead)
        else:
            raise SyntaxError

parser = Parser()
parser.expr()
print '\n'
