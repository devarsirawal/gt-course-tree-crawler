from grammar.PrerequisitesVisitor import PrerequisitesVisitor

class PrefixNotationVisitor(PrerequisitesVisitor):

    def visitExpression(self, ctx):
        return ["or"] + list(filter(lambda term: term is not None, map(lambda term_ctx: self.visit(term_ctx), ctx.term())))

    def visitTerm(self, ctx):
        return ["and"] + list(filter(lambda atom: atom is not None, map(lambda atom_ctx: self.visit(atom_ctx), ctx.atom())))

    def visitAtom(self, ctx):
        course = ctx.course()
        expression = ctx.expression()
        test = ctx.test()
        if course is not None:
            return self.visit(course)
        elif expression is not None:
            return self.visit(expression)
        elif test is not None:
            return None

        raise Exception("Empty atom received")

    def visitCourse(self, ctx):
        subject = str(ctx.COURSE_SUBJECT())
        number = str(ctx.COURSE_NUMBER())

        grade = None
        grade_ctx = ctx.GRADE_LETTER()
        if grade_ctx is not None:
            grade = str(grade_ctx)
        
        return { "id": f"{subject} {number}", "grade": grade}
