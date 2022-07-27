# Telegram bot to take miners list 
`from website moonarch.app/miners`


#####parser.py file is used for parsing data

For getting data from the website have used the `Selenium` library because all website is loaded using js functions. 
`Selenium` use a browser for opening the tab. As a browser use **Mozilla Firefox**. To parse data was used the `bs4` library.

#####miners_bot.py file user to start Telegram bot

For do not compromise auth token program use `python-dotenv` library. With created file named **variables** formated as bollow.

    TOKEN=12...ADE

