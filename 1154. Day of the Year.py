class Solution:
    def dayOfYear(self, date: str) -> int:
        
        list_year=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

        day=int(date[-2:])
        year=int(date[:4])
        month=int(date[5:7])

        if year%4==0 and year!=1900 and month>2 :
            day+=1

        return list_year[month-1]+day


        
#c++ version
# #include <bits/stdc++.h>
# using namespace std;

# class Solution {
# public:
#     int dayOfYear(string date) {
#         vector<int> list_year = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};

#         int year = stoi(date.substr(0, 4));
#         int month = stoi(date.substr(5, 2));
#         int day = stoi(date.substr(8, 2));

#         // Leap year check
#         if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
#             if (month > 2) {
#                 day += 1;
#             }
#         }

#         return list_year[month - 1] + day;
#     }
# };
