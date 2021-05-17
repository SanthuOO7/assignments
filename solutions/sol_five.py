
# Write your code here
def modified_power_sets(s):
    powersets = []
    u_string = []
    for char in s:
        if char not in u_string:
            u_string.append(char)
    s = "".join(u_string) 
    for i in range(len(s)):
        for x in range(i, len(s)):
            powersets.append({s[i:x]})
    return len(powersets)

if __name__ == "__main__":
    for i in range(int(input())):
        inp_string = input()
        res = modified_power_sets(inp_string)
        print(res)