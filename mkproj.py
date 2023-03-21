import os
import sys
import shutil

VERSION = "Mkproj version 0.7"
SUPP_LANG = ["java","py","c","cpp","cs","js","go","rs","rb","kt","ts","lua","lsp","scala","swift","php","html",]


SUPP_LANG_HELP = """
Supported languages:
Language    Extension
---------------------
Java        java
Python      py
C           c
C++         cpp
C#          cs
JavaScript  js
Go          go
Rust        rs
Ruby        rb
Kotlin      kt
TypeScript  ts
Lua         lua
Lisp        lsp
Scala       scala
Swift       swift
PHP         php
HTML        html
---------------------
"""

HELP_TEXT = """
mkproj - Generates a project with a hello world program in the specified language
Command line arguments:

    -help\tShow this help text (mkproj -help)
    -cr\t\tCreate a new project (mkproj -cr [your project name] [programming language extension])
    -crf\tCreate a  new file (mkproj -crf [your file name] [programming language extension])
    -sl\t\tShow supported languages (mkproj -sl)    
    -v\t\tShow the version of mkproj (mkproj -v)
  
"""

FILE_EXISTS = "File already exists do you want to rewrite it? (y/n)"
SOURCE_CODE_CANCELED = "Yout source code wasn't created"
CSS_FILE_Q = "Do you want a css file?(y/n)"
NO_CSS_FILE  = "There will be no css file"
SOURCE_CODE_CREATED = "Source code has been created."
PROJECT_EXISTS = "Project already exists do you want to rewrite it? (y/n)"
ASK_FOR_MAIN_FILE = "Please type the name for your main file: "
PROJECT_CREATED = "project has been made"
PROJECT_CANCELED = "Yout project wasn't created"
NO_COMMANDLNE_ARGS = "No command line arguments try -help"
NO_LANG = "There is no supported language named: "
MISSING_COMMANDLINE_AG = "Missing command line arguments use -help"
UNKNOWN_COMMAND = " is an unknown command use -help"
LANG_SELECT = "Please select a language,to see the supported languages use \"mkproj -sl\" "
MANY_ARGS = "To mutch arguments try -help"


def check_dir(dir_name):
    sub_dirs =[name for name in os.listdir("./") if os.path.isdir(os.path.join("./", name))]
    return dir_name in sub_dirs

def check_file(file_name):
    files = os.listdir("./")
    sub_files = [name for name in files if os.path.isfile("./"+'/'+name)]
    return file_name in sub_files

def check_lanuage(lang):
    return lang in SUPP_LANG

def write_file(filename,content):
    with open(filename,"w") as f:
        f.write(content)
        f.close()

def get_hello_world(filename,lang):

    if lang == SUPP_LANG[0]: # Java code
        return ("class "+filename[0].upper() + filename[1::]+" {\n "
                "\tpublic static void main(String[] args) {\n"
                "\t\tSystem.out.println(\"Hello, World!\");\n"
                "\t}\n"
                "}")

    if lang == SUPP_LANG[1]: # Python code
        return ("def main():\n"
                "\tprint(\"Hello world!\")\n\n"
                "if __name__ == \"__main__\":\n"
                "\tmain()")

    if lang == SUPP_LANG[2]: # C code
        return ("#include <stdio.h>\n"
                "int main() {\n"
                "\tprintf(\"Hello, World!\");\n"
                "\treturn 0;\n"
                "}")

    if lang == SUPP_LANG[3]: # C++ code
        return ("#include <iostream>\n"
                "int main() {\n"
                "\tstd::cout << \"Hello World!\";\n"
                "\treturn 0;\n"
                "}")

    if lang == SUPP_LANG[4]: # C# code
        return ("namespace "+filename[0].upper() + filename[1::]+"Namespace\n"
                "{\n"
                "\tclass "+filename[0].upper() + filename[1::]+" {\n"
                "\t\tstatic void Main(string[] args)\n"
                "\t\t{\n"
                "\t\t\tSystem.Console.WriteLine(\"Hello World!\");\n"
                "\t\t}\n"
                "\t}\n"
            "}")

    if lang == SUPP_LANG[5]: # JavaScript code
        return "console.log(\"Hello world!\")"
    
    if lang == SUPP_LANG[6]: # Go code
        return ("package main\n\n"
                "import \"fmt\"\n\n"
                "func main() {\n"
                "\tfmt.Println(\"Hello world!\")\n"
                "}")
    
    if lang == SUPP_LANG[7]:# Rust code
        return ("fn main() {\n"
                "\tprintln!(\"Hello world!\");\n"
                "}")
    
    if lang == SUPP_LANG[8]:# Ruby code
        return ("puts \"Hello world!\"")
    
    if lang == SUPP_LANG[9]:# Kotlin code
        return ("fun main() {\n"
                "\tprintln(\"Hello world!\")\n"
                "}")
    
    if lang == SUPP_LANG[10]:# TypeScript code
        return ("console.log(\"Hello world!\")")
    
    if lang == SUPP_LANG[11]:# Lua code
        return ("print(\"Hello world!\")")
    
    if lang == SUPP_LANG[12]:# Lisp code
        return ("(print \"Hello world!\")")
    
    if lang == SUPP_LANG[13]:# Scala code
        return ("object "+filename[0].upper() + filename[1::]+" {\n"
                "\tdef main(args: Array[String]): Unit = {\n"
                "\t\tprintln(\"Hello world!\")\n"
                "\t}\n"
                "}")
    
    if lang == SUPP_LANG[14]:# Swift code
        return ("print(\"Hello world!\")")
    
    if lang == SUPP_LANG[15]:# PHP code
        return ("<?php\n"
                "\techo \"Hello world!\";\n"
                "?>")
    

    if lang == SUPP_LANG[16]:# html code
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
        need_frewrite = input(FILE_EXISTS)
        if need_frewrite.lower() == "y":
            write_file(path +"/" + file_name,get_hello_world(class_name,lang))

        else:
            print(SOURCE_CODE_CANCELED)

    else:
        write_file(path +"/" + file_name,get_hello_world(class_name,lang))

    if lang == SUPP_LANG[16]: # if html
        need_css = input(CSS_FILE_Q)

        if need_css.lower() == "y":
            file_name = class_name + ".css"
            write_file(path +"/" + file_name,get_hello_world(class_name,"css"))
        else:
            print(NO_CSS_FILE)
    print(SOURCE_CODE_CREATED)

def create_proj(name,lang):

    if check_dir(name):
        need_rewrite = input(PROJECT_EXISTS)
        if need_rewrite.lower() == "y":
            shutil.rmtree(name)
            parent_dir = "./"
            path = os.path.join(parent_dir, name)
            class_name = input(ASK_FOR_MAIN_FILE)

            os.mkdir(path)
            create_source_code(lang, path,class_name)
            print(name, PROJECT_CREATED)
            sys.exit()
        else:
            print(PROJECT_CANCELED)
        sys.exit()
    parent_dir = "./"
    path = os.path.join(parent_dir, name)
    class_name = input(ASK_FOR_MAIN_FILE)

    os.mkdir(path)
    create_source_code(lang, path,class_name)
    print(name,PROJECT_CREATED)

def handle_arguments(arg):

    if len(arg)-1 == 0:
        print(NO_COMMANDLNE_ARGS)
        sys.exit()

    if arg[1] == "-help":
        print(HELP_TEXT)
        sys.exit()

    if arg[1] == "-sl":
        print(SUPP_LANG_HELP)
        sys.exit()

    if arg[1] == "-cr":
        if len(arg) == 4:
            if check_lanuage(arg[3]):
                create_proj(arg[2],arg[3])
            else: print(NO_LANG ,arg[3])
        else:
            print(MISSING_COMMANDLINE_AG)
        sys.exit()

    if arg[1] == "-crf":
        if len(arg) == 4:
            if check_lanuage(arg[3]):
                create_source_code(arg[3],"./",arg[2])
            else: print(NO_LANG,arg[3])
        else:
            print(MISSING_COMMANDLINE_AG)
        sys.exit()

    if arg[1] == "-v":
        print(VERSION)

        sys.exit()

    if arg[1][0] == "-":
        print(arg[1],UNKNOWN_COMMAND)
        sys.exit()

    if len(arg)-1 == 1 :
        print(LANG_SELECT)
        sys.exit()

    if len(arg) > 3:
        print(MANY_ARGS)
        sys.exit()


def main():
    handle_arguments(sys.argv)
    



if __name__ == "__main__":
    main()