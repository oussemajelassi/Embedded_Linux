#include <modbus.h>
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <sys/ioctl.h>
#include <linux/serial.h>
#include <inttypes.h>
#include <stdlib.h>
#include <asm/ioctls.h>

#define UART_PATH "/dev/ttyS0"

/*
 * Modbus slave (server):
 *
 * This is a sample program using libModbus to communicate over a rs232 uart
 * using the modbus protocol.
 */

//Simple function that grab temperature on my laptop and copy it to the mapping
//structure from libmodbus ( this code is for test purpose ).
void update_temps(modbus_mapping_t *mb_mapping)
{
	FILE *f1,*f2;
	uint32_t t1,t2;
	size_t s;

	//f1 = fopen("/sys/class/thermal/thermal_zone0/temp","r");
	//fscanf(f1,"%"PRIu32,&t1);
	t1 = 2000/1000;
	mb_mapping->tab_registers[0] =(uint16_t) t1;

	//f2 = fopen("/sys/class/thermal/thermal_zone1/temp","r");
	//fscanf(f2,"%"PRIu32,&t2);
	t2 = 3000/1000;
	mb_mapping->tab_registers[1] =(uint16_t) t2;

	//fclose(f1);
	//fclose(f2);
}

int main(int argc, char *argv[]){
	int ret,rc;
	uint8_t *request;//Will contain internal libmodubs data from a request that must be given back to answer
	modbus_t *ctx;
	modbus_mapping_t *mb_mapping;

	//Set uart configuration and store it into the modbus context structure
	ctx = modbus_new_rtu(UART_PATH, 115200, 'N', 8, 1);
	if (ctx == NULL) {
		perror("Unable to create the libmodbus context");
		return -1;
	}

	request= malloc(MODBUS_RTU_MAX_ADU_LENGTH);
	modbus_set_debug(ctx, TRUE);

	ret = modbus_set_slave(ctx, 1);//Set slave address
	if(ret < 0){
		perror("modbus_set_slave error");
		return -1;
	}

	//Works fine without it, I got a "Bad file descriptor" with it, likely
	//because my uart is RS232 only...
/*	ret = modbus_rtu_set_serial_mode(ctx, MODBUS_RTU_RS232);
	if(ret < 0){
		perror("modbus_rtu_set_serial_mode error\n");
		return -1;
	}
*/
	//Modbus is configured, now it must opens the UART (even if a connexion
	//does not make sense in the modbus protocol.
	ret = modbus_connect(ctx);
	if(ret < 0){
		perror("modbus_connect error");
		return -1;
	}

	//Init the modbus mapping structure, will contain the data
	//that will be read/write by a client.
	mb_mapping = modbus_mapping_new(MODBUS_MAX_READ_BITS, 0,
					MODBUS_MAX_READ_REGISTERS, 0);
	if(mb_mapping == NULL){
		perror("Cannot allocate mb_mapping");
		return -1;
	}

	for(;;){
		do {
			rc = modbus_receive(ctx, request);
		} while (rc == 0);
		if(rc < 0){
			perror("Error in modbus receive");
		//	return -1;
		}
		printf("Request received rc= %d\n",rc);
		update_temps(mb_mapping);
		ret = modbus_reply(ctx,request,rc,mb_mapping);//rc, request size must be given back to modbus_reply as well as "request" data
		if(ret < 0){
			perror("modbus reply error");
			return -1;
		}
	}

	//Clean up everything:
	modbus_mapping_free(mb_mapping);
	modbus_close(ctx);
	modbus_free(ctx);

	return 0;
}
