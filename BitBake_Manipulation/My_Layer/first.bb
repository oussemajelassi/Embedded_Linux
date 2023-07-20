DESCRIPTION = "Prints Hello World"
PN = 'first'
PV = '1'
do_build[nostamp] = '1'
python do_build() {
   bb.plain("********************");
   bb.plain("*                  *");
   bb.plain("*  Hello, World!   *");
   bb.plain("*                  *");
   bb.plain("********************");
}
