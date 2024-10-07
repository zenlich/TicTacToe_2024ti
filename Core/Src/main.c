/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2024 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "maixcam.h"
#include "oled.h"
#include "moto.h"

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

    uint8_t maixcam_rcvd;

    uint8_t mode1,mode2,mode;
    uint8_t pos=0;
    
    int num,flag=0;
    
    int begin;
    
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */
  OLED_Init();
  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_TIM2_Init();
  MX_USART1_UART_Init();
  MX_TIM3_Init();
  MX_UART5_Init();
  MX_USART2_UART_Init();
  MX_USART3_UART_Init();
  /* USER CODE BEGIN 2 */
    HAL_UART_Receive_IT(&huart1, &maixcam_rcvd,1);
    SerialSendString("$x\r\n");
    SerialSendString("G92 X0Y0Z0\r\n"); // jiaozhun
//    SerialSendString("G01 X57Y90 F20000\r\n");
//    moto_qipan_pos(163,201);
    
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {

      if(mode == 1)
      {
          if(begin){
          moto_qipan_pos(qizi_x,qizi_y);
          moto_get();
          
          moto_qipan_pos(qipan_x,qipan_y);
          moto_put();

//          HAL_Delay(3000);
          moto_position_zero();
          led_out();
          begin=0;
          }
      }
      while(mode == 2)
      {
        if(begin)
        {
          if(flag==0)
          {
              if(num == 0)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 1)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 2)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();
                  //elec m on
                  flag=1;
              }
              else if (num == 3)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
          }
          else
          {
              if(begin)
              {
                moto_qipan_pos(qipan_x,qipan_y);
                moto_put();
                
                  //led on
                moto_position_zero();
                led_out();
                num++;
                flag=0;
                begin=0;
              }
          }
        }
      }
      while(mode == 3)
      {
        if(begin)
        {
          if(flag == 0)
          {
              if(num == 0)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 1)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 2)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();
                  //elec m on
                  flag=1;
              }
              else if (num == 3)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
          }
          else
          {
                
                moto_qipan_pos(qipan_x,qipan_y);
                moto_put();
                
                  //led on
                moto_position_zero();
                led_out();
                num++;
                flag=0;
                begin=0;
              
          }
        }
      }
      while(mode == 4)
      {
          if(begin)
          {
          if(flag == 0)
          {
              if(num == 0)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 1)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 2)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();
                  //elec m on
                  flag=1;
              }
              else if (num == 3)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 4)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 5)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
          }
          else
          {
                moto_qipan_pos(qipan_x,qipan_y);
                moto_put();
                
                  //led on
                moto_position_zero();
                led_out();
                num++;
                flag=0;
                begin=0;
          }
          }
          
      }
      while(mode==5)
          {
          if(begin)
          {
          if(flag == 0)
          {
              if(num == 0)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 1)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 2)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();
                  //elec m on
                  flag=1;
              }
              else if (num == 3)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 4)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
              else if (num == 5)
              {
                  moto_qipan_pos(qizi_x,qizi_y);
                  moto_get();

                  flag=1;
              }
          }
          else
          {
                moto_qipan_pos(qipan_x,qipan_y);
                moto_put();
                
                  //led on
                moto_position_zero();
                led_out();
                num++;
                flag=0;
                begin=0;
          }
          }
          
      }
    
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV1;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL9;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/* USER CODE BEGIN 4 */
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
    if(GPIO_Pin == GPIO_PIN_0)
    {
       HAL_TIM_Base_Start_IT(&htim3);
    }
    if(GPIO_Pin == GPIO_PIN_8)
    {
        HAL_TIM_Base_Start_IT(&htim3);
    }
       
    if(GPIO_Pin == GPIO_PIN_9)
    {
        HAL_TIM_Base_Start_IT(&htim3);
    }
}

void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    int8_t temp1;
    if (huart == &huart1)
		{
            temp1=maixcam_rcvd;
            Maixcam_Receive_Data(temp1);
			HAL_UART_Receive_IT(&huart1, &maixcam_rcvd, 1);
		}
}

void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
  if(htim==(&htim3))
  {
       HAL_TIM_Base_Stop_IT(&htim3);
      
       if(HAL_GPIO_ReadPin(GPIOA,GPIO_PIN_0)==1)
       {
           pos+=1;
           if(pos>10)
           {
            pos=0;
           }
           OLED_ShowNum(2,1,pos,3);
       }
       if(HAL_GPIO_ReadPin(GPIOC,GPIO_PIN_8)==0)
       {
            begin=1;
            OLED_ShowNum(3,1,begin,3);
       }
       if(HAL_GPIO_ReadPin(GPIOC,GPIO_PIN_9)==0)
       {
            mode++;
           num=0;
    OLED_ShowSignedNum(1,1,mode,3);
       }

  }
        
}

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
