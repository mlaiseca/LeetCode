class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # usually i would use split() but cannot split using '' or else there will be an error
        ran = list(ransomNote)
        mag = list(magazine)

        for x in ran:
            try:
                mag.remove(x)
            except ValueError:
                return False
            
        
        return True
                
class TestCase:
    t_1 = {'r': 'a', 'm': 'b'}
    t_2 = {'r': 'aa', 'm': 'ab'}
    t_3 = {'r': 'aa', 'm': 'aab'}


t = TestCase()
s = Solution()

# test 1
result = s.canConstruct(t.t_1.get('r'), t.t_1.get('m'))
print(result)

# test 2
result = s.canConstruct(t.t_2.get('r'), t.t_2.get('m'))
print(result)

# test 3
result = s.canConstruct(t.t_3.get('r'), t.t_3.get('m'))
print(result)
