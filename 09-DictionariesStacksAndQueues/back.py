import queue

# Create a stack for visited websites
visited_websites = queue.LifoQueue()

# Some previously visited websites
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True:
    website = input('Enter website name (0 for back): ')

    if website == '0':  # Going back to the last visited website
        if visited_websites.empty():
            print("No more previously visited websites to go back to.")
            break
        else:
            print('<-- Going back to a previously visited website')
            website = visited_websites.get()
    elif website != "":  # Visiting a new website
        visited_websites.put(website)

    # Print the name of the website you are currently viewing
    print('You are currently viewing:', website)
    print()

