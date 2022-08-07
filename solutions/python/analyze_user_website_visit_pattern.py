from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        sorted_patterns = sorted(zip(timestamp, username, website))
  
        visit_map = defaultdict(list)
        for t, u, w in sorted_patterns:
            visit_map[u].append(w)
        
        count_map = defaultdict(int)
        for website_list in visit_map.values():
            combs = set(combinations(website_list, 3))
            for c in combs:
                count_map[c] += 1
        
        sorted_count_map = sorted(count_map, key=lambda x: (-count_map[x], x))
        return sorted_count_map[0]
