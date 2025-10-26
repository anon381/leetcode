
class Bank:
    def __init__(self, balance):
        self.balances = balance
        self.n = len(balance)

    def _is_valid(self, account):
        return 1 <= account <= self.n

    def transfer(self, account1, account2, money):
        if not self._is_valid(account1) or not self._is_valid(account2):
            return False
        i1, i2 = account1 - 1, account2 - 1
        if self.balances[i1] < money:
            return False
        self.balances[i1] -= money
        self.balances[i2] += money
        return True

    def deposit(self, account, money):
        if not self._is_valid(account):
            return False
        self.balances[account - 1] += money
        return True

    def withdraw(self, account, money):
        if not self._is_valid(account):
            return False
        idx = account - 1
        if self.balances[idx] < money:
            return False
        self.balances[idx] -= money
        return True


"""
Usage:
obj = Bank([100, 200, 300])
a = obj.transfer(1, 2, 50)
b = obj.deposit(2, 100)
c = obj.withdraw(3, 150)
"""
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)



#in cpp
class Bank {
private: 
    bool isValid(int num){
        if(num > n || num<1) return false;
        return true;
    }
public:
    unordered_map<int, long long> mp;
    int n;
    Bank(vector<long long>& balance) {
        n = balance.size();
        for(int i=1; i<=balance.size(); i++){
            mp[i] = balance[i-1];
        }
    }
    
    bool transfer(int account1, int account2, long long money) {
        if(!isValid(account1) || !isValid(account2)){
            return false;
        }
        if(money>mp[account1]){
            return false;
        }
        else{
            mp[account2] += money;
            mp[account1] -= money;
            return true;
        }
    }
    
    bool deposit(int account, long long money) {
        if(!isValid(account)) return false;
        mp[account] += money;
        return true;
    }
    
    bool withdraw(int account, long long money) {
        if(money > mp[account] || !isValid(account)) return false;
        mp[account] -= money;
        return true;
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
