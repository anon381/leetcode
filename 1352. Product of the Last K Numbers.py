
# Function Description:
# This class maintains a list of numbers and allows efficient retrieval of the product
# of the last k numbers added. It handles zeros by resetting the product list, ensuring
# that queries for products including zeros return 0. The add operation and getProduct
# operation are both optimized for constant time complexity.
#
# Time Complexity: O(1) for add, O(1) for getProduct
# Space Complexity: O(n), where n is the number of added elements

class ProductOfNumbers:

    def __init__(self):
        self.product=[1]
        self.n=1

    def add(self, num: int) -> None:
        if num==0:
            self.product=[1]
            self.n=1
        else:
            self.product.append(self.product[-1]*num)
            self.n+=1

    def getProduct(self, k: int) -> int:
        if self.n<=k:
            return 0
        else:
            return self.product[-1]//self.product[-k-1]

# C++ version of the above Python code:
#
# class ProductOfNumbers {
#     vector<int> products;
# public:
#     ProductOfNumbers() { products.push_back(1); }
#     void add(int num) {
#         if (num == 0) products = {1};
#         else products.push_back(products.back() * num);
#     }
#     int getProduct(int k) {
#         if (products.size() <= k) return 0;
#         return products.back() / products[products.size() - k - 1];
#     }
# };
#
# Java version of the above Python code:
#
# import java.util.*;
# class ProductOfNumbers {
#     List<Integer> products = new ArrayList<>();
#     public ProductOfNumbers() { products.add(1); }
#     public void add(int num) {
#         if (num == 0) products = new ArrayList<>(Arrays.asList(1));
#         else products.add(products.get(products.size()-1) * num);
#     }
#     public int getProduct(int k) {
#         if (products.size() <= k) return 0;
#         return products.get(products.size()-1) / products.get(products.size()-k-1);
#     }
# }
#

