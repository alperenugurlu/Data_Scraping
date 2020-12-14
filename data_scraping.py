import requests

from bs4 import BeautifulSoup


print('''▌│█║▌║▌║ 𝐀𝐥𝐩𝐞𝐫𝐞𝐧 𝐓. 𝐔𝐠𝐮𝐫𝐥𝐮 ║▌║▌║█│▌
      
      
      ♞▀▄▀▄♝▀▄▀▄
      
      
▌│█║▌║▌║ 𝐀𝐥𝐩𝐞𝐫𝐞𝐧 𝐓. 𝐔𝐠𝐮𝐫𝐥𝐮 ║▌║▌║█│▌''')



#Type in the address of the website you want to engrave data on.

shell_url = 'https://github.com/payloadbox/xss-payload-list'

r = requests.get(shell_url)
soup = BeautifulSoup(r.content, 'html.parser')

#Click the right mouse button on the interface of the website to examine or check the item,
#find the titles related to the section you want to engrave ('div' - 'class') and write to this section. the example is as follows.
#example --> soup.find('details',{'class': 'xss-cheat-sheet-container-eventhandlers'})    
 
results =soup.find('pre')

#('details',{'class': 'xss-cheat-sheet-container-eventhandlers'})

print(results.get_text('\nI \n'))



