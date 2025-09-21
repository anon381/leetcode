Complexity

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





#in java
    class MovieRentingSystem {
    private static class Node {
        final int shop;
        final int movie;
        final int price;
        Node(int shop, int movie, int price) {
            this.shop = shop;
            this.movie = movie;
            this.price = price;
        }
    }
    private static final Comparator<Node> CMP =
        (a, b) -> {
            int c = Integer.compare(a.price, b.price);
            if (c != 0) return c;
            c = Integer.compare(a.shop, b.shop);
            if (c != 0) return c;
            return Integer.compare(a.movie, b.movie);
        };
    private final Map<Integer, TreeSet<Node>> availableByMovie = new HashMap<>();
    private final TreeSet<Node> rentedSet = new TreeSet<>(CMP);
    private final Map<Long, Node> byPair = new HashMap<>();

    private static long key(int shop, int movie) {
        return (((long) shop) << 32) ^ (movie & 0xffffffffL);
    }

    public MovieRentingSystem(int n, int[][] entries) {
        for (int[] e : entries) {
            int shop = e[0], movie = e[1], price = e[2];
            Node node = new Node(shop, movie, price);
            byPair.put(key(shop, movie), node);
            availableByMovie
                .computeIfAbsent(movie, k -> new TreeSet<>(CMP))
                .add(node);
        }
    }
    public List<Integer> search(int movie) {
        List<Integer> ans = new ArrayList<>(5);
        TreeSet<Node> set = availableByMovie.get(movie);
        if (set == null || set.isEmpty()) return ans;
        Iterator<Node> it = set.iterator();
        for (int i = 0; i < 5 && it.hasNext(); i++) {
            ans.add(it.next().shop);
        }
        return ans;
    }
    public void rent(int shop, int movie) {
        long k = key(shop, movie);
        Node node = byPair.get(k);
        if (node == null) return; // defensive
        TreeSet<Node> set = availableByMovie.get(movie);
        if (set != null) set.remove(node);
        rentedSet.add(node);
    }
    public void drop(int shop, int movie) {
        long k = key(shop, movie);
        Node node = byPair.get(k);
        if (node == null) return; // defensive
        rentedSet.remove(node);
        availableByMovie
            .computeIfAbsent(movie, x -> new TreeSet<>(CMP))
            .add(node);
    }
    public List<List<Integer>> report() {
        List<List<Integer>> ans = new ArrayList<>(5);
        Iterator<Node> it = rentedSet.iterator();
        for (int i = 0; i < 5 && it.hasNext(); i++) {
            Node n = it.next();
            ans.add(Arrays.asList(n.shop, n.movie));
        }
        return ans;
    }
}







#in javascript
var MovieRentingSystem = function (_n, entries) {
    this.maxNumSearchResults = 5;
    let sorted = [...entries]
        .sort(([shop1, _1, price1], [shop2, _2, price2]) => {
            let priceDiff = price1 - price2;
            return priceDiff? priceDiff: shop1 - shop2;
        });
    this.movies = sorted
        .reduce((movies, [shop, movie]) => {
            let shops = movies[movie];
            if(shops == undefined)
                shops = movies[movie] = [];
            shops.push(shop);
            return movies;
        }, {});
    this.shops = sorted
        .reduce((shops, [shop, movie, price]) => {
            let data = shops[shop];
            if(data == undefined)
                data = shops[shop] = {};
            data[movie] = {price};
            return shops;
        }, {});
    this.rented = [];
};
MovieRentingSystem.prototype.search = function (movie) {
    let results = [],
        shops = this.movies[movie];

    if (shops) {
        for (let i = 0, l = shops.length; results.length < this.maxNumSearchResults && i < l; i++) {
            let shop = shops[i];

            if (!this.shops[shop][movie].rented) results.push(shop);
        }
    }

    return results;
};
MovieRentingSystem.prototype.rent = function (shop, movie) {
    if (this.shops[shop][movie].rented == undefined) {
        let rentData = [shop, movie];

        this.shops[shop][movie].rented = rentData;
        this.rented.push(rentData);
    }
};
MovieRentingSystem.prototype.drop = function (shop, movie) {
    let movieData = this.shops[shop]?.[movie].rented;
    if (movieData) {
        this.rented.splice(this.rented.indexOf(movieData), 1);
        delete this.shops[shop][movie].rented;
    }
};
MovieRentingSystem.prototype.report = function () {
    return this.rented
        .sort(([shop1, movie1], [shop2, movie2]) => {
            let priceDiff = this.shops[shop1][movie1].price - this.shops[shop2][movie2].price;
            if(!priceDiff)
                return shop1 == shop2? movie1 - movie2 : shop1 - shop2;
            return priceDiff;
        })
        .slice(0, this.maxNumSearchResults);
};
