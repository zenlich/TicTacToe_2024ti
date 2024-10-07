#include "moto.h"
#include "usart.h"
#include "string.h"
#include "stdio.h"
#include "stdlib.h"
#include "math.h"

uint8_t flag_get=1;
int16_t x1,y1;

unsigned char G_data;
#define G_DATA_SIZE 100
char G_data0[G_DATA_SIZE] = "G01 X0Y0Z0F15000\r\n";
unsigned char Get_data;

//unsigned char d1[]= "G01 X0Y0Z0F10000\r\n";
//unsigned char d2[]= "G01 X0Y0Z0F10000\r\n";
//unsigned char d3[]= "G01 X0Y0Z0F10000\r\n";
//unsigned char d4[]= "G01 X0Y0Z0F10000\r\n";
//unsigned char d5[]= "G01 X0Y0Z0F10000\r\n";
//unsigned char d6[]= "G01 X0Y0Z0F10000\r\n";
//unsigned char d7[]= "G01 X0Y0Z0F10000\r\n";
//unsigned char d8[]= "G01 X0Y0Z0F10000\r\n";
//unsigned char d9[]= "G01 X0Y0Z0F10000\r\n";
//unsigned char d11[]="G01 X0Y0Z0F10000\r\n" ;
//unsigned char d12[]="G01 X0Y0Z0F10000\r\n" ;
//unsigned char d13[]="G01 X0Y0Z0F10000\r\n" ;
//unsigned char d14[]="G01 X0Y0Z0F10000\r\n" ;
//unsigned char d15[]="G01 X0Y0Z0F10000\r\n" ;
//unsigned char d21[]="G01 X0Y0Z0F10000\r\n" ;
//unsigned char d22[]="G01 X0Y0Z0F10000\r\n" ;
//unsigned char d23[]="G01 X0Y0Z0F10000\r\n" ;
//unsigned char d24[]="G01 X0Y0Z0F10000\r\n" ;
//unsigned char d25[]="G01 X0Y0Z0F10000\r\n" ;

void moto_position(uint8_t pos)
{
    if(flag_get)
    {
    switch(pos)
    {
        
        case 1:SerialSendString("G01 X57Y90 F20000\r\n"); break;
        case 2:SerialSendString("G01 X89Y90 F20000\r\n"); break;
        case 3:SerialSendString("G01 X121Y90 F20000\r\n"); break;
        case 4:SerialSendString("G01 X57Y122 F20000\r\n"); break;
        case 5:SerialSendString("G01 X89Y122 F20000\r\n"); break;
        case 6:SerialSendString("G01 X121Y122 F20000\r\n"); break;
        case 7:SerialSendString("G01 X57Y154 F20000\r\n"); break;
        case 8:SerialSendString("G01 X89Y154 F20000\r\n"); break;
        case 9:SerialSendString("G01 X121Y154 F20000\r\n"); break;
        case 11:SerialSendString("G01 X27Y35 F20000\r\n"); break;
        case 12:SerialSendString("G01 X58Y35 F20000\r\n"); break;
        case 13:SerialSendString("G01 X89Y35 F20000\r\n"); break;
        case 14:SerialSendString("G01 X120Y35 F20000\r\n"); break;
        case 15:SerialSendString("G01 X151Y35 F20000\r\n"); break;
        case 21:SerialSendString("G01 X27Y208 F20000\r\n"); break;
        case 22:SerialSendString("G01 X58Y208 F20000\r\n"); break;
        case 23:SerialSendString("G01 X89Y208 F20000\r\n"); break;
        case 24:SerialSendString("G01 X120Y208 F20000\r\n"); break;
        case 25:SerialSendString("G01 X151Y208 F20000\r\n"); break;
     }
    }
    HAL_Delay(2000);
    flag_get=0;
    
}

void moto_qipan_pos(uint8_t x, uint8_t y)
{
    x1=(int)((x-94)*0.712+38);
    y1=(int)((y-89)*0.72+72);
    update_G_data0(x1, y1);
    SerialSendString(G_data0);
    HAL_Delay(2000);
//    OLED_ShowSignedNum(4,1,x1,3);
//    OLED_ShowSignedNum(4,6,y1,3);
}    

void moto_position_zero()
{
    SerialSendString("G01 X0Y0Z0 F15000\r\n");
}

void moto_get_ronato(int8_t jiaodu,uint8_t pos)
{
//    int16_t x0,y0;
//    double radian; // 使用 double 类型来存储弧度值
//    double x_prime, y_prime; // 临时变量，用于存储平移到原点后的坐标
//    double x_double, y_double; // 临时变量，用于存储旋转后的坐标
//    switch(pos)
//    { 
//        case 1:x0=57;y0=90; break;
//        case 2:x0=89;y0=90; break;
//        case 3:x0=121;y0=90; break;
//        case 4:x0=57;y0=122; break;
//        case 5:x0=89;y0=122; break;
//        case 6:x0=121;y0=122; break;
//        case 7:x0=57;y0=154; break;
//        case 8:x0=89;y0=154; break;
//        case 9:x0=121;y0=154; break;
//    }

//    radian = (double)jiaodu * 3.14 / 180.0; // 将角度转换为弧度
//    x_prime = x0 - 89.0; // 平移到原点
//    y_prime = y0 - 122.0; // 平移到原点
//    x_double = x_prime * cos(radian) - y_prime * sin(radian);
//    y_double = x_prime * sin(radian) + y_prime * cos(radian);
//    x1=(int)x_double+89;
//    y1=(int)y_double+122;
//    
//     OLED_ShowSignedNum(4,1,x1,3);
//     OLED_ShowSignedNum(4,6,y1,3);

}
    
void moto_get()
{
    SerialSendString("G01 Z7 F15000\r\n");
    elec_out();
    HAL_Delay(500);
    SerialSendString("G01 Z1 F15000\r\n");
    flag_get=1;
}

void moto_put()
{
    SerialSendString("G01 Z5 F15000\r\n");
    elec_out();
    HAL_Delay(500);
    SerialSendString("G01 Z1 F15000\r\n");
    flag_get=1;
    //led on
}    

void elec_out() // 0 off 1 on
{


        HAL_GPIO_TogglePin(GPIOB,GPIO_PIN_8);

}
    
void led_out() // 0 off 1 on
{

        HAL_GPIO_TogglePin(GPIOA,GPIO_PIN_8);
        HAL_Delay(2000);
        HAL_GPIO_TogglePin(GPIOA,GPIO_PIN_8); 
    
}    

void update_G_data0(int x, int y) {
    // 确保 x 和 y 的值在合理范围内
    if (x < -99999 || x > 99999 || y < -99999 || y > 99999) {
        printf("Error: X or Y value out of range.\n");
        return;
    }

    // 使用 snprintf 将新的 X 和 Y 值格式化到 G_data0 中
    snprintf(G_data0, G_DATA_SIZE, "G01 X%dY%dZ0F15000\r\n", x, y);
}
