import os
path = input("Enter a  path (Copy from above) : ")
extension = input("Enter an extension(Eg: .py, .jpg ) : ")
flag = input("Do you want to print the whole directory summary (y/n) : ")
pre_files = list()
final_files = list()

def validate_extension():
    count = 0
    for i in extension:
        if i is ".":
            count += 1
    if count!=1:
        raise Exception("Invalid extension. Check the examples given")

def preprocess():
    print("Please wait while proccessing...")
    global final_files
    global pre_files
    for (dirpath, dirnames, filenames) in os.walk(path):
        pre_files.append(filenames)
        
    for i in pre_files:
        if str(type(i))=="<class 'list'>":
            for j in i:
                final_files.append(j)
        else:
            final_files.append(i)
    return final_files

def percent(files, ext):
    summary = dict()
    count = 0
    result = float()
    for i in files:
        try:
            if i[i.index("."):]== ext:
                count = count+1
            else:
                if i[i.index("."):] in list(summary.keys()):
                    summary[i[i.index("."):]] +=1
                else:
                    summary[i[i.index("."):]] = 1
        except: continue
    try:
        result = round(count*100/len(files), 4)
        if count is 0:
            print("WARNING:number of files found with this extension is 0. Check you extension.")
        return result, len(files), count, summary
    except:
        print("0 files found. Check your path.")
        return None
    



if __name__ == "__main__":
    validate_extension()
    files = preprocess()
    result = percent(files, extension)
    if str(type(result))=="<class 'tuple'>":
        print("==============EXTENSION SUMMARY===================")
        print(f"{extension} files :\t",result[2])
        print("Total files :\t", result[1])
        print("\n---------------------------")
        print("Percentage :\t", result[0],"%")
        print("---------------------------")
        if flag.lower() == "n":
            print("==================================================")
        else:
            others = result[3]
            print("\n=====Other Files=====")
            for i, j in zip(others.keys(), others.values()):
                print(f"{i} :\t{j}")
            print("==================================================")
