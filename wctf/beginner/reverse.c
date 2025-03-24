
int main()
{

	char* flag = "t`qcxo0s0o2.kd\.k\o0s0o20z";
	char* input[100];
	int index = strlen(flag)-1;

	for(int i = 0; i < strlen(flag); i++)
	{
		input[i] = flag[i]+3;
	}

	for(int j = 0; j <= index - 1; j+=2)
	{
		int tmp = flag[j];
		flag[j] = flag[index-1-j-1];
		flag[index-1-j-1] = tmp;
	}


}


flag = list("t`qcxo0s0o2.kd\\.k\\o0s0o20z")
index = len(flag) - 1
input_chars = [""] * len(flag)

# Step 1: Shift each character by +3 in ASCII
for i in range(len(flag)):
    input_chars[i] = chr(ord(flag[i]) + 3)

# Step 2: Reverse every two characters in the string
for j in range(0, index, 2):
    flag[j], flag[index - j - 1] = flag[index - j - 1], flag[j]

output_str = "".join(input_chars)
print(output_str)