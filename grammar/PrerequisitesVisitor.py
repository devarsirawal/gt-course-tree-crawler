# Generated from Prerequisites.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PrerequisitesParser import PrerequisitesParser
else:
    from PrerequisitesParser import PrerequisitesParser

# This class defines a complete generic visitor for a parse tree produced by PrerequisitesParser.

class PrerequisitesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrerequisitesParser#parse.
    def visitParse(self, ctx:PrerequisitesParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrerequisitesParser#expression.
    def visitExpression(self, ctx:PrerequisitesParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrerequisitesParser#term.
    def visitTerm(self, ctx:PrerequisitesParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrerequisitesParser#atom.
    def visitAtom(self, ctx:PrerequisitesParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrerequisitesParser#course.
    def visitCourse(self, ctx:PrerequisitesParser.CourseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrerequisitesParser#test.
    def visitTest(self, ctx:PrerequisitesParser.TestContext):
        return self.visitChildren(ctx)



del PrerequisitesParser