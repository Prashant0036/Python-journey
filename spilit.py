def split_and_join(line):
    l=line.split(" ")
    
    lc="-".join(l)
    return lc

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)