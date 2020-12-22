public class Solution 
{
    public int NumJewelsInStones(string jewels, string stones) 
    {
        var res = 0;
        
        foreach (char c in jewels) 
            foreach (char s in stones) 
                if (c == s)
                    res++;
        
        return res;
    }
}