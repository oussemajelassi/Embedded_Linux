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


