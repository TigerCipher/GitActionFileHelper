import os
import sys
import getopt
import fileinput

def main(argv):
    #Set up defaults for when no options are passed
    buildType = 'mvn'
    inFile = 'templates/maven_template.yml'
    outFile = './maven.yml'
    token_artifact_name = 'ARTIFACT_NAME'
    data_to_insert = 'MyProject'
    try:
        opts, args = getopt.getopt(argv, "ht:o:n:", ["type=", "output=", "name="])
    except getopt.GetoptError:
        print("actionhelper -t <build type> -o <output file>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("actionhelper -t <build type> -o <output file> -n <artifact name>")
            print("Default options:")
            print("Type = mvn")
            print("Output file = maven.yml")
            print("Name = MyProject")
            sys.exit()
        elif opt in ("-t", "--type"):
            buildType = arg
        elif opt in ("-o", "--output"):
            outFile = arg
        elif opt in ("-n", "--name"):
            data_to_insert = arg
    print("Creating workflow file", outFile, "with build type", buildType)

    if buildType == "mvn" or buildType == "maven":
        inFile = "templates/maven_template.yml"
    
    app_path = "./"
    if getattr(sys, 'frozen', False):
        app_path = os.path.dirname(sys.executable)
    else:
        app_path = os.path.dirname(os.path.abspath(__file__))

    inputFile = os.path.join(app_path, inFile)
    f = open(inputFile, 'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace(token_artifact_name, data_to_insert)

    f = open(outFile, 'w')
    f.write(newdata)
    f.close()


if __name__ == "__main__":
    main(sys.argv[1:])