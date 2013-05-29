# coding:utf-8
import sys
class Tag(object):
    @staticmethod
    def NUM():
        return 256

    @staticmethod
    def ID():
        return 257

    @staticmethod
    def TRUE():
        return 258

    @staticmethod
    def FALSE():
        return 259

## 单一表示的词法对象
## 基本上，单一表示应该用常量防止Token被修改
## 但是python并没有提供常量
## 解决方法也不太简洁，所以用变量表示
## 但是为了更符合常量要求，使用隐藏参数
class Token(object):
    def __init__(self,tag):
        self._tag = tag

## 常量单元
class Num(Token):
    def __init__(self,value):
        Token.__init__(self,Tag.NUM())
        assert isinstance(value,int)
        self.__value = value
    @property
    def num(self):
        return self.__value

## Word既可以用于保留字，也可以用于标识符
class Word(Token):
    def __init__(self,tag,string):
        Token.__init__(self,tag)
        self.__lexeme = string
    @property
    def lexeme(self):
        return self.__lexeme

class Lexer(object):
    def __init__(self):
        self.lines = 1;
        self.peek = ''
        self.words = {}
        ## 保留字储存
        self.reserver(Word(Tag.TRUE(),'true'))
        self.reserver(Word(Tag.FALSE(),'false'))

    def reserver(self,word):
        self.words[word.lexeme] = word

    def scan(self):
        stdin = (c for c in raw_input('### '))##sys.stdin)
        while True:
            self.peek = stdin.next()
            if self.peek == ' ' or self.peek == '\t':
                continue
            elif self.peek == '\n':
                self.lines += 1
            else:break

        ## 对常量的解析
        if self.peek.isdigit():
            value = self.peek
            while True:
                try:
                    self.peek = stdin.next()
                    if self.peek.isdigit():
                        value = ''.join((value,self.peek))
                    else:break
                except StopIteration:
                    break
            return Num(int(value))

        if self.peek.isalpha():
            string = self.peek
            while True:
                try:
                    self.peek = stdin.next()
                    if self.peek.isalpha():
                        string = ''.join((string,self.peek))
                    else:break
                except StopIteration:
                    break
            if self.words.get(string) != None:
                return self.words[string]
            else:
                word = Word(Tag.ID(),string)
                self.words[string] = word
                return word
        ## 如果不是常量，也不是标识符保留字
        ## 那么就应该是符号，*或者+等
        t = Token(self.peek)
        self.peek = ''
        return t
