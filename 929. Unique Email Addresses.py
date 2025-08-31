class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            unique_emails.add((local, domain))
        return len(unique_emails)


#in cpp
# class Solution {
# public:
#     int numUniqueEmails(vector<string>& emails) {
#         set<pair<string, string>> uniqueEmails;
        
#         for (const string& email : emails) {
#             size_t atPos = email.find('@');
#             string local = email.substr(0, atPos);
#             string domain = email.substr(atPos + 1);
            
#             size_t plusPos = local.find('+');
#             if (plusPos != string::npos) {
#                 local = local.substr(0, plusPos);
#             }
            
#             local.erase(remove(local.begin(), local.end(), '.'), local.end());
#             uniqueEmails.insert({local, domain});
#         }
        
#         return uniqueEmails.size();
#     }
# };


        

# in java

# class Solution {
#     public int numUniqueEmails(String[] emails) {
#         Set<String> uniqueEmails = new HashSet<>();
        
#         for (String email : emails) {
#             String[] parts = email.split("@");
#             String local = parts[0];
#             String domain = parts[1];
            
#             local = local.split("\\+")[0];
#             local = local.replace(".", "");
            
#             uniqueEmails.add(local + "@" + domain);
#         }
        
#         return uniqueEmails.size();
#     }
# }
