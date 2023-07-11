# Embedded_Linux
This will have all my work and progress while learning from scratch Embedded Linux 
Starting the journey there will be a few concepts one should be aware of before starting the actual develeopment : 

## The build/compilation process : 

This will describe the major steps that any **C code** runs to before being finally executed. 
Esentially translating the original text from being a high level programming language to a machine code.

### Preprocessing : 

This is the first step, It targets the commands beginning with `#` ( nammed directives ).
Its main purpose is to **eliminate comments**, expand **Macros** and **included Files** as long as dealing with **conditional compiling**.

Lets take a look at #include : 
This statement indicates that I want to read from a file, so the preprocessor will open that file and paste all its content to current file.

We can ask the compiler to preprocess a file simply by calling : 
`gcc -E helloworld.c -o helloworld.i`

### Compiler : 

The compiler have an essential job which is to convert the text files to an intermediate format : **Object File**.

#### Files as seen by the compiler : 

From a compiler perspective, Files are not the end goal but they are just a way of feeding the compiler with source code.
We are basically expecting from the compiler to take our .CPP / .C files and convert them to object files as we said.
The resulting files from the compiler are **Assembly files** which is still **readable** by humans but very **specefic to the target processor**

#### Optimization : 

The compiling phase includes also optimizing code in term of size and perfromance.
One can choose either to work with an optimizer or not as well as choosing the focus of optimizing ( size / time / etc.. ) .


### Assembly : 

This is the third step the in the whole process and it takes as input the assembly code provided after step 2 and transform it into **pure binary code** 

### Linking : 

This is the final step and it will generate the final .exe file which is the executable file.

The need to a linker came by the fact that each file in C is compiled seperately for example : 
```C
///FILE_1.CPP :

int check ( int a ) ;

int add ( int a , int b )
{
if check ( a )
return 1 ;
}

```
this examples compiles in C++ but there will be a problem when building because building invokes the linker.

In fact when a compiler create the .o file it puts a **reference** or so called **signature** to the functions.

This signature depens on three things : **Function name** , **Return Type** and **Number of parameters**.

The Linker will simply match the called function to the declared one ( same name , params and return type ).

We can also talk about two major concepts : 

#### External linking :
Let's take a look at this example where we hve two files : 


```
// add.c
int amount = 0 ;
int main ()
{
SUB();
return 0 ;
}
```

```
// sub.c
void sub()
{
Amount = 10 - 3  ; 
}
```
Here we will have a compiler problem : Amount is undeclared in sub.c
The solution here is to use the storage class **extern**.

#### Internal linking : 
Internal linking is the opposite of the external, here we want to make a variable private to a certain file using the keyword **static**.


## Linux Libraries : 
Generally speaking, The code we write will be used several times which led us to introduce the concept of a library which will enable reusing our code as much as we need.

Mainly there is two types of libraries : 

### Static Libraries :

The linker here makes a copy of all library functions to the .exe file.

#### Creating the library
To create a static library in C we first need to compile the source code of all the files that we will have in this library
For instance : I have add.c and sub.c : 
`gcc -c add.c -o add.o`
`gcc -c sub.c -o sub.o`
finally : 
`ar rcs calc.a add.o sub.o`
Here `ar` stands for **archive** and `rcs` stands for **replace and create** static libray.

#### Data Linking : 
First, We create the object file of main 
`gcc -c main.c -o main.o`
Now we will **link** the main program with the static library : 
`gcc main.c -L. -calc -o main`

==> As a Final result Static Linking **combines** your work with the library into **one binary code**.

### Dynamic Library

Every program can access this library at runtime avoiding the creation of multiple copies for every program.
When using dynamic Library we are attacking the biggest of our fears which is the loss of memory.
Doing so makes possible for different program to use the same library without actually having them, IN other terms we will not have one big binary code executed that have both the application program and the library code.
Folowing these steps I managed to Create my own 'hello world" example of a shared library.

#### Compiling with Position Independent Code : 

`gcc -c -Wall -Werror -fpic geometry.c`
this will create the .o file : ![image](https://github.com/oussemajelassi/Embedded_Linux/assets/100140668/a1ab4100-4455-4985-929d-9cc4dca1d837)

#### Creating the shared library file : 

We will use the object file created to create th .so file wich is the shared library : 
`gcc -shared -o libgeometry.so geometry.o`
![image](https://github.com/oussemajelassi/Embedded_Linux/assets/100140668/89bd33fb-d545-4fc1-b715-447940d6e1e2)

#### Compile Main Program : 

Now we have to compile Main, We have to tell the compiler where to find our library and so : 
`gcc -L/home/flooki/Desktop/Embedded_Linux/Shared_Library_Manipulation/My_Library -Wall -o program main.c -lgeometry`

#### Making our Library ready for use to any program :

Next step is To make our library ready for use.
Typically the Loader have a default location for all libraries, since our new masterpiece is created away from this default place we either have to put it there or we have to export its path so it become recognizable.

1 : `sudo cp libgeometry.so /usr/lib`

2 : `export LD_LIBRARY_PATH=:/home/flooki/Desktop/Embedded_Linux/Shared_Library_Manipulation/My_Library`


==> ![image](https://github.com/oussemajelassi/Embedded_Linux/assets/100140668/7fc993a0-6ac7-41b4-b29d-90299718b1d5)




