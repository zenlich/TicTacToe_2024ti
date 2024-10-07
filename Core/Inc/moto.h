#ifndef __MOTO_H_
#define __MOTO_H_

#include "stm32f1xx_hal.h"
#include "stdint.h"

extern int16_t x1,y1;

void moto_position(uint8_t pos);
void moto_position_zero(void);
void moto_get(void);
void moto_put(void);
void elec_out(void);
void led_out(void);
void update_G_data0(int x, int y);
void moto_qipan_pos(uint8_t x, uint8_t y);
void moto_get_ronato(int8_t jiaodu,uint8_t pos);


#endif
