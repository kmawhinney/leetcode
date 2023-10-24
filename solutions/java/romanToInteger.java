class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> romanMap = new HashMap<String, Integer>();
        romanMap.put("I", 1);
        romanMap.put("V", 5);
        romanMap.put("X", 10);
        romanMap.put("L", 50);
        romanMap.put("C", 100);
        romanMap.put("D", 500);
        romanMap.put("M", 1000);

        int result = 0;

        for (int i = 0; i < s.length(); i++) {
            String currSymbol = String.valueOf(s.charAt(i));

            if (i+1 < s.length() && romanMap.get(currSymbol) < romanMap.get(String.valueOf(s.charAt(i+1)))) {
                result -= romanMap.get(currSymbol);
            } else {
                result += romanMap.get(currSymbol);
            }
        }

        return result;
    }
}
