# Generated from Prerequisites.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\5\2\22\n\2\3\3\3\3\3\3\7\3\27\n\3\f\3\16\3\32")
        buf.write("\13\3\3\4\3\4\3\4\7\4\37\n\4\f\4\16\4\"\13\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5*\n\5\3\6\5\6-\n\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\63\n\6\3\7\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\29\2\21")
        buf.write("\3\2\2\2\4\23\3\2\2\2\6\33\3\2\2\2\b)\3\2\2\2\n,\3\2\2")
        buf.write("\2\f\64\3\2\2\2\16\22\5\4\3\2\17\22\5\b\5\2\20\22\7\2")
        buf.write("\2\3\21\16\3\2\2\2\21\17\3\2\2\2\21\20\3\2\2\2\22\3\3")
        buf.write("\2\2\2\23\30\5\6\4\2\24\25\7\4\2\2\25\27\5\6\4\2\26\24")
        buf.write("\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\5\3\2\2\2\32\30\3\2\2\2\33 \5\b\5\2\34\35\7\3\2\2\35")
        buf.write("\37\5\b\5\2\36\34\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3")
        buf.write("\2\2\2!\7\3\2\2\2\" \3\2\2\2#*\5\n\6\2$*\5\f\7\2%&\7\5")
        buf.write("\2\2&\'\5\4\3\2\'(\7\6\2\2(*\3\2\2\2)#\3\2\2\2)$\3\2\2")
        buf.write("\2)%\3\2\2\2*\t\3\2\2\2+-\7\b\2\2,+\3\2\2\2,-\3\2\2\2")
        buf.write("-.\3\2\2\2./\7\f\2\2/\62\7\13\2\2\60\61\7\t\2\2\61\63")
        buf.write("\7\7\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\13\3\2\2\2\64")
        buf.write("\65\7\n\2\2\65\66\7\13\2\2\66\r\3\2\2\2\b\21\30 ),\62")
        return buf.getvalue()


class PrerequisitesParser ( Parser ):

    grammarFileName = "Prerequisites.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'or'", "'('", "')'", "<INVALID>", 
                     "<INVALID>", "'Minimum Grade of'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "OPARENS", "CPARENS", "GRADE_LETTER", 
                      "COURSE_PREFIX", "GRADE_PREFIX", "TEST_NAME", "COURSE_NUMBER", 
                      "COURSE_SUBJECT", "SPACE" ]

    RULE_parse = 0
    RULE_expression = 1
    RULE_term = 2
    RULE_atom = 3
    RULE_course = 4
    RULE_test = 5

    ruleNames =  [ "parse", "expression", "term", "atom", "course", "test" ]

    EOF = Token.EOF
    AND=1
    OR=2
    OPARENS=3
    CPARENS=4
    GRADE_LETTER=5
    COURSE_PREFIX=6
    GRADE_PREFIX=7
    TEST_NAME=8
    COURSE_NUMBER=9
    COURSE_SUBJECT=10
    SPACE=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PrerequisitesParser.ExpressionContext,0)


        def atom(self):
            return self.getTypedRuleContext(PrerequisitesParser.AtomContext,0)


        def EOF(self):
            return self.getToken(PrerequisitesParser.EOF, 0)

        def getRuleIndex(self):
            return PrerequisitesParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):
        localctx = PrerequisitesParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.state = 15
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.atom()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(PrerequisitesParser.EOF)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # TermContext
            self.right = None # TermContext

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrerequisitesParser.TermContext)
            else:
                return self.getTypedRuleContext(PrerequisitesParser.TermContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(PrerequisitesParser.OR)
            else:
                return self.getToken(PrerequisitesParser.OR, i)

        def getRuleIndex(self):
            return PrerequisitesParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PrerequisitesParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            localctx.left = self.term()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrerequisitesParser.OR:
                self.state = 18
                self.match(PrerequisitesParser.OR)
                self.state = 19
                localctx.right = self.term()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # AtomContext
            self.right = None # AtomContext

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PrerequisitesParser.AtomContext)
            else:
                return self.getTypedRuleContext(PrerequisitesParser.AtomContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(PrerequisitesParser.AND)
            else:
                return self.getToken(PrerequisitesParser.AND, i)

        def getRuleIndex(self):
            return PrerequisitesParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = PrerequisitesParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            localctx.left = self.atom()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PrerequisitesParser.AND:
                self.state = 26
                self.match(PrerequisitesParser.AND)
                self.state = 27
                localctx.right = self.atom()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def course(self):
            return self.getTypedRuleContext(PrerequisitesParser.CourseContext,0)


        def test(self):
            return self.getTypedRuleContext(PrerequisitesParser.TestContext,0)


        def OPARENS(self):
            return self.getToken(PrerequisitesParser.OPARENS, 0)

        def expression(self):
            return self.getTypedRuleContext(PrerequisitesParser.ExpressionContext,0)


        def CPARENS(self):
            return self.getToken(PrerequisitesParser.CPARENS, 0)

        def getRuleIndex(self):
            return PrerequisitesParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = PrerequisitesParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PrerequisitesParser.COURSE_PREFIX, PrerequisitesParser.COURSE_SUBJECT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.course()
                pass
            elif token in [PrerequisitesParser.TEST_NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.test()
                pass
            elif token in [PrerequisitesParser.OPARENS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(PrerequisitesParser.OPARENS)
                self.state = 36
                self.expression()
                self.state = 37
                self.match(PrerequisitesParser.CPARENS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CourseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.subject = None # Token
            self.number = None # Token
            self.grade = None # Token

        def COURSE_SUBJECT(self):
            return self.getToken(PrerequisitesParser.COURSE_SUBJECT, 0)

        def COURSE_NUMBER(self):
            return self.getToken(PrerequisitesParser.COURSE_NUMBER, 0)

        def COURSE_PREFIX(self):
            return self.getToken(PrerequisitesParser.COURSE_PREFIX, 0)

        def GRADE_PREFIX(self):
            return self.getToken(PrerequisitesParser.GRADE_PREFIX, 0)

        def GRADE_LETTER(self):
            return self.getToken(PrerequisitesParser.GRADE_LETTER, 0)

        def getRuleIndex(self):
            return PrerequisitesParser.RULE_course

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCourse" ):
                listener.enterCourse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCourse" ):
                listener.exitCourse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCourse" ):
                return visitor.visitCourse(self)
            else:
                return visitor.visitChildren(self)




    def course(self):

        localctx = PrerequisitesParser.CourseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_course)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PrerequisitesParser.COURSE_PREFIX:
                self.state = 41
                self.match(PrerequisitesParser.COURSE_PREFIX)


            self.state = 44
            localctx.subject = self.match(PrerequisitesParser.COURSE_SUBJECT)
            self.state = 45
            localctx.number = self.match(PrerequisitesParser.COURSE_NUMBER)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PrerequisitesParser.GRADE_PREFIX:
                self.state = 46
                self.match(PrerequisitesParser.GRADE_PREFIX)
                self.state = 47
                localctx.grade = self.match(PrerequisitesParser.GRADE_LETTER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.score = None # Token

        def TEST_NAME(self):
            return self.getToken(PrerequisitesParser.TEST_NAME, 0)

        def COURSE_NUMBER(self):
            return self.getToken(PrerequisitesParser.COURSE_NUMBER, 0)

        def getRuleIndex(self):
            return PrerequisitesParser.RULE_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest" ):
                listener.enterTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest" ):
                listener.exitTest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTest" ):
                return visitor.visitTest(self)
            else:
                return visitor.visitChildren(self)




    def test(self):

        localctx = PrerequisitesParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_test)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            localctx.name = self.match(PrerequisitesParser.TEST_NAME)
            self.state = 51
            localctx.score = self.match(PrerequisitesParser.COURSE_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





