cmd_/home/flooki/Desktop/Embedded_Linux/Kernel_Modules/Module.symvers := sed 's/\.ko$$/\.o/' /home/flooki/Desktop/Embedded_Linux/Kernel_Modules/modules.order | scripts/mod/modpost -m -a  -o /home/flooki/Desktop/Embedded_Linux/Kernel_Modules/Module.symvers -e -i Module.symvers   -T -
