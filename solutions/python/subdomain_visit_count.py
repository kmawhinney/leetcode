from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = defaultdict(int)
        result = []

        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            fragments = domain.split(".")

            for i in range(len(fragments)):
                counts[".".join(fragments[i:])] += count

        for domain, count in counts.items():
            result.append(f"{count} {domain}")
        
        return result
