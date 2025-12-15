import argparse
import sys
from create_template import execute_template_functions
from personalize_docs import rename_parent_folder, modify_discussion_files
from version import __version__

#------------------------------------------------------------------------------------------------------#
#--------------------------------------- Interactive wizard logic -------------------------------------#
#------------------------------------------------------------------------------------------------------#

def run_wizard():
    print("-----------------Class Directory Creation Tool-----------------\n")
    print(f"                            v{__version__}\n")
    print("💡\033[3m Press CTRL + C at any point to quit. \033[0m\n")
    initial_prompt = input("💬 Would you like you create a new class template directory? (y or n): ")
    print()
    while True:
        while True:
            if initial_prompt.lower() == "y": 
                execute_template_functions()
                print("✅\033[3m The template has been created. \033[0m\n")
                break
            elif initial_prompt.lower() == "n":
                print("ℹ️\033[3m Exiting program. \033[0m")
                sys.exit(0)
            else:
                print("❌\033[3m Invalid input. \033[0m\n")
                initial_prompt = input("💬 Please enter 'y' or 'n': ")
                print()
                continue
        folder_name = input("💬 Enter the new course name: ").strip()
        folder_mod = rename_parent_folder(folder_name)
        print(f"\n✅\033[3m The template has been renamed to '{folder_mod}'. \033[0m\n")
        file_name = input("💬 Enter the class name for the Discussions files: ").strip()
        file_mod = modify_discussion_files(folder_name, file_name) 
        print(f"\n✅\033[3m The class has been specified as '{file_mod}' in the Discussions files. \033[0m\n")
        secondary_prompt = input("💬 Would you like to create another template directory? (y or n): ")
        print()
        while True:
            if secondary_prompt.lower() == "y":
                break
            elif secondary_prompt.lower() == "n":
                print("ℹ️\033[3m Exiting program. \033[0m")
                sys.exit(0)
            else:
                print("❌\033[3m Invalid input. \033[0m\n")
                secondary_prompt = input("💬 Please enter 'y' or 'n': ")
                print()
                continue

#------------------------------------------------------------------------------------------------------#
#----------------------------------- CLI argument and error handling ----------------------------------#
#------------------------------------------------------------------------------------------------------#

def main():
    # TODO: Add additional non-interactive mode flags (parameters) later (e.g., --create, --rename, --modify)
    # To see available flags, type 'python cli.py --help' in the Windows command line
    parser = argparse.ArgumentParser(
        prog="course-template",
        description="Interactive wizard to create and personalize class templates."
    )
    parser.add_argument(
        "--noninteractive",
        action = "store_true",
        help = "Run without interactive prompts (not yet fully implemented)."
    )
    parser.add_argument(
        "--interactive",
        action = "store_true", 
        help = "Launch in interactive mode."
    )
    parser.add_argument(
        "--version", 
        action = "store_true", 
        help = "Show version info and exit.")
    args = parser.parse_args()

    # Error and flag handling block
    try:
        if args.noninteractive:
            print("\nℹ️\033[3m Running in non-interactive mode... \033[0m")
            print("\n❌\033[3m Not yet fully implemented, exiting program... \033[0m")
            # TODO: Add logic here later
            sys.exit(0)
        elif args.interactive:
            print("\nℹ️\033[3m Starting interactive wizard... \033[0m\n")
            run_wizard()
        elif args.version:
            print(f"\nℹ️ Class Directory Creation Tool v{__version__}")
            sys.exit(0)
        else:
            print("\nℹ️\033[3m Starting interactive wizard... \033[0m\n")
            run_wizard()
    except KeyboardInterrupt:
        print("\n\nℹ️\033[3m Cancelled by user. \033[0m")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

# Entry point

if __name__ == "__main__":
    main()