# AlphaBot2.Pizero
playing AlphaBot2.Pizero
### Here is the setup site: https://www.waveshare.com/wiki/AlphaBot2-PiZero#Motor_testing

## Follow the steps given but
there are some files you need to make some changes manually.

like the print 'blablablabla'

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/7a02738a-1f9c-4865-afd0-567436194034)


change into print('blablabla')

just a smell thing to change

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/9545566c-c1f0-4206-a9a1-d081b283b788)


# ways for you to EZ chnage some code

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/6f70ea4f-accf-4550-8446-9093ea174fbe)
![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/e2224fd6-ed37-4af1-a603-92b343b18ddd)

  first you need to connect to your pi first( remember what name, user_name and password you have given your pi). it works just like a file explorer.

**![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/782dd238-d136-4196-961a-0deee3697fa9)

change some code in visual studio and used WinSCP to deliver the CHANGE CODE.

da
## if you have python2 and python3 in your pi
make sure you use the right command

  python2

    example: python2 fileName.py

  pip2

    example: pip3 install something

  python3

    example: python3 fileName.py

  pip3

    example: pip3 install something

## Actual only until the Infrared line tracking code works
my servo motor, camera and bluetooth may have broken already.

## best don't used python2
i have tried using pip2 to install all the libraries

    sudo pip2 install spidev
  
these libraries show some error

 ![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/19b75b31-8b14-4609-81ef-cac21656f2b9)

 
## import socketserver (FOR python 3 only)
for python3 users the socketserver MUST BE WRITTEN in small letter 

Before

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/844d68d7-4026-4e08-b945-32d363376472)

After

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/8719e38a-1059-46f7-a5d1-3b2350c609c5)




Before

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/98b9dc5e-a855-4718-9972-f49bde764721)

After

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/d1bf91d3-924f-4ecd-8f89-deb46ff5e378)


## error needs to be done 
Step 1

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/0bd8647a-f63a-4441-9b31-aff59e8cce51)

Step 2

delete the space 

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/706362cf-b1d6-418d-b494-e575f8d462f9)

Step 3

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/5790baa4-1480-45f6-815d-dfb8e93e89f2)

Step 4

replace the space again

problem solve (find where the red line repeat the all the step)

![image](https://github.com/jingxianthong/AlphaBot2.Pizero/assets/77329585/36f56c82-d3f9-46ec-ba48-89a6c4a750b3)
