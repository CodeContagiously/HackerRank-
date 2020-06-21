public class MinMax {
    public static void main(String[] args) {
        MinMax array = new MinMax();
        int[] a = {1, 2, 3, 4};
        int[] b = {4, 3, 2, 1}; // there is more to this.
        int[] sol = array.sumArray(a, b);
        System.out.print(a);
        System.out.println(b); // more to this
        System.out.println(sol);
    }

    static void miniMaxSum(int[] arr) {
        int[] sumList = new int[5];
        int Sum;
        for (int i = 0; i < 5; i++) {
            Sum = arraySum(sumArray(Index(arr, 0, i), Index(arr, i + 1, arr.length)));
            //define index and sum methods, SumArrays
            sumList[i] = Sum;
        }

    }

    static int arraySum(int[] b)
    //sum elements in array
    {
        int total = 0;
        for (int i = 0; i < b.length; i++) {
            total += b[i];
        }
        return total;
    }

    static int[] sumArray(int[] a, int[] b)
    //Sum arrays
    {
        int[] newArray = new int[a.length + b.length];
        int i = 0;
        for (int j = 0; j < a.length; j++) {
            newArray[i] += a[j];
            i += 1;
        }
        for (int j = 0; j < b.length; j++) {
            newArray[i] = b[j];
        }
        return newArray;
    }

    static int[] Index(int[] a, int start, int end) {
        int[] newArray = new int[end - start];
        for (int j = 0; j < end - start; j++) {
            newArray[j] = a[start + j];
        }
        return newArray;

    }

    ///.............................../////....................///.........

}

