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


```C
// add.c
int amount = 0 ;
int main ()
{
SUB();
return 0 ;
}
```

```C
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



## Makefile :

A MakeFile is a file that will **automate** the compilation process.
For instance, If you have a library with many source code files we will have to go by all the commands for every file in order to finally get everything ready to execute. Make File will automate all this process.
One other utility is that when we **change one file** the makefile will not recreate all the object files but **only the changed** one which is far more rapid.

```Makefile
geometry.o : geometry.c
```
This syntax means that I want to **create** a .o file which is the compiled file and so I **need** the geometry.c file.

==> Its a dependency !
```Makefile
geometry.o : geometry.c
  `gcc -o geometry.o -c main.c`
```
Next we put the command that will generate geometry.o.
Note that we can put any other command such as echo or anything else.

```Makefile
program : main.o geometry.o
  gcc -o program main.o geometry.o
main.o : main.c
  `gcc -o main.o -c main.c`
geometry.o : geometry.c
  `gcc -o geometry.o -c geometry.c`
```
Now We are adding the final result which is program.

All that compiling process is now reduced to one command : 
`make` : ![image](https://github.com/oussemajelassi/Embedded_Linux/assets/100140668/c3fff869-ce1d-4a3e-a530-b7d8dc01540d)

## Linux Drivers : 

Linux drivers are a piece of code that handles everything related to a hardware.
Their main job is to abstract to us as users dealing with hardware.
The Relationship between User space and Kernel space is maintained only by **System calls**.

### Kernel Modules : 

First we should note that a Kernel module may not be a device driver att all.
As a Kernel module is a piece of compiled code that can be plugged in when needed and at runtime.
Modifying this module doesnot require us to reboot neither rebuild all the kernel.

==> Most of the drivers are built as kernel modules ! 

### Compiling the Modules : 

As already mentionned, Makefiles are a big help when talking about compiling however we need to pay attention when dealing with modules since it have a specefic syntax : 
```Makefile
obj-m += My_Module.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
```
### Modules in action :

Next we will plug in our module.
We will be interested in the ".ko" file which stands for kernel object.

==> ``sudo insmod My_Module.ko ``

### keeping track of the module output :

Our module is very simple it prints some words on the kernel log buffer.
to look if it is added to all kernel modules : ``lsmod`` : 
![image](https://github.com/oussemajelassi/Embedded_Linux/assets/100140668/e866421a-0755-4417-8684-fd844f324080)

or we can use : ``dmesg`` : 
![image](https://github.com/oussemajelassi/Embedded_Linux/assets/100140668/eb162001-4449-4e43-924d-ba14c91f3678)





