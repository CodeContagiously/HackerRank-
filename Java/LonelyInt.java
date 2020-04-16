public class LonelyInt
{
    public static void main(String[] args){}
    static int lonelyinteger(int[] a)
    {
        int lonelyInt = 0; //set lonelyInt to 0
        for (int num : a)
        {
            lonelyInt = lonelyInt ^ num; // use "xor" operator to manipulate bit so only the unique int remains
        }
        return lonelyInt;
    }
}
