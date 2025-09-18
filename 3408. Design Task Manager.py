class TaskManager(object):
    def __init__(self, tasks):
        self.heap = []
        self.taskPriority = {}
        self.taskOwner = {}
        for t in tasks:
            self.add(t[0], t[1], t[2])

    def add(self, userId, taskId, priority):
        heapq.heappush(self.heap, (-priority, -taskId))
        self.taskPriority[taskId] = priority
        self.taskOwner[taskId] = userId

    def edit(self, taskId, newPriority):
        heapq.heappush(self.heap, (-newPriority, -taskId))
        self.taskPriority[taskId] = newPriority

    def rmv(self, taskId):
        self.taskPriority[taskId] = -1

    def execTop(self):
        while self.heap:
            negp, negid = heapq.heappop(self.heap)
            p = -negp
            tid = -negid
            if self.taskPriority.get(tid, -2) == p:
                self.taskPriority[tid] = -1
                return self.taskOwner.get(tid, -1)
        return -1


#in cpp

# class TaskManager {
#   priority_queue<pair<int, int>> tasks;
#   unordered_map<int, int> taskPriority;
#   unordered_map<int, int> taskOwner;

# public:
#   TaskManager(vector<vector<int>>& tasks) {
#     for (const auto& task : tasks) {
#       add(task[0], task[1], task[2]);
#     }
#   }
    
#   void add(int userId, int taskId, int priority) {
#     tasks.push({priority, taskId});
#     taskPriority[taskId] = priority;
#     taskOwner[taskId] = userId;
#   }
    
#   void edit(int taskId, int newPriority) {
#     tasks.push({newPriority, taskId});
#     taskPriority[taskId] = newPriority;
#   }
    
#   void rmv(int taskId) {
#     taskPriority[taskId] = -1;
#   }
    
#   int execTop() {
#     while (!tasks.empty()) {
#       const auto task = tasks.top();
#       tasks.pop();
#       if (task.first == taskPriority[task.second]) {
#         taskPriority[task.second] = -1;
#         return taskOwner[task.second];
#       }
#     }
#     return -1;
#   }
# };



#in java
# class TaskManager {
#     private PriorityQueue<int[]> pq;
#     private Map<Integer,Integer> taskPriority;
#     private Map<Integer,Integer> taskOwner;

#     public TaskManager(List<List<Integer>> tasks) {
#         pq = new PriorityQueue<>((a,b) -> {
#             if (b[0] != a[0]) return b[0] - a[0];
#             return b[1] - a[1];
#         });
#         taskPriority = new HashMap<>();
#         taskOwner = new HashMap<>();
#         for (List<Integer> t : tasks) add(t.get(0), t.get(1), t.get(2));
#     }

#     public void add(int userId, int taskId, int priority) {
#         pq.add(new int[]{priority, taskId});
#         taskPriority.put(taskId, priority);
#         taskOwner.put(taskId, userId);
#     }

#     public void edit(int taskId, int newPriority) {
#         pq.add(new int[]{newPriority, taskId});
#         taskPriority.put(taskId, newPriority);
#     }

#     public void rmv(int taskId) {
#         taskPriority.put(taskId, -1);
#     }

#     public int execTop() {
#         while (!pq.isEmpty()) {
#             int[] t = pq.poll();
#             int p = t[0], id = t[1];
#             if (taskPriority.getOrDefault(id, -2) == p) {
#                 taskPriority.put(id, -1);
#                 return taskOwner.getOrDefault(id, -1);
#             }
#         }
#         return -1;
#     }
# }
