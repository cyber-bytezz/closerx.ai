import java.io.*;
import java.util.*;

// Read only region start
class UserMainCode
{
    public String asciiSumCheck(String[] input1, int input2, int input3){
        // Read only region end
        for (int i = 0; i < input2; i++) {
            char a = input1[i].charAt(0);
            for (int j = i + 1; j < input2; j++) {
                char b = input1[j].charAt(0);
                if ((int)a + (int)b == input3) {
                    return "" + a + b;
                }
            }
        }
        return "-1";
    }
}
