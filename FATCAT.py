##!usr/bin/python3
#<|>Coded by DJebbarAnon
#<|>Information ghatring tool (fatcat)
# ▄████  ██     ▄▄▄▄▀ ▄█▄    ██     ▄▄▄▄▀ 
# █▀   ▀ █ █ ▀▀▀ █    █▀ ▀▄  █ █ ▀▀▀ █    
# █▀▀    █▄▄█    █    █   ▀  █▄▄█    █      
# █      █  █   █     █▄  ▄▀ █  █   █        /\_/\  
#  █        █  ▀      ▀███▀     █  ▀        ( 0.0 )
#   ▀      █                   █       		
#         ▀                   ▀   
#C0der: 	 DjebbarAnon						
#Fb...:   facebook.com/djebbar.bassem.16				
#Github:  https://github.com/DjebbarAnon
#Youtube:  https://www.youtube.com/channel/UC1iAl3FOqQsVUwdAJ4zk3Kg
#
#
#
#
#
#
#
#
#
__author__ = "DjebbarAnon (bassem)"
__email__  ="bassemdjebbar@gmail.com"
#Imports
import sys
import os
import time
import requests
import urllib.request
import platform
#colors
class colors:
	def __init__(self):
		self.end = '\033[0m' # end
		self.red = '\033[31m' # red
		self.green = '\033[32m' # green
		self.orange = '\033[33m' # orange
		self.blue = '\033[34m' # blue
		self.purple = '\033[35m' # purple
		self.white = "\x1b[97m" #end white		
color = colors()	
class slowprints():
	def slowprint( self , slow ) :
		for slow_print in slow + "\n" :
			sys.stdout.write(slow_print)
			sys.stdout.flush()
			time.sleep(3./90)
	def slowprint2( self , slow ) :
		for slow_print in slow + "\n" :
			sys.stdout.write(slow_print)
			sys.stdout.flush()
			time.sleep(4./500)
class clear_up_colora :
	def clear_cls(self):
		if platform.system() == ("Linux") :
			os.system("clear && clear")
		elif platform.system() == ("Windows") :
			os.system("cls && cls")
		else:
			pass
	def color_a(self):
		if platform.system() == ("Windows") :
			os.system("color a")
		else:
			pass
def internet_checker():
	print('\33[8;24;80t')
	clear_up_colora().clear_cls()
	clear_up_colora().color_a()
	try:
		import urllib.request
	except:
		pass
	try:
		urllib.request.urlopen("http://goolge.com")
		while True:
			slowprints().slowprint( color.white + "[*] Checking the internet connection ......" + color.end )
			time.sleep(2)
			slowprints().slowprint( color.green + "[+] Connected !!" + color.end )
			time.sleep(0.2)
			print( color.red + "\t \t    {#}DjebbarAnon{#}" + color.end )
			
			print( color.green + '''
 | |_________________________________
 | |////////////////                |
 | |////////////////                |
 | |////////////////                |
 | |/////////////a$$$$$e.           |
 | |////////////$$P/_ ,i`           |
 | |///////////$$$//\$$$>,          |
 | |///////////$$$///'\$            |    
 | |///////////\$$a/   `,           |
 | |/////////////"$$$$P"            |
 | |////////////////                |
 | |////////////////                |
 | |////////////////                |
 | |mt-2"""""""""""""""""""""""""""""
''' + color.end )
			time.sleep(2)
			slowprints().slowprint( "[*] Loading the script ......")
			time.sleep(2)
			slowprints().slowprint( "[+] The script is ready")
			break;
			os.system(" clear && clear ")
	except urllib.error.URLError as msg :
		slowprints().slowprint( color.white + " [*] Checking the internet connection ......" + color.end)
		time.sleep(2)
		print( color.orange + '''
\t \t   ____                   _  __
\t \t  / __/______  ________  (_)/_/
\t \t / _// __/ _ \/ __/ __/ _ / /  
\t \t/___/_/  \___/_/ /_/   (_) /   
\t \t                         |_|  
''' + color.end )			
		print(" ")
		slowprints().slowprint( color.red + " [!] Sorry there is no internet connection ! !" + color.end)
		print("\t")
		time.sleep(0.5)
		slowprints().slowprint( color.red + " [!] Checke your internet connection then run the script again" + color.end )
		print(" ")
		slowprints().slowprint( color.red + " [!] Exiting" + color.end )
		time.sleep(1)
		sys.exit(0)
		clear_up_colora().clear_cls()
		return		
def contu_ex():
	contunex = input( color.white + ">>[C]ontinue or [E]xit : " + color.end )
	if contunex == "c":
		banner()
		menu()
		main()
	elif contunex == "C":
		banner()
		menu()
		main()
	elif contunex == "continue":
		banner()
		menu()
		main()
	elif contunex == "Continue":
		banner()
		menu()
		main()
	else:
		clear_up_colora().clear_cls()
		print( color.white + "\t \t ]#############() BYEEEEEEEEEEE !! ()#############[" + color.end )
		print(" ")
		print(color.orange + "\t \t DjebbarAnon Was here " + color. end )
		print( color.red + '''	
			 	
\t      .... NO! ...                  ... MNO! ...
\t   ..... MNO!! ...................... MNNOO! ...
\t  ..... MMNO! ......................... MNNOO!! .
\t ..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
\t  ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
\t     ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
\t    ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
\t    ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
\t     ....... MMMMM..    OPPMMP    .,OMI! ....
\t      ...... MMMM::   o.,OPMP,.o   ::I!! ...
\t          .... NNM:::.,,OOPM!P,.::::!! ....
\t           .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
\t          ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
\t            .. MMMMMNNOOMMNNIIIPPPOO!! ......
\t           ...... MMMONNMMNNNIIIOO!..........
\t        ....... MN MOMMMNNNIIIIIO! OO ..........
\t     ......... MNO! IiiiiiiiiiiiI OOOO ...........
\t   ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
\t    .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
\t    ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
\t       ...... OO! ................. ON! .......
\t          ................................
''' + color.end )
		time.sleep(1)	
		slowprints().slowprint( color.red + "[!] Exiting" + color.end )
		time.sleep(5)
		clear_up_colora().clear_cls()
		sys.exit(0)	
def banner():
	print('\33[8;35;80t')
	clear_up_colora().clear_cls()
	clear_up_colora().color_a()
	logo =(''' \033[33m                   

\t \t ▄████  ██     ▄▄▄▄▀ ▄█▄    ██     ▄▄▄▄▀ 
\t \t █▀   ▀ █ █ ▀▀▀ █    █▀ ▀▄  █ █ ▀▀▀ █    
\t \t █▀▀    █▄▄█    █    █   ▀  █▄▄█    █      
\t \t █      █  █   █     █▄  ▄▀ █  █   █        /\_/\  
\t \t  █        █  ▀      ▀███▀     █  ▀        ( 0.0 )
\t \t   ▀      █                   █       		
\t \t         ▀                   ▀   \033[0m    
\033[32m--------------------------------------------------------------------------------\033[0m
	\033[31m C0der:\033[0m 	\033[32m DjebbarAnon\033[0m						
	\033[31m Fb...:\033[0m  \033[32m facebook.com/djebbar.bassem.16\033[0m							
	\033[31m Github:\033[0m \033[32m https://github.com/DjebbarAnon\033[0m
	\033[31m Youtube:\033[0m \033[32m https://www.youtube.com/channel/UC1iAl3FOqQsVUwdAJ4zk3Kg \033[0m
\033[32m--------------------------------------------------------------------------------\033[0m''')						
											
	print(logo)
def menu():
	print( color.red + " .::[1]::. ==========================>" + color.end , color.green + " |DNS Lookup|")
	print( color.red + " .::[2]::. ==========================>" + color.end , color.green + " |Whois Lookup|")
	print( color.red + " .::[3]::. ==========================>" + color.end , color.green + " |GeoIP Lookup|")
	print( color.red + " .::[4]::. ==========================>" + color.end , color.green + " |Subnet Lookup Online|")
	print( color.red + " .::[5]::. ==========================>" + color.end , color.green + " |Traceroute|")
	print( color.red + " .::[6]::. ==========================>" + color.end , color.green + " |Zone Transfe|")
	print( color.red + " .::[7]::. ==========================>" + color.end , color.green + " |HTTP Headers|")
	print( color.red + " .::[8]::. ==========================>" + color.end , color.green + " |Reverse IP|")
	print( color.red + " .::[9]::. ==========================>" + color.end , color.green + " |Page Links|")
	print( color.red + " .::[10]::. ==========================>" + color.end , color.green + "|Find Host Records|")
	print( color.red + " .::[11]::. ==========================>" + color.end , color.green + "|Tcp port scan|")
	print( color.red + " .::[12]::. ==========================>" + color.end , color.green + "|Reverse DNS|")
	print( color.red + " .::[13]::. ==========================>" + color.end , color.green + "|Find Shared DNS Servers|")
	print( color.red + " .::[14]::. ==========================>" + color.end , color.green + "|About me|")
	print( color.red + " .::[15]::. ==========================>" + color.end , color.green + "|Exit|")
	print("\033[32m-\033[0m"*80)
	print('''\t \t \t  \033[33mGreetz To\033[0m
		\033[31mOussama,Ishak,Rahim, Louey\033[0m''')
def main():
	try:
		your_choice = int(input( color.white + ">> Chose ~# : " + color.end ))
		if your_choice == 1 :

				clear_up_colora().clear_cls()
				clear_up_colora().color_a()
				print( color.purple + '''			
██▄      ▄      ▄▄▄▄▄   █    ████▄ ████▄ █  █▀  ▄   █ ▄▄ 
█  █      █    █     ▀▄ █    █   █ █   █ █▄█     █  █   █ 
█   █ ██   █ ▄  ▀▀▀▀▄   █    █   █ █   █ █▀▄  █   █ █▀▀▀  
█  █  █ █  █  ▀▄▄▄▄▀    ███▄ ▀████ ▀████ █  █ █   █ █     
███▀  █  █ █                ▀              █  █▄ ▄█  █    
      █   ██                              ▀    ▀▀▀    ▀   
''' + color.end)
				print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
				print(color.green + " \t \t \t EXAMPLE : " + color.end)
				print(color.green + " \t \t \t \t google.com" + color.end )
				print( color.red + "-"*80 + color.end )
				input_dnslookup = input( color.white + "[*] Enter you domain here : " + color.end )
				full_site ="http://api.hackertarget.com/dnslookup/?q=" + input_dnslookup
				openlink =requests.get (full_site)
				print( color.red + "-"*80 + color.end)
				print( color.green + openlink.text + color.end )
				print( color.red + "-"*80 + color.end)
				f1 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
				if f1 == "Y" :
					f = open("Dns_lookup.txt","w")
					print(f.write(openlink.text))
					f.close()
					print("\t")
					print( color.red + "-"*80 + color.end )
					print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
					print( color.red + "-"*80 + color.end )
					print("\t")
					contu_ex()	
							
				elif f1 == "y":
					f = open("Dns_lookup.txt","w")
					print(f.write(openlink.text))
					f.close()
					print("\t")
					print( color.red + "-"*80 + color.end )
					print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
					print( color.red + "-"*80 + color.end )
					print("\t")
					contu_ex()
				elif f1 == "Yes":
					f = open("Dns_lookup.txt","w")
					print(f.write(openlink.text))
					f.close()
					print("\t")
					print( color.red + "-"*80 + color.end )
					print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
					print( color.red + "-"*80 + color.end )
					print("\t")
					contu_ex()
				elif f1 == "yes":
					f = open("Dns_lookup.txt","w")
					print(f.write(openlink.text))
					f.close()
					print("\t")
					print( color.red + "-"*80 + color.end )
					print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
					print( color.red + "-"*80 + color.end )
					print("\t")
					contu_ex()
				else:
					print("\t")
					print( color.red + "-"*80 + color.end )
					print( color.red + "[!] Your output are not saved" + color.end )
					print( color.red + "-"*80 + color.end )
					print("\t")
					contu_ex()
		elif your_choice == 2:
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + '''		

  ▄ ▄    ▄  █ ████▄ ▄█    ▄▄▄▄▄   █    ████▄ ████▄ █  █▀  ▄   █ ▄▄  
 █   █  █   █ █   █ ██   █     ▀▄ █    █   █ █   █ █▄█     █  █   █ 
█ ▄   █ ██▀▀█ █   █ ██ ▄  ▀▀▀▀▄   █    █   █ █   █ █▀▄  █   █ █▀▀▀  
█  █  █ █   █ ▀████ ▐█  ▀▄▄▄▄▀    ███▄ ▀████ ▀████ █  █ █   █ █     
 █ █ █     █         ▐                ▀              █  █▄ ▄█  █    
  ▀ ▀     ▀                                         ▀    ▀▀▀    ▀ 
''' + color.end )
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t [Domain]google.com Or [ip] 216.58.212.164" + color.end )
			print( color.red + "-"*80 + color.end )
			input_whoislookip = input( color.white + "[*] Enter ip or domain for lookup : " + color.end )
			fullinputsite = ( "http://api.hackertarget.com/whois/?q=" + input_whoislookip )
			openlink1 = requests.get (fullinputsite)
			print( color.red + "-"*80 + color.end )
			print( color.green + openlink1.text + color.end )
			print( color.red + "-"*80 + color.end )
			f2 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f2 == "Y":
				f = open("WhoisLookiup.txt","w")
				print(f.write(openlink1.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f2 == "y":
				f = open("WhoisLookup.txt","w")
				print(f.write(openlink1.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f2 == "yes":
				f = open("WhoisLookup.txt","w")
				print(f.write(openlink1.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f2 == "Yes":
				f = open("WhoisLookup.txt","w")
				print(f.write(openlink1.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			else:
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 3 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + '''						
  ▄▀  ▄███▄   ████▄ ▄█ █ ▄▄  █    ████▄ ████▄ █  █▀  ▄   █ ▄▄  
▄▀    █▀   ▀  █   █ ██ █   █ █    █   █ █   █ █▄█     █  █   █ 
█ ▀▄  ██▄▄    █   █ ██ █▀▀▀  █    █   █ █   █ █▀▄  █   █ █▀▀▀  
█   █ █▄   ▄▀ ▀████ ▐█ █     ███▄ ▀████ ▀████ █  █ █   █ █     
 ███  ▀███▀          ▐  █        ▀              █  █▄ ▄█  █    
                         ▀                     ▀    ▀▀▀    ▀   
''' + color.end ) 
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t [ip] 216.58.212.164" + color.end )
			print( color.red + "-"*80 + color.end )										
			input_geoiplookup = input( color.white + "[*] Enter ip adress : "  + color.end )
			full_website = ( "http://api.hackertarget.com/geoip/?q=" + input_geoiplookup)
			open_full_website = requests.get(full_website)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_full_website.text + color.end)
			print( color.red + "-"*80 + color.end )
			f3 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end)
			if f3 == "Y":
				f = open("geoIpLookup","w")
				print(f.write(open_full_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f3 == "y":
				f = open("geoIpLookup","w")
				print(f.write(open_full_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				
				contu_ex()	
			elif f3 == "Yes":
				f = open("geoIpLookup","w")
				print(f.write(open_full_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f3 == "yes":
				f = open("geoIpLookup","w")
				print(f.write(open_full_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			else:
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 4 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + '''				
   ▄▄▄▄▄   ▄   ███      ▄   ▄███▄     ▄▄▄▄▀ █    ████▄ ████▄ █  █▀  ▄   █ ▄▄  
  █     ▀▄  █  █  █      █  █▀   ▀ ▀▀▀ █    █    █   █ █   █ █▄█     █  █   █ 
▄  ▀▀▀▀▄ █   █ █ ▀ ▄ ██   █ ██▄▄       █    █    █   █ █   █ █▀▄  █   █ █▀▀▀  
 ▀▄▄▄▄▀  █   █ █  ▄▀ █ █  █ █▄   ▄▀   █     ███▄ ▀████ ▀████ █  █ █   █ █     
         █▄ ▄█ ███   █  █ █ ▀███▀    ▀          ▀              █  █▄ ▄█  █    
          ▀▀▀        █   ██                                   ▀    ▀▀▀    ▀ 			
				
''' + color.end )
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t 192.168.1.32/27" + color.end )
			print( color.red + "-"*80 + color.end )
			input_subnetlookup = input( color.white + "[*] Enter cidr or ip with netmask : " + color.end )
			full_input_site = ("http://api.hackertarget.com/subnetcalc/?q=" + input_subnetlookup )
			open_full_input_site = requests.get (full_input_site)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_full_input_site.text + color.end )
			print( color.red + "-"*80 + color.end )
			f4 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f4 == "Y" :
				f = open("SubnetLookUp","w")
				print(f.write(open_full_input_site.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f4 == "y" :
				f = open("SubnetLookUp","w")
				print(f.write(open_full_input_site.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f4 == "Yes" :
				f = open("SubnetLookUp","w")
				print(f.write(open_full_input_site.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f4 == "yes" :
				f = open("SubnetLookUp","w")
				print(f.write(open_full_input_site.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			else:
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 5 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + '''		
   ▄▄▄▄▀ █▄▄▄▄ ██   ▄█▄    ▄███▄   █▄▄▄▄ ████▄   ▄     ▄▄▄▄▀ ▄███▄   
▀▀▀ █    █  ▄▀ █ █  █▀ ▀▄  █▀   ▀  █  ▄▀ █   █    █ ▀▀▀ █    █▀   ▀  
    █    █▀▀▌  █▄▄█ █   ▀  ██▄▄    █▀▀▌  █   █ █   █    █    ██▄▄    
   █     █  █  █  █ █▄  ▄▀ █▄   ▄▀ █  █  ▀████ █   █   █     █▄   ▄▀ 
  ▀        █      █ ▀███▀  ▀███▀     █         █▄ ▄█  ▀      ▀███▀   
          ▀      █                  ▀           ▀▀▀                  
                ▀                                                  
''' + color.end )
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t [Domain]google.com Or [ip] 216.58.212.164" + color.end )
			print( color.red + "-"*80 + color.end )
			input_traceroute = input( color.white + "[*] Enter ip or Domain : " + color.end )
			full_traceroute_website = ("http://api.hackertarget.com/mtr/?q=" + input_traceroute )
			open_full_traceroute_website = requests.get (full_traceroute_website)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_full_traceroute_website.text + color.end)
			print( color.red + "-"*80 + color.end )
			f5 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f5 == "Y" :
				f = open("Traceroute","w")
				print(f.write(open_full_traceroute_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f5 == "y" :
				f = open("Traceroute","w")
				print(f.write(open_full_traceroute_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f5 == "Yes" :
				f = open("Traceroute","w")
				print(f.write(open_full_traceroute_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f5 == "yes" :
				f = open("Traceroute","w")
				print(f.write(open_full_traceroute_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			else :
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 6 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + '''		
  ____                  ______                  ___       
 /_  / ___  ___  ___   /_  __/______ ____  ___ / _/__ ____
  / /_/ _ \/ _ \/ -_)   / / / __/ _ `/ _ \(_-</ _/ -_) __/
 /___/\___/_//_/\__/   /_/ /_/  \_,_/_//_/___/_/ \__/_/   
                                                                                                                                                                                                                                      				
''' + color.end )	
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t [Domain]google.com" + color.end )
			print( color.red + "-"*80 + color.end )
			input_zone_transfer = input( color.white + "[*] Enter Domain to test : " + color.end )
			zone_transfer_full_website = ("http://api.hackertarget.com/zonetransfer/?q=" + input_zone_transfer)
			open_zone_transfer_full_website = requests.get (zone_transfer_full_website)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_zone_transfer_full_website.text + color.end)
			print( color.red + "-"*80 + color.end )
			f5 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f5 == "Y" :
				f = open("Zone Transfer","w")
				print(f.write(open_zone_transfer_full_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f5 == "y" :
				f = open("Zone Transfer","w")
				print(f.write(open_zone_transfer_full_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f5 == "Yes" :
				f = open("Zone Transfer","w")
				print(f.write(open_zone_transfer_full_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f5 == "yes" :
				f = open("Zone Transfer","w")
				print(f.write(open_zone_transfer_full_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			else :
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 7 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + ''' 				
    __  ____  __           __  __               __         
   / / / / /_/ /_____     / / / /__  ____ _____/ /__  _____
  / /_/ / __/ __/ __ \   / /_/ / _ \/ __ `/ __  / _ \/ ___/
 / __  / /_/ /_/ /_/ /  / __  /  __/ /_/ / /_/ /  __/ /    
/_/ /_/\__/\__/ .___/  /_/ /_/\___/\__,_/\__,_/\___/_/     
             /_/                                                                                                          
''' + color.end )
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t www.example.com" + color.end )
			print( color.red + "-"*80 + color.end )
			input_http_header = input( color.white + "[*] Enter the web adress : " + color.end )
			full_input_http_header = ("http://api.hackertarget.com/httpheaders/?q=" + input_http_header)
			open_full_header_website = requests.get (full_input_http_header)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_full_header_website.text + color.end)
			print( color.red + "-"*80 + color.end )
			f6 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f6 == "Y" :
				f = open("Http Header","w")
				print(f.write(open_full_header_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f6 == "y" :
				f = open("Http Header","w")
				print(f.write(open_full_header_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f6 == "Yes" : 
				f = open("Http Header","w")
				print(f.write(open_full_header_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f6 == "yes" :
				f = open("Http Header","w")
				print(f.write(open_full_header_website.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			else : 
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 8 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + '''
,------.                                                ,--.        
|  .--. ' ,---.,--.  ,--.,---. ,--.--. ,---.  ,---.     |  | ,---.  
|  '--'.'| .-. :\  `'  /| .-. :|  .--'(  .-' | .-. :    |  || .-. | 
|  |\  \ \   --. \    / \   --.|  |   .-'  `)\   --.    |  || '-' ' 
`--' '--' `----'  `--'   `----'`--'   `----'  `----'    `--'|  |-'  
                                                            `--'  
''' + color.end )
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t 216.58.212.164 " + color.end )
			print( color.red + "-"*80 + color.end )
			input_reverse_ip = input( color.white + "[*] Enter ip adress : " + color.end )
			full_input_reverse_ip = "http://api.hackertarget.com/reverseiplookup/?q=" + input_reverse_ip
			open_full_reverse_ip = requests.get (full_input_reverse_ip)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_full_reverse_ip.text + color.end)
			print( color.red + "-"*80 + color.end )
			f7 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f7 == "Y" : 
				f = open("Reverse ip","w")
				print(f.write(open_full_reverse_ip.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f7 == "y" :
				f = open("Reverse ip","w")
				print(f.write(open_full_reverse_ip.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f7 == "Yes" :
				f = open("Reverse ip","w")
				print(f.write(open_full_reverse_ip.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f7 == "yes" : 
				f = open("Reverse ip","w")
				print(f.write(open_full_reverse_ip.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			else :
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 9 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + '''
,------.                           ,--.   ,--.        ,--.            
|  .--. ' ,--,--. ,---.  ,---.     |  |   `--',--,--, |  |,-.  ,---.  
|  '--' |' ,-.  || .-. || .-. :    |  |   ,--.|      \|     / (  .-'  
|  | --' \ '-'  |' '-' '\   --.    |  '--.|  ||  ||  ||  \  \ .-'  `) 
`--'      `--`--'.`-  /  `----'    `-----'`--'`--''--'`--'`--'`----'
''' + color.end )
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t www.example.com " + color.end )
			print( color.red + "-"*80 + color.end )
			input_page_links = input( color.white + "[*] Enter Web adress : " + color.end )
			full_input_page_links = "https://api.hackertarget.com/pagelinks/?q=" + input_page_links
			open_full_input_page_links = requests.get (full_input_page_links)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_full_input_page_links.text + color.end)
			print( color.red + "-"*80 + color.end )
			f8 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f8 == "Y" : 
				f = open("Page links","w")
				print(f.write(open_full_input_page_links.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f8 == "y" :
				f = open("Page links","w")
				print(f.write(open_full_input_page_links.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f8 == "Yes" : 
				f = open("Page links","w")
				print(f.write(open_full_input_page_links.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f8 == "yes" : 
				f = open("Page links","w")
				print(f.write(open_full_input_page_links.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			else :
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 10 : 
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + '''	
			
			
`.---        .    ,-   ,. -.    .-,--.                   .     
 |__ . ,-. ,-|   /    / |   \    `|__/ ,-. ,-. ,-. ,-. ,-| ,-. 
,|   | | | | |   |   /~~|-. |     | \  |-' |   | | |   | | `-. 
`'   ' ' ' `-'   \ ,'   `-' /   `-'  ` `-' `-' `-' '   `-' `-' 
                  `-      -'                                   
''' + color.end )
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t example.com " + color.end )
			print( color.red + "-"*80 + color.end )
			input_host_records = input( color.white + "[*] Enter Domain to searche : " + color.end )
			full_input_host_records = "http://api.hackertarget.com/hostsearch/?q=" + input_host_records
			open_full_input_host_records = requests.get (full_input_host_records)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_full_input_host_records.text + color.end)
			print( color.red + "-"*80 + color.end )
			f9 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f9 == "Y" : 
				f = open("Find Host Records","w")
				print(f.write(open_full_input_host_records.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f9 == "y" : 
				f = open("Find Host Records","w")
				print(f.write(open_full_input_host_records.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f9 == "Yes" :
				f = open("Find Host Records","w")
				print(f.write(open_full_input_host_records.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f9 == "yes" :
				f = open("Find Host Records","w")
				print(f.write(open_full_input_host_records.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			else : 
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 11 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + '''				
,--,--'        .-,--.         .    .---.             
`- | ,-. ,-.    '|__/ ,-. ,-. |-   \___  ,-. ,-. ,-. 
 , | |   | |    .|    | | |   |        \ |   ,-| | | 
 `-' `-' |-'    `'    `-' '   `'   `---' `-' `-^ ' ' 
         |                                           
         '                                           
''' + color.end )	
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t 216.58.212.164 " + color.end )
			print( color.red + "-"*80 + color.end )	
			input_tcp_port_scan = input( color.white + "[*] Enter Ip Adress : " + color.end )
			full_input_tcp_port_scan = "http://api.hackertarget.com/nmap/?q=" + input_tcp_port_scan
			open_full_input_tcp_port_scan = requests.get (full_input_tcp_port_scan)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_full_input_tcp_port_scan.text + color.end)
			print( color.red + "-"*80 + color.end )
			f10 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f10 == "Y" : 
				f = open("Tcp Port Scan","w")
				print(f.write(open_full_input_tcp_port_scan.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f10 == "y" :
				f = open("Tcp Port Scan","w")
				print(f.write(open_full_input_tcp_port_scan.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f10 == "Yes" :
				f = open("Tcp Port Scan","w")
				print(f.write(open_full_input_tcp_port_scan.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f10 == "yes" :
				f = open("Tcp Port Scan","w")
				print(f.write(open_full_input_tcp_port_scan.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			else : 
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 12 : 
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + ''' 		
.-,--.                            .-,--.          
 `|__/ ,-. .  , ,-. ,-. ,-. ,-.   ' |   \ ,-. ,-. 
  | \  |-' | /  |-' |   `-. |-'   , |   / | | `-. 
`-'  ` `-' `'   `-' '   `-' `-'   `-^--'  ' ' `-' 
''' + color.end )
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t 216.58.212.164 " + color.end )
			print( color.red + "-"*80 + color.end )	
			input_reverse_dns = input( color.white + "[*] Enter Ip Adress / Ip range / Domain Name : " + color.end )
			full_input_reverse_dns = "http://api.hackertarget.com/reversedns/?q=" + input_reverse_dns 
			open_full_input_reverse_dns = requests.get (full_input_reverse_dns)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_full_input_reverse_dns.text + color.end)
			print( color.red + "-"*80 + color.end )
			f11 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f11 == "Y" : 
				f = open("Reverse Dns","w")
				print(f.write(open_full_input_reverse_dns.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f11 == "y" : 
				f = open("Reverse Dns","w")
				print(f.write(open_full_input_reverse_dns.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f11 == "Yes" :
				f = open("Reverse Dns","w")
				print(f.write(open_full_input_reverse_dns.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f11 == "yes" :
				f = open("Reverse Dns","w")
				print(f.write(open_full_input_reverse_dns.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			else : 
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
		elif your_choice == 13 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.purple + '''		
  ___ _                    _ ___          ___                         
 / __| |_  __ _ _ _ ___ __| |   \ _ _  __/ __| ___ _ ___ _____ _ _ ___
 \__ \ ' \/ _` | '_/ -_) _` | |) | ' \(_-<__ \/ -_) '_\ V / -_) '_(_-<
 |___/_||_\__,_|_| \___\__,_|___/|_||_/__/___/\___|_|  \_/\___|_| /__/                                                                 			
''' + color.end )
			print("\033[31m---------------------------------\033[0m"+ color.white + "USEAGE"+"\033[31m-----------------------------------------\033[0m")
			print(color.green + " \t \t \t EXAMPLE : " + color.end)
			print(color.green + " \t \t \t \t ns1.dnsserver.com " + color.end )
			print( color.red + "-"*80 + color.end )	
			input_shared_dns_servers = input( color.white + "[*] Enter Host Name of DNS server : " + color.end )
			full_input_shared_dns_servers = "http://api.hackertarget.com/findshareddns/?q=" + input_shared_dns_servers
			open_full_input_shared_dns_servers = requests.get (full_input_shared_dns_servers)
			print( color.red + "-"*80 + color.end )
			print( color.green + open_full_input_shared_dns_servers.text + color.end)
			print( color.red + "-"*80 + color.end )
			f12 = input( color.white + "[*] Do you wanna save your output as txt file ? Y/n : " + color.end )
			if f12 == "Y" : 
				f = open("Shared Dns Servers","w")
				print(f.write(open_full_input_reverse_dns.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			elif f12 == "y" : 
				f = open("Shared Dns Servers","w")
				print(f.write(open_full_input_reverse_dns.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f12 == "Yes" : 
				f = open("Shared Dns Servers","w")
				print(f.write(open_full_input_reverse_dns.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()	
			elif f12 == "yes" :
				f = open("Shared Dns Servers","w")
				print(f.write(open_full_input_reverse_dns.text))
				f.close()
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.green + "[+] your output saved successfully on Fatcat folder !!" + color.end)
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
			else :
				print("\t")
				print( color.red + "-"*80 + color.end )
				print( color.red + "[!] Your output are not saved" + color.end )
				print( color.red + "-"*80 + color.end )
				print("\t")
				contu_ex()
				
		elif your_choice == 14 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			slowprints().slowprint2( color.orange + "[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]" + color.end )
			slowprints().slowprint2( "\t \t \t Author : DjebbarAnon" )
			slowprints().slowprint2( color.orange + "[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]" + color.end )
			slowprints().slowprint2("\t \t \t Github : https://github.com/DjebbarAnon")
			slowprints().slowprint2( color.orange + "[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]" + color.end )
			slowprints().slowprint2("\tYoutube : https://www.youtube.com/channel/UC1iAl3FOqQsVUwdAJ4zk3Kg")
			slowprints().slowprint2( color.orange + "[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]" + color.end )
			slowprints().slowprint2("\tFacebook : https://www.facebook.com/djebbar.bassem.16 " )
			slowprints().slowprint2( color.orange + "[+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]" + color.end )
			print( color.red + '''	
			 	
\t      .... NO! ...                  ... MNO! ...
\t   ..... MNO!! ...................... MNNOO! ...
\t  ..... MMNO! ......................... MNNOO!! .
\t ..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
\t  ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
\t     ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
\t    ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
\t    ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
\t     ....... MMMMM..    OPPMMP    .,OMI! ....
\t      ...... MMMM::   o.,OPMP,.o   ::I!! ...
\t          .... NNM:::.,,OOPM!P,.::::!! ....
\t           .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
\t          ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
\t            .. MMMMMNNOOMMNNIIIPPPOO!! ......
\t           ...... MMMONNMMNNNIIIOO!..........
\t        ....... MN MOMMMNNNIIIIIO! OO ..........
\t     ......... MNO! IiiiiiiiiiiiI OOOO ...........
\t   ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
\t    .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
\t    ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
\t       ...... OO! ................. ON! .......
\t          ................................
''' + color.end )
			contu_ex()
		elif your_choice == 15 :
			clear_up_colora().clear_cls()
			clear_up_colora().color_a()
			print( color.orange + '''	
			 	
\t      .... NO! ...                  ... MNO! ...
\t   ..... MNO!! ...................... MNNOO! ...
\t  ..... MMNO! ......................... MNNOO!! .
\t ..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
\t  ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
\t     ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
\t    ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
\t    ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
\t     ....... MMMMM..    OPPMMP    .,OMI! ....
\t      ...... MMMM::   o.,OPMP,.o   ::I!! ...
\t          .... NNM:::.,,OOPM!P,.::::!! ....
\t           .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
\t          ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
\t            .. MMMMMNNOOMMNNIIIPPPOO!! ......
\t           ...... MMMONNMMNNNIIIOO!..........
\t        ....... MN MOMMMNNNIIIIIO! OO ..........
\t     ......... MNO! IiiiiiiiiiiiI OOOO ...........
\t   ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
\t    .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
\t    ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
\t       ...... OO! ................. ON! .......
\t          ................................
''' + color.end )
			slowprints().slowprint( color.red + " [!] Exiting " + color.end)
			time.sleep(3)
		else:
			banner()
			menu()
			main()
	except (KeyboardInterrupt):
		sys.exit(0)
if __name__ == '__main__':
	internet_checker()
	banner()
	menu()
	main()
	
		
