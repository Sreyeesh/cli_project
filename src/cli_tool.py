import argparse
import os


def list_files(path):
    """ List files in the speicificed directory path. """
    files = os.listdir(path)
    print(f"Files in {path}: {files}")



def main():
    parser = argparse.ArgumentParser(description="Simple CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    greet_parser = subparsers.add_parser("greet")
    greet_parser.add_argument("name", help="Your name")

    list_files_parser = subparsers.add_parser("list-files")
    list_files_parser.add_argument("path", help="Directory path")
    
    args = parser.parse_args()
    if args.command == "greet":
        print(f"Hello, {args.name} !")
    elif args.command == "list-files":
        list_files(args.path)


            
    
    

  


if __name__ == "__main__":
    main()