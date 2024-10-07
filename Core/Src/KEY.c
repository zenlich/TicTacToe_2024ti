#include "KEY.h"

uint8_t Key_Scan(GPIO_TypeDef *GPIOx,uint16_t GPIO_PIN)
{
    if (HAL_GPIO_ReadPin(GPIOx,GPIO_PIN) == 1)
    {
        
        return 1;
    }
    else
    {
        return 0;
    }   
}
