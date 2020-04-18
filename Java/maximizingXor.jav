#WarmUp
#Hackerrank Bit Manipulation [https://www.hackerrank.com/challenges/maximizing-xor/problem]
#

static int maximizingXor(int l, int r)
    {
        int maxVal = 0;
        for (int num=l; num <= r-1; num++ )
        {
            if((num^num+1) > maxVal) maxVal =  num ^ num+1;
        }
        return maxVal;


    }
