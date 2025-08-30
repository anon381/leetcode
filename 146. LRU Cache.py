class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        prev, next = self.latest.prev, self.latest
        prev.next = next.prev = node
        node.next = next
        node.prev = prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]




#in cpp
# class Node {
# public:
#     int key;
#     int val;
#     Node* prev;
#     Node* next;

#     Node(int key, int val) : key(key), val(val), prev(nullptr), next(nullptr) {}
# };

# class LRUCache {
# public:
# private:
#     int cap;
#     std::unordered_map<int, Node*> cache;
#     Node* oldest;
#     Node* latest;

# public:
#     LRUCache(int capacity) : cap(capacity) {
#         oldest = new Node(0, 0);
#         latest = new Node(0, 0);
#         oldest->next = latest;
#         latest->prev = oldest;
#     }

#     int get(int key) {
#         if (cache.find(key) != cache.end()) {
#             Node* node = cache[key];
#             remove(node);
#             insert(node);
#             return node->val;
#         }
#         return -1;
#     }

# private:
#     void remove(Node* node) {
#         Node* prev = node->prev;
#         Node* next = node->next;
#         prev->next = next;
#         next->prev = prev;
#     }

#     void insert(Node* node) {
#         Node* prev = latest->prev;
#         Node* next = latest;
#         prev->next = next->prev = node;
#         node->next = next;
#         node->prev = prev;
#     }

# public:
#     void put(int key, int value) {
#         if (cache.find(key) != cache.end()) {
#             remove(cache[key]);
#         }
#         Node* newNode = new Node(key, value);
#         cache[key] = newNode;
#         insert(newNode);

#         if (cache.size() > cap) {
#             Node* lru = oldest->next;
#             remove(lru);
#             cache.erase(lru->key);
#             delete lru;
#         }
#     }

#     // Destructor to release memory used by the nodes
#     ~LRUCache() {
#         Node* curr = oldest;
#         while (curr != nullptr) {
#             Node* next = curr->next;
#             delete curr;
#             curr = next;
#         }
#     }
# };




#in java
# class Node {
#     int key;
#     int val;
#     Node prev;
#     Node next;

#     public Node(int key, int val) {
#         this.key = key;
#         this.val = val;
#         this.prev = null;
#         this.next = null;
#     }
# }


# class LRUCache {

#     private int cap;
#     private Map<Integer, Node> cache;
#     private Node oldest;
#     private Node latest;

#     public LRUCache(int capacity) {
#         this.cap = capacity;
#         this.cache = new HashMap<>();
#         this.oldest = new Node(0, 0);
#         this.latest = new Node(0, 0);
#         this.oldest.next = this.latest;
#         this.latest.prev = this.oldest;
#     }

#     public int get(int key) {
#         if (cache.containsKey(key)) {
#             Node node = cache.get(key);
#             remove(node);
#             insert(node);
#             return node.val;
#         }
#         return -1;
#     }

#     private void remove(Node node) {
#         Node prev = node.prev;
#         Node next = node.next;
#         prev.next = next;
#         next.prev = prev;
#     }

#     private void insert(Node node) {
#         Node prev = latest.prev;
#         Node next = latest;
#         prev.next = next.prev = node;
#         node.next = next;
#         node.prev = prev;
#     }

#     public void put(int key, int value) {
#         if (cache.containsKey(key)) {
#             remove(cache.get(key));
#         }
#         Node newNode = new Node(key, value);
#         cache.put(key, newNode);
#         insert(newNode);

#         if (cache.size() > cap) {
#             Node lru = oldest.next;
#             remove(lru);
#             cache.remove(lru.key);
#         }
#     }
# }
