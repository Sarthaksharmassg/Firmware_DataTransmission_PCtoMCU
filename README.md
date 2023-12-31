# Firmware_DataTransmission_PCtoMCU
This project focuses on the transmission of a given text on a set baud rate to a Arduino MCU and back to PC from the Arduino MCU all while measuring live transmission rate and ensuring atomicity and correctness of transmitted text.
a. Real time Transmission rate from the PC
b. Real time Transmission rate to the PC are both different from BAUD rate(bps) due to associated overheads.
The actual throughput maybe different from the said BAUD rate.

Text:
*“Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one.* 

*In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs," Rajan said in the note." Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently."*

### Details:

1. The above text consists of close to 1000 characters (including spaces). 
2. This data is to be sent from your PC to an MCU by UART (2400 baud rate). 
3. Upon receiving this data, the MCU stores it in the EEPROM memory as and when it is receiving data. Not all at once.
4. After the entire text data set has been transferred from the PC to the MCU, the MCU starts retrieving the stored data from EEPROM and sends it to the PC. 
5. On the PC side, the data being received is printed on the console screen of PC.
6. During any transmission of data to and from the PC, the console needs to print the live real-time data transmission speed in bits/second.
