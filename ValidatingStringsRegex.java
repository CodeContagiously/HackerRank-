/**
Given a string write a regex expression to find all strings that start and end with same letter
example:

"a", "aa", and "bababbb" is a match
"ab" and "baba" is not a match
**/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    final static Scanner scan = new Scanner(System.in);
    final static String fileName = System.getenv("OUTPUT_PATH");
     
    final static String regularExpression = "^(a).*(a)$|^(b).*(b)$"; //my code...
    

    public static void main(String[] args) throws IOException 
    {
        int query = Integer.parseInt(scan.nextLine());
        String[] result = new String[query];
        Arrays.fill(result, "False");
        
        for (int i = 0; i < query; i++) 
        {
            String someString = scan.nextLine();
            // if(someString.length()==0) result[i] = "True";
            if(someString.length()==1 || someString.length()==0) result[i] = "True"; //my code, dealing with edge case of single string
            else if (someString.matches(regularExpression)) {
                result[i] = "True";
            }
        }
        
        BufferedWriter fileOut = new BufferedWriter(new FileWriter(fileName));
        for (String res: result) {
            fileOut.write(res + "\n");
        }
        
        fileOut.close();
    }
}
