import sys, getopt, binascii

def main(argv):
#VARIABLES
    help_message = "main.py -i <inputfile> -o <outputfile>"


    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print help
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print help_message
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            output = arg
    if inputfile is not "^":
        try:
            f = open(inputfile, "rb")
        except:
            print "Error! Probably file not found..."
            sys.exit(2)

    whole = ("{:02x}".format(ord(c)) for c in f.read())
    tmp = list(whole)
    print "---File in Hex Below---"
    #print tmp

    string = ""
    index = 0
    
    while (index < len(tmp)):
        if ((index % 4) == 3):
            string += tmp[index]
            string += tmp[index - 1]
            string += tmp[index - 2]
            string += tmp[index - 3]

        index += 1

    outfile = open(output, "w+")
    outfile.write(binascii.unhexlify(string))
    outfile.close()

    print "--Done!---"

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        sys.exit(0)
