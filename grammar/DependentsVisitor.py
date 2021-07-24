from grammar.PrerequisitesVisitor import PrerequisitesVisitor

class DependentsVisitor(PrerequisitesVisitor):

    def visitExpression(self, ctx):
        return list(filter(lambda term: term is not None, map(lambda term_ctx: self.visit(term_ctx), ctx.term())))

    def visitTerm(self, ctx):
        return list(filter(lambda atom: atom is not None, map(lambda atom_ctx: self.visit(atom_ctx), ctx.atom())))

    def visitAtom(self, ctx):
        course = ctx.course()
        expression = ctx.expression()

        if course is not None:
            return self.visit(course)
        elif expression is not None:
            return self.visit(expression)

        raise Exception("Empty atom received")

    def visitCourse(self, ctx):
        subject = str(ctx.COURSE_SUBJECT())
        number = str(ctx.COURSE_NUMBER())
        
        return f"{ctx.COURSE_SUBJECT()} {ctx.COURSE_NUMBER()}"
