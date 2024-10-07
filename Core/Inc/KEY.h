#ifndef __KEY_H_
#define __KEY_H_

#include "stm32f1xx_hal.h"

uint8_t Key_Scan(GPIO_TypeDef *GPIOx,uint16_t GPIO_PIN);

#endif
