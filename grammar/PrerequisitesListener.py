# Generated from Prerequisites.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrerequisitesParser import PrerequisitesParser
else:
    from PrerequisitesParser import PrerequisitesParser

# This class defines a complete listener for a parse tree produced by PrerequisitesParser.
class PrerequisitesListener(ParseTreeListener):

    # Enter a parse tree produced by PrerequisitesParser#parse.
    def enterParse(self, ctx:PrerequisitesParser.ParseContext):
        pass

    # Exit a parse tree produced by PrerequisitesParser#parse.
    def exitParse(self, ctx:PrerequisitesParser.ParseContext):
        pass


    # Enter a parse tree produced by PrerequisitesParser#expression.
    def enterExpression(self, ctx:PrerequisitesParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PrerequisitesParser#expression.
    def exitExpression(self, ctx:PrerequisitesParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PrerequisitesParser#term.
    def enterTerm(self, ctx:PrerequisitesParser.TermContext):
        pass

    # Exit a parse tree produced by PrerequisitesParser#term.
    def exitTerm(self, ctx:PrerequisitesParser.TermContext):
        pass


    # Enter a parse tree produced by PrerequisitesParser#atom.
    def enterAtom(self, ctx:PrerequisitesParser.AtomContext):
        pass

    # Exit a parse tree produced by PrerequisitesParser#atom.
    def exitAtom(self, ctx:PrerequisitesParser.AtomContext):
        pass


    # Enter a parse tree produced by PrerequisitesParser#course.
    def enterCourse(self, ctx:PrerequisitesParser.CourseContext):
        pass

    # Exit a parse tree produced by PrerequisitesParser#course.
    def exitCourse(self, ctx:PrerequisitesParser.CourseContext):
        pass


    # Enter a parse tree produced by PrerequisitesParser#test.
    def enterTest(self, ctx:PrerequisitesParser.TestContext):
        pass

    # Exit a parse tree produced by PrerequisitesParser#test.
    def exitTest(self, ctx:PrerequisitesParser.TestContext):
        pass



del PrerequisitesParser