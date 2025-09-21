class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = {}  # (shop, movie) -> price
        self.movie_shops = {}  # movie -> list of (price, shop)
        self.rented = set()  # (shop, movie) that are currently rented

        for shop, movie, price in entries:
            self.available[(shop, movie)] = price
            if movie not in self.movie_shops:
                self.movie_shops[movie] = []
            self.movie_shops[movie].append((price, shop))

        # Sort shops by price for each movie initially
        for movie in self.movie_shops:
            self.movie_shops[movie].sort()

    def search(self, movie: int) -> List[int]:
        result = []
        for price, shop in self.movie_shops.get(movie, []):
            if (shop, movie) not in self.rented:
                result.append(shop)
            if len(result) == 5:
                break
        return result

    def rent(self, shop: int, movie: int) -> None:
        self.rented.add((shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented.discard((shop, movie))

    def report(self) -> List[List[int]]:
        rented_list = []
        for shop, movie in self.rented:
            price = self.available[(shop, movie)]
            rented_list.append((price, shop, movie))

        rented_list.sort()
        return [[shop, movie] for price, shop, movie in rented_list[:5]]





#in cpp
struct Node {
    int shop, movie, price;
    bool operator<(const Node& other) const {
        if (price != other.price) return price < other.price;
        if (shop != other.shop) return shop < other.shop;
        return movie < other.movie;
    }
};

class MovieRentingSystem {
    unordered_map<long long, Node> byPair;
    unordered_map<int, set<Node>> availableByMovie;
    set<Node> rentedSet;

    long long key(int shop, int movie) {
        return ((long long)shop << 32) ^ movie;
    }

public:
    MovieRentingSystem(int n, vector<vector<int>>& entries) {
        for (auto& e : entries) {
            int shop = e[0], movie = e[1], price = e[2];
            Node node{shop, movie, price};
            byPair[key(shop, movie)] = node;
            availableByMovie[movie].insert(node);
        }
    }

    vector<int> search(int movie) {
        vector<int> res;
        if (availableByMovie.count(movie) == 0) return res;
        auto& s = availableByMovie[movie];
        int count = 0;
        for (auto it = s.begin(); it != s.end() && count < 5; ++it, ++count) {
            res.push_back(it->shop);
        }
        return res;
    }

    void rent(int shop, int movie) {
        long long k = key(shop, movie);
        Node node = byPair[k];
        availableByMovie[movie].erase(node);
        rentedSet.insert(node);
    }

    void drop(int shop, int movie) {
        long long k = key(shop, movie);
        Node node = byPair[k];
        rentedSet.erase(node);
        availableByMovie[movie].insert(node);
    }

    vector<vector<int>> report() {
        vector<vector<int>> res;
        int count = 0;
        for (auto it = rentedSet.begin(); it != rentedSet.end() && count < 5; ++it, ++count) {
            res.push_back({it->shop, it->movie});
        }
        return res;
    }
};
