#include<reg51.h>
#include"lcd12864.h"

unsigned char code CharCode[]="��ӭ����о�ӵ���xhmcu.taobao.com��������5V���ֿ�ף�׹�����죡";
							  
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
			if(i==16)  //��һ����д������
			{
				LCD12864_SetWindow(1,0);
			}

			if(i==32)  //��������д������
			{
				LCD12864_SetWindow(2,0);
			}
			if(i==48)  //��������д������
			{
				LCD12864_SetWindow(3,0);
			}
			
		}
		while(1);	
	}	
}
