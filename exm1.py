import os
path = input("enter path")
output_file="err2.log"

def function(filepath,output_filepath):
    count = 0

    with open(filepath,"r") as f, open(output_filepath, "w") as out:
        
        lines=f.readlines()

        print("-----------Full Data----------")
        print("".join(lines))

        last_three_lines=lines[-3:]
        print("------------Last 3 lines -------")
        print("".join(last_three_lines))

        f.seek(0) #pointerrrrrr
        print("---------------error lines---------------")

        for line in f:
            if "error" in line.lower():
                print(line,end="")
                out.write(line)
                count+=1
    return count


filename = os.path.basename(path)
print("File name:", filename)

result=function(path,output_file)
print("\nTotal error count",result)

#with open(path, "r") as f:
#   data = f.read()

#print(data)
