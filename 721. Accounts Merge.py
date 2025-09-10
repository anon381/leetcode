from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        sol = defaultdict(list)
        for a in accounts:
            name = a[0]
            cur_emails = set(a[1:])
            if name not in sol:
                sol[name]=[cur_emails]
            else:
                merged=False
                newsets=[]
                for cur_set in sol[name]:
                    if len(cur_set.intersection(cur_emails)):
                        cur_emails.update(cur_set)
                        merged=True
                    else:
                        newsets.append(cur_set)
                if not merged:
                    sol[name].append(cur_emails)
                else:
                    newsets.append(cur_emails)
                    sol[name]=newsets
        output =[]
        for k in sol.keys():
            inner = sol[k]
            for cur_set in inner:
                output.append([k]+sorted(list(cur_set)))
        return output
        

# C++ version of the above Python code: