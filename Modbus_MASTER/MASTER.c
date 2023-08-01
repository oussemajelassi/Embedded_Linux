#include <stdio.h>
#include <unistd.h>
#include <modbus.h>
#include <string.h>
#include <errno.h>
#include <sys/ioctl.h>
#include <linux/serial.h>
#include <asm/ioctls.h>

#define NB_REGS 2
#define UART_PATH "/dev/ttyUSB0"


int main()
{
    int ret;
    modbus_t *ctx;
    uint16_t dest [NB_REGS];

    struct timeval response_timeout;
    response_timeout.tv_sec = 10;
    response_timeout.tv_usec = 0;

    ctx = modbus_new_rtu(UART_PATH, 115200, 'N', 8, 1);
    if (ctx == NULL) {
        perror("Unable to create the libmodbus context\n");
        return -1;
    }

    modbus_set_response_timeout(ctx, &response_timeout);

    ret = modbus_set_slave(ctx, 1);
    if(ret < 0){
        perror("modbus_set_slave error\n");
        return -1;
    }

/*	ret = modbus_rtu_set_serial_mode(ctx, MODBUS_RTU_RS232);
    if(ret < 0){
        perror("modbus_rtu_set_serial_mode error\n");
        return;
    }
*/
    ret = modbus_connect(ctx);
    if(ret < 0){
        perror("modbus_connect error\n");
        return -1;
    }

    for(;;){
        // Read 2 registers from adress 0, copy data to dest.
        ret = modbus_read_registers(ctx, 0, NB_REGS, dest);
        if(ret < 0){
            perror("modbus_read_regs error\n");
            return -1;
        }

        printf("Temp0 on pc = %d\n",dest[0]);
        printf("Temp1 on pc = %d\n",dest[1]);

        sleep(1);
    }

    modbus_close(ctx);
    modbus_free(ctx);

}
