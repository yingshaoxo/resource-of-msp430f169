#include<reg51.h>
#include"lcd12864.h"

unsigned char code CharCode[]="欢迎光临芯河电子xhmcu.taobao.com蓝屏白字5V带字库祝亲购物愉快！";
							  
void main()
{
	unsigned char i;

	LCD12864_Init();
	while(1)
	{
		LCD12864_SetWindow(0, 0);
		while(CharCode[i]!='\0')
		{
			LCD12864_WriteData(CharCode[i]);
			i++;
			if(i==16)  //第一行满写第三行
			{
				LCD12864_SetWindow(1,0);
			}

			if(i==32)  //第三行满写第四行
			{
				LCD12864_SetWindow(2,0);
			}
			if(i==48)  //第三行满写第四行
			{
				LCD12864_SetWindow(3,0);
			}
			
		}
		while(1);	
	}	
}
