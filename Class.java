import java.io.*;
import java.util.*;

// Read only region start
class UserMainCode
{
    public int maxOddAdjacentPair(int input1, int[] input2){
        // Read only region end
        int maxSum = -1;
        for (int i = 0; i < input1 - 1; i++) {
            int sum = input2[i] + input2[i + 1];
            if (sum % 2 != 0 && sum > maxSum) {
                maxSum = sum;
            }
        }
        return maxSum;
    }
}
