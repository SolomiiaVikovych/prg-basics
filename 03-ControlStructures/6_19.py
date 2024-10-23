print("SURVEY")
interested_in_cs = input("Are you interested in computer science? (y/n): ")
likes_games = input("Do you like playing computer games? (y/n): ")
has_instagram = input("Do you have an Instagram account? (y/n): ")
interested_in_cs = True if interested_in_cs.lower() == 'y' else False
likes_games = True if likes_games.lower() == 'n' else False
has_instagram = True if has_instagram.lower() == 'y' else False
print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if interested_in_cs else 'No'}")
print(f"Playing computer games: {'Yes' if likes_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if has_instagram else 'No'}")
