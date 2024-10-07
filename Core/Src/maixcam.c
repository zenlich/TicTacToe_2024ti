#include "stm32f1xx_hal.h"
#include "maixcam.h"
#include "moto.h"

int maixcam_data[7];
uint8_t qipan_x,qipan_y,qizi_x,qizi_y;
int i=0;

void Maixcam_Receive_Data(uint8_t data)
{
    static uint8_t state = 0;
    if(state == 0 && data == 0x2C)
    {
        state=1;
        maixcam_data[0]=data;
    }
    else if(state == 1 )
    {
        state=2;
        maixcam_data[1]=data;
    }
    else if(state == 2 )
    {
        state=3;
        maixcam_data[2]=data;
    }
    else if(state == 3 )
    {
        state=4;
        maixcam_data[3]=data;
    }
    else if(state == 4 )
    {
        state=5;
        maixcam_data[4]=data;
    }
    else if(state == 5)
    {
        if(data == 0x5B)        //包尾
        {
            state=0;
            maixcam_data[5]=data;
            Maixcam_Data();
        }
        else if (data != 0x5B)
        {
            state=0;
            for(i=0;i<6;i++)
            {
                maixcam_data[i]=0x00;
            }
        }
    }
    else
    {
        state=0;
        for(i=0;i<6;i++)
        {
            maixcam_data[i]=0x00;
        }
    }
}

void Maixcam_Data()
{
    qizi_x=maixcam_data[1];
    qizi_y=maixcam_data[2];
    qipan_x=maixcam_data[3];
    qipan_y=maixcam_data[4];
//        OLED_ShowSignedNum(1,1,qizi_x,3);
//    OLED_ShowSignedNum(1,6,qizi_y,3);
//            OLED_ShowSignedNum(2,1,qipan_x,3);
//    OLED_ShowSignedNum(2,6,qipan_y,3);
}
