
import time 
import serial 

#import serial.tools.list_ports

text="""“Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one.* 

*In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs," Rajan said in the note." Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently." """
s=serial.Serial('COM4',baudrate=2400)
s.stopbits=serial.STOPBITS_ONE
s.parity=serial.PARITY_NONE
s.bytesize=serial.EIGHTBITS
#Data Trasmission
time.sleep(2)
for byte in text:
    t0=time.time()
    s.write(byte.encode('utf-8'))   # Python default- Unicode string format (16 bytes). Hence encode to UTF-8 byte wise is a requirement which oherwise results in a TypeError
    transmit_time=time.time()-t0
    if(transmit_time!=0):
        print(f"Trasmit rate {8.0/transmit_time}")
#print(text)
#print ("transmission time=")
#print(transmit_time)
#time.sleep(10)
#s.close()
i1=0
t=len(text)
while i1<=t:
    #t0=time.time()
    if(s.in_waiting>0):
        
        byte_read = s.read()
        received_time=time.time()-t0
        t0=time.time()
        if(received_time != 0):
            speed = (8.0/received_time)
            print(f"{speed} bps"),
        print(byte_read)
        #time.sleep(100)
        i1=i1+1
    #print(s.readline().decode('utf-8'))
s.close()