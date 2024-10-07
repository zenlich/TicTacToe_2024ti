#ifndef __MAIXCAM_H_
#define __MAIXCAM_H_

#include "stm32f1xx_hal.h"

void Maixcam_Receive_Data(uint8_t data);
void Maixcam_Data(void);

extern int maixcam_data[7];
extern uint8_t qizi_x,qizi_y,qipan_x,qipan_y;

#endif
