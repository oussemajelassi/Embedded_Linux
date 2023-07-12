#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

static int __init My_Module_init (void)
{
  printk (" module has been loaded \n") ;
  return 0 ;
}


static void __exit My_Module_exit(void)
 {
  /* code */
  printk (" module has been unloaded \n") ;
}

module_init(My_Module_init);
module_exit(My_Module_exit);

MODULE_LICENSE("GPL");
