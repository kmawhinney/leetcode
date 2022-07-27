class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        total_units = 0
        total_boxes = 0
        
        for box in sorted(boxTypes, key=lambda x: x[1], reverse=True):
            while total_boxes < truckSize and box[0] > 0:
                total_units += box[1]
                total_boxes += 1
                box[0] -= 1
                    
        return total_units
