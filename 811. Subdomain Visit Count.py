class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = collections.Counter()
        for cd in cpdomains:
            n, s = cd.split()
            count[s] += int(n)
            for i in range(len(s)):
                if s[i] == '.':
                    count[s[i + 1:]] += int(n)
        return ["%d %s" % (count[k], k) for k in count]

#in cpp
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        unordered_map<string, int> count;
        for (auto cd : cpdomains) {
            int i = cd.find(" ");
            int n = stoi(cd.substr (0, i));
            string s = cd.substr (i + 1);
            for (int i = 0; i < s.size(); ++i)
                if (s[i] == '.')
                    count[s.substr(i + 1)] += n;
            count[s] += n;
        }
        vector<string> res;
        for (auto k : count)
            res.push_back (to_string(k.second) + " " + k.first);
        return res;
    }


#in java
