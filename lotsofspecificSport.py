from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Sport, Base, SpecificSportItem, User

engine = create_engine('sqlite:///sportspecificSport.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# SpecificSport for Soccer
sport1 = Sport(user_id=1, name="Soccer")

session.add(sport1)
session.commit()

specificSportItem1 = SpecificSportItem(user_id=1, name="Shinguards", description="Pad worn to protect the shins when playing soccer, hockey, and other sports.", category="Soccer", sport=sport1)

session.add(specificSportItem1)
session.commit()

specificSportItem2 = SpecificSportItem(user_id=1, name="Jersey", description="Vest to represent the individual and the team.", category="Soccer", sport=sport1)


session.add(specificSportItem2)
session.commit()


# SpecificSport for Basketball
sport2 = Sport(user_id=1, name="Basketball")

session.add(sport2)
session.commit()


specificSportItem1 = SpecificSportItem(user_id=1, name="Basketball", description="The ball that only allow players to touch with hands.", category="Basketball", sport=sport2)

session.add(specificSportItem1)
session.commit()

specificSportItem2 = SpecificSportItem(user_id=1, name="Jersey", description="Vest to represent the individual and the team.", category="Basketball", sport=sport2)

session.add(specificSportItem2)
session.commit()

specificSportItem3 = SpecificSportItem(user_id=1, name="Basketball Hoop", description="Target for the basketball to earn points.", category="Basketball", sport=sport2)

session.add(specificSportItem3)
session.commit()


# SpecificSport for Baseball
sport3 = Sport(user_id=1, name="Baseball")

session.add(sport3)
session.commit()


specificSportItem1 = SpecificSportItem(user_id=1, name="Baseball Bat", description="Baseball can only use bat to hit the ball.", category="Baseball", sport=sport3)

session.add(specificSportItem1)
session.commit()

specificSportItem2 = SpecificSportItem(user_id=1, name="Jersey", description="Vest to represent the individual and the team.", category="Baseball", sport=sport3)

session.add(specificSportItem2)
session.commit()

specificSportItem3 = SpecificSportItem(user_id=1, name="Softball", description="Softballs are ideal for batting practice or casual games, and come equipped with a convenient mesh bag.", category="Baseball", sport=sport3)

session.add(specificSportItem3)
session.commit()



# SpecificSport for Frisbee
sport4 = Sport(user_id=1, name="Frisbee")

session.add(sport4)
session.commit()


specificSportItem1 = SpecificSportItem(user_id=1, name="Frisbee", description="Combining the non-stop movement and athletic endurance of soccer with the aerial passing skills of football, a game of ultimate is played by two teams with a flying disc on a field with end zones, similar to football.", category="Frisbee", sport=sport4)

session.add(specificSportItem1)
session.commit()



# SpecificSport for Snowboarding
sport5 = Sport(user_id=1, name="Snowboarding")

session.add(sport5)
session.commit()


specificSportItem1 = SpecificSportItem(user_id=1, name="Ski Jacket", description="To keep warm in the snow.", category="Snowboarding", sport=sport5)

session.add(specificSportItem1)
session.commit()

specificSportItem2 = SpecificSportItem(user_id=1, name="Board", description="Snowbard are light, short and flexible with twin tips. They are good for riders who want a lively ride anywhere on the mountain.", category="Snowboarding", sport=sport5)

session.add(specificSportItem2)
session.commit()



# SpecificSport for Rock climbing
sport6 = Sport(user_id=1, name="Rock Climbing")

session.add(sport6)
session.commit()


specificSportItem1 = SpecificSportItem(user_id=1, name="Rope", description="Designed for heavy use and year-round climbing, the burly Black Diamond 9.9mm Non-Dry rope boasts a thick diameter for heavy use on varied climbs.", category="Rock Climbing", sport=sport6)

session.add(specificSportItem1)
session.commit()

specificSportItem2 = SpecificSportItem(user_id=1, name="Harness", description="This Harness is surprisingly lightweight and breathable, while preserving the uncompromising security, comfort and durability for which Black Diamond is known.", category="Rock Climbing", sport=sport6)

session.add(specificSportItem2)
session.commit()



# SpecificSport for Foosball
sport7 = Sport(user_id=1, name="Foosball")

session.add(sport7)
session.commit()

specificSportItem1 = SpecificSportItem(user_id=1, name="Soccer Ball", description="High quality and durable mini table soccer balls, this set of balls is just what the foosball enthusiast needs.", category="Foosball", sport=sport7)

session.add(specificSportItem1)
session.commit()

specificSportItem2 = SpecificSportItem(user_id=1, name="Table", description="Player friendly table that is made for the professional player and available to the general public and perfect for youth programs.", category="Foosball", sport=sport7)

session.add(specificSportItem2)
session.commit()


# SpecificSport for Skating
sport8 = Sport(user_id=1, name="Skating")

session.add(sport8)
session.commit()


specificSportItem1 = SpecificSportItem(user_id=1, name="Ice Skates", description="Comfortably glide around the rink with the cushioned design. Engineered for casual performance that boasts a soft, padded interior, the SoftSkate 180s consistently keep you supported and maintain your stride.", category="Skating", sport=sport8)

session.add(specificSportItem1)
session.commit()

specificSportItem2 = SpecificSportItem(user_id=1, name="Blade Guards", description="Protect your skate blades. Convenient drain holes allow moisture to vent to prevent rusting. Constructed for flexible attachment to accommodate skates of all sizes.", category="Skating", sport=sport8)

session.add(specificSportItem2)
session.commit()


# SpecificSport for Hockey
sport9 = Sport(user_id=1, name="Hockey")

session.add(sport9)
session.commit()


specificSportItem1 = SpecificSportItem(user_id=1, name="Hockey Skates", description="Skates feature a responsive, lightweight quarter package to give you the balance and acceleration needed to make an impact in the rink.", category="Hockey", sport=sport9)

session.add(specificSportItem1)
session.commit()

specificSportItem2 = SpecificSportItem(user_id=1, name="Hockey Sticks", description="Ice Hockey Stick boasts an explosive, quick release without the need of heavily loading the puck.", category="Hockey", sport=sport9)

session.add(specificSportItem2)
session.commit()



print "added sports and specific sport items!"
