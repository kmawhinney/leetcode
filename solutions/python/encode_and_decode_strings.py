class Codec:
    def encode(self, strs: List[str]) -> str:
        return '🥔'.join(strs)
        

    def decode(self, s: str) -> List[str]:
        return s.split('🥔')
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
