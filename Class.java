public String asciiSumCheck(String[] input1, int input2, int input3) {
    for (int i = 0; i < input2; i++) {
        for (int j = i + 1; j < input2; j++) {
            int sum = (int)input1[i].charAt(0) + (int)input1[j].charAt(0);
            if (sum == input3) {
                return input1[i] + input1[j];
            }
        }
    }
    return "-1";
}
