import os
import sys
import shutil

VERSION = "Mkproj version 0.8"
SUPP_LANG = ["java","py","c","cpp","cs","js","go","rs","rb","kt","ts","lua","lsp","scala","swift","php","html",]
COMMAND_LINE_ARGS = ["-help","-cr","-crf","-diradd","-fileadd","-sl","-v","-creator"]

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
    -diradd\tAdd a directory to your project (mkproj -diradd [directory name])
    \t\t (mkproj -diradd [root directory name] [directory name])
    -fileadd\tAdd an empty file to your project (mkproj -fileadd [file name] [programming language extension])
    -sl\t\tShow supported languages (mkproj -sl)    
    -v\t\tShow the version of mkproj (mkproj -v)
    -creator\tShow the creator of mkproj (mkproj -creator)
"""

CREATOR_TEXT = """
This program was made by:
    Name:\tSzolnoki Alex
    Email:\tszolnoki.alex699@gmail.com
    Github:\thttps://github.com/thetalkingweed
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
NO_COMMANDLINE_ARGS = "No command line arguments try -help"
NO_LANG = "There is no supported language named: "
MISSING_COMMANDLINE_AG = "Missing command line arguments use -help"
UNKNOWN_COMMAND = " is an unknown command use -help"
LANG_SELECT = "Please select a language,to see the supported languages use \"mkproj -sl\" "
MANY_ARGS = "To mutch arguments try -help"
DIR_EXISTS = "Directory already exists."
DIR_CREATED = "Directory has been created."
DIR_NOT_EXISTS = "Directory doesn't exists."
FILE_CREATED = "File has been created."

JAVA_HELLO = """
public class main_class_name {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        }
    }
"""
PYTHNO_HELLO = """
def main():
    print("Hello world!")

if __name__ == "__main__":
    main()
"""

C_HELLO = """
#include <stdio.h>
int main() {
    printf("Hello, World!");
    return 0;
}
"""

CPP_HELLO = """
#include <iostream>
int main() {
    std::cout << "Hello World!";
    return 0;
}
"""

CS_HELLO = """
namespace main_class_nameNamespace
{
    class main_class_name
    {
        static void Main(string[] args)
        {
            System.Console.WriteLine("Hello, World!");
        }
    }
}
"""

JS_HELLO = """
console.log("Hello, World!");
"""

GO_HELLO = """
package main
import "fmt"
func main() {
    fmt.Println("Hello, World!")
}
"""

RUST_HELLO = """
fn main() {
    println!("Hello, world!");
}
"""

RUBY_HELLO = """
puts "Hello, World!"
"""

KOTLIN_HELLO = """
fun main(args: Array<String>) {
    println("Hello, World!")
}
"""

TYPESCRIPT_HELLO = """
console.log("Hello, World!");
"""

LUA_HELLO = """
print("Hello, World!")
"""

LISP_HELLO = """
(print "Hello, World!")
"""

SCALA_HELLO = """
object name_of_object {
    def main(args: Array[String]) {
        println("Hello, world!")
    }
}
"""
SWIFT_HELLO = """
print("Hello, World!")
"""

PHP_HELLO = """
<?php
    echo "Hello, World!";
?>
"""

HTML_HELLO = """
<!DOCTYPE html>
<html lang=en>
<head>
    <meta charset=UTF-8>
    <meta http-equiv=X-UA-Compatible content=IE=edge>
    <meta name=viewport content=width=device-width, initial-scale=1.0>
    <link rel=stylesheet href=+filename_of_html+.css>
    <title>+filename_of_html+</title>
</head>
    <body>
        <div class=container>
            <h2>Hello World!</h2>
        </div>
    </body>
</html>

"""

CSS_BODY = """
.container{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 30%;
    margin: auto;
}
h2{
    font-family: 'Courier New', Courier, monospace;
}
"""


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
        return JAVA_HELLO.replace("main_class_name",filename[0].upper() + filename[1::])

    if lang == SUPP_LANG[1]: # Python code
        return PYTHNO_HELLO

    if lang == SUPP_LANG[2]: # C code
        return C_HELLO

    if lang == SUPP_LANG[3]: # C++ code
        return CPP_HELLO

    if lang == SUPP_LANG[4]: # C# code
        return CS_HELLO.replace("main_class_name",filename[0].upper() + filename[1::])

    if lang == SUPP_LANG[5]: # JavaScript code
        return JS_HELLO
    
    if lang == SUPP_LANG[6]: # Go code
        return GO_HELLO
    
    if lang == SUPP_LANG[7]:# Rust code
        return RUST_HELLO
    
    if lang == SUPP_LANG[8]:# Ruby code
        return RUBY_HELLO
    
    if lang == SUPP_LANG[9]:# Kotlin code
        return KOTLIN_HELLO
    
    if lang == SUPP_LANG[10]:# TypeScript code
        return TYPESCRIPT_HELLO
    
    if lang == SUPP_LANG[11]:# Lua code
        return LUA_HELLO
    
    if lang == SUPP_LANG[12]:# Lisp code
        return LISP_HELLO
    
    if lang == SUPP_LANG[13]:# Scala code
        return SCALA_HELLO.replace("name_of_object",filename[0].upper() + filename[1::])
    
    if lang == SUPP_LANG[14]:# Swift code
        return SWIFT_HELLO
    
    if lang == SUPP_LANG[15]:# PHP code
        return PHP_HELLO

    if lang == SUPP_LANG[16]:# html code
        return HTML_HELLO.replace("+filename_of_html+",filename)
    
    if lang == "css":
        return CSS_BODY


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
        print(NO_COMMANDLINE_ARGS)
        sys.exit()

    if arg[1] == COMMAND_LINE_ARGS[0]: # -help
        print(HELP_TEXT)
        sys.exit()

    if arg[1] == COMMAND_LINE_ARGS[5]: # -sl
        print(SUPP_LANG_HELP)
        sys.exit()

    if arg[1] == COMMAND_LINE_ARGS[1]: # -cr
        if len(arg) == 4:
            if check_lanuage(arg[3]):
                create_proj(arg[2],arg[3])
            else: print(NO_LANG ,arg[3])
        else:
            print(MISSING_COMMANDLINE_AG)
        sys.exit()

    if arg[1] == COMMAND_LINE_ARGS[2]: # -crf
        if len(arg) == 4:
            if check_lanuage(arg[3]):
                create_source_code(arg[3],"./",arg[2])
            else: print(NO_LANG,arg[3])
        else:
            print(MISSING_COMMANDLINE_AG)
        sys.exit()

    if arg[1] == COMMAND_LINE_ARGS[3]: # -diradd
        if len(arg) == 3:
            if check_dir(arg[2]):
                print(DIR_EXISTS)
            else:
                os.mkdir(arg[2])
                print(DIR_CREATED)
        elif len(arg) == 4:
            if check_dir(arg[2]):
                os.mkdir(arg[2] + "/" + arg[3])
            elif not check_dir(arg[2]):
                print(arg[2],DIR_NOT_EXISTS)
        else:
            print(MANY_ARGS)
        sys.exit()

    if arg[1] == COMMAND_LINE_ARGS[4]: # -fileadd
        if len(arg) == 4:
            if check_file(arg[2]):
                need_frewrite = input(FILE_EXISTS)
                if need_frewrite.lower() == "y":
                    write_file(arg[2]+"."+arg[3],"")

                else:
                    print(SOURCE_CODE_CANCELED)

            elif not check_lanuage(arg[3]):
                print(NO_LANG,arg[3])
            else:
                write_file(arg[2]+"."+arg[3],"")
                print(FILE_CREATED)
        else:
            print(MISSING_COMMANDLINE_AG)
        sys.exit()

    if arg[1] == COMMAND_LINE_ARGS[6]: # -v
        print(VERSION)
        sys.exit()

    if arg[1] == COMMAND_LINE_ARGS[7]: # -creator
        print(CREATOR_TEXT)
        sys.exit()

    if arg[1] not in COMMAND_LINE_ARGS:
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