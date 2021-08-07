class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        #Declare left and right as 0
        #Move right forward
        ##if letter is unique add it to unique_to_index
        ##if len(unique_to_index) > 2 
        ##Update left and unique_to_index by removing the value at lowest index in s (value not seen in the longest time)
        ##You can get the char to remove by check min of unique_to_index values and then removing the char at that index(Since this map stores indices)
        ##update Maxlen with max(MaxLen, right - left + 1)
        ##NOTE RIGHT - LEFT + 1 = length of string
        left = 0
        right = 0
        unique_to_index = {}
        max_len = 0
        while(right < len(s)):
            unique_to_index[s[right]] = right
            if(len(unique_to_index) > 2):
                smallest_index_of_letters_encountered = min(unique_to_index.values()) #this is the index of the letter that has not been encountered in the longest time
                left = smallest_index_of_letters_encountered + 1
                unique_to_index.pop(s[smallest_index_of_letters_encountered])
            max_len = max(right-left + 1, max_len)
            right+=1
        return max_len
        
                        
                    
            
