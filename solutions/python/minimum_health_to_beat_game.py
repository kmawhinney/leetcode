class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        total_damage = sum(damage)
        max_damage = max(damage)
        
        if max_damage <= armor:
            total_damage -= max_damage
        else:
            total_damage -= armor
        
        return total_damage + 1
