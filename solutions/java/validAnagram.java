class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> charCount = new HashMap<>();

        if (s.length() != t.length()) {
            return false;
        }

        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }

        for (char c : t.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) - 1);
        }

        for (int val : charCount.values()) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
}
