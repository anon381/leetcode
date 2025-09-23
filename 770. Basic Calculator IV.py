
class Expression:
    def __init__(self, value: Dict[Tuple[str, ...], int] = None):
        self.value = value if value else {}

    def __sub__(self, other: 'Expression') -> 'Expression':
        res = dict(self.value)

        for var, coef in other.value.items():
            res[var] = res.get(var, 0) - coef

        return Expression(value=res)

    def __add__(self, other: 'Expression') -> 'Expression':
        res = dict(self.value)

        for var, coef in other.value.items():
            res[var] = res.get(var, 0) + coef

        return Expression(value=res)

    def __mul__(self, other: 'Expression') -> 'Expression':
        res = {}
        for var1, coef1 in self.value.items():
            for var2, coef2 in other.value.items():
                new_var = tuple(sorted(var1 + var2))
                res[new_var] = res.get(new_var, 0) + coef1 * coef2
        return Expression(value=res)

    def __neg__(self) -> 'Expression':
        return Expression() - self

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        varmap = dict(zip(evalvars, evalints))

        def tokenize(expression: str) -> List[str]:
            return re.findall(r'[a-z]+|[0-9]+|[\+\-\*\(\)]', expression)

        def process_tokens(tokens: List[str]) -> Expression:
            stack = []
            xpr = Expression()
            last_op = '+'
            ops = {'+', '-', '*'}

            def apply_op(op: str, expr: Expression) -> None:
                if op == '+':
                    stack.append(expr)
                elif op == '-':
                    stack.append(-expr)
                elif op == '*':
                    stack.append(stack.pop() * expr)

            for token in tokens:
                if token.isdigit():
                    xpr = Expression(value={(): int(token)})
                elif token.isalpha():
                    if token in varmap:
                        xpr = Expression(value={(): varmap[token]})
                    else:
                        xpr = Expression(value={(token,): 1})
                elif token in ops:
                    apply_op(last_op, xpr)
                    xpr = Expression()
                    last_op = token
                elif token == '(':
                    stack.append(last_op)
                    last_op = '+'
                elif token == ')':
                    apply_op(last_op, xpr)
                    xpr = Expression()

                    while isinstance(stack[-1], Expression):
                        xpr += stack.pop()

                    last_op = stack.pop()

            apply_op(last_op, xpr)
            return sum(stack, Expression())

        def format_result(result: Expression) -> List[str]:
            formatted = []

            for var, coef in sorted(
                result.value.items(),
                key=lambda x: (-len(x[0]), x[0])):
                if coef:
                    formatted.append(f'{coef}' + ('*' + '*'.join(var) if var else ''))

            return formatted

        tokens = tokenize(expression)
        result = process_tokens(tokens)

        return format_result(result)



#in cpp
