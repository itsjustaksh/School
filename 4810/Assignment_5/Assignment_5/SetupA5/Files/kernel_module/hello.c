#include <linux/module.h>
#include <linux/kernel.h>

int initialization(void)
{
    printk(KERN_INFO "Hello Aksh Ravi!\n");
    return 0;
}

void cleanup(void)
{
    printk(KERN_INFO "Bye-bye Aksh Ravi! Sayonara!\n");
}

module_init(initialization);
module_exit(cleanup);

MODULE_LICENSE("GPL");
