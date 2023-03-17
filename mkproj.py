import os
import sys
import shutil

VERSION = "0.6"
SUPP_LANG = ["java","py","c","cpp","cs","js","go","rs","html"]

def check_dir(dir_name):
    sub_dirs =[name for name in os.listdir("./") if os.path.isdir(os.path.join("./", name))]
    return dir_name in sub_dirs

def check_file(file_name):
    files = os.listdir("./")
    sub_files = [name for name in files if os.path.isfile("./"+'/'+name)]

    return file_name in sub_files

def check_lanuage(lang):
    lang_list = SUPP_LANG

    return lang in lang_list

def write_file(filename,content):
    with open(filename,"w") as f:
        f.write(content)
        f.close()

def get_hello_world(filename,lang):

    if lang == SUPP_LANG[0]:
        return ("class "+filename[0].upper() + filename[1::]+" {\n "
                "\tpublic static void main(String[] args) {\n"
                "\t\tSystem.out.println(\"Hello, World!\");\n"
                "\t}\n"
                "}")

    if lang == SUPP_LANG[1]:
        return ("def main():\n"
                "\tprint(\"Hello world!\")\n\n"
                "if __name__ == \"__main__\":\n"
                "\tmain()")

    if lang == SUPP_LANG[2]:
        return ("#include <stdio.h>\n"
                "int main() {\n"
                "\tprintf(\"Hello, World!\");\n"
                "\treturn 0;\n"
                "}")

    if lang == SUPP_LANG[3]:
        return ("#include <iostream>\n"
                "int main() {\n"
                "\tstd::cout << \"Hello World!\";\n"
                "\treturn 0;\n"
                "}")

    if lang == SUPP_LANG[4]:
        return ("namespace "+filename[0].upper() + filename[1::]+"Namespace\n"
                "{\n"
                "\tclass "+filename[0].upper() + filename[1::]+" {\n"
                "\t\tstatic void Main(string[] args)\n"
                "\t\t{\n"
                "\t\t\tSystem.Console.WriteLine(\"Hello World!\");\n"
                "\t\t}\n"
                "\t}\n"
            "}")

    if lang == SUPP_LANG[5]:
        return "console.log(\"Hello world!\")"
    if lang == SUPP_LANG[6]:
        return ("package main\n\n"
                "import \"fmt\"\n\n"
                "func main() {\n"
                "\tfmt.Println(\"Hello world!\")\n"
                "}")
    if lang == SUPP_LANG[7]:
        return ("fn main() {\n"
                "\tprintln!(\"Hello world!\");\n"
                "}")
    if lang == SUPP_LANG[8]:
        return ("<!DOCTYPE html>\n"
                "<html lang=\"en\">\n"
                "<head>\n"
                "\t<meta charset=\"UTF-8\">\n"
                "\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n"
                "\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
                "\t<link rel=\"stylesheet\" href=\""+filename+".css\">\n"
                "<title>"+filename+"</title>\n"
                "</head>\n"
                "<body>\n"
                "\t<div class=\"container\">\n"
                "\t\t<h2>Hello World!</h2>\n"
                "\t</div>\n"
                "</body>\n"
                "</html>\n")
    if lang == "css":
        return(".container{\n"
               "\tdisplay: flex;\n"
               "\tjustify-content: center;\n"
               "\talign-items: center;\n"
               "\twidth: 30%;\n"
               "\tmargin: auto;\n"
               "}\n\n"
               "h2{\n"
               "\tfont-family: 'Courier New', Courier, monospace;\n"
               "}\n"
        )


def create_source_code(lang,path,class_name):
    file_name =class_name +"." + lang

    if check_file(file_name):
        need_frewrite = input("File already exists do you want to rewrite it? (y/n)")
        if need_frewrite.lower() == "y":
            write_file(path +"/" + file_name,get_hello_world(class_name,lang))

        else:
            print("Yout source code wasn't created")

    else:
        write_file(path +"/" + file_name,get_hello_world(class_name,lang))

    if lang == "html":
        need_css = input("Do you want a css file?(y/n)")

        if need_css.lower() == "y":
            file_name = class_name + ".css"
            write_file(path +"/" + file_name,get_hello_world(class_name,"css"))
        else:
            print("There will be no css file")
    print("Source code has been created.")

def create_proj(name,lang):

    if check_dir(name):
        need_rewrite = input("Project already exists do you want to rewrite it? (y/n)")
        if need_rewrite.lower() == "y":
            shutil.rmtree(name)
            parent_dir = "./"
            path = os.path.join(parent_dir, name)
            class_name = input("Please type the name for your main file: ");

            os.mkdir(path)
            create_source_code(lang, path,class_name)
            print(name,"project has been made")
            sys.exit()
        else:
            print("Yout project wasn't created")
        sys.exit()
    parent_dir = "./"
    path = os.path.join(parent_dir, name)
    class_name = input("Please type the name for your main file: ");

    os.mkdir(path)
    create_source_code(lang, path,class_name)
    print(name,"project has been made")

def handle_arguments(arg):



    if len(arg)-1 == 0:
        print("No command line arguments try -help")
        sys.exit()

    if arg[1] == "-help":
        print("-sl\t - List the supported languages")
        print("-cr\t - Create a new project (mkproj -cr [your project name] [programming language extension])")
        print("-crf\t - Create a new file (mkproj -crf [your file name] [programming language extension])")
        print("-v\t - Version")
        sys.exit()

    if arg[1] == "-sl":
        lang_list = SUPP_LANG
        print("Supported languages:")
        print("Language\t Extension")
        print("-"*15)
        print("Java\t\t java")
        print("Python\t\t py")
        print("C\t\t c")
        print("C++\t\t cpp")
        print("C#\t\t cs")
        print("JavaScript\t js")
        print("Go\t\t go")
        print("Rust\t\t rs")
        print("HTML\t\t html")
        print("-"*15)

        sys.exit()

    if arg[1] == "-cr":
        if len(arg) == 4:
            if check_lanuage(arg[3]):
                create_proj(arg[2],arg[3])
            else: print("There is no language named: ",arg[3])
        else:
            print("Missing command line arguments use -help")
        sys.exit()


    if arg[1] == "-crf":
        if len(arg) == 4:
            if check_lanuage(arg[3]):
                create_source_code(arg[3],"./",arg[2])
            else: print("There is no language named: ",arg[3])
        else:
            print("Missing command line arguments use -help")
        sys.exit()

    if arg[1] == "-v":
        print("Mkproj version " + VERSION)

        sys.exit()




    if arg[1][0] == "-":
        print(arg[1],"is an unknown command use -help")
        sys.exit()

    if len(arg)-1 == 1 :
        print("Please select a language,to see the supported languages use \"mkproj -sl\" ")
        sys.exit()



    if len(arg) > 3:
        print("To mutch arguments try -help")
        sys.exit()

def main():
    handle_arguments(sys.argv)
    



if __name__ == "__main__":
    main()