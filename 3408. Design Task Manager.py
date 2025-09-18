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
