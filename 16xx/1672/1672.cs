public class Solution 
{
    public int MaximumWealth(int[][] accounts) 
    {
        if (accounts == null)
            throw new NullReferenceException();
        
        var maxSum = 0;
        
        for (int i = 0; i < accounts.Length; ++i)
        {
            var row = accounts[i];
            var sum = 0;
            
            for (int j = 0; j < row.Length; ++j)
                sum += row[j];
            
            if (sum > maxSum)
                maxSum = sum;
        }
        
        return maxSum;
    }
}