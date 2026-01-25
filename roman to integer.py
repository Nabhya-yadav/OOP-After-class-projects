class RomanToInteger:
    
    def __init__(self):
        
        self.roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def convert(self, s: str) -> int:
       
        total = 0
        n = len(s)
        for i in range(n):
            current_value = self.roman_map[s[i]]
            
            if i + 1 < n and self.roman_map[s[i+1]] > current_value:
                
                total -= current_value
            else:
                
                total += current_value
        return total


converter = RomanToInteger()


print(f"III: {converter.convert('III')}")
print(f"LVIII: {converter.convert('LVIII')}")
print(f"MCMXCIV: {converter.convert('MCMXCIV')}")
