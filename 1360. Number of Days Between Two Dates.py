import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))
        return abs((datetime.date(y1, m1, d1) - datetime.date(y2, m2, d2)).days)

# C++ version of the above Python code:
#
# #include <string>
# #include <sstream>
# #include <ctime>
# #include <cstdlib>
# using namespace std;
# class Solution {
# public:
#     int daysBetweenDates(string date1, string date2) {
#         auto toDays = [](string date) {
#             int y, m, d;
#             sscanf(date.c_str(), "%d-%d-%d", &y, &m, &d);
#             tm t = {};
#             t.tm_year = y - 1900;
#             t.tm_mon = m - 1;
#             t.tm_mday = d;
#             return mktime(&t) / (24 * 3600);
#         };
#         return abs(toDays(date1) - toDays(date2));
#     }
# };
#