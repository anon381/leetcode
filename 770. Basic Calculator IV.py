
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
class Solution {
public:
    vector<string> basicCalculatorIV(string expr, vector<string>& variables, vector<int>& values) {
        unordered_map<string, int> valueMap;
        int n = variables.size();
        for (int i = 0; i < n; ++i) valueMap[variables[i]] = values[i];
        
        int idx = 0;
        unordered_map<string, int> resultMap = evaluateExpression(expr, valueMap, idx);
        vector<pair<string, int>> resultList(resultMap.begin(), resultMap.end());
        
        sort(resultList.begin(), resultList.end(), compareByDegree);
        
        vector<string> finalResult;
        for (auto& entry : resultList) {
            if (entry.second == 0) continue;
            finalResult.push_back(to_string(entry.second));
            if (!entry.first.empty()) finalResult.back() += "*" + entry.first;
        }
        
        return finalResult;
    }
    
private:
    unordered_map<string, int> evaluateExpression(string& expression, unordered_map<string, int>& valueMap, int& idx) {
        vector<unordered_map<string, int>> operands;
        vector<char> operators = {'+'};
        int len = expression.size();
        
        while (idx < len && expression[idx] != ')') {
            if (expression[idx] == '(') {
                idx++;
                operands.push_back(evaluateExpression(expression, valueMap, idx));
            } else {
                int start = idx;
                while (idx < len && expression[idx] != ' ' && expression[idx] != ')') idx++;
                string token = expression.substr(start, idx - start);
                bool isNumber = true;
                
                for (char c : token) {
                    if (!isdigit(c)) {
                        isNumber = false;
                        break;
                    }
                }
                
                unordered_map<string, int> temp;
                if (isNumber) {
                    temp[""] = stoi(token);
                } else if (valueMap.count(token)) {
                    temp[""] = valueMap[token];
                } else {
                    temp[token] = 1;
                }
                operands.push_back(temp);
            }
            
            if (idx < len && expression[idx] == ' ') {
                operators.push_back(expression[++idx]);
                idx += 2;
            }
        }
        idx++;
        
        return combineOperands(operands, operators);
    }
    
    unordered_map<string, int> combineOperands(vector<unordered_map<string, int>>& operands, vector<char>& operators) {
        unordered_map<string, int> result;
        int numOps = operators.size();
        
        for (int i = numOps - 1; i >= 0; --i) {
            unordered_map<string, int> temp = operands[i];
            while (i >= 0 && operators[i] == '*') {
                temp = multiplyOperands(temp, operands[--i]);
            }
            int sign = operators[i] == '+' ? 1 : -1;
        
            for (auto& p : temp) result[p.first] += sign * p.second;
        }
        
        return result;
    }
    
    unordered_map<string, int> multiplyOperands(unordered_map<string, int>& left, unordered_map<string, int>& right) {
        unordered_map<string, int> result;
        for (auto& leftPair : left) {
            for (auto& rightPair : right) {
                string combined = combineStrings(leftPair.first, rightPair.first);
                result[combined] += leftPair.second * rightPair.second;
            }
        }
        return result;
    }
    
    string combineStrings(const string& a, const string& b) {
        if (a.empty()) return b;
        if (b.empty()) return a;
        
        vector<string> leftTokens = splitString(a, '*');
        vector<string> rightTokens = splitString(b, '*');
        
        for (auto& s : rightTokens) leftTokens.push_back(s);
        sort(leftTokens.begin(), leftTokens.end());
        
        string combinedStr;
        for (auto& token : leftTokens) combinedStr += token + '*';
        combinedStr.pop_back();
        
        return combinedStr;
    }
    
    static vector<string> splitString(const string& s, char delimiter) {
        vector<string> parts;
        int start = 0, len = s.size();
        
        while (start < len) {
            int end = s.find(delimiter, start);
            if (end == string::npos) end = len;
            parts.push_back(s.substr(start, end - start));
            start = end + 1;
        }
        
        return parts;
    }
    
    static bool compareByDegree(pair<string, int>& a, pair<string, int>& b) {
        string left = a.first, right = b.first;
        vector<string> leftTokens = splitString(left, '*');
        vector<string> rightTokens = splitString(right, '*');
        
        return leftTokens.size() > rightTokens.size() || (leftTokens.size() == rightTokens.size() && leftTokens < rightTokens);
    }
};
