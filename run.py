from core import Core
import sys, getopt

def main(argv):
    base = 'Required'
    current = 'Required'
    try:
        opts, args = getopt.getopt(argv,"hb:c:",["base=","current="])
    except getopt.GetoptError:
        print ('update_files_service.py -r <base_directory> -c <current_directory>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            sys.exit()
        elif opt in ("-b", "--base"):
            base = arg
        elif opt in ("-c", "--current"):
            current = arg
    
    print ('Base folder is "', base)
    print ('Current is "', current)

    core = Core(base, current)

    core.run()

if __name__ == "__main__":
   main(sys.argv[1:])