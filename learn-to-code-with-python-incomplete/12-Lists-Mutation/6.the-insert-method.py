plays = ["Hamlet", "Macbeth", "King Lear"]

plays.insert(1, "Julius Caeser")
print(plays)

plays.insert(0,"Othello")
print(plays)

plays.insert(0,"Othello")
print(plays)

plays.insert(10,"Rome & Juliet") # will at add at the end as index 10 does not exist
print(plays)

plays.insert(-1,"Testament") # will at add at the end as index 10 does not exist
print(plays)

plays.insert(-1,"A Midsummer Night's Dream") # will at add at the end as index 10 does not exist
print(plays)

plays.insert(-1,"Blah1") # will at add at the end as index 10 does not exist
print(plays)

plays.insert(-1,"Blah2") # will at add at the end as index 10 does not exist
print(plays)

plays.insert(-1,"Blah3") # will at add at the end as index 10 does not exist
print(plays)

for index, value in enumerate(plays):
    print(f"The Index value is {index} and the value in the index is {value}")