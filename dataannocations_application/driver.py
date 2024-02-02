def read_file(message_file: str) -> dict[int, str]:
    message = {}
    f = open(message_file, "r")
    for line in f.readlines():
        temp = line.split(" ")
        message[int(temp[0])] = temp[1].removesuffix("\n")
    return message
    
# parse ends of pyramid
def decode(message_file: str) -> str:
    lines = read_file(message_file)
    index = 1
    line = 1
    answer = ""
    while index <= len(lines):
        # print(index) # DEBUG
        answer += lines[index] + " "

        line += 1
        index += line
    
    return answer.removesuffix(" ")

def main():
    # print(decode("text.txt"))
    print(decode("coding_qual_input.txt"))

main()