indtroducing of wifi hacking



tool

macchanger


hor to change adaptor form managed mode to monitor mode
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
┌──(root㉿kali)-[/home/kali]
└─# ifconfig wlan0 down
                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# iwconfig mode monitor wlan0
iwconfig: unknown command "monitor"
                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# iwconfig wlan0 mode monitor      
                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# ifconfig wlan0 up          
                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# iwconfig                   
lo        no wireless extensions.

eth0      no wireless extensions.

wlan0     IEEE 802.11  Mode:Monitor  Frequency:2.412 GHz  Tx-Power=20 dBm   
          Retry short limit:7   RTS thr=2347 B   Fragment thr:off
          Power Management:off
          
                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# ifconfig wlan0 down
                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# iwconfig wlan0 mode managed   
                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# ifconfig wlan0 up          
                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# iwconfig                   
lo        no wireless extensions.

eth0      no wireless extensions.

wlan0     IEEE 802.11  ESSID:off/any  
          Mode:Managed  Access Point: Not-Associated   Tx-Power=20 dBm   
          Retry short limit:7   RTS thr=2347 B   Fragment thr:off
          Encryption key:off
          Power Management:off
          
                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# airmon-ng check kill

Killing these processes:

    PID Name
    846 wpa_supplicant

                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# airmon-ng start wlan0


PHY     Interface       Driver          Chipset

phy0    wlan0           rtl8xxxu        Realtek Semiconductor Corp. RTL8188FTV 802.11b/g/n 1T1R 2.4G WLAN Adapter
                (mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon)
                (mac80211 station mode vif disabled for [phy0]wlan0)

                                                                                                                                                                                                                                            
┌──(root㉿kali)-[/home/kali]
└─# 


sniffing
