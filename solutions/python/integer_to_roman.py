class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        int_to_roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        for key in int_to_roman.keys():
            if num == 0:
                break
            while num >= key:
                num -= key
                roman += int_to_roman[key]
                
        return roman
