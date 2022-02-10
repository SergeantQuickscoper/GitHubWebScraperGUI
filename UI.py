import scraper
import tkinter 


root = tkinter.Tk()


def DisplayScrape():
    username = UsernameEntry.get()
    ProfilePictureEntry.delete(0, tkinter.END)
    finalURL = scraper.GitHubWebScraper.GetWebPageData(username)
    ProfilePictureEntry.insert(0, finalURL)

root.title("GitHub Web Scraper")
UsernameEntry = tkinter.Entry(root)
NameEntry = tkinter.Entry(root)
FollowersEntry = tkinter.Entry(root)
FollowingEntry = tkinter.Entry(root)
ProfilePictureEntry = tkinter.Entry(root)
ScrapeButton = tkinter.Button(root, text="Scrape!", command=DisplayScrape)



UsernameEntry.grid(column=2, row=1)
FollowingEntry.grid(column=1, row=3, pady = 25, padx = 25)
FollowersEntry.grid(column=3, row=3)
FollowersEntry.grid(column=3, row=3)
ScrapeButton.grid(column=2, row=4)
ProfilePictureEntry.grid(column=3, row=2, pady = 25, padx = 25)
NameEntry.grid(column=1, row=2)

UsernameEntry.insert(0, "GitHub User")
FollowersEntry.insert(0, "Followers")
FollowingEntry.insert(0, "Following")
ProfilePictureEntry.insert(0, "Profile Picture")
NameEntry.insert(0, "Profile Name")








root.mainloop()