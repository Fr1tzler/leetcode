public class Solution 
{
    public string RestoreString(string s, int[] indices) 
    {
        var res = new char[s.Length];
        
        for(var i = 0; i < s.Length; ++i)
            res[indices[i]] = s[i]; 
        
        return new string(res);  
    }
}