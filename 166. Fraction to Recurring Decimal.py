class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        fraction = []
        if (numerator < 0) ^ (denominator < 0):
            fraction.append("-")

        dividend = abs(numerator)
        divisor = abs(denominator)
        fraction.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return "".join(fraction)

        fraction.append(".")
        map_dict = {}
        while remainder != 0:
            if remainder in map_dict:
                fraction.insert(map_dict[remainder], "(")
                fraction.append(")")
                break
            map_dict[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder // divisor))
            remainder %= divisor

        return "".join(fraction)





#in cpp
class Solution {
public:
    std::string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0)
            return "0";        

        std::string fraction;
        if ((numerator < 0) ^ (denominator < 0))
            fraction += "-";        

        long long dividend = std::llabs((long long)numerator);
        long long divisor = std::llabs((long long)denominator);
        fraction += std::to_string(dividend / divisor);
        long long remainder = dividend % divisor;
        if (remainder == 0) {
            return fraction;
        }

        fraction += ".";
        std::unordered_map<long long, int> map;
        while (remainder != 0) {
            if (map.count(remainder)) {
                fraction.insert(map[remainder], "(");
                fraction += ")";
                break;
            }
            map[remainder] = fraction.size();
            remainder *= 10;
            fraction += std::to_string(remainder / divisor);
            remainder %= divisor;
        }

        return fraction;
    }
};








#in  java
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0)
            return "0";
        
        StringBuilder fraction = new StringBuilder();
        if (numerator < 0 ^ denominator < 0)
            fraction.append("-");        

        long dividend = Math.abs(Long.valueOf(numerator));
        long divisor = Math.abs(Long.valueOf(denominator));
        fraction.append(dividend / divisor);
        long remainder = dividend % divisor;
        if (remainder == 0) {
            return fraction.toString();
        }

        fraction.append(".");
        Map<Long, Integer> map = new HashMap<>();
        while (remainder != 0) {
            if (map.containsKey(remainder)) {
                fraction.insert(map.get(remainder), "(");
                fraction.append(")");
                break;
            }
            map.put(remainder, fraction.length());
            remainder *= 10;
            fraction.append(remainder / divisor);
            remainder %= divisor;
        }

        return fraction.toString();
    }
}
