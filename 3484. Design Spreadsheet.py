# Space:
# O(N + L) 

# Time per operation:
# setCell → O(1)
# resetCell → O(1)
# getValue → O(L)

class Spreadsheet(object):

    def __init__(self, rows):
        self.mpp = {}

    def setCell(self, cell, value):
        self.mpp[cell] = value

    def resetCell(self, cell):
        self.mpp[cell] = 0

    def getValue(self, formula):
        formula = formula[1:]
        for i in range(len(formula)):
            if formula[i] == '+':
                s1, s2 = formula[:i], formula[i+1:]
                left = self.mpp.get(s1, 0) if s1[0].isupper() else int(s1)
                right = self.mpp.get(s2, 0) if s2[0].isupper() else int(s2)
                return left + right
        return 0


#in cpp
# class Spreadsheet {
# public:
#     unordered_map<string, int> mpp;
#     Spreadsheet(int rows) {}
#     void setCell(string cell, int value) { 
#         mpp[cell] = value; 
#     }
#     void resetCell(string cell) { 
#         mpp[cell] = 0; 
#     }

#     int getValue(string s) {
#         s = s.substr(1);
#         for (int i = 0; i < s.size(); i++) {
#             if (s[i] == '+') {
#                 string s1 = s.substr(0, i), s2 = s.substr(i + 1);
#                 int left = s1[0] >= 'A' && s1[0] <= 'Z' ? mpp[s1] : stoi(s1);
#                 int right = s2[0] >= 'A' && s2[0] <= 'Z' ? mpp[s2] : stoi(s2);
#                 return left + right;
#             }
#         }
#         return 0;
#     }
# };



#in java
# class Spreadsheet {
#     HashMap<String, Integer> mpp = new HashMap<>();
#     public Spreadsheet(int rows) {}
#     public void setCell(String cell, int value) {
#         mpp.put(cell, value);
#     }
#     public void resetCell(String cell) {
#         mpp.put(cell, 0);
#     }
#     public int getValue(String formula) {
#         formula = formula.substring(1);
#         for (int i = 0; i < formula.length(); i++) {
#             if (formula.charAt(i) == '+') {
#                 String s1 = formula.substring(0, i), s2 = formula.substring(i + 1);
#                 int left = Character.isUpperCase(s1.charAt(0)) ? mpp.getOrDefault(s1, 0) : Integer.parseInt(s1);
#                 int right = Character.isUpperCase(s2.charAt(0)) ? mpp.getOrDefault(s2, 0) : Integer.parseInt(s2);
#                 return left + right;
#             }
#         }
#         return 0;
#     }
# }
