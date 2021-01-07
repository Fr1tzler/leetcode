public class CustomStack 
{
    private int[] stack;
    
    private int currentPos = -1;
    
    private int maxSize;

    public CustomStack(int maxSize) 
    {
        stack = new int[maxSize];
        this.maxSize = maxSize;
    }
    
    public void Push(int x) 
    {
        if (currentPos < maxSize - 1) 
            stack[++currentPos] = x;
    }
    
    public int Pop() 
    {
        if (currentPos < 0) 
            return -1;
        
        return stack[currentPos--];
    }
    
    public void Increment(int k, int val) 
    {
        for (int i = 0; i < k && i < maxSize; i++) 
            stack[i] += val;
    }
}