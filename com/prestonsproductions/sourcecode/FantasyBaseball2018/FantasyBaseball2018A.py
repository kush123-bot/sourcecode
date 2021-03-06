# TEAM NAME:
# TEAM NUMBER:
# PARTICIPANT NAMES:

# SOURCE CODE
# 2018 - Fantasy Baseball - Team Builder
# DIVISION B/C

''' INSTRUCTIONS

SCENARIO: Fantasy Baseball - Team Builder
DESCRIPTION: Online fantasy sports applications are an example of using massive data sets to calculate statistics 
and map trends. Behind these platforms is code that processes millions of statistics and run numerous algorithms. 
This test will have you build small pieces of a fantasy sports platform. We will use Major League Baseball as the model
because baseball contains a large number of statistics...and it is the author's favorite. :) 

You will use batting data from the 2016 MLB season (Minimum 20 at-bats). Your code/functions will be tested/graded against batting data
from the 2017 MLB season.
https://www.baseball-reference.com/leagues/MLB/2016-standard-batting.shtml
https://www.baseball-reference.com/leagues/MLB/2017-standard-batting.shtml

1. TASK: For each question, write your code to solve each objective. (return the answer programmatically. ie. via variables)
2. TOTAL POINTS: 114
3. WINNER: High Score
4. TIE BREAKER: Question 19. If there is still a tie, question 18, 17 and so on will break the tie.

TIPS: 
* Some questions may ask you to call functions from previous questions.
* The main function (at bottom) will call and run all of the questions and print the answers. Do not modify this function.
* Programs that do not run/compile will not be eligible to receive full points as determined by the Source Code rules.
* Run your program often to test and check for errors.

INFORMATION: The majority of questions will use a list of dictionaries (batting_data). Each item in the list will represent one player. The dictionary
will contain specific data for each player. View the template below:

[
    {
        'NAME':'Mike Trout',     # Name of Player (String)
        'AGE':25,                # Age of Player (Number)
        'TEAM':'LAA',            # Player's Team (String)
        'POSITION':'CF',         # Primary Fielding Position (String)
        'ATBATS':402,            # Total At Bats (Number)
        'RUNS':92,               # Total Runs Scored (Number)
        'HITS':123,              # Total Hits (Number)
        'DOUBLES':25,            # Number of Hits that were Doubles (2 Bases) (Number)
        'TRIPLES':3,             # Number of Hits that were Triples (3 Bases) (Number)
        'HOMERUNS':33,           # Number of Hits that were Homers (4 bases) (Number)
        'RBI':72,                # Total Runs Batted In (Number)
        'WALKS':94,              # Total Walks (Number)
        'STRIKEOUTS':90,         # Total Strikeouts (Number)
    },
    ...
]

GOOD LUCK! '''

# QUESTION 0: TEAM NAME
# OBJECTIVE A (2): Build a string with the name of your fantasy team. 
# Include your school name followed by any text you like. Append the 
# parameter date to the end of your string. Return the name.
# ex return string) Bath High School Super Squad 01/01/2018
def getTeamName(date):
    
    return 'Bath High School Super Squad '+date

# QUESTION 1: BASE HIT
# OBJECTIVE A (2): A base hit (or single) is when a player reaches first base, 
# but does not advance for that play. Our data set contains total hits,
# doubles (2B), Triples (3B, and Homeruns, but not singles. Determine how many of the total
# hits were singles. ie. total - 2B - 3B - HR
def getTotalSingles(totalhits, doubles, triples, homeruns):
    
    return totalhits - doubles - triples - homeruns

# QUESTION 2: BATTING AVERAGE
# OBJECTIVE A (2): Batting Average is found by dividing the number
# of Hits by the number of at-bats. The at-bats and hits are parameters
# to the function below (Numbers). Return the average.
# OBJECTIVE B (3): Round the average to 3 decimal places (use round() function)
# and remove the leading 0. Example format: .277
def getBattingAverage(hits, atbats):
    avg = hits / atbats
    
    return str(round(avg, 3))[1:]

# QUESTION 3: PLAYERS NAME
# OBJECTIVE A (2): A players name will be passed in as the parameter name.
# The players first and last name will be separated by one space ' '. Split
# the first and last name and return the values in a list. ex) [firstname, lastname]
# OBJECTIVE B (3): The first and last name may not be capitalized. Make sure the
# first character or the players first and last name is capitalized. 
def getFirstLastName(name):
    sname = name.split(' ')
    first = sname[0][0].upper()+sname[0][1:]
    last = sname[1][0].upper()+sname[1][1:]
    return [first, last]

# QUESTION 4: FANTASY POINTS 
# OBJECTIVE A (3): In fantasy sports, specific statistics are worth a 
# designated number of points. The best way for us to model this is by
# creating a dictionary. Each key will be the statistic name, and the 
# value will be how many points they are worth. Build and return the dictionary
# with the following key, value pairs. NOTE, the values will all be numbers. Make
# sure the key names match exactly as defined here.
# SINGLES:1, DOUBLES:2, TRIPLES:3, HOMERUNS:4, RUNS:2, RBI:2, WALKS:1, STRIKEOUTS:-1
def getPointSystem():
    points = {
        'SINGLES':1,
        'DOUBLES':2,
        'TRIPLES':3,
        'HOMERUNS':4,
        'RUNS':2,
        'RBI':2,
        'WALKS':1,
        'STRIKEOUTS':-1,
        }
    return points

# QUESTION 5: AVERAGE PLAYER AGE
# OBJECTIVE A (4): As described in the instructions, the parameter batting_data
# is a list of dictionaries holding players data. (See instructions for specifics. Data comes
# from the main method at the bottom of the file.) To start with this data, find the average
# age of all the players. Return the value. Do not round.
def getAverageAge(batting_data):
    ages = 0
    for p in batting_data:
        ages += p['AGE']
    return ages / len(batting_data)

# QUESTION 6: POSITION COUNTER
# OBJECTIVE A (4): The function below has parameter of batting_data (List) and a fielding
# position (String) (ie 'CF','1B', etc). Find and return how many players fielding position
# is the value in parameter, position.
# OBJECTIVE B (2): If the position 'DH' (which is not a fielding) position is passed as a position, return -1.
def getPositionCount(batting_data, position):
    if (position == 'DH'): return -1
    count = 0
    for p in batting_data:
        if (p['POSITION'] == position):
            count += 1
    return count

# QUESTION 7: GENERIC HIGHEST STAT FINDER
# OBJECTIVE A (5): Using a similar concept of making generic functions as question 6, 
# find the player with the highest/most of the statistic as specified by the parameter
# stat (ie. 'RUNS', 'HITS'). stat will be one of the attributes from a player dictionary
# in batting_data. 
# Return the NAME or names of the player(s) in a list with the highest of the stat.
def getMostStat(batting_data, stat):
    count = 0
    players = []
    for p in batting_data:
        if (p[stat] == count):
            players.append(p['NAME'])
        elif (p[stat] > count):
            count = p[stat]
            players = []
            players.append(p['NAME'])
    return players

# QUESTION 8: FILTER PLAYERS
# OBJECTIVE A (5): The function below has one parameter, which is the batting data.
# Search the list and find all players that have 100 or more RBI. Return the player
# NAMEs in a list.
# OBJECTIVE B (2): Sort the list by first name.
def getPlayers(batting_data):
    players = []
    for p in batting_data:
        if p['RBI'] >= 100:
            players.append(p['NAME'])
    players.sort()
    return players

# QUESTION 9: DOUBLE RANGE
# OBJECTIVE A (5): Find the lowest amount of doubles and highest amount of doubles
# in the batting_data from only players who have 400 ATBATS or more. Return the
# values in a list [lowest doubles, highest doubles]
def getDoubleRange(batting_data):
    doubles = [-1,-1];
    for p in batting_data:
        if p['ATBATS'] >= 400:
            if doubles[0] == -1:
                doubles[0] = p['DOUBLES']
                doubles[1] = p['DOUBLES']
            if p['DOUBLES'] < doubles[0]: doubles[0] = p['DOUBLES']          
            elif p['DOUBLES'] > doubles[1]: doubles[1] = p['DOUBLES']
    return doubles

# QUESTION 10: POSITION WITH MOST PLAYERS
# OBJECTIVE A (6): Using the batting data, find the position or positions with the most
# number of players. Return the position(s) in a list.
def getHighestPlayedPosition(batting_data):
    count = 0
    positionMap = {}
    position = []
    for p in batting_data:
        if p['POSITION'] in positionMap:
            positionMap[p['POSITION']] += 1
        else:
            positionMap[p['POSITION']] = 1
    
    for pos in positionMap:
        if (positionMap[pos] == count):
            position.append(pos)
        elif (positionMap[pos] > count):
            count = positionMap[pos]
            position = []
            position.append(pos)

    return position

# QUESTION 11: SLUGGING PERCENTAGE
# OBJECTIVE A (6): Slugging percentage for a player is calculated by the following equation.
# slugging = ((SINGLES) + (2 * DOUBLES) + (3 * TRIPLES) + (4 * HOMERUNS)) / ATBATS
# Determine the player in the batting data with the highest slugging percentage and has at least 300 ATBATS. 
# Return a list with the player name and slugging percentage (do not round).
def getHighestSlugging(batting_data):
    player = ['',0];
    for p in batting_data:
        if (p['ATBATS'] >= 300):
                s = (getTotalSingles(p['HITS'], p['DOUBLES'], p['TRIPLES'], p['HOMERUNS']) + 2*p['DOUBLES'] + 3*p['TRIPLES'] + 4*p['HOMERUNS']) / p['ATBATS']
                if s == player[1]:
                    player[0].append(', '+p['NAME'])
                elif s > player[1]:
                    player[0] = p['NAME']
                    player[1] = s
    return player

# QUESTION 12: PLAYERS FANTASY POINTS
# OBJECTIVE A (6): You have used batting_data. Below, this function has one parameter
# representing a dictionary of one player. Get your point system dictionary from 
# question 4 getPointSystem(). For each statistic in the point system, calculate how many points the player
# earned for the season. Sum all the points together and return the total points.
# Remember, each value in getPointSystem() is per 1 statistic. Use getTotalSingles to determine 'SINGLES'. 
# (or rewrite the logic yourself).
def getPlayerPoints(player):
    total = 0;
    points = getPointSystem()
    for statistic in points:
        if (statistic == 'SINGLES'):
            singles = getTotalSingles(player['HITS'],player['DOUBLES'],player['TRIPLES'],player['HOMERUNS'])
            total += singles * points[statistic]
        else:
            total += points[statistic] * player[statistic]

    return total

# QUESTION 13: TEAM FANTASY POINTS
# OBJECTIVE A (7): Given the batting data and team identifier, team, 
# find the total number of fantasy points earned by the team's players.
# Return the number. Use getPlayerPoints() for each player on the team.
# OBJECTIVE B (2): If the team has more than 4000 points append the string
# 'PRO TEAM' to the number.
def getTeamFantasyPoints(batting_data, team):
    total = 0
    for p in batting_data:
        if (team == p['TEAM']):
            total += getPlayerPoints(p)
    if total > 4000: return str(total)+' PRO TEAM'
    return total

# QUESTION 14: BEST FANTASY TEAM
# OBJECTIVE A (7): You guessed it! What is the optimal fantasy team of batters? The list of batting_data
# is passed into the function below. Also passed in is a dictionary, positions. This includes positions 
# C,1B,2B,3B,SS,LF,CF,RF,DH as the keys. (Designated Hitter instead of pitcher). For each position in the dictionary, positions,
# find the player that would earn the most fantasy points based on getPlayerPoints() function, set that player NAME as the
# value of the position key in the dictionary and return the dictionary. 
# NOTE: Do not consider there being more than one player with the highest points per position.
def getOptimalFantasyTeam(batting_data, positions):
    for pos in positions:
        total = 0;
        for player in batting_data:
            if (player['POSITION'] == pos):
                playerTotal = getPlayerPoints(player)
                if (playerTotal > total):
                    total = playerTotal
                    positions[pos] = player['NAME']

    return positions

# QUESTION 15: ATBATS VARIANCE
# OBJECTIVE A (8): Variance is defined as the average of the squared differences from the mean.
# Use the algorithm below to find the  variance. DO NOT use a built in function.
# 1. Calculate the AVERAGE of the ATBATS.
# 2. Calculate the sum of deviations of each ATBATS by the formula:
#    deviation += (ATBATS - AVERAGE) * (ATBATS - AVERAGE)
# 3. Calculate the average of the deviations values. This is the variance. Return the value.
def getAtBatVariance(batting_data):
    variance = 0
    count = 0
    avg = 0
    for p in batting_data:
        avg += p['ATBATS']
        count += 1
    avg = avg / count
    
    for p in batting_data: 
        variance += (p['ATBATS'] - avg)**2

    return variance / count

# QUESTION 16: IDENTICAL FANTASY POINTS
# OBJECTIVE A (8): Some players might have the same Fantasy Points.
# Determine the points for each player with your function 
# getPlayerPoints(). If two or more players earned the same number
# of points, put and return the results in a dictionary in the following format:
# { '100' : ['Gary Sanchez','Joey Votto'], '200' : ['Carlos Santana','Eric Hosmer'], ... }
# Only consider players with 400 or more at bats.
def getIdenticalPoints(batting_data):
    players = {}
    identicial = {}
    for p in batting_data:
        if p['ATBATS'] >= 400:
            points = getPlayerPoints(p)
            if points not in players:
                players[points] = [p['NAME']]
            else:
                players[points].append(p['NAME'])
    for p in players:
        if len(players[p]) > 1:
            identicial[p] = players[p]
    return identicial

# QUESTION 17: PLAYER ANAGRAMS
# OBJECTIVE A (8): An Anagram is a word or phrase that is made up of the exact same characters as
# another word or phrase. The batting_data is passed into the function below along with a string, phrase.
# Write code to find all player names that are an Anagram for the given phrase. Return the player names in a list.
# HINT: Remove the spaces from the phrase and player names. Normalize characters to upper case.
def getAnagrams(batting_data, phrase):
    anagrams = []
    phrase = phrase.replace(' ','')
    for p in batting_data:
        player = p['NAME'].replace(' ','')
        if (sorted(player.upper()) == sorted(phrase.upper())):
            anagrams.append(p['NAME'])
    return anagrams


# QUESTION 18: MEDIAN HOMERUNS
# OBJECTIVE A (8): The median is the middle number in a set. If there is an even amount of
# numbers, you average the two middle numbers. Find the median number of HOMERUNS in the batting_data
# and return the number. Do not use a built in library.
# HINT: Sort the list using the sort(key=getHomeRuns) function with key parameter. Use the function getHomeRuns as the key value. 
# HINT: Use Integer Division when searching for the middle index.
def getMedianDuration(batting_data):
    median = 0
    batting_data.sort(key=getHomeRuns)
    if (len(batting_data) % 2 != 0):
        median = batting_data[len(batting_data)//2]['HOMERUNS']
    else:
        median = (batting_data[len(batting_data)//2]['HOMERUNS'] + batting_data[(len(batting_data)//2)-1]['HOMERUNS']) / 2
    return median

def getHomeRuns(player):
    return player['HOMERUNS']

# QUESTION 19: FREE STYLE
# OBJECTIVE A (2): Write a custom function that calculates a statistic with the batting_data and returns a string
# OBJECTIVE B (1): Write a comment that explains what statistic you are calculating AND why it is important.
# OBJECTIVE C (1): Call a previous function within your calculation.
# DO NOT USE A BUILT IN FUNCTION.
def getStatistic(batting_data):
    x = 0

    return x

###############################
# MAIN FUNCTION
# NOTE: It is in your best interest to not modify values in this function.
# Input for the programming questions is test data. The supervisor will use 
# different values to grade your program.
###############################
def main():
    positions = {'C':'','1B':'','2B':'','3B':'','SS':'','LF':'','CF':'','RF':'','DH':'',}
      
    # Print Question Answer
    print('Source Code (MAIN) - Division B/C - Fantasy Baseball - Team Builder')
    
    print('QUESTION 0 A (2): '+getTeamName('04/27/2018')) # Bath High School Super Squad 04/27/2018
    print('QUESTION 1 A (2): '+str(getTotalSingles(167,30,4,34))) # 99
    
    print('QUESTION 2 A (2): '+str(getBattingAverage(113, 425))) # 0.26588235294117646 or .266
    print('QUESTION 2 B (3): '+str(getBattingAverage(113, 425))) # .266
    
    print('QUESTION 3 A (2): '+str(getFirstLastName('nicholas castellanos'))) #['nicholas', 'castellanos'] or ['Nicholas', 'Castellanos']
    print('QUESTION 3 B (3): '+str(getFirstLastName('nicholas castellanos'))) # ['Nicholas', 'Castellanos']
    
    print('QUESTION 4 A (3): '+str(getPointSystem())) # {'STRIKEOUT': -1, 'TRIPLE': 3, 'SINGLE': 1, 'RUN': 2, 'WALK': 1, 'RBI': 2, 'DOUBLE': 2, 'HOMERUN': 4} not in order
    print('QUESTION 5 A (4): '+str(getAverageAge(batting_data_2017))) # 27.973724884080372
    
    print('QUESTION 6 A (4): '+str(getPositionCount(batting_data_2017, 'CF'))) # 59
    print('QUESTION 6 B (2): '+str(getPositionCount(batting_data_2017, 'DH'))) # -1
    
    print('QUESTION 7 A (5): '+str(getMostStat(batting_data_2017,'STRIKEOUTS'))) # ['Aaron Judge']
    
    print('QUESTION 8 A (5): '+str(getPlayers(batting_data_2017))) #un sorted ['Aaron Judge', 'Albert Pujols', 'Anthony Rendon', 'Anthony Rizzo', 'Charlie Blackmon', 'Edwin Encarnacion', 'Giancarlo Stanton', 'J.D. Martinez', 'Jake Lamb', 'Jay Bruce', 'Joey Votto', 'Jonathan Schoop', 'Jose Abreu', 'Justin Upton', 'Khris Davis', 'Marcell Ozuna', 'Mookie Betts', 'Nelson Cruz', 'Nicholas Castellanos', 'Nolan Arenado', 'Nomar Mazara', 'Paul Goldschmidt', 'Ryan Zimmerman', 'Travis Shaw']
    print('QUESTION 8 B (2): '+str(getPlayers(batting_data_2017))) #sorted ['Aaron Judge', 'Albert Pujols', 'Anthony Rendon', 'Anthony Rizzo', 'Charlie Blackmon', 'Edwin Encarnacion', 'Giancarlo Stanton', 'J.D. Martinez', 'Jake Lamb', 'Jay Bruce', 'Joey Votto', 'Jonathan Schoop', 'Jose Abreu', 'Justin Upton', 'Khris Davis', 'Marcell Ozuna', 'Mookie Betts', 'Nelson Cruz', 'Nicholas Castellanos', 'Nolan Arenado', 'Nomar Mazara', 'Paul Goldschmidt', 'Ryan Zimmerman', 'Travis Shaw']
    
    print('QUESTION 9 A (5): '+str(getDoubleRange(batting_data_2017))) # [9, 56]
    print('QUESTION 10 A (6): '+str(getHighestPlayedPosition(batting_data_2017))) # ['P']    
    print('QUESTION 11 A (6): '+str(getHighestSlugging(batting_data_2017))) # ['J.D. Martinez', 0.6898148148148148]
    print('QUESTION 12 A (6): '+str(getPlayerPoints({'NAME':'Kris Bryant','AGE':25,'TEAM':'CHC','POSITION':'3B','ATBATS':549,'RUNS':111,'HITS':162,'DOUBLES':38,'TRIPLES':4,'HOMERUNS':29,'RBI':73,'WALKS':95,'STRIKEOUTS':128}))) # 630 
  
    print('QUESTION 13 A (7): '+str(getTeamFantasyPoints(batting_data_2017,'ATL'))) # 3612
    print('QUESTION 13 B (2): '+str(getTeamFantasyPoints(batting_data_2017,'CHC'))) # 4609 PRO TEAM
    
    print('QUESTION 14 A (7): '+str(getOptimalFantasyTeam(batting_data_2017, positions))) # {'SS': 'Francisco Lindor', 'RF': 'Giancarlo Stanton', '1B': 'Joey Votto', 'C': 'Gary Sanchez', 'DH': 'Edwin Encarnacion', 'LF': 'Marcell Ozuna', '3B': 'Nolan Arenado', 'CF': 'Charlie Blackmon', '2B': 'Jose Altuve'}
    print('QUESTION 15 A (8): '+str(getAtBatVariance(batting_data_2017))) # 38047.51921721706
    print('QUESTION 16 A (8): '+str(getIdenticalPoints(batting_data_2017))) # {388: ['Trevor Story', 'Hanley Ramirez'], 389: ['Odubel Herrera', 'Starlin Castro'], 518: ['Eddie Rosario', 'Corey Seager'], 263: ['Alex Gordon', 'Matt Davidson'], 584: ['Manny Machado', 'Robinson Cano', 'Jake Lamb'], 521: ['Shin-Soo Choo', 'Eugenio Suarez', 'Tommy Pham'], 332: ['Carlos Beltran', 'Brandon Drury'], 461: ['Wil Myers', 'Todd Frazier'], 463: ['Corey Dickerson', 'Kendrys Morales'], 528: ['Kyle Seager', 'Matt Carpenter'], 312: ['Manuel Margot', 'Randal Grichuk'], 403: ['Kevin Pillar', 'Mark Trumbo', 'Scott Schebler'], 343: ['Tim Anderson', 'Danny Valencia'], 408: ['Brandon Crawford', 'A.J. Pollock'], 282: ['Jose Peraza', 'Ryan Goins'], 410: ['Cesar Hernandez', 'Eduardo Escobar'], 415: ['Denard Span', 'Eduardo Nunez'], 481: ['Albert Pujols', 'Lorenzo Cain', 'Buster Posey'], 482: ['Xander Bogaerts', 'Joe Mauer'], 549: ['Andrew Benintendi', 'Mike Moustakas'], 358: ['Tommy Joseph', 'Kyle Schwarber'], 360: ['Orlando Arcia', 'Jackie Bradley'], 425: ['Jean Segura', 'Asdrubal Cabrera'], 429: ['Ryon Healy', 'Salvador Perez'], 431: ['Jorge Polanco', 'Dexter Fowler'], 520: ['Andrelton Simmons', 'Josh Reddick'], 376: ['Trea Turner', 'Dustin Pedroia'], 505: ['Adam Duvall', 'Yuli Gurriel', 'Mark Reynolds', 'Marwin Gonzalez'], 378: ['Ben Gamel', 'Jason Heyward']}
    print('QUESTION 17 A (8): '+str(getAnagrams(batting_data_2017, 'grey ke sale'))) # ['Kyle Seager']
    print('QUESTION 18 A (8): '+str(getMedianDuration(batting_data_2017))) # 5
    
    print('QUESTION 19 A (2): '+str(getStatistic(batting_data_2017))) # Check for Answer
    print('QUESTION 19 B (1): '+'Check for comment explaining function.')
    print('QUESTION 19 C (1): '+'Check if previous function in file was called.')

batting_data_2017 = [
{'NAME':'Ender Inciarte','AGE':26,'TEAM':'ATL','POSITION':'CF','ATBATS':662,'RUNS':93,'HITS':201,'DOUBLES':27,'TRIPLES':5,'HOMERUNS':11,'RBI':57,'WALKS':49,'STRIKEOUTS':94,},
{'NAME':'Dee Gordon','AGE':29,'TEAM':'MIA','POSITION':'2B','ATBATS':653,'RUNS':114,'HITS':201,'DOUBLES':20,'TRIPLES':9,'HOMERUNS':2,'RBI':33,'WALKS':25,'STRIKEOUTS':93,},
{'NAME':'Francisco Lindor','AGE':23,'TEAM':'CLE','POSITION':'SS','ATBATS':651,'RUNS':99,'HITS':178,'DOUBLES':44,'TRIPLES':4,'HOMERUNS':33,'RBI':89,'WALKS':60,'STRIKEOUTS':93,},
{'NAME':'Charlie Blackmon','AGE':30,'TEAM':'COL','POSITION':'CF','ATBATS':644,'RUNS':137,'HITS':213,'DOUBLES':35,'TRIPLES':14,'HOMERUNS':37,'RBI':104,'WALKS':65,'STRIKEOUTS':135,},
{'NAME':'Elvis Andrus','AGE':28,'TEAM':'TEX','POSITION':'SS','ATBATS':643,'RUNS':100,'HITS':191,'DOUBLES':44,'TRIPLES':4,'HOMERUNS':20,'RBI':88,'WALKS':38,'STRIKEOUTS':101,},
{'NAME':'Manny Machado','AGE':24,'TEAM':'BAL','POSITION':'3B','ATBATS':630,'RUNS':81,'HITS':163,'DOUBLES':33,'TRIPLES':1,'HOMERUNS':33,'RBI':95,'WALKS':50,'STRIKEOUTS':115,},
{'NAME':'Mookie Betts','AGE':24,'TEAM':'BOS','POSITION':'RF','ATBATS':628,'RUNS':101,'HITS':166,'DOUBLES':46,'TRIPLES':2,'HOMERUNS':24,'RBI':102,'WALKS':77,'STRIKEOUTS':79,},
{'NAME':'Jonathan Schoop','AGE':25,'TEAM':'BAL','POSITION':'2B','ATBATS':622,'RUNS':92,'HITS':182,'DOUBLES':35,'TRIPLES':0,'HOMERUNS':32,'RBI':105,'WALKS':35,'STRIKEOUTS':142,},
{'NAME':'Jose Abreu','AGE':30,'TEAM':'CHW','POSITION':'1B','ATBATS':621,'RUNS':95,'HITS':189,'DOUBLES':43,'TRIPLES':6,'HOMERUNS':33,'RBI':102,'WALKS':35,'STRIKEOUTS':119,},
{'NAME':'Melky Cabrera','AGE':32,'TEAM':'TOT','POSITION':'LF','ATBATS':620,'RUNS':78,'HITS':177,'DOUBLES':30,'TRIPLES':2,'HOMERUNS':17,'RBI':85,'WALKS':36,'STRIKEOUTS':74,},
{'NAME':'Brian Dozier','AGE':30,'TEAM':'MIN','POSITION':'2B','ATBATS':617,'RUNS':106,'HITS':167,'DOUBLES':30,'TRIPLES':4,'HOMERUNS':34,'RBI':93,'WALKS':78,'STRIKEOUTS':141,},
{'NAME':'Nicholas Castellanos','AGE':25,'TEAM':'DET','POSITION':'3B','ATBATS':614,'RUNS':73,'HITS':167,'DOUBLES':36,'TRIPLES':10,'HOMERUNS':26,'RBI':101,'WALKS':41,'STRIKEOUTS':142,},
{'NAME':'Evan Longoria','AGE':31,'TEAM':'TBR','POSITION':'3B','ATBATS':613,'RUNS':71,'HITS':160,'DOUBLES':36,'TRIPLES':2,'HOMERUNS':20,'RBI':86,'WALKS':46,'STRIKEOUTS':109,},
{'NAME':'Marcell Ozuna','AGE':26,'TEAM':'MIA','POSITION':'LF','ATBATS':613,'RUNS':93,'HITS':191,'DOUBLES':30,'TRIPLES':2,'HOMERUNS':37,'RBI':124,'WALKS':64,'STRIKEOUTS':144,},
{'NAME':'DJ LeMahieu','AGE':28,'TEAM':'COL','POSITION':'2B','ATBATS':609,'RUNS':95,'HITS':189,'DOUBLES':28,'TRIPLES':4,'HOMERUNS':8,'RBI':64,'WALKS':59,'STRIKEOUTS':90,},
{'NAME':'Freddy Galvis','AGE':27,'TEAM':'PHI','POSITION':'SS','ATBATS':608,'RUNS':71,'HITS':155,'DOUBLES':29,'TRIPLES':6,'HOMERUNS':12,'RBI':61,'WALKS':45,'STRIKEOUTS':111,},
{'NAME':'Rougned Odor','AGE':23,'TEAM':'TEX','POSITION':'2B','ATBATS':607,'RUNS':79,'HITS':124,'DOUBLES':21,'TRIPLES':3,'HOMERUNS':30,'RBI':75,'WALKS':32,'STRIKEOUTS':162,},
{'NAME':'Nolan Arenado','AGE':26,'TEAM':'COL','POSITION':'3B','ATBATS':606,'RUNS':100,'HITS':187,'DOUBLES':43,'TRIPLES':7,'HOMERUNS':37,'RBI':130,'WALKS':62,'STRIKEOUTS':106,},
{'NAME':'Eric Hosmer','AGE':27,'TEAM':'KCR','POSITION':'1B','ATBATS':603,'RUNS':98,'HITS':192,'DOUBLES':31,'TRIPLES':1,'HOMERUNS':25,'RBI':94,'WALKS':66,'STRIKEOUTS':104,},
{'NAME':'Christian Yelich','AGE':25,'TEAM':'MIA','POSITION':'CF','ATBATS':602,'RUNS':100,'HITS':170,'DOUBLES':36,'TRIPLES':2,'HOMERUNS':18,'RBI':81,'WALKS':80,'STRIKEOUTS':137,},
{'NAME':'Alcides Escobar','AGE':30,'TEAM':'KCR','POSITION':'SS','ATBATS':599,'RUNS':71,'HITS':150,'DOUBLES':36,'TRIPLES':5,'HOMERUNS':6,'RBI':54,'WALKS':15,'STRIKEOUTS':102,},
{'NAME':'Adam Jones','AGE':31,'TEAM':'BAL','POSITION':'CF','ATBATS':597,'RUNS':82,'HITS':170,'DOUBLES':28,'TRIPLES':1,'HOMERUNS':26,'RBI':73,'WALKS':27,'STRIKEOUTS':113,},
{'NAME':'Giancarlo Stanton','AGE':27,'TEAM':'MIA','POSITION':'RF','ATBATS':597,'RUNS':123,'HITS':168,'DOUBLES':32,'TRIPLES':0,'HOMERUNS':59,'RBI':132,'WALKS':85,'STRIKEOUTS':163,},
{'NAME':'Brett Gardner','AGE':33,'TEAM':'NYY','POSITION':'LF','ATBATS':594,'RUNS':96,'HITS':157,'DOUBLES':26,'TRIPLES':4,'HOMERUNS':21,'RBI':63,'WALKS':72,'STRIKEOUTS':122,},
{'NAME':'Nick Markakis','AGE':33,'TEAM':'ATL','POSITION':'RF','ATBATS':593,'RUNS':76,'HITS':163,'DOUBLES':39,'TRIPLES':1,'HOMERUNS':8,'RBI':76,'WALKS':68,'STRIKEOUTS':110,},
{'NAME':'Albert Pujols','AGE':37,'TEAM':'LAA','POSITION':'DH','ATBATS':593,'RUNS':53,'HITS':143,'DOUBLES':17,'TRIPLES':0,'HOMERUNS':23,'RBI':101,'WALKS':37,'STRIKEOUTS':93,},
{'NAME':'Robinson Cano','AGE':34,'TEAM':'SEA','POSITION':'2B','ATBATS':592,'RUNS':79,'HITS':166,'DOUBLES':33,'TRIPLES':0,'HOMERUNS':23,'RBI':97,'WALKS':49,'STRIKEOUTS':85,},
{'NAME':'Jose Altuve','AGE':27,'TEAM':'HOU','POSITION':'2B','ATBATS':590,'RUNS':112,'HITS':204,'DOUBLES':39,'TRIPLES':4,'HOMERUNS':24,'RBI':81,'WALKS':58,'STRIKEOUTS':84,},
{'NAME':'Andrelton Simmons','AGE':27,'TEAM':'LAA','POSITION':'SS','ATBATS':589,'RUNS':77,'HITS':164,'DOUBLES':38,'TRIPLES':2,'HOMERUNS':14,'RBI':69,'WALKS':47,'STRIKEOUTS':67,},
{'NAME':'Corey Dickerson','AGE':28,'TEAM':'TBR','POSITION':'LF','ATBATS':588,'RUNS':84,'HITS':166,'DOUBLES':33,'TRIPLES':4,'HOMERUNS':27,'RBI':62,'WALKS':35,'STRIKEOUTS':152,},
{'NAME':'Tim Anderson','AGE':24,'TEAM':'CHW','POSITION':'SS','ATBATS':587,'RUNS':72,'HITS':151,'DOUBLES':26,'TRIPLES':4,'HOMERUNS':17,'RBI':56,'WALKS':13,'STRIKEOUTS':162,},
{'NAME':'Jose Bautista','AGE':36,'TEAM':'TOR','POSITION':'RF','ATBATS':587,'RUNS':92,'HITS':119,'DOUBLES':27,'TRIPLES':0,'HOMERUNS':23,'RBI':65,'WALKS':84,'STRIKEOUTS':170,},
{'NAME':'Adam Duvall','AGE':28,'TEAM':'CIN','POSITION':'LF','ATBATS':587,'RUNS':78,'HITS':146,'DOUBLES':37,'TRIPLES':3,'HOMERUNS':31,'RBI':99,'WALKS':39,'STRIKEOUTS':170,},
{'NAME':'Whit Merrifield','AGE':28,'TEAM':'KCR','POSITION':'2B','ATBATS':587,'RUNS':80,'HITS':169,'DOUBLES':32,'TRIPLES':6,'HOMERUNS':19,'RBI':78,'WALKS':29,'STRIKEOUTS':88,},
{'NAME':'Kevin Pillar','AGE':28,'TEAM':'TOR','POSITION':'CF','ATBATS':587,'RUNS':72,'HITS':150,'DOUBLES':37,'TRIPLES':1,'HOMERUNS':16,'RBI':42,'WALKS':33,'STRIKEOUTS':95,},
{'NAME':'Jose Ramirez','AGE':24,'TEAM':'CLE','POSITION':'3B','ATBATS':585,'RUNS':107,'HITS':186,'DOUBLES':56,'TRIPLES':6,'HOMERUNS':29,'RBI':83,'WALKS':52,'STRIKEOUTS':69,},
{'NAME':'Lorenzo Cain','AGE':31,'TEAM':'KCR','POSITION':'CF','ATBATS':584,'RUNS':86,'HITS':175,'DOUBLES':27,'TRIPLES':5,'HOMERUNS':15,'RBI':49,'WALKS':54,'STRIKEOUTS':100,},
{'NAME':'Billy Hamilton','AGE':26,'TEAM':'CIN','POSITION':'CF','ATBATS':582,'RUNS':85,'HITS':144,'DOUBLES':17,'TRIPLES':11,'HOMERUNS':4,'RBI':38,'WALKS':44,'STRIKEOUTS':133,},
{'NAME':'Kyle Seager','AGE':29,'TEAM':'SEA','POSITION':'3B','ATBATS':578,'RUNS':72,'HITS':144,'DOUBLES':33,'TRIPLES':1,'HOMERUNS':27,'RBI':88,'WALKS':58,'STRIKEOUTS':110,},
{'NAME':'Ryon Healy','AGE':25,'TEAM':'OAK','POSITION':'DH','ATBATS':576,'RUNS':66,'HITS':156,'DOUBLES':29,'TRIPLES':0,'HOMERUNS':25,'RBI':78,'WALKS':23,'STRIKEOUTS':142,},
{'NAME':'Maikel Franco','AGE':24,'TEAM':'PHI','POSITION':'3B','ATBATS':575,'RUNS':66,'HITS':132,'DOUBLES':29,'TRIPLES':1,'HOMERUNS':24,'RBI':76,'WALKS':41,'STRIKEOUTS':95,},
{'NAME':'Andrew Benintendi','AGE':22,'TEAM':'BOS','POSITION':'LF','ATBATS':573,'RUNS':84,'HITS':155,'DOUBLES':26,'TRIPLES':1,'HOMERUNS':20,'RBI':90,'WALKS':70,'STRIKEOUTS':112,},
{'NAME':'Brandon Phillips','AGE':36,'TEAM':'TOT','POSITION':'2B','ATBATS':572,'RUNS':81,'HITS':163,'DOUBLES':34,'TRIPLES':1,'HOMERUNS':13,'RBI':60,'WALKS':21,'STRIKEOUTS':73,},
{'NAME':'Anthony Rizzo','AGE':27,'TEAM':'CHC','POSITION':'1B','ATBATS':572,'RUNS':99,'HITS':156,'DOUBLES':32,'TRIPLES':3,'HOMERUNS':32,'RBI':109,'WALKS':91,'STRIKEOUTS':90,},
{'NAME':'Xander Bogaerts','AGE':24,'TEAM':'BOS','POSITION':'SS','ATBATS':571,'RUNS':94,'HITS':156,'DOUBLES':32,'TRIPLES':6,'HOMERUNS':10,'RBI':62,'WALKS':56,'STRIKEOUTS':116,},
{'NAME':'Carlos Santana','AGE':31,'TEAM':'CLE','POSITION':'1B','ATBATS':571,'RUNS':90,'HITS':148,'DOUBLES':37,'TRIPLES':3,'HOMERUNS':23,'RBI':79,'WALKS':88,'STRIKEOUTS':94,},
{'NAME':'Andrew McCutchen','AGE':30,'TEAM':'PIT','POSITION':'CF','ATBATS':570,'RUNS':94,'HITS':159,'DOUBLES':30,'TRIPLES':2,'HOMERUNS':28,'RBI':88,'WALKS':73,'STRIKEOUTS':116,},
{'NAME':'Kole Calhoun','AGE':29,'TEAM':'LAA','POSITION':'RF','ATBATS':569,'RUNS':77,'HITS':139,'DOUBLES':23,'TRIPLES':2,'HOMERUNS':19,'RBI':71,'WALKS':71,'STRIKEOUTS':134,},
{'NAME':'Jed Lowrie','AGE':33,'TEAM':'OAK','POSITION':'2B','ATBATS':567,'RUNS':86,'HITS':157,'DOUBLES':49,'TRIPLES':3,'HOMERUNS':14,'RBI':69,'WALKS':73,'STRIKEOUTS':100,},
{'NAME':'Wil Myers','AGE':26,'TEAM':'SDP','POSITION':'1B','ATBATS':567,'RUNS':80,'HITS':138,'DOUBLES':29,'TRIPLES':3,'HOMERUNS':30,'RBI':74,'WALKS':70,'STRIKEOUTS':180,},
{'NAME':'Khris Davis','AGE':29,'TEAM':'OAK','POSITION':'LF','ATBATS':566,'RUNS':91,'HITS':140,'DOUBLES':28,'TRIPLES':1,'HOMERUNS':43,'RBI':110,'WALKS':73,'STRIKEOUTS':195,},
{'NAME':'Justin Smoak','AGE':30,'TEAM':'TOR','POSITION':'1B','ATBATS':560,'RUNS':85,'HITS':151,'DOUBLES':29,'TRIPLES':1,'HOMERUNS':38,'RBI':90,'WALKS':73,'STRIKEOUTS':128,},
{'NAME':'Mark Trumbo','AGE':31,'TEAM':'BAL','POSITION':'DH','ATBATS':559,'RUNS':79,'HITS':131,'DOUBLES':22,'TRIPLES':0,'HOMERUNS':23,'RBI':65,'WALKS':42,'STRIKEOUTS':149,},
{'NAME':'Joey Votto','AGE':33,'TEAM':'CIN','POSITION':'1B','ATBATS':559,'RUNS':106,'HITS':179,'DOUBLES':34,'TRIPLES':1,'HOMERUNS':36,'RBI':100,'WALKS':134,'STRIKEOUTS':83,},
{'NAME':'Paul Goldschmidt','AGE':29,'TEAM':'ARI','POSITION':'1B','ATBATS':558,'RUNS':117,'HITS':166,'DOUBLES':34,'TRIPLES':3,'HOMERUNS':36,'RBI':120,'WALKS':94,'STRIKEOUTS':147,},
{'NAME':'Kendrys Morales','AGE':34,'TEAM':'TOR','POSITION':'DH','ATBATS':557,'RUNS':67,'HITS':139,'DOUBLES':25,'TRIPLES':0,'HOMERUNS':28,'RBI':85,'WALKS':43,'STRIKEOUTS':132,},
{'NAME':'Justin Upton','AGE':29,'TEAM':'TOT','POSITION':'LF','ATBATS':557,'RUNS':100,'HITS':152,'DOUBLES':44,'TRIPLES':0,'HOMERUNS':35,'RBI':109,'WALKS':74,'STRIKEOUTS':180,},
{'NAME':'Alex Bregman','AGE':23,'TEAM':'HOU','POSITION':'3B','ATBATS':556,'RUNS':88,'HITS':158,'DOUBLES':39,'TRIPLES':5,'HOMERUNS':19,'RBI':71,'WALKS':55,'STRIKEOUTS':97,},
{'NAME':'Nelson Cruz','AGE':36,'TEAM':'SEA','POSITION':'DH','ATBATS':556,'RUNS':91,'HITS':160,'DOUBLES':28,'TRIPLES':0,'HOMERUNS':39,'RBI':119,'WALKS':70,'STRIKEOUTS':140,},
{'NAME':'Jay Bruce','AGE':30,'TEAM':'TOT','POSITION':'RF','ATBATS':555,'RUNS':82,'HITS':141,'DOUBLES':29,'TRIPLES':2,'HOMERUNS':36,'RBI':101,'WALKS':57,'STRIKEOUTS':139,},
{'NAME':'Mike Moustakas','AGE':28,'TEAM':'KCR','POSITION':'3B','ATBATS':555,'RUNS':75,'HITS':151,'DOUBLES':24,'TRIPLES':0,'HOMERUNS':38,'RBI':85,'WALKS':34,'STRIKEOUTS':94,},
{'NAME':'Edwin Encarnacion','AGE':34,'TEAM':'CLE','POSITION':'DH','ATBATS':554,'RUNS':96,'HITS':143,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':38,'RBI':107,'WALKS':104,'STRIKEOUTS':133,},
{'NAME':'Nomar Mazara','AGE':22,'TEAM':'TEX','POSITION':'RF','ATBATS':554,'RUNS':64,'HITS':140,'DOUBLES':30,'TRIPLES':2,'HOMERUNS':20,'RBI':101,'WALKS':55,'STRIKEOUTS':127,},
{'NAME':'Ian Kinsler','AGE':35,'TEAM':'DET','POSITION':'2B','ATBATS':551,'RUNS':90,'HITS':130,'DOUBLES':25,'TRIPLES':3,'HOMERUNS':22,'RBI':52,'WALKS':55,'STRIKEOUTS':86,},
{'NAME':'Josh Bell','AGE':24,'TEAM':'PIT','POSITION':'1B','ATBATS':549,'RUNS':75,'HITS':140,'DOUBLES':26,'TRIPLES':6,'HOMERUNS':26,'RBI':90,'WALKS':66,'STRIKEOUTS':117,},
{'NAME':'Kris Bryant','AGE':25,'TEAM':'CHC','POSITION':'3B','ATBATS':549,'RUNS':111,'HITS':162,'DOUBLES':38,'TRIPLES':4,'HOMERUNS':29,'RBI':73,'WALKS':95,'STRIKEOUTS':128,},
{'NAME':'George Springer','AGE':27,'TEAM':'HOU','POSITION':'CF','ATBATS':548,'RUNS':112,'HITS':155,'DOUBLES':29,'TRIPLES':0,'HOMERUNS':34,'RBI':85,'WALKS':64,'STRIKEOUTS':111,},
{'NAME':'Shin-Soo Choo','AGE':34,'TEAM':'TEX','POSITION':'RF','ATBATS':544,'RUNS':96,'HITS':142,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':22,'RBI':78,'WALKS':77,'STRIKEOUTS':134,},
{'NAME':'Trey Mancini','AGE':25,'TEAM':'BAL','POSITION':'LF','ATBATS':543,'RUNS':65,'HITS':159,'DOUBLES':26,'TRIPLES':4,'HOMERUNS':24,'RBI':78,'WALKS':33,'STRIKEOUTS':139,},
{'NAME':'Aaron Judge','AGE':25,'TEAM':'NYY','POSITION':'RF','ATBATS':542,'RUNS':128,'HITS':154,'DOUBLES':24,'TRIPLES':3,'HOMERUNS':52,'RBI':114,'WALKS':127,'STRIKEOUTS':208,},
{'NAME':'Eddie Rosario','AGE':25,'TEAM':'MIN','POSITION':'LF','ATBATS':542,'RUNS':79,'HITS':157,'DOUBLES':33,'TRIPLES':2,'HOMERUNS':27,'RBI':78,'WALKS':35,'STRIKEOUTS':106,},
{'NAME':'Corey Seager','AGE':23,'TEAM':'LAD','POSITION':'SS','ATBATS':539,'RUNS':85,'HITS':159,'DOUBLES':33,'TRIPLES':0,'HOMERUNS':22,'RBI':77,'WALKS':67,'STRIKEOUTS':131,},
{'NAME':'Travis Shaw','AGE':27,'TEAM':'MIL','POSITION':'3B','ATBATS':538,'RUNS':84,'HITS':147,'DOUBLES':34,'TRIPLES':1,'HOMERUNS':31,'RBI':101,'WALKS':60,'STRIKEOUTS':138,},
{'NAME':'Jake Lamb','AGE':26,'TEAM':'ARI','POSITION':'3B','ATBATS':536,'RUNS':89,'HITS':133,'DOUBLES':30,'TRIPLES':4,'HOMERUNS':30,'RBI':105,'WALKS':87,'STRIKEOUTS':152,},
{'NAME':'Didi Gregorius','AGE':27,'TEAM':'NYY','POSITION':'SS','ATBATS':534,'RUNS':73,'HITS':153,'DOUBLES':27,'TRIPLES':0,'HOMERUNS':25,'RBI':87,'WALKS':25,'STRIKEOUTS':70,},
{'NAME':'Daniel Murphy','AGE':32,'TEAM':'WSN','POSITION':'2B','ATBATS':534,'RUNS':94,'HITS':172,'DOUBLES':43,'TRIPLES':3,'HOMERUNS':23,'RBI':93,'WALKS':52,'STRIKEOUTS':77,},
{'NAME':'Eugenio Suarez','AGE':25,'TEAM':'CIN','POSITION':'3B','ATBATS':534,'RUNS':87,'HITS':139,'DOUBLES':25,'TRIPLES':2,'HOMERUNS':26,'RBI':82,'WALKS':84,'STRIKEOUTS':147,},
{'NAME':'Tim Beckham','AGE':27,'TEAM':'TOT','POSITION':'SS','ATBATS':533,'RUNS':67,'HITS':148,'DOUBLES':18,'TRIPLES':5,'HOMERUNS':22,'RBI':62,'WALKS':36,'STRIKEOUTS':167,},
{'NAME':'J.T. Realmuto','AGE':26,'TEAM':'MIA','POSITION':'C','ATBATS':532,'RUNS':68,'HITS':148,'DOUBLES':31,'TRIPLES':5,'HOMERUNS':17,'RBI':65,'WALKS':36,'STRIKEOUTS':106,},
{'NAME':'Yuli Gurriel','AGE':33,'TEAM':'HOU','POSITION':'1B','ATBATS':529,'RUNS':69,'HITS':158,'DOUBLES':43,'TRIPLES':1,'HOMERUNS':18,'RBI':75,'WALKS':22,'STRIKEOUTS':62,},
{'NAME':'Odubel Herrera','AGE':25,'TEAM':'PHI','POSITION':'CF','ATBATS':526,'RUNS':67,'HITS':148,'DOUBLES':42,'TRIPLES':3,'HOMERUNS':14,'RBI':56,'WALKS':31,'STRIKEOUTS':126,},
{'NAME':'Joe Mauer','AGE':34,'TEAM':'MIN','POSITION':'1B','ATBATS':525,'RUNS':69,'HITS':160,'DOUBLES':36,'TRIPLES':1,'HOMERUNS':7,'RBI':71,'WALKS':66,'STRIKEOUTS':83,},
{'NAME':'David Peralta','AGE':29,'TEAM':'ARI','POSITION':'RF','ATBATS':525,'RUNS':82,'HITS':154,'DOUBLES':31,'TRIPLES':3,'HOMERUNS':14,'RBI':57,'WALKS':43,'STRIKEOUTS':94,},
{'NAME':'Domingo Santana','AGE':24,'TEAM':'MIL','POSITION':'RF','ATBATS':525,'RUNS':88,'HITS':146,'DOUBLES':29,'TRIPLES':0,'HOMERUNS':30,'RBI':85,'WALKS':73,'STRIKEOUTS':178,},
{'NAME':'Jean Segura','AGE':27,'TEAM':'SEA','POSITION':'SS','ATBATS':524,'RUNS':80,'HITS':157,'DOUBLES':30,'TRIPLES':2,'HOMERUNS':11,'RBI':45,'WALKS':34,'STRIKEOUTS':83,},
{'NAME':'Ryan Zimmerman','AGE':32,'TEAM':'WSN','POSITION':'1B','ATBATS':524,'RUNS':90,'HITS':159,'DOUBLES':33,'TRIPLES':0,'HOMERUNS':36,'RBI':108,'WALKS':44,'STRIKEOUTS':126,},
{'NAME':'Steven Souza','AGE':28,'TEAM':'TBR','POSITION':'RF','ATBATS':523,'RUNS':78,'HITS':125,'DOUBLES':21,'TRIPLES':2,'HOMERUNS':30,'RBI':78,'WALKS':84,'STRIKEOUTS':179,},
{'NAME':'Mark Reynolds','AGE':33,'TEAM':'COL','POSITION':'1B','ATBATS':520,'RUNS':82,'HITS':139,'DOUBLES':22,'TRIPLES':1,'HOMERUNS':30,'RBI':97,'WALKS':69,'STRIKEOUTS':175,},
{'NAME':'Brandon Crawford','AGE':30,'TEAM':'SFG','POSITION':'SS','ATBATS':518,'RUNS':58,'HITS':131,'DOUBLES':34,'TRIPLES':1,'HOMERUNS':14,'RBI':77,'WALKS':42,'STRIKEOUTS':113,},
{'NAME':'Avisail Garcia','AGE':26,'TEAM':'CHW','POSITION':'RF','ATBATS':518,'RUNS':75,'HITS':171,'DOUBLES':27,'TRIPLES':5,'HOMERUNS':18,'RBI':80,'WALKS':33,'STRIKEOUTS':111,},
{'NAME':'Chris Taylor','AGE':26,'TEAM':'LAD','POSITION':'CF','ATBATS':514,'RUNS':85,'HITS':148,'DOUBLES':34,'TRIPLES':5,'HOMERUNS':21,'RBI':72,'WALKS':50,'STRIKEOUTS':142,},
{'NAME':'Chase Headley','AGE':33,'TEAM':'NYY','POSITION':'3B','ATBATS':512,'RUNS':77,'HITS':140,'DOUBLES':30,'TRIPLES':1,'HOMERUNS':12,'RBI':61,'WALKS':60,'STRIKEOUTS':132,},
{'NAME':'Logan Morrison','AGE':29,'TEAM':'TBR','POSITION':'1B','ATBATS':512,'RUNS':75,'HITS':126,'DOUBLES':22,'TRIPLES':1,'HOMERUNS':38,'RBI':85,'WALKS':81,'STRIKEOUTS':149,},
{'NAME':'Cesar Hernandez','AGE':27,'TEAM':'PHI','POSITION':'2B','ATBATS':511,'RUNS':85,'HITS':150,'DOUBLES':26,'TRIPLES':6,'HOMERUNS':9,'RBI':34,'WALKS':61,'STRIKEOUTS':104,},
{'NAME':'Max Kepler','AGE':24,'TEAM':'MIN','POSITION':'RF','ATBATS':511,'RUNS':67,'HITS':124,'DOUBLES':32,'TRIPLES':2,'HOMERUNS':19,'RBI':69,'WALKS':47,'STRIKEOUTS':114,},
{'NAME':'Joe Panik','AGE':26,'TEAM':'SFG','POSITION':'2B','ATBATS':511,'RUNS':60,'HITS':147,'DOUBLES':28,'TRIPLES':5,'HOMERUNS':10,'RBI':53,'WALKS':46,'STRIKEOUTS':54,},
{'NAME':'Ben Gamel','AGE':25,'TEAM':'SEA','POSITION':'LF','ATBATS':509,'RUNS':68,'HITS':140,'DOUBLES':27,'TRIPLES':5,'HOMERUNS':11,'RBI':59,'WALKS':36,'STRIKEOUTS':122,},
{'NAME':'Mitch Moreland','AGE':31,'TEAM':'BOS','POSITION':'1B','ATBATS':508,'RUNS':73,'HITS':125,'DOUBLES':34,'TRIPLES':0,'HOMERUNS':22,'RBI':79,'WALKS':57,'STRIKEOUTS':120,},
{'NAME':'Anthony Rendon','AGE':27,'TEAM':'WSN','POSITION':'3B','ATBATS':508,'RUNS':81,'HITS':153,'DOUBLES':41,'TRIPLES':1,'HOMERUNS':25,'RBI':100,'WALKS':84,'STRIKEOUTS':82,},
{'NAME':'Orlando Arcia','AGE':22,'TEAM':'MIL','POSITION':'SS','ATBATS':506,'RUNS':56,'HITS':140,'DOUBLES':17,'TRIPLES':2,'HOMERUNS':15,'RBI':53,'WALKS':36,'STRIKEOUTS':100,},
{'NAME':'Trevor Story','AGE':24,'TEAM':'COL','POSITION':'SS','ATBATS':503,'RUNS':68,'HITS':120,'DOUBLES':32,'TRIPLES':3,'HOMERUNS':24,'RBI':82,'WALKS':49,'STRIKEOUTS':191,},
{'NAME':'Jordy Mercer','AGE':30,'TEAM':'PIT','POSITION':'SS','ATBATS':502,'RUNS':52,'HITS':128,'DOUBLES':24,'TRIPLES':5,'HOMERUNS':14,'RBI':58,'WALKS':51,'STRIKEOUTS':88,},
{'NAME':'Yadier Molina','AGE':34,'TEAM':'STL','POSITION':'C','ATBATS':501,'RUNS':60,'HITS':137,'DOUBLES':27,'TRIPLES':1,'HOMERUNS':18,'RBI':82,'WALKS':28,'STRIKEOUTS':74,},
{'NAME':'Jose Reyes','AGE':34,'TEAM':'NYM','POSITION':'SS','ATBATS':501,'RUNS':75,'HITS':123,'DOUBLES':25,'TRIPLES':7,'HOMERUNS':15,'RBI':58,'WALKS':50,'STRIKEOUTS':79,},
{'NAME':'Yasiel Puig','AGE':26,'TEAM':'LAD','POSITION':'RF','ATBATS':499,'RUNS':72,'HITS':131,'DOUBLES':24,'TRIPLES':2,'HOMERUNS':28,'RBI':74,'WALKS':64,'STRIKEOUTS':100,},
{'NAME':'Matt Carpenter','AGE':31,'TEAM':'STL','POSITION':'1B','ATBATS':497,'RUNS':91,'HITS':120,'DOUBLES':31,'TRIPLES':2,'HOMERUNS':23,'RBI':69,'WALKS':109,'STRIKEOUTS':125,},
{'NAME':'Denard Span','AGE':33,'TEAM':'SFG','POSITION':'CF','ATBATS':497,'RUNS':73,'HITS':135,'DOUBLES':31,'TRIPLES':5,'HOMERUNS':12,'RBI':43,'WALKS':40,'STRIKEOUTS':69,},
{'NAME':'Hanley Ramirez','AGE':33,'TEAM':'BOS','POSITION':'DH','ATBATS':496,'RUNS':58,'HITS':120,'DOUBLES':24,'TRIPLES':0,'HOMERUNS':23,'RBI':62,'WALKS':51,'STRIKEOUTS':116,},
{'NAME':'Tommy Joseph','AGE':25,'TEAM':'PHI','POSITION':'1B','ATBATS':495,'RUNS':51,'HITS':119,'DOUBLES':27,'TRIPLES':1,'HOMERUNS':22,'RBI':69,'WALKS':33,'STRIKEOUTS':129,},
{'NAME':'Buster Posey','AGE':30,'TEAM':'SFG','POSITION':'C','ATBATS':494,'RUNS':62,'HITS':158,'DOUBLES':34,'TRIPLES':0,'HOMERUNS':12,'RBI':67,'WALKS':61,'STRIKEOUTS':66,},
{'NAME':'Hunter Pence','AGE':34,'TEAM':'SFG','POSITION':'RF','ATBATS':493,'RUNS':55,'HITS':128,'DOUBLES':13,'TRIPLES':5,'HOMERUNS':13,'RBI':67,'WALKS':40,'STRIKEOUTS':102,},
{'NAME':'Jorge Polanco','AGE':23,'TEAM':'MIN','POSITION':'SS','ATBATS':488,'RUNS':60,'HITS':125,'DOUBLES':30,'TRIPLES':3,'HOMERUNS':13,'RBI':74,'WALKS':41,'STRIKEOUTS':78,},
{'NAME':'Dansby Swanson','AGE':23,'TEAM':'ATL','POSITION':'SS','ATBATS':488,'RUNS':59,'HITS':113,'DOUBLES':23,'TRIPLES':2,'HOMERUNS':6,'RBI':51,'WALKS':59,'STRIKEOUTS':120,},
{'NAME':'Manuel Margot','AGE':22,'TEAM':'SDP','POSITION':'CF','ATBATS':487,'RUNS':53,'HITS':128,'DOUBLES':18,'TRIPLES':7,'HOMERUNS':13,'RBI':39,'WALKS':35,'STRIKEOUTS':106,},
{'NAME':'Jose Peraza','AGE':23,'TEAM':'CIN','POSITION':'2B','ATBATS':487,'RUNS':50,'HITS':126,'DOUBLES':9,'TRIPLES':4,'HOMERUNS':5,'RBI':37,'WALKS':20,'STRIKEOUTS':70,},
{'NAME':'Josh Harrison','AGE':29,'TEAM':'PIT','POSITION':'2B','ATBATS':486,'RUNS':66,'HITS':132,'DOUBLES':26,'TRIPLES':2,'HOMERUNS':16,'RBI':47,'WALKS':28,'STRIKEOUTS':90,},
{'NAME':'Yolmer Sanchez','AGE':25,'TEAM':'CHW','POSITION':'2B','ATBATS':484,'RUNS':63,'HITS':129,'DOUBLES':19,'TRIPLES':8,'HOMERUNS':12,'RBI':59,'WALKS':35,'STRIKEOUTS':111,},
{'NAME':'Jackie Bradley','AGE':27,'TEAM':'BOS','POSITION':'CF','ATBATS':482,'RUNS':58,'HITS':118,'DOUBLES':19,'TRIPLES':3,'HOMERUNS':17,'RBI':63,'WALKS':48,'STRIKEOUTS':124,},
{'NAME':'Cody Bellinger','AGE':21,'TEAM':'LAD','POSITION':'1B','ATBATS':480,'RUNS':87,'HITS':128,'DOUBLES':26,'TRIPLES':4,'HOMERUNS':39,'RBI':97,'WALKS':64,'STRIKEOUTS':146,},
{'NAME':'Asdrubal Cabrera','AGE':31,'TEAM':'NYM','POSITION':'SS','ATBATS':479,'RUNS':66,'HITS':134,'DOUBLES':32,'TRIPLES':0,'HOMERUNS':14,'RBI':59,'WALKS':50,'STRIKEOUTS':83,},
{'NAME':'Josh Reddick','AGE':30,'TEAM':'HOU','POSITION':'RF','ATBATS':477,'RUNS':77,'HITS':150,'DOUBLES':34,'TRIPLES':4,'HOMERUNS':13,'RBI':82,'WALKS':43,'STRIKEOUTS':72,},
{'NAME':'Alex Gordon','AGE':33,'TEAM':'KCR','POSITION':'LF','ATBATS':476,'RUNS':52,'HITS':99,'DOUBLES':20,'TRIPLES':2,'HOMERUNS':9,'RBI':45,'WALKS':45,'STRIKEOUTS':126,},
{'NAME':'Todd Frazier','AGE':31,'TEAM':'TOT','POSITION':'3B','ATBATS':474,'RUNS':74,'HITS':101,'DOUBLES':19,'TRIPLES':1,'HOMERUNS':27,'RBI':76,'WALKS':83,'STRIKEOUTS':125,},
{'NAME':'Scott Schebler','AGE':26,'TEAM':'CIN','POSITION':'RF','ATBATS':473,'RUNS':63,'HITS':110,'DOUBLES':25,'TRIPLES':2,'HOMERUNS':30,'RBI':67,'WALKS':39,'STRIKEOUTS':125,},
{'NAME':'Salvador Perez','AGE':27,'TEAM':'KCR','POSITION':'C','ATBATS':471,'RUNS':57,'HITS':126,'DOUBLES':24,'TRIPLES':1,'HOMERUNS':27,'RBI':80,'WALKS':17,'STRIKEOUTS':95,},
{'NAME':'Gary Sanchez','AGE':24,'TEAM':'NYY','POSITION':'C','ATBATS':471,'RUNS':79,'HITS':131,'DOUBLES':20,'TRIPLES':0,'HOMERUNS':33,'RBI':90,'WALKS':40,'STRIKEOUTS':120,},
{'NAME':'Carlos Gonzalez','AGE':31,'TEAM':'COL','POSITION':'RF','ATBATS':470,'RUNS':72,'HITS':123,'DOUBLES':34,'TRIPLES':0,'HOMERUNS':14,'RBI':57,'WALKS':56,'STRIKEOUTS':119,},
{'NAME':'Javier Baez','AGE':24,'TEAM':'CHC','POSITION':'2B','ATBATS':469,'RUNS':75,'HITS':128,'DOUBLES':24,'TRIPLES':2,'HOMERUNS':23,'RBI':75,'WALKS':30,'STRIKEOUTS':144,},
{'NAME':'Miguel Cabrera','AGE':34,'TEAM':'DET','POSITION':'1B','ATBATS':469,'RUNS':50,'HITS':117,'DOUBLES':22,'TRIPLES':0,'HOMERUNS':16,'RBI':60,'WALKS':54,'STRIKEOUTS':110,},
{'NAME':'Matthew Joyce','AGE':32,'TEAM':'OAK','POSITION':'RF','ATBATS':469,'RUNS':78,'HITS':114,'DOUBLES':33,'TRIPLES':0,'HOMERUNS':25,'RBI':68,'WALKS':66,'STRIKEOUTS':113,},
{'NAME':'Eric Thames','AGE':30,'TEAM':'MIL','POSITION':'1B','ATBATS':469,'RUNS':83,'HITS':116,'DOUBLES':26,'TRIPLES':4,'HOMERUNS':31,'RBI':63,'WALKS':75,'STRIKEOUTS':163,},
{'NAME':'Carlos Beltran','AGE':40,'TEAM':'HOU','POSITION':'DH','ATBATS':467,'RUNS':60,'HITS':108,'DOUBLES':29,'TRIPLES':0,'HOMERUNS':14,'RBI':51,'WALKS':33,'STRIKEOUTS':102,},
{'NAME':'Eduardo Nunez','AGE':30,'TEAM':'TOT','POSITION':'3B','ATBATS':467,'RUNS':60,'HITS':146,'DOUBLES':33,'TRIPLES':0,'HOMERUNS':12,'RBI':58,'WALKS':18,'STRIKEOUTS':54,},
{'NAME':'Yangervis Solarte','AGE':29,'TEAM':'SDP','POSITION':'2B','ATBATS':466,'RUNS':49,'HITS':119,'DOUBLES':21,'TRIPLES':0,'HOMERUNS':18,'RBI':64,'WALKS':37,'STRIKEOUTS':61,},
{'NAME':'Jose Iglesias','AGE':27,'TEAM':'DET','POSITION':'SS','ATBATS':463,'RUNS':56,'HITS':118,'DOUBLES':33,'TRIPLES':1,'HOMERUNS':6,'RBI':54,'WALKS':21,'STRIKEOUTS':65,},
{'NAME':'Byron Buxton','AGE':23,'TEAM':'MIN','POSITION':'CF','ATBATS':462,'RUNS':69,'HITS':117,'DOUBLES':14,'TRIPLES':6,'HOMERUNS':16,'RBI':51,'WALKS':38,'STRIKEOUTS':150,},
{'NAME':'Scooter Gennett','AGE':27,'TEAM':'CIN','POSITION':'2B','ATBATS':461,'RUNS':80,'HITS':136,'DOUBLES':22,'TRIPLES':3,'HOMERUNS':27,'RBI':97,'WALKS':30,'STRIKEOUTS':114,},
{'NAME':'Eduardo Escobar','AGE':28,'TEAM':'MIN','POSITION':'3B','ATBATS':457,'RUNS':62,'HITS':116,'DOUBLES':16,'TRIPLES':5,'HOMERUNS':21,'RBI':73,'WALKS':33,'STRIKEOUTS':98,},
{'NAME':'Justin Turner','AGE':32,'TEAM':'LAD','POSITION':'3B','ATBATS':457,'RUNS':72,'HITS':147,'DOUBLES':32,'TRIPLES':0,'HOMERUNS':21,'RBI':71,'WALKS':59,'STRIKEOUTS':56,},
{'NAME':'Chris Davis','AGE':31,'TEAM':'BAL','POSITION':'1B','ATBATS':456,'RUNS':65,'HITS':98,'DOUBLES':15,'TRIPLES':1,'HOMERUNS':26,'RBI':61,'WALKS':61,'STRIKEOUTS':195,},
{'NAME':'Marwin Gonzalez','AGE':28,'TEAM':'HOU','POSITION':'LF','ATBATS':455,'RUNS':67,'HITS':138,'DOUBLES':34,'TRIPLES':0,'HOMERUNS':23,'RBI':90,'WALKS':49,'STRIKEOUTS':99,},
{'NAME':'Yonder Alonso','AGE':30,'TEAM':'TOT','POSITION':'1B','ATBATS':451,'RUNS':72,'HITS':120,'DOUBLES':22,'TRIPLES':0,'HOMERUNS':28,'RBI':67,'WALKS':68,'STRIKEOUTS':118,},
{'NAME':'Danny Valencia','AGE':32,'TEAM':'SEA','POSITION':'1B','ATBATS':450,'RUNS':54,'HITS':115,'DOUBLES':19,'TRIPLES':3,'HOMERUNS':15,'RBI':66,'WALKS':40,'STRIKEOUTS':122,},
{'NAME':'Joey Gallo','AGE':23,'TEAM':'TEX','POSITION':'3B','ATBATS':449,'RUNS':85,'HITS':94,'DOUBLES':18,'TRIPLES':3,'HOMERUNS':41,'RBI':80,'WALKS':75,'STRIKEOUTS':196,},
{'NAME':'Curtis Granderson','AGE':36,'TEAM':'TOT','POSITION':'CF','ATBATS':449,'RUNS':74,'HITS':95,'DOUBLES':24,'TRIPLES':3,'HOMERUNS':26,'RBI':64,'WALKS':71,'STRIKEOUTS':123,},
{'NAME':'Brandon Drury','AGE':24,'TEAM':'ARI','POSITION':'2B','ATBATS':445,'RUNS':41,'HITS':119,'DOUBLES':37,'TRIPLES':2,'HOMERUNS':13,'RBI':63,'WALKS':28,'STRIKEOUTS':103,},
{'NAME':'Hunter Renfroe','AGE':25,'TEAM':'SDP','POSITION':'RF','ATBATS':445,'RUNS':51,'HITS':103,'DOUBLES':25,'TRIPLES':1,'HOMERUNS':26,'RBI':58,'WALKS':27,'STRIKEOUTS':140,},
{'NAME':'Tommy Pham','AGE':29,'TEAM':'STL','POSITION':'LF','ATBATS':444,'RUNS':95,'HITS':136,'DOUBLES':22,'TRIPLES':2,'HOMERUNS':23,'RBI':73,'WALKS':71,'STRIKEOUTS':117,},
{'NAME':'Cory Spangenberg','AGE':26,'TEAM':'SDP','POSITION':'3B','ATBATS':444,'RUNS':57,'HITS':117,'DOUBLES':18,'TRIPLES':2,'HOMERUNS':13,'RBI':46,'WALKS':34,'STRIKEOUTS':128,},
{'NAME':'Starlin Castro','AGE':27,'TEAM':'NYY','POSITION':'2B','ATBATS':443,'RUNS':66,'HITS':133,'DOUBLES':18,'TRIPLES':1,'HOMERUNS':16,'RBI':63,'WALKS':23,'STRIKEOUTS':93,},
{'NAME':'Freddie Freeman','AGE':27,'TEAM':'ATL','POSITION':'1B','ATBATS':440,'RUNS':84,'HITS':135,'DOUBLES':35,'TRIPLES':2,'HOMERUNS':28,'RBI':71,'WALKS':65,'STRIKEOUTS':95,},
{'NAME':'Zack Cozart','AGE':31,'TEAM':'CIN','POSITION':'SS','ATBATS':438,'RUNS':80,'HITS':130,'DOUBLES':24,'TRIPLES':7,'HOMERUNS':24,'RBI':63,'WALKS':62,'STRIKEOUTS':78,},
{'NAME':'Yasmani Grandal','AGE':28,'TEAM':'LAD','POSITION':'C','ATBATS':438,'RUNS':50,'HITS':108,'DOUBLES':27,'TRIPLES':0,'HOMERUNS':22,'RBI':58,'WALKS':40,'STRIKEOUTS':130,},
{'NAME':'Matt Kemp','AGE':32,'TEAM':'ATL','POSITION':'LF','ATBATS':438,'RUNS':47,'HITS':121,'DOUBLES':23,'TRIPLES':1,'HOMERUNS':19,'RBI':64,'WALKS':27,'STRIKEOUTS':99,},
{'NAME':'Ben Zobrist','AGE':36,'TEAM':'CHC','POSITION':'2B','ATBATS':435,'RUNS':58,'HITS':101,'DOUBLES':20,'TRIPLES':3,'HOMERUNS':12,'RBI':50,'WALKS':54,'STRIKEOUTS':71,},
{'NAME':'Jason Heyward','AGE':27,'TEAM':'CHC','POSITION':'RF','ATBATS':432,'RUNS':59,'HITS':112,'DOUBLES':15,'TRIPLES':4,'HOMERUNS':11,'RBI':59,'WALKS':41,'STRIKEOUTS':67,},
{'NAME':'J.D. Martinez','AGE':29,'TEAM':'TOT','POSITION':'RF','ATBATS':432,'RUNS':85,'HITS':131,'DOUBLES':26,'TRIPLES':3,'HOMERUNS':45,'RBI':104,'WALKS':53,'STRIKEOUTS':128,},
{'NAME':'Hernan Perez','AGE':26,'TEAM':'MIL','POSITION':'LF','ATBATS':432,'RUNS':47,'HITS':112,'DOUBLES':19,'TRIPLES':3,'HOMERUNS':14,'RBI':51,'WALKS':20,'STRIKEOUTS':79,},
{'NAME':'Martin Maldonado','AGE':30,'TEAM':'LAA','POSITION':'C','ATBATS':429,'RUNS':43,'HITS':95,'DOUBLES':19,'TRIPLES':1,'HOMERUNS':14,'RBI':38,'WALKS':15,'STRIKEOUTS':119,},
{'NAME':'David Freese','AGE':34,'TEAM':'PIT','POSITION':'3B','ATBATS':426,'RUNS':44,'HITS':112,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':10,'RBI':52,'WALKS':58,'STRIKEOUTS':116,},
{'NAME':'Jedd Gyorko','AGE':28,'TEAM':'STL','POSITION':'3B','ATBATS':426,'RUNS':52,'HITS':116,'DOUBLES':21,'TRIPLES':2,'HOMERUNS':20,'RBI':67,'WALKS':47,'STRIKEOUTS':105,},
{'NAME':'Mike Napoli','AGE':35,'TEAM':'TEX','POSITION':'1B','ATBATS':425,'RUNS':60,'HITS':82,'DOUBLES':11,'TRIPLES':1,'HOMERUNS':29,'RBI':66,'WALKS':49,'STRIKEOUTS':163,},
{'NAME':'A.J. Pollock','AGE':29,'TEAM':'ARI','POSITION':'CF','ATBATS':425,'RUNS':73,'HITS':113,'DOUBLES':33,'TRIPLES':6,'HOMERUNS':14,'RBI':49,'WALKS':35,'STRIKEOUTS':71,},
{'NAME':'Miguel Sano','AGE':24,'TEAM':'MIN','POSITION':'3B','ATBATS':424,'RUNS':75,'HITS':112,'DOUBLES':15,'TRIPLES':2,'HOMERUNS':28,'RBI':77,'WALKS':54,'STRIKEOUTS':173,},
{'NAME':'Lucas Duda','AGE':31,'TEAM':'TOT','POSITION':'1B','ATBATS':423,'RUNS':50,'HITS':92,'DOUBLES':28,'TRIPLES':0,'HOMERUNS':30,'RBI':64,'WALKS':60,'STRIKEOUTS':135,},
{'NAME':'Jonathan Lucroy','AGE':31,'TEAM':'TOT','POSITION':'C','ATBATS':423,'RUNS':45,'HITS':112,'DOUBLES':21,'TRIPLES':3,'HOMERUNS':6,'RBI':40,'WALKS':46,'STRIKEOUTS':51,},
{'NAME':'Carlos Correa','AGE':22,'TEAM':'HOU','POSITION':'SS','ATBATS':422,'RUNS':82,'HITS':133,'DOUBLES':25,'TRIPLES':1,'HOMERUNS':24,'RBI':84,'WALKS':53,'STRIKEOUTS':92,},
{'NAME':'Kyle Schwarber','AGE':24,'TEAM':'CHC','POSITION':'LF','ATBATS':422,'RUNS':67,'HITS':89,'DOUBLES':16,'TRIPLES':1,'HOMERUNS':30,'RBI':59,'WALKS':59,'STRIKEOUTS':150,},
{'NAME':'Matt Wieters','AGE':31,'TEAM':'WSN','POSITION':'C','ATBATS':422,'RUNS':43,'HITS':95,'DOUBLES':20,'TRIPLES':0,'HOMERUNS':10,'RBI':52,'WALKS':38,'STRIKEOUTS':94,},
{'NAME':'Dexter Fowler','AGE':31,'TEAM':'STL','POSITION':'CF','ATBATS':420,'RUNS':68,'HITS':111,'DOUBLES':22,'TRIPLES':9,'HOMERUNS':18,'RBI':64,'WALKS':63,'STRIKEOUTS':101,},
{'NAME':'Bryce Harper','AGE':24,'TEAM':'WSN','POSITION':'RF','ATBATS':420,'RUNS':95,'HITS':134,'DOUBLES':27,'TRIPLES':1,'HOMERUNS':29,'RBI':87,'WALKS':68,'STRIKEOUTS':99,},
{'NAME':'Ryan Goins','AGE':29,'TEAM':'TOR','POSITION':'SS','ATBATS':418,'RUNS':37,'HITS':99,'DOUBLES':21,'TRIPLES':1,'HOMERUNS':9,'RBI':62,'WALKS':31,'STRIKEOUTS':96,},
{'NAME':'Paul DeJong','AGE':23,'TEAM':'STL','POSITION':'SS','ATBATS':417,'RUNS':55,'HITS':119,'DOUBLES':26,'TRIPLES':1,'HOMERUNS':25,'RBI':65,'WALKS':21,'STRIKEOUTS':124,},
{'NAME':'Josh Donaldson','AGE':31,'TEAM':'TOR','POSITION':'3B','ATBATS':415,'RUNS':65,'HITS':112,'DOUBLES':21,'TRIPLES':0,'HOMERUNS':33,'RBI':78,'WALKS':76,'STRIKEOUTS':111,},
{'NAME':'Keon Broxton','AGE':27,'TEAM':'MIL','POSITION':'CF','ATBATS':414,'RUNS':66,'HITS':91,'DOUBLES':15,'TRIPLES':4,'HOMERUNS':20,'RBI':49,'WALKS':40,'STRIKEOUTS':175,},
{'NAME':'Matt Davidson','AGE':26,'TEAM':'CHW','POSITION':'DH','ATBATS':414,'RUNS':43,'HITS':91,'DOUBLES':16,'TRIPLES':1,'HOMERUNS':26,'RBI':68,'WALKS':19,'STRIKEOUTS':165,},
{'NAME':'Randal Grichuk','AGE':25,'TEAM':'STL','POSITION':'LF','ATBATS':412,'RUNS':53,'HITS':98,'DOUBLES':25,'TRIPLES':3,'HOMERUNS':22,'RBI':59,'WALKS':26,'STRIKEOUTS':133,},
{'NAME':'Trea Turner','AGE':24,'TEAM':'WSN','POSITION':'SS','ATBATS':412,'RUNS':75,'HITS':117,'DOUBLES':24,'TRIPLES':6,'HOMERUNS':11,'RBI':45,'WALKS':30,'STRIKEOUTS':80,},
{'NAME':'Derek Dietrich','AGE':27,'TEAM':'MIA','POSITION':'3B','ATBATS':406,'RUNS':56,'HITS':101,'DOUBLES':22,'TRIPLES':5,'HOMERUNS':13,'RBI':53,'WALKS':36,'STRIKEOUTS':98,},
{'NAME':'Adam Frazier','AGE':25,'TEAM':'PIT','POSITION':'LF','ATBATS':406,'RUNS':55,'HITS':112,'DOUBLES':20,'TRIPLES':6,'HOMERUNS':6,'RBI':53,'WALKS':36,'STRIKEOUTS':57,},
{'NAME':'Dustin Pedroia','AGE':33,'TEAM':'BOS','POSITION':'2B','ATBATS':406,'RUNS':46,'HITS':119,'DOUBLES':19,'TRIPLES':0,'HOMERUNS':7,'RBI':62,'WALKS':49,'STRIKEOUTS':48,},
{'NAME':'Jonathan Villar','AGE':26,'TEAM':'MIL','POSITION':'2B','ATBATS':403,'RUNS':49,'HITS':97,'DOUBLES':18,'TRIPLES':1,'HOMERUNS':11,'RBI':40,'WALKS':30,'STRIKEOUTS':132,},
{'NAME':'Mike Trout','AGE':25,'TEAM':'LAA','POSITION':'CF','ATBATS':402,'RUNS':92,'HITS':123,'DOUBLES':25,'TRIPLES':3,'HOMERUNS':33,'RBI':72,'WALKS':94,'STRIKEOUTS':90,},
{'NAME':'Michael Taylor','AGE':26,'TEAM':'WSN','POSITION':'CF','ATBATS':399,'RUNS':55,'HITS':108,'DOUBLES':23,'TRIPLES':3,'HOMERUNS':19,'RBI':53,'WALKS':29,'STRIKEOUTS':137,},
{'NAME':'Cameron Maybin','AGE':30,'TEAM':'TOT','POSITION':'CF','ATBATS':395,'RUNS':63,'HITS':90,'DOUBLES':20,'TRIPLES':2,'HOMERUNS':10,'RBI':35,'WALKS':51,'STRIKEOUTS':94,},
{'NAME':'Victor Martinez','AGE':38,'TEAM':'DET','POSITION':'DH','ATBATS':392,'RUNS':38,'HITS':100,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':10,'RBI':47,'WALKS':36,'STRIKEOUTS':63,},
{'NAME':'Gerardo Parra','AGE':30,'TEAM':'COL','POSITION':'LF','ATBATS':392,'RUNS':56,'HITS':121,'DOUBLES':24,'TRIPLES':1,'HOMERUNS':10,'RBI':71,'WALKS':20,'STRIKEOUTS':67,},
{'NAME':'Austin Hedges','AGE':24,'TEAM':'SDP','POSITION':'C','ATBATS':387,'RUNS':36,'HITS':83,'DOUBLES':17,'TRIPLES':0,'HOMERUNS':18,'RBI':55,'WALKS':23,'STRIKEOUTS':122,},
{'NAME':'Mike Zunino','AGE':26,'TEAM':'SEA','POSITION':'C','ATBATS':387,'RUNS':52,'HITS':97,'DOUBLES':25,'TRIPLES':0,'HOMERUNS':25,'RBI':64,'WALKS':39,'STRIKEOUTS':160,},
{'NAME':'Guillermo Heredia','AGE':26,'TEAM':'SEA','POSITION':'CF','ATBATS':386,'RUNS':43,'HITS':96,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':6,'RBI':24,'WALKS':27,'STRIKEOUTS':64,},
{'NAME':'Neil Walker','AGE':31,'TEAM':'TOT','POSITION':'2B','ATBATS':385,'RUNS':59,'HITS':102,'DOUBLES':21,'TRIPLES':2,'HOMERUNS':14,'RBI':49,'WALKS':55,'STRIKEOUTS':77,},
{'NAME':'Jorge Bonifacio','AGE':24,'TEAM':'KCR','POSITION':'RF','ATBATS':384,'RUNS':55,'HITS':98,'DOUBLES':15,'TRIPLES':1,'HOMERUNS':17,'RBI':40,'WALKS':35,'STRIKEOUTS':118,},
{'NAME':'Brandon Belt','AGE':29,'TEAM':'SFG','POSITION':'1B','ATBATS':382,'RUNS':63,'HITS':92,'DOUBLES':27,'TRIPLES':3,'HOMERUNS':18,'RBI':51,'WALKS':66,'STRIKEOUTS':104,},
{'NAME':'Robbie Grossman','AGE':27,'TEAM':'MIN','POSITION':'DH','ATBATS':382,'RUNS':62,'HITS':94,'DOUBLES':22,'TRIPLES':1,'HOMERUNS':9,'RBI':45,'WALKS':67,'STRIKEOUTS':79,},
{'NAME':'Ryan Braun','AGE':33,'TEAM':'MIL','POSITION':'LF','ATBATS':380,'RUNS':58,'HITS':102,'DOUBLES':28,'TRIPLES':2,'HOMERUNS':17,'RBI':52,'WALKS':38,'STRIKEOUTS':76,},
{'NAME':'Kevin Kiermaier','AGE':27,'TEAM':'TBR','POSITION':'CF','ATBATS':380,'RUNS':56,'HITS':105,'DOUBLES':15,'TRIPLES':3,'HOMERUNS':15,'RBI':39,'WALKS':31,'STRIKEOUTS':99,},
{'NAME':'Jon Jay','AGE':32,'TEAM':'CHC','POSITION':'LF','ATBATS':379,'RUNS':65,'HITS':112,'DOUBLES':18,'TRIPLES':3,'HOMERUNS':2,'RBI':34,'WALKS':37,'STRIKEOUTS':80,},
{'NAME':'Gregory Polanco','AGE':25,'TEAM':'PIT','POSITION':'RF','ATBATS':379,'RUNS':39,'HITS':95,'DOUBLES':20,'TRIPLES':0,'HOMERUNS':11,'RBI':35,'WALKS':27,'STRIKEOUTS':60,},
{'NAME':'Justin Bour','AGE':29,'TEAM':'MIA','POSITION':'1B','ATBATS':377,'RUNS':52,'HITS':109,'DOUBLES':18,'TRIPLES':0,'HOMERUNS':25,'RBI':83,'WALKS':47,'STRIKEOUTS':95,},
{'NAME':'Willson Contreras','AGE':25,'TEAM':'CHC','POSITION':'C','ATBATS':377,'RUNS':50,'HITS':104,'DOUBLES':21,'TRIPLES':0,'HOMERUNS':21,'RBI':74,'WALKS':45,'STRIKEOUTS':98,},
{'NAME':'Delino DeShields','AGE':24,'TEAM':'TEX','POSITION':'LF','ATBATS':376,'RUNS':75,'HITS':101,'DOUBLES':15,'TRIPLES':2,'HOMERUNS':6,'RBI':22,'WALKS':44,'STRIKEOUTS':109,},
{'NAME':'Michael Conforto','AGE':24,'TEAM':'NYM','POSITION':'LF','ATBATS':373,'RUNS':72,'HITS':104,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':27,'RBI':68,'WALKS':57,'STRIKEOUTS':113,},
{'NAME':'Matt Holliday','AGE':37,'TEAM':'NYY','POSITION':'DH','ATBATS':373,'RUNS':50,'HITS':86,'DOUBLES':18,'TRIPLES':0,'HOMERUNS':19,'RBI':64,'WALKS':46,'STRIKEOUTS':114,},
{'NAME':'Aaron Altherr','AGE':26,'TEAM':'PHI','POSITION':'LF','ATBATS':372,'RUNS':58,'HITS':101,'DOUBLES':24,'TRIPLES':5,'HOMERUNS':19,'RBI':65,'WALKS':32,'STRIKEOUTS':104,},
{'NAME':'Tucker Barnhart','AGE':26,'TEAM':'CIN','POSITION':'C','ATBATS':370,'RUNS':26,'HITS':100,'DOUBLES':24,'TRIPLES':2,'HOMERUNS':7,'RBI':44,'WALKS':42,'STRIKEOUTS':68,},
{'NAME':'Mitch Haniger','AGE':26,'TEAM':'SEA','POSITION':'RF','ATBATS':369,'RUNS':58,'HITS':104,'DOUBLES':25,'TRIPLES':2,'HOMERUNS':16,'RBI':47,'WALKS':31,'STRIKEOUTS':93,},
{'NAME':'Carlos Gomez','AGE':31,'TEAM':'TEX','POSITION':'CF','ATBATS':368,'RUNS':51,'HITS':94,'DOUBLES':23,'TRIPLES':1,'HOMERUNS':17,'RBI':51,'WALKS':31,'STRIKEOUTS':127,},
{'NAME':'Ian Happ','AGE':22,'TEAM':'CHC','POSITION':'CF','ATBATS':364,'RUNS':62,'HITS':92,'DOUBLES':17,'TRIPLES':3,'HOMERUNS':24,'RBI':68,'WALKS':39,'STRIKEOUTS':129,},
{'NAME':'Brandon Moss','AGE':33,'TEAM':'KCR','POSITION':'DH','ATBATS':362,'RUNS':41,'HITS':75,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':22,'RBI':50,'WALKS':37,'STRIKEOUTS':128,},
{'NAME':'Chris Owings','AGE':25,'TEAM':'ARI','POSITION':'SS','ATBATS':362,'RUNS':41,'HITS':97,'DOUBLES':25,'TRIPLES':1,'HOMERUNS':12,'RBI':51,'WALKS':17,'STRIKEOUTS':87,},
{'NAME':'Logan Forsythe','AGE':30,'TEAM':'LAD','POSITION':'2B','ATBATS':361,'RUNS':56,'HITS':81,'DOUBLES':19,'TRIPLES':0,'HOMERUNS':6,'RBI':36,'WALKS':69,'STRIKEOUTS':109,},
{'NAME':'Jason Castro','AGE':30,'TEAM':'MIN','POSITION':'C','ATBATS':356,'RUNS':49,'HITS':86,'DOUBLES':22,'TRIPLES':0,'HOMERUNS':10,'RBI':47,'WALKS':45,'STRIKEOUTS':108,},
{'NAME':'Jacoby Ellsbury','AGE':33,'TEAM':'NYY','POSITION':'CF','ATBATS':356,'RUNS':65,'HITS':94,'DOUBLES':20,'TRIPLES':4,'HOMERUNS':7,'RBI':39,'WALKS':41,'STRIKEOUTS':63,},
{'NAME':'Kolten Wong','AGE':26,'TEAM':'STL','POSITION':'2B','ATBATS':354,'RUNS':55,'HITS':101,'DOUBLES':27,'TRIPLES':3,'HOMERUNS':4,'RBI':42,'WALKS':41,'STRIKEOUTS':60,},
{'NAME':'James McCann','AGE':27,'TEAM':'DET','POSITION':'C','ATBATS':352,'RUNS':39,'HITS':89,'DOUBLES':14,'TRIPLES':2,'HOMERUNS':13,'RBI':49,'WALKS':26,'STRIKEOUTS':89,},
{'NAME':'Addison Russell','AGE':23,'TEAM':'CHC','POSITION':'SS','ATBATS':352,'RUNS':52,'HITS':84,'DOUBLES':21,'TRIPLES':3,'HOMERUNS':12,'RBI':43,'WALKS':29,'STRIKEOUTS':91,},
{'NAME':'Yunel Escobar','AGE':34,'TEAM':'LAA','POSITION':'3B','ATBATS':350,'RUNS':43,'HITS':96,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':7,'RBI':31,'WALKS':29,'STRIKEOUTS':51,},
{'NAME':'Brian McCann','AGE':33,'TEAM':'HOU','POSITION':'C','ATBATS':349,'RUNS':47,'HITS':84,'DOUBLES':12,'TRIPLES':1,'HOMERUNS':18,'RBI':62,'WALKS':38,'STRIKEOUTS':58,},
{'NAME':'Travis d''Arnaud','AGE':28,'TEAM':'NYM','POSITION':'C','ATBATS':348,'RUNS':39,'HITS':85,'DOUBLES':19,'TRIPLES':1,'HOMERUNS':16,'RBI':57,'WALKS':23,'STRIKEOUTS':59,},
{'NAME':'Mikie Mahtook','AGE':27,'TEAM':'DET','POSITION':'CF','ATBATS':348,'RUNS':50,'HITS':96,'DOUBLES':15,'TRIPLES':6,'HOMERUNS':12,'RBI':38,'WALKS':23,'STRIKEOUTS':79,},
{'NAME':'Luis Valbuena','AGE':31,'TEAM':'LAA','POSITION':'3B','ATBATS':347,'RUNS':42,'HITS':69,'DOUBLES':15,'TRIPLES':0,'HOMERUNS':22,'RBI':65,'WALKS':48,'STRIKEOUTS':106,},
{'NAME':'Jarrod Dyson','AGE':32,'TEAM':'SEA','POSITION':'CF','ATBATS':346,'RUNS':56,'HITS':87,'DOUBLES':13,'TRIPLES':3,'HOMERUNS':5,'RBI':30,'WALKS':28,'STRIKEOUTS':55,},
{'NAME':'Daniel Descalso','AGE':30,'TEAM':'ARI','POSITION':'2B','ATBATS':344,'RUNS':47,'HITS':80,'DOUBLES':16,'TRIPLES':5,'HOMERUNS':10,'RBI':51,'WALKS':48,'STRIKEOUTS':89,},
{'NAME':'Marcus Semien','AGE':26,'TEAM':'OAK','POSITION':'SS','ATBATS':342,'RUNS':53,'HITS':85,'DOUBLES':19,'TRIPLES':1,'HOMERUNS':10,'RBI':40,'WALKS':38,'STRIKEOUTS':85,},
{'NAME':'Welington Castillo','AGE':30,'TEAM':'BAL','POSITION':'C','ATBATS':341,'RUNS':44,'HITS':96,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':20,'RBI':53,'WALKS':22,'STRIKEOUTS':97,},
{'NAME':'Yan Gomes','AGE':29,'TEAM':'CLE','POSITION':'C','ATBATS':341,'RUNS':43,'HITS':79,'DOUBLES':15,'TRIPLES':0,'HOMERUNS':14,'RBI':56,'WALKS':31,'STRIKEOUTS':99,},
{'NAME':'Stephen Piscotty','AGE':26,'TEAM':'STL','POSITION':'RF','ATBATS':341,'RUNS':40,'HITS':80,'DOUBLES':16,'TRIPLES':1,'HOMERUNS':9,'RBI':39,'WALKS':52,'STRIKEOUTS':87,},
{'NAME':'Adrian Beltre','AGE':38,'TEAM':'TEX','POSITION':'3B','ATBATS':340,'RUNS':47,'HITS':106,'DOUBLES':22,'TRIPLES':1,'HOMERUNS':17,'RBI':71,'WALKS':39,'STRIKEOUTS':52,},
{'NAME':'Matt Adams','AGE':28,'TEAM':'TOT','POSITION':'1B','ATBATS':339,'RUNS':46,'HITS':93,'DOUBLES':22,'TRIPLES':1,'HOMERUNS':20,'RBI':65,'WALKS':23,'STRIKEOUTS':88,},
{'NAME':'C.J. Cron','AGE':27,'TEAM':'LAA','POSITION':'1B','ATBATS':339,'RUNS':39,'HITS':84,'DOUBLES':14,'TRIPLES':1,'HOMERUNS':16,'RBI':56,'WALKS':22,'STRIKEOUTS':96,},
{'NAME':'Ian Desmond','AGE':31,'TEAM':'COL','POSITION':'LF','ATBATS':339,'RUNS':47,'HITS':93,'DOUBLES':11,'TRIPLES':1,'HOMERUNS':7,'RBI':40,'WALKS':24,'STRIKEOUTS':87,},
{'NAME':'Michael Brantley','AGE':30,'TEAM':'CLE','POSITION':'LF','ATBATS':338,'RUNS':47,'HITS':101,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':9,'RBI':52,'WALKS':31,'STRIKEOUTS':50,},
{'NAME':'Brad Miller','AGE':27,'TEAM':'TBR','POSITION':'2B','ATBATS':338,'RUNS':43,'HITS':68,'DOUBLES':13,'TRIPLES':3,'HOMERUNS':9,'RBI':40,'WALKS':63,'STRIKEOUTS':110,},
{'NAME':'Norichika Aoki','AGE':35,'TEAM':'TOT','POSITION':'LF','ATBATS':336,'RUNS':48,'HITS':93,'DOUBLES':20,'TRIPLES':2,'HOMERUNS':5,'RBI':35,'WALKS':29,'STRIKEOUTS':44,},
{'NAME':'Darwin Barney','AGE':31,'TEAM':'TOR','POSITION':'2B','ATBATS':336,'RUNS':34,'HITS':78,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':6,'RBI':25,'WALKS':18,'STRIKEOUTS':64,},
{'NAME':'Rajai Davis','AGE':36,'TEAM':'TOT','POSITION':'CF','ATBATS':336,'RUNS':56,'HITS':79,'DOUBLES':19,'TRIPLES':2,'HOMERUNS':5,'RBI':20,'WALKS':27,'STRIKEOUTS':83,},
{'NAME':'Wilmer Flores','AGE':25,'TEAM':'NYM','POSITION':'3B','ATBATS':336,'RUNS':42,'HITS':91,'DOUBLES':17,'TRIPLES':1,'HOMERUNS':18,'RBI':52,'WALKS':17,'STRIKEOUTS':54,},
{'NAME':'Jason Kipnis','AGE':30,'TEAM':'CLE','POSITION':'2B','ATBATS':336,'RUNS':43,'HITS':78,'DOUBLES':25,'TRIPLES':0,'HOMERUNS':12,'RBI':35,'WALKS':28,'STRIKEOUTS':71,},
{'NAME':'Erick Aybar','AGE':33,'TEAM':'SDP','POSITION':'SS','ATBATS':333,'RUNS':37,'HITS':78,'DOUBLES':15,'TRIPLES':1,'HOMERUNS':7,'RBI':22,'WALKS':28,'STRIKEOUTS':57,},
{'NAME':'Wilmer Difo','AGE':25,'TEAM':'WSN','POSITION':'SS','ATBATS':332,'RUNS':47,'HITS':90,'DOUBLES':10,'TRIPLES':4,'HOMERUNS':5,'RBI':21,'WALKS':24,'STRIKEOUTS':74,},
{'NAME':'Adeiny Hechavarria','AGE':28,'TEAM':'TOT','POSITION':'SS','ATBATS':330,'RUNS':37,'HITS':86,'DOUBLES':14,'TRIPLES':5,'HOMERUNS':8,'RBI':30,'WALKS':13,'STRIKEOUTS':67,},
{'NAME':'Manny Pina','AGE':30,'TEAM':'MIL','POSITION':'C','ATBATS':330,'RUNS':45,'HITS':92,'DOUBLES':21,'TRIPLES':0,'HOMERUNS':9,'RBI':43,'WALKS':20,'STRIKEOUTS':79,},
{'NAME':'Seth Smith','AGE':34,'TEAM':'BAL','POSITION':'RF','ATBATS':330,'RUNS':50,'HITS':85,'DOUBLES':19,'TRIPLES':0,'HOMERUNS':13,'RBI':32,'WALKS':36,'STRIKEOUTS':79,},
{'NAME':'Christian Vazquez','AGE':26,'TEAM':'BOS','POSITION':'C','ATBATS':324,'RUNS':43,'HITS':94,'DOUBLES':18,'TRIPLES':2,'HOMERUNS':5,'RBI':32,'WALKS':17,'STRIKEOUTS':64,},
{'NAME':'Andrew Romine','AGE':31,'TEAM':'DET','POSITION':'2B','ATBATS':318,'RUNS':45,'HITS':74,'DOUBLES':17,'TRIPLES':2,'HOMERUNS':4,'RBI':25,'WALKS':22,'STRIKEOUTS':67,},
{'NAME':'Tyler Flowers','AGE':31,'TEAM':'ATL','POSITION':'C','ATBATS':317,'RUNS':41,'HITS':89,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':12,'RBI':49,'WALKS':31,'STRIKEOUTS':82,},
{'NAME':'Ronald Torreyes','AGE':24,'TEAM':'NYY','POSITION':'2B','ATBATS':315,'RUNS':35,'HITS':92,'DOUBLES':15,'TRIPLES':1,'HOMERUNS':3,'RBI':36,'WALKS':11,'STRIKEOUTS':43,},
{'NAME':'Steve Pearce','AGE':34,'TEAM':'TOR','POSITION':'LF','ATBATS':313,'RUNS':38,'HITS':79,'DOUBLES':17,'TRIPLES':1,'HOMERUNS':13,'RBI':37,'WALKS':27,'STRIKEOUTS':68,},
{'NAME':'Nick Williams','AGE':23,'TEAM':'PHI','POSITION':'RF','ATBATS':313,'RUNS':45,'HITS':90,'DOUBLES':14,'TRIPLES':4,'HOMERUNS':12,'RBI':55,'WALKS':20,'STRIKEOUTS':97,},
{'NAME':'Jose Pirela','AGE':27,'TEAM':'SDP','POSITION':'LF','ATBATS':312,'RUNS':43,'HITS':90,'DOUBLES':25,'TRIPLES':4,'HOMERUNS':10,'RBI':40,'WALKS':27,'STRIKEOUTS':71,},
{'NAME':'Alex Avila','AGE':30,'TEAM':'TOT','POSITION':'C','ATBATS':311,'RUNS':41,'HITS':82,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':14,'RBI':49,'WALKS':62,'STRIKEOUTS':120,},
{'NAME':'Gorkys Hernandez','AGE':29,'TEAM':'SFG','POSITION':'LF','ATBATS':310,'RUNS':40,'HITS':79,'DOUBLES':20,'TRIPLES':1,'HOMERUNS':0,'RBI':22,'WALKS':31,'STRIKEOUTS':73,},
{'NAME':'Starling Marte','AGE':28,'TEAM':'PIT','POSITION':'LF','ATBATS':309,'RUNS':48,'HITS':85,'DOUBLES':7,'TRIPLES':2,'HOMERUNS':7,'RBI':31,'WALKS':20,'STRIKEOUTS':63,},
{'NAME':'Chase Utley','AGE':38,'TEAM':'LAD','POSITION':'2B','ATBATS':309,'RUNS':43,'HITS':73,'DOUBLES':20,'TRIPLES':4,'HOMERUNS':8,'RBI':34,'WALKS':32,'STRIKEOUTS':57,},
{'NAME':'Carlos Asuaje','AGE':25,'TEAM':'SDP','POSITION':'2B','ATBATS':307,'RUNS':28,'HITS':83,'DOUBLES':14,'TRIPLES':1,'HOMERUNS':4,'RBI':21,'WALKS':28,'STRIKEOUTS':76,},
{'NAME':'Russell Martin','AGE':34,'TEAM':'TOR','POSITION':'C','ATBATS':307,'RUNS':49,'HITS':68,'DOUBLES':12,'TRIPLES':0,'HOMERUNS':13,'RBI':35,'WALKS':50,'STRIKEOUTS':83,},
{'NAME':'Howie Kendrick','AGE':33,'TEAM':'TOT','POSITION':'LF','ATBATS':305,'RUNS':40,'HITS':96,'DOUBLES':16,'TRIPLES':3,'HOMERUNS':9,'RBI':41,'WALKS':22,'STRIKEOUTS':68,},
{'NAME':'Adam Engel','AGE':25,'TEAM':'CHW','POSITION':'CF','ATBATS':301,'RUNS':34,'HITS':50,'DOUBLES':11,'TRIPLES':3,'HOMERUNS':6,'RBI':21,'WALKS':19,'STRIKEOUTS':117,},
{'NAME':'Aaron Hicks','AGE':27,'TEAM':'NYY','POSITION':'CF','ATBATS':301,'RUNS':54,'HITS':80,'DOUBLES':18,'TRIPLES':0,'HOMERUNS':15,'RBI':52,'WALKS':51,'STRIKEOUTS':67,},
{'NAME':'Leury Garcia','AGE':26,'TEAM':'CHW','POSITION':'CF','ATBATS':300,'RUNS':41,'HITS':81,'DOUBLES':15,'TRIPLES':2,'HOMERUNS':9,'RBI':33,'WALKS':13,'STRIKEOUTS':69,},
{'NAME':'Evan Gattis','AGE':30,'TEAM':'HOU','POSITION':'C','ATBATS':300,'RUNS':41,'HITS':79,'DOUBLES':22,'TRIPLES':0,'HOMERUNS':12,'RBI':55,'WALKS':18,'STRIKEOUTS':50,},
{'NAME':'Albert Almora','AGE':23,'TEAM':'CHC','POSITION':'CF','ATBATS':299,'RUNS':39,'HITS':89,'DOUBLES':18,'TRIPLES':1,'HOMERUNS':8,'RBI':46,'WALKS':19,'STRIKEOUTS':53,},
{'NAME':'Bradley Zimmer','AGE':24,'TEAM':'CLE','POSITION':'CF','ATBATS':299,'RUNS':41,'HITS':72,'DOUBLES':15,'TRIPLES':2,'HOMERUNS':8,'RBI':39,'WALKS':26,'STRIKEOUTS':99,},
{'NAME':'Enrique Hernandez','AGE':25,'TEAM':'LAD','POSITION':'CF','ATBATS':297,'RUNS':46,'HITS':64,'DOUBLES':24,'TRIPLES':2,'HOMERUNS':11,'RBI':37,'WALKS':41,'STRIKEOUTS':80,},
{'NAME':'Cameron Rupp','AGE':28,'TEAM':'PHI','POSITION':'C','ATBATS':295,'RUNS':35,'HITS':64,'DOUBLES':17,'TRIPLES':0,'HOMERUNS':14,'RBI':34,'WALKS':34,'STRIKEOUTS':114,},
{'NAME':'Yoenis Cespedes','AGE':31,'TEAM':'NYM','POSITION':'LF','ATBATS':291,'RUNS':46,'HITS':85,'DOUBLES':17,'TRIPLES':2,'HOMERUNS':17,'RBI':42,'WALKS':26,'STRIKEOUTS':61,},
{'NAME':'Ben Revere','AGE':29,'TEAM':'LAA','POSITION':'LF','ATBATS':291,'RUNS':37,'HITS':80,'DOUBLES':13,'TRIPLES':2,'HOMERUNS':1,'RBI':20,'WALKS':15,'STRIKEOUTS':25,},
{'NAME':'Matt Chapman','AGE':24,'TEAM':'OAK','POSITION':'3B','ATBATS':290,'RUNS':39,'HITS':68,'DOUBLES':23,'TRIPLES':2,'HOMERUNS':14,'RBI':40,'WALKS':32,'STRIKEOUTS':92,},
{'NAME':'Adam Rosales','AGE':34,'TEAM':'TOT','POSITION':'SS','ATBATS':289,'RUNS':25,'HITS':65,'DOUBLES':16,'TRIPLES':0,'HOMERUNS':7,'RBI':36,'WALKS':11,'STRIKEOUTS':100,},
{'NAME':'Ezequiel Carrera','AGE':30,'TEAM':'TOR','POSITION':'LF','ATBATS':287,'RUNS':38,'HITS':81,'DOUBLES':10,'TRIPLES':1,'HOMERUNS':8,'RBI':20,'WALKS':30,'STRIKEOUTS':75,},
{'NAME':'Nick Hundley','AGE':33,'TEAM':'SFG','POSITION':'C','ATBATS':287,'RUNS':27,'HITS':70,'DOUBLES':23,'TRIPLES':0,'HOMERUNS':9,'RBI':35,'WALKS':12,'STRIKEOUTS':81,},
{'NAME':'Aledmys Diaz','AGE':26,'TEAM':'STL','POSITION':'SS','ATBATS':286,'RUNS':31,'HITS':74,'DOUBLES':17,'TRIPLES':0,'HOMERUNS':7,'RBI':20,'WALKS':13,'STRIKEOUTS':42,},
{'NAME':'Trevor Plouffe','AGE':31,'TEAM':'TOT','POSITION':'3B','ATBATS':283,'RUNS':31,'HITS':56,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':9,'RBI':19,'WALKS':28,'STRIKEOUTS':88,},
{'NAME':'Chad Pinder','AGE':25,'TEAM':'OAK','POSITION':'RF','ATBATS':282,'RUNS':36,'HITS':67,'DOUBLES':15,'TRIPLES':1,'HOMERUNS':15,'RBI':42,'WALKS':18,'STRIKEOUTS':92,},
{'NAME':'Austin Jackson','AGE':30,'TEAM':'CLE','POSITION':'CF','ATBATS':280,'RUNS':46,'HITS':89,'DOUBLES':19,'TRIPLES':3,'HOMERUNS':7,'RBI':35,'WALKS':33,'STRIKEOUTS':64,},
{'NAME':'Jesus Aguilar','AGE':27,'TEAM':'MIL','POSITION':'1B','ATBATS':279,'RUNS':40,'HITS':74,'DOUBLES':15,'TRIPLES':2,'HOMERUNS':16,'RBI':52,'WALKS':25,'STRIKEOUTS':94,},
{'NAME':'Stephen Vogt','AGE':32,'TEAM':'TOT','POSITION':'C','ATBATS':279,'RUNS':25,'HITS':65,'DOUBLES':15,'TRIPLES':1,'HOMERUNS':12,'RBI':40,'WALKS':21,'STRIKEOUTS':56,},
{'NAME':'Kevan Smith','AGE':29,'TEAM':'CHW','POSITION':'C','ATBATS':276,'RUNS':23,'HITS':78,'DOUBLES':17,'TRIPLES':0,'HOMERUNS':4,'RBI':30,'WALKS':9,'STRIKEOUTS':46,},
{'NAME':'Kurt Suzuki','AGE':33,'TEAM':'ATL','POSITION':'C','ATBATS':276,'RUNS':38,'HITS':78,'DOUBLES':13,'TRIPLES':0,'HOMERUNS':19,'RBI':50,'WALKS':17,'STRIKEOUTS':39,},
{'NAME':'Joc Pederson','AGE':25,'TEAM':'LAD','POSITION':'CF','ATBATS':273,'RUNS':44,'HITS':58,'DOUBLES':20,'TRIPLES':0,'HOMERUNS':11,'RBI':35,'WALKS':39,'STRIKEOUTS':68,},
{'NAME':'Chris Iannetta','AGE':34,'TEAM':'ARI','POSITION':'C','ATBATS':272,'RUNS':38,'HITS':69,'DOUBLES':19,'TRIPLES':0,'HOMERUNS':17,'RBI':43,'WALKS':37,'STRIKEOUTS':87,},
{'NAME':'Jose Martinez','AGE':28,'TEAM':'STL','POSITION':'1B','ATBATS':272,'RUNS':47,'HITS':84,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':14,'RBI':46,'WALKS':32,'STRIKEOUTS':60,},
{'NAME':'Miguel Rojas','AGE':28,'TEAM':'MIA','POSITION':'SS','ATBATS':272,'RUNS':37,'HITS':79,'DOUBLES':16,'TRIPLES':2,'HOMERUNS':1,'RBI':26,'WALKS':27,'STRIKEOUTS':32,},
{'NAME':'Sandy Leon','AGE':28,'TEAM':'BOS','POSITION':'C','ATBATS':271,'RUNS':32,'HITS':61,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':7,'RBI':39,'WALKS':25,'STRIKEOUTS':74,},
{'NAME':'Adam Lind','AGE':33,'TEAM':'WSN','POSITION':'1B','ATBATS':267,'RUNS':39,'HITS':81,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':14,'RBI':59,'WALKS':28,'STRIKEOUTS':47,},
{'NAME':'Danny Espinosa','AGE':30,'TEAM':'TOT','POSITION':'2B','ATBATS':266,'RUNS':30,'HITS':46,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':6,'RBI':31,'WALKS':21,'STRIKEOUTS':109,},
{'NAME':'Francisco Cervelli','AGE':31,'TEAM':'PIT','POSITION':'C','ATBATS':265,'RUNS':31,'HITS':66,'DOUBLES':13,'TRIPLES':2,'HOMERUNS':5,'RBI':31,'WALKS':32,'STRIKEOUTS':65,},
{'NAME':'Robinson Chirinos','AGE':33,'TEAM':'TEX','POSITION':'C','ATBATS':263,'RUNS':46,'HITS':67,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':17,'RBI':38,'WALKS':34,'STRIKEOUTS':79,},
{'NAME':'Joey Rickard','AGE':26,'TEAM':'BAL','POSITION':'RF','ATBATS':261,'RUNS':29,'HITS':63,'DOUBLES':15,'TRIPLES':0,'HOMERUNS':4,'RBI':19,'WALKS':9,'STRIKEOUTS':63,},
{'NAME':'Pablo Sandoval','AGE':30,'TEAM':'TOT','POSITION':'3B','ATBATS':259,'RUNS':27,'HITS':57,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':9,'RBI':32,'WALKS':16,'STRIKEOUTS':53,},
{'NAME':'Taylor Motter','AGE':27,'TEAM':'SEA','POSITION':'SS','ATBATS':258,'RUNS':29,'HITS':51,'DOUBLES':12,'TRIPLES':0,'HOMERUNS':7,'RBI':26,'WALKS':21,'STRIKEOUTS':62,},
{'NAME':'John Jaso','AGE':33,'TEAM':'PIT','POSITION':'RF','ATBATS':256,'RUNS':28,'HITS':54,'DOUBLES':19,'TRIPLES':0,'HOMERUNS':10,'RBI':35,'WALKS':40,'STRIKEOUTS':66,},
{'NAME':'Mallex Smith','AGE':24,'TEAM':'TBR','POSITION':'CF','ATBATS':256,'RUNS':33,'HITS':69,'DOUBLES':8,'TRIPLES':4,'HOMERUNS':2,'RBI':12,'WALKS':23,'STRIKEOUTS':62,},
{'NAME':'J.J. Hardy','AGE':34,'TEAM':'BAL','POSITION':'SS','ATBATS':254,'RUNS':24,'HITS':55,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':4,'RBI':24,'WALKS':12,'STRIKEOUTS':48,},
{'NAME':'Caleb Joseph','AGE':31,'TEAM':'BAL','POSITION':'C','ATBATS':254,'RUNS':31,'HITS':65,'DOUBLES':14,'TRIPLES':1,'HOMERUNS':8,'RBI':28,'WALKS':10,'STRIKEOUTS':72,},
{'NAME':'Omar Narvaez','AGE':25,'TEAM':'CHW','POSITION':'C','ATBATS':253,'RUNS':23,'HITS':70,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':2,'RBI':14,'WALKS':38,'STRIKEOUTS':45,},
{'NAME':'Tyler Saladino','AGE':27,'TEAM':'CHW','POSITION':'2B','ATBATS':253,'RUNS':23,'HITS':45,'DOUBLES':9,'TRIPLES':2,'HOMERUNS':0,'RBI':10,'WALKS':23,'STRIKEOUTS':67,},
{'NAME':'Juan Lagares','AGE':28,'TEAM':'NYM','POSITION':'CF','ATBATS':252,'RUNS':37,'HITS':63,'DOUBLES':16,'TRIPLES':2,'HOMERUNS':3,'RBI':15,'WALKS':14,'STRIKEOUTS':56,},
{'NAME':'Jayson Werth','AGE':38,'TEAM':'WSN','POSITION':'LF','ATBATS':252,'RUNS':35,'HITS':57,'DOUBLES':10,'TRIPLES':1,'HOMERUNS':10,'RBI':29,'WALKS':35,'STRIKEOUTS':69,},
{'NAME':'Brian Goodwin','AGE':26,'TEAM':'WSN','POSITION':'CF','ATBATS':251,'RUNS':41,'HITS':63,'DOUBLES':21,'TRIPLES':1,'HOMERUNS':13,'RBI':30,'WALKS':23,'STRIKEOUTS':69,},
{'NAME':'Eric Sogard','AGE':31,'TEAM':'MIL','POSITION':'2B','ATBATS':249,'RUNS':37,'HITS':68,'DOUBLES':15,'TRIPLES':1,'HOMERUNS':3,'RBI':18,'WALKS':45,'STRIKEOUTS':37,},
{'NAME':'Alex Presley','AGE':31,'TEAM':'DET','POSITION':'RF','ATBATS':245,'RUNS':30,'HITS':77,'DOUBLES':10,'TRIPLES':3,'HOMERUNS':3,'RBI':20,'WALKS':15,'STRIKEOUTS':49,},
{'NAME':'Chris Young','AGE':33,'TEAM':'BOS','POSITION':'LF','ATBATS':243,'RUNS':30,'HITS':57,'DOUBLES':12,'TRIPLES':2,'HOMERUNS':7,'RBI':25,'WALKS':30,'STRIKEOUTS':55,},
{'NAME':'Johan Camargo','AGE':23,'TEAM':'ATL','POSITION':'3B','ATBATS':241,'RUNS':30,'HITS':72,'DOUBLES':21,'TRIPLES':2,'HOMERUNS':4,'RBI':27,'WALKS':12,'STRIKEOUTS':51,},
{'NAME':'Greg Garcia','AGE':27,'TEAM':'STL','POSITION':'3B','ATBATS':241,'RUNS':27,'HITS':61,'DOUBLES':9,'TRIPLES':2,'HOMERUNS':2,'RBI':20,'WALKS':37,'STRIKEOUTS':64,},
{'NAME':'Troy Tulowitzki','AGE':32,'TEAM':'TOR','POSITION':'SS','ATBATS':241,'RUNS':16,'HITS':60,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':7,'RBI':26,'WALKS':17,'STRIKEOUTS':40,},
{'NAME':'Kennys Vargas','AGE':26,'TEAM':'MIN','POSITION':'1B','ATBATS':241,'RUNS':33,'HITS':61,'DOUBLES':13,'TRIPLES':0,'HOMERUNS':11,'RBI':41,'WALKS':20,'STRIKEOUTS':77,},
{'NAME':'Lonnie Chisenhall','AGE':28,'TEAM':'CLE','POSITION':'RF','ATBATS':236,'RUNS':34,'HITS':68,'DOUBLES':17,'TRIPLES':1,'HOMERUNS':12,'RBI':53,'WALKS':25,'STRIKEOUTS':55,},
{'NAME':'Adrian Gonzalez','AGE':35,'TEAM':'LAD','POSITION':'1B','ATBATS':231,'RUNS':14,'HITS':56,'DOUBLES':17,'TRIPLES':0,'HOMERUNS':3,'RBI':30,'WALKS':16,'STRIKEOUTS':43,},
{'NAME':'Jake Marisnick','AGE':26,'TEAM':'HOU','POSITION':'CF','ATBATS':230,'RUNS':50,'HITS':56,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':16,'RBI':35,'WALKS':20,'STRIKEOUTS':90,},
{'NAME':'Austin Romine','AGE':28,'TEAM':'NYY','POSITION':'C','ATBATS':229,'RUNS':19,'HITS':50,'DOUBLES':9,'TRIPLES':1,'HOMERUNS':2,'RBI':21,'WALKS':16,'STRIKEOUTS':57,},
{'NAME':'Tony Wolters','AGE':25,'TEAM':'COL','POSITION':'C','ATBATS':229,'RUNS':30,'HITS':55,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':0,'RBI':16,'WALKS':33,'STRIKEOUTS':55,},
{'NAME':'JT Riddle','AGE':25,'TEAM':'MIA','POSITION':'SS','ATBATS':228,'RUNS':20,'HITS':57,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':3,'RBI':31,'WALKS':12,'STRIKEOUTS':50,},
{'NAME':'Chris Herrmann','AGE':29,'TEAM':'ARI','POSITION':'C','ATBATS':226,'RUNS':35,'HITS':41,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':10,'RBI':27,'WALKS':29,'STRIKEOUTS':67,},
{'NAME':'Gregor Blanco','AGE':33,'TEAM':'ARI','POSITION':'LF','ATBATS':224,'RUNS':43,'HITS':55,'DOUBLES':10,'TRIPLES':3,'HOMERUNS':3,'RBI':13,'WALKS':31,'STRIKEOUTS':59,},
{'NAME':'Ketel Marte','AGE':23,'TEAM':'ARI','POSITION':'SS','ATBATS':223,'RUNS':30,'HITS':58,'DOUBLES':11,'TRIPLES':2,'HOMERUNS':5,'RBI':18,'WALKS':29,'STRIKEOUTS':37,},
{'NAME':'Rafael Devers','AGE':20,'TEAM':'BOS','POSITION':'3B','ATBATS':222,'RUNS':34,'HITS':63,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':10,'RBI':30,'WALKS':18,'STRIKEOUTS':57,},
{'NAME':'Bruce Maxwell','AGE':26,'TEAM':'OAK','POSITION':'C','ATBATS':219,'RUNS':21,'HITS':52,'DOUBLES':12,'TRIPLES':0,'HOMERUNS':3,'RBI':22,'WALKS':31,'STRIKEOUTS':63,},
{'NAME':'Austin Barnes','AGE':27,'TEAM':'LAD','POSITION':'C','ATBATS':218,'RUNS':35,'HITS':63,'DOUBLES':15,'TRIPLES':2,'HOMERUNS':8,'RBI':38,'WALKS':39,'STRIKEOUTS':43,},
{'NAME':'Rene Rivera','AGE':33,'TEAM':'TOT','POSITION':'C','ATBATS':218,'RUNS':23,'HITS':55,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':10,'RBI':35,'WALKS':14,'STRIKEOUTS':70,},
{'NAME':'Daniel Robertson','AGE':23,'TEAM':'TBR','POSITION':'2B','ATBATS':218,'RUNS':22,'HITS':45,'DOUBLES':7,'TRIPLES':2,'HOMERUNS':5,'RBI':19,'WALKS':29,'STRIKEOUTS':73,},
{'NAME':'Michael Saunders','AGE':30,'TEAM':'TOT','POSITION':'RF','ATBATS':218,'RUNS':26,'HITS':44,'DOUBLES':9,'TRIPLES':2,'HOMERUNS':6,'RBI':21,'WALKS':15,'STRIKEOUTS':55,},
{'NAME':'Ozzie Albies','AGE':20,'TEAM':'ATL','POSITION':'2B','ATBATS':217,'RUNS':34,'HITS':62,'DOUBLES':9,'TRIPLES':5,'HOMERUNS':6,'RBI':28,'WALKS':21,'STRIKEOUTS':36,},
{'NAME':'Alen Hanson','AGE':24,'TEAM':'TOT','POSITION':'2B','ATBATS':217,'RUNS':36,'HITS':48,'DOUBLES':9,'TRIPLES':3,'HOMERUNS':4,'RBI':11,'WALKS':12,'STRIKEOUTS':52,},
{'NAME':'Roberto Perez','AGE':28,'TEAM':'CLE','POSITION':'C','ATBATS':217,'RUNS':22,'HITS':45,'DOUBLES':12,'TRIPLES':0,'HOMERUNS':8,'RBI':38,'WALKS':26,'STRIKEOUTS':71,},
{'NAME':'Jose Osuna','AGE':24,'TEAM':'PIT','POSITION':'RF','ATBATS':215,'RUNS':31,'HITS':50,'DOUBLES':13,'TRIPLES':4,'HOMERUNS':7,'RBI':30,'WALKS':9,'STRIKEOUTS':40,},
{'NAME':'T.J. Rivera','AGE':28,'TEAM':'NYM','POSITION':'3B','ATBATS':214,'RUNS':27,'HITS':62,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':5,'RBI':27,'WALKS':9,'STRIKEOUTS':32,},
{'NAME':'Hyun Soo Kim','AGE':29,'TEAM':'TOT','POSITION':'LF','ATBATS':212,'RUNS':20,'HITS':49,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':1,'RBI':14,'WALKS':22,'STRIKEOUTS':46,},
{'NAME':'Wilson Ramos','AGE':29,'TEAM':'TBR','POSITION':'C','ATBATS':208,'RUNS':19,'HITS':54,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':11,'RBI':35,'WALKS':10,'STRIKEOUTS':36,},
{'NAME':'Allen Cordoba','AGE':21,'TEAM':'SDP','POSITION':'LF','ATBATS':202,'RUNS':17,'HITS':42,'DOUBLES':2,'TRIPLES':2,'HOMERUNS':4,'RBI':15,'WALKS':18,'STRIKEOUTS':54,},
{'NAME':'Yoan Moncada','AGE':22,'TEAM':'CHW','POSITION':'2B','ATBATS':199,'RUNS':31,'HITS':46,'DOUBLES':8,'TRIPLES':2,'HOMERUNS':8,'RBI':22,'WALKS':29,'STRIKEOUTS':74,},
{'NAME':'Ichiro Suzuki','AGE':43,'TEAM':'MIA','POSITION':'RF','ATBATS':196,'RUNS':19,'HITS':50,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':3,'RBI':20,'WALKS':17,'STRIKEOUTS':35,},
{'NAME':'Matt Szczur','AGE':27,'TEAM':'TOT','POSITION':'LF','ATBATS':195,'RUNS':28,'HITS':44,'DOUBLES':12,'TRIPLES':2,'HOMERUNS':3,'RBI':18,'WALKS':34,'STRIKEOUTS':44,},
{'NAME':'Cliff Pennington','AGE':33,'TEAM':'LAA','POSITION':'2B','ATBATS':194,'RUNS':23,'HITS':49,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':3,'RBI':21,'WALKS':16,'STRIKEOUTS':58,},
{'NAME':'Kelby Tomlinson','AGE':27,'TEAM':'SFG','POSITION':'3B','ATBATS':194,'RUNS':32,'HITS':50,'DOUBLES':4,'TRIPLES':2,'HOMERUNS':1,'RBI':11,'WALKS':23,'STRIKEOUTS':46,},
{'NAME':'Matt Olson','AGE':23,'TEAM':'OAK','POSITION':'1B','ATBATS':189,'RUNS':33,'HITS':49,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':24,'RBI':45,'WALKS':22,'STRIKEOUTS':60,},
{'NAME':'Peter Bourjos','AGE':30,'TEAM':'TBR','POSITION':'LF','ATBATS':188,'RUNS':27,'HITS':42,'DOUBLES':9,'TRIPLES':3,'HOMERUNS':5,'RBI':15,'WALKS':12,'STRIKEOUTS':53,},
{'NAME':'Elias Diaz','AGE':26,'TEAM':'PIT','POSITION':'C','ATBATS':188,'RUNS':18,'HITS':42,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':1,'RBI':19,'WALKS':11,'STRIKEOUTS':38,},
{'NAME':'Tyler Moore','AGE':30,'TEAM':'MIA','POSITION':'1B','ATBATS':187,'RUNS':17,'HITS':43,'DOUBLES':14,'TRIPLES':0,'HOMERUNS':6,'RBI':30,'WALKS':10,'STRIKEOUTS':56,},
{'NAME':'Chris Gimenez','AGE':34,'TEAM':'MIN','POSITION':'C','ATBATS':186,'RUNS':28,'HITS':41,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':7,'RBI':16,'WALKS':33,'STRIKEOUTS':60,},
{'NAME':'Jeff Mathis','AGE':34,'TEAM':'ARI','POSITION':'C','ATBATS':186,'RUNS':13,'HITS':40,'DOUBLES':10,'TRIPLES':2,'HOMERUNS':2,'RBI':11,'WALKS':14,'STRIKEOUTS':61,},
{'NAME':'Jace Peterson','AGE':27,'TEAM':'ATL','POSITION':'LF','ATBATS':186,'RUNS':15,'HITS':40,'DOUBLES':9,'TRIPLES':2,'HOMERUNS':2,'RBI':17,'WALKS':27,'STRIKEOUTS':48,},
{'NAME':'Miguel Montero','AGE':33,'TEAM':'TOT','POSITION':'C','ATBATS':185,'RUNS':24,'HITS':40,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':6,'RBI':16,'WALKS':23,'STRIKEOUTS':47,},
{'NAME':'Devon Travis','AGE':26,'TEAM':'TOR','POSITION':'2B','ATBATS':185,'RUNS':22,'HITS':48,'DOUBLES':18,'TRIPLES':0,'HOMERUNS':5,'RBI':24,'WALKS':7,'STRIKEOUTS':38,},
{'NAME':'Chris Carter','AGE':30,'TEAM':'NYY','POSITION':'1B','ATBATS':184,'RUNS':20,'HITS':37,'DOUBLES':5,'TRIPLES':1,'HOMERUNS':8,'RBI':26,'WALKS':20,'STRIKEOUTS':76,},
{'NAME':'Daniel Nava','AGE':34,'TEAM':'PHI','POSITION':'LF','ATBATS':183,'RUNS':21,'HITS':55,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':4,'RBI':21,'WALKS':26,'STRIKEOUTS':38,},
{'NAME':'Pat Valaika','AGE':24,'TEAM':'COL','POSITION':'SS','ATBATS':182,'RUNS':28,'HITS':47,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':13,'RBI':40,'WALKS':7,'STRIKEOUTS':53,},
{'NAME':'Derek Norris','AGE':28,'TEAM':'TBR','POSITION':'C','ATBATS':179,'RUNS':21,'HITS':36,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':9,'RBI':24,'WALKS':12,'STRIKEOUTS':48,},
{'NAME':'Patrick Kivlehan','AGE':27,'TEAM':'CIN','POSITION':'RF','ATBATS':178,'RUNS':23,'HITS':37,'DOUBLES':5,'TRIPLES':1,'HOMERUNS':9,'RBI':26,'WALKS':22,'STRIKEOUTS':61,},
{'NAME':'Brandon Nimmo','AGE':24,'TEAM':'NYM','POSITION':'LF','ATBATS':177,'RUNS':26,'HITS':46,'DOUBLES':11,'TRIPLES':1,'HOMERUNS':5,'RBI':21,'WALKS':33,'STRIKEOUTS':60,},
{'NAME':'Jesus Sucre','AGE':29,'TEAM':'TBR','POSITION':'C','ATBATS':176,'RUNS':20,'HITS':45,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':7,'RBI':29,'WALKS':7,'STRIKEOUTS':35,},
{'NAME':'Mark Canha','AGE':28,'TEAM':'OAK','POSITION':'RF','ATBATS':173,'RUNS':16,'HITS':36,'DOUBLES':13,'TRIPLES':1,'HOMERUNS':5,'RBI':14,'WALKS':7,'STRIKEOUTS':56,},
{'NAME':'Adonis Garcia','AGE':32,'TEAM':'ATL','POSITION':'3B','ATBATS':173,'RUNS':19,'HITS':41,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':5,'RBI':19,'WALKS':7,'STRIKEOUTS':23,},
{'NAME':'John Hicks','AGE':27,'TEAM':'DET','POSITION':'1B','ATBATS':173,'RUNS':25,'HITS':46,'DOUBLES':12,'TRIPLES':0,'HOMERUNS':6,'RBI':22,'WALKS':13,'STRIKEOUTS':51,},
{'NAME':'Abraham Almonte','AGE':28,'TEAM':'CLE','POSITION':'RF','ATBATS':172,'RUNS':26,'HITS':40,'DOUBLES':8,'TRIPLES':3,'HOMERUNS':3,'RBI':14,'WALKS':20,'STRIKEOUTS':46,},
{'NAME':'Andrew Knapp','AGE':25,'TEAM':'PHI','POSITION':'C','ATBATS':171,'RUNS':26,'HITS':44,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':3,'RBI':13,'WALKS':31,'STRIKEOUTS':56,},
{'NAME':'Deven Marrero','AGE':26,'TEAM':'BOS','POSITION':'3B','ATBATS':171,'RUNS':32,'HITS':36,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':4,'RBI':27,'WALKS':12,'STRIKEOUTS':61,},
{'NAME':'Rhys Hoskins','AGE':24,'TEAM':'PHI','POSITION':'LF','ATBATS':170,'RUNS':37,'HITS':44,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':18,'RBI':48,'WALKS':37,'STRIKEOUTS':46,},
{'NAME':'Jett Bandy','AGE':27,'TEAM':'MIL','POSITION':'C','ATBATS':169,'RUNS':14,'HITS':35,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':6,'RBI':18,'WALKS':15,'STRIKEOUTS':51,},
{'NAME':'Alexi Amarista','AGE':28,'TEAM':'COL','POSITION':'2B','ATBATS':168,'RUNS':22,'HITS':40,'DOUBLES':10,'TRIPLES':0,'HOMERUNS':3,'RBI':19,'WALKS':7,'STRIKEOUTS':38,},
{'NAME':'Danny Santana','AGE':26,'TEAM':'TOT','POSITION':'LF','ATBATS':168,'RUNS':19,'HITS':34,'DOUBLES':10,'TRIPLES':2,'HOMERUNS':4,'RBI':23,'WALKS':8,'STRIKEOUTS':41,},
{'NAME':'Nick Ahmed','AGE':27,'TEAM':'ARI','POSITION':'SS','ATBATS':167,'RUNS':24,'HITS':42,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':6,'RBI':21,'WALKS':10,'STRIKEOUTS':39,},
{'NAME':'Dominic Smith','AGE':22,'TEAM':'NYM','POSITION':'1B','ATBATS':167,'RUNS':17,'HITS':33,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':9,'RBI':26,'WALKS':14,'STRIKEOUTS':49,},
{'NAME':'Dixon Machado','AGE':25,'TEAM':'DET','POSITION':'SS','ATBATS':166,'RUNS':17,'HITS':43,'DOUBLES':5,'TRIPLES':1,'HOMERUNS':1,'RBI':11,'WALKS':10,'STRIKEOUTS':32,},
{'NAME':'Jarrett Parker','AGE':28,'TEAM':'SFG','POSITION':'LF','ATBATS':166,'RUNS':14,'HITS':41,'DOUBLES':12,'TRIPLES':2,'HOMERUNS':4,'RBI':23,'WALKS':10,'STRIKEOUTS':54,},
{'NAME':'Yasmany Tomas','AGE':26,'TEAM':'ARI','POSITION':'LF','ATBATS':166,'RUNS':19,'HITS':40,'DOUBLES':11,'TRIPLES':1,'HOMERUNS':8,'RBI':32,'WALKS':13,'STRIKEOUTS':50,},
{'NAME':'Brandon Guyer','AGE':31,'TEAM':'CLE','POSITION':'RF','ATBATS':165,'RUNS':23,'HITS':39,'DOUBLES':7,'TRIPLES':1,'HOMERUNS':2,'RBI':20,'WALKS':15,'STRIKEOUTS':43,},
{'NAME':'Amed Rosario','AGE':21,'TEAM':'NYM','POSITION':'SS','ATBATS':165,'RUNS':16,'HITS':41,'DOUBLES':4,'TRIPLES':4,'HOMERUNS':4,'RBI':10,'WALKS':3,'STRIKEOUTS':49,},
{'NAME':'Ryan Schimpf','AGE':29,'TEAM':'SDP','POSITION':'3B','ATBATS':165,'RUNS':24,'HITS':26,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':14,'RBI':25,'WALKS':27,'STRIKEOUTS':70,},
{'NAME':'Jabari Blash','AGE':27,'TEAM':'SDP','POSITION':'RF','ATBATS':164,'RUNS':24,'HITS':35,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':5,'RBI':16,'WALKS':28,'STRIKEOUTS':66,},
{'NAME':'Drew Butera','AGE':33,'TEAM':'KCR','POSITION':'C','ATBATS':163,'RUNS':18,'HITS':37,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':3,'RBI':14,'WALKS':12,'STRIKEOUTS':41,},
{'NAME':'Ehire Adrianza','AGE':27,'TEAM':'MIN','POSITION':'SS','ATBATS':162,'RUNS':30,'HITS':43,'DOUBLES':9,'TRIPLES':2,'HOMERUNS':2,'RBI':24,'WALKS':16,'STRIKEOUTS':25,},
{'NAME':'Raimel Tapia','AGE':23,'TEAM':'COL','POSITION':'RF','ATBATS':160,'RUNS':27,'HITS':46,'DOUBLES':12,'TRIPLES':2,'HOMERUNS':2,'RBI':16,'WALKS':8,'STRIKEOUTS':36,},
{'NAME':'Yandy Diaz','AGE':25,'TEAM':'CLE','POSITION':'3B','ATBATS':156,'RUNS':25,'HITS':41,'DOUBLES':8,'TRIPLES':1,'HOMERUNS':0,'RBI':13,'WALKS':21,'STRIKEOUTS':35,},
{'NAME':'Giovanny Urshela','AGE':25,'TEAM':'CLE','POSITION':'3B','ATBATS':156,'RUNS':14,'HITS':35,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':1,'RBI':15,'WALKS':8,'STRIKEOUTS':22,},
{'NAME':'Tyler Collins','AGE':27,'TEAM':'DET','POSITION':'CF','ATBATS':150,'RUNS':18,'HITS':29,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':5,'RBI':14,'WALKS':18,'STRIKEOUTS':55,},
{'NAME':'Ryder Jones','AGE':23,'TEAM':'SFG','POSITION':'1B','ATBATS':150,'RUNS':12,'HITS':26,'DOUBLES':5,'TRIPLES':2,'HOMERUNS':2,'RBI':5,'WALKS':10,'STRIKEOUTS':52,},
{'NAME':'Rio Ruiz','AGE':23,'TEAM':'ATL','POSITION':'3B','ATBATS':150,'RUNS':22,'HITS':29,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':4,'RBI':19,'WALKS':19,'STRIKEOUTS':41,},
{'NAME':'Josh Phegley','AGE':29,'TEAM':'OAK','POSITION':'C','ATBATS':149,'RUNS':14,'HITS':30,'DOUBLES':11,'TRIPLES':0,'HOMERUNS':3,'RBI':10,'WALKS':9,'STRIKEOUTS':26,},
{'NAME':'Greg Bird','AGE':24,'TEAM':'NYY','POSITION':'1B','ATBATS':147,'RUNS':20,'HITS':28,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':9,'RBI':28,'WALKS':19,'STRIKEOUTS':42,},
{'NAME':'Derek Fisher','AGE':23,'TEAM':'HOU','POSITION':'LF','ATBATS':146,'RUNS':21,'HITS':31,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':5,'RBI':17,'WALKS':17,'STRIKEOUTS':54,},
{'NAME':'Jaycob Brugman','AGE':25,'TEAM':'OAK','POSITION':'CF','ATBATS':143,'RUNS':12,'HITS':38,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':3,'RBI':12,'WALKS':18,'STRIKEOUTS':38,},
{'NAME':'Cheslor Cuthbert','AGE':24,'TEAM':'KCR','POSITION':'3B','ATBATS':143,'RUNS':10,'HITS':33,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':2,'RBI':18,'WALKS':9,'STRIKEOUTS':39,},
{'NAME':'A.J. Ellis','AGE':36,'TEAM':'MIA','POSITION':'C','ATBATS':143,'RUNS':17,'HITS':30,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':6,'RBI':14,'WALKS':12,'STRIKEOUTS':29,},
{'NAME':'Nick Delmonico','AGE':24,'TEAM':'CHW','POSITION':'LF','ATBATS':141,'RUNS':25,'HITS':37,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':9,'RBI':23,'WALKS':23,'STRIKEOUTS':31,},
{'NAME':'JaCoby Jones','AGE':25,'TEAM':'DET','POSITION':'CF','ATBATS':141,'RUNS':14,'HITS':24,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':3,'RBI':13,'WALKS':9,'STRIKEOUTS':65,},
{'NAME':'Jose Lobaton','AGE':32,'TEAM':'WSN','POSITION':'C','ATBATS':141,'RUNS':11,'HITS':24,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':4,'RBI':11,'WALKS':14,'STRIKEOUTS':35,},
{'NAME':'Devin Mesoraco','AGE':29,'TEAM':'CIN','POSITION':'C','ATBATS':141,'RUNS':17,'HITS':30,'DOUBLES':5,'TRIPLES':1,'HOMERUNS':6,'RBI':14,'WALKS':18,'STRIKEOUTS':38,},
{'NAME':'Brock Holt','AGE':29,'TEAM':'BOS','POSITION':'2B','ATBATS':140,'RUNS':20,'HITS':28,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':0,'RBI':7,'WALKS':19,'STRIKEOUTS':34,},
{'NAME':'Martin Prado','AGE':33,'TEAM':'MIA','POSITION':'3B','ATBATS':140,'RUNS':13,'HITS':35,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':2,'RBI':12,'WALKS':6,'STRIKEOUTS':22,},
{'NAME':'Hector Sanchez','AGE':27,'TEAM':'SDP','POSITION':'C','ATBATS':137,'RUNS':14,'HITS':30,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':8,'RBI':25,'WALKS':5,'STRIKEOUTS':41,},
{'NAME':'Rey Fuentes','AGE':26,'TEAM':'ARI','POSITION':'CF','ATBATS':136,'RUNS':19,'HITS':32,'DOUBLES':1,'TRIPLES':2,'HOMERUNS':3,'RBI':9,'WALKS':8,'STRIKEOUTS':35,},
{'NAME':'Clint Frazier','AGE':22,'TEAM':'NYY','POSITION':'LF','ATBATS':134,'RUNS':16,'HITS':31,'DOUBLES':9,'TRIPLES':4,'HOMERUNS':4,'RBI':17,'WALKS':7,'STRIKEOUTS':43,},
{'NAME':'Sean Rodriguez','AGE':32,'TEAM':'TOT','POSITION':'3B','ATBATS':132,'RUNS':18,'HITS':22,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':5,'RBI':8,'WALKS':16,'STRIKEOUTS':57,},
{'NAME':'Chris Stewart','AGE':35,'TEAM':'PIT','POSITION':'C','ATBATS':131,'RUNS':8,'HITS':24,'DOUBLES':1,'TRIPLES':2,'HOMERUNS':0,'RBI':4,'WALKS':9,'STRIKEOUTS':22,},
{'NAME':'Andres Blanco','AGE':33,'TEAM':'PHI','POSITION':'3B','ATBATS':130,'RUNS':10,'HITS':25,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':3,'RBI':13,'WALKS':12,'STRIKEOUTS':34,},
{'NAME':'Luke Maile','AGE':26,'TEAM':'TOR','POSITION':'C','ATBATS':130,'RUNS':10,'HITS':19,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':2,'RBI':7,'WALKS':3,'STRIKEOUTS':35,},
{'NAME':'Ryan Rua','AGE':27,'TEAM':'TEX','POSITION':'LF','ATBATS':129,'RUNS':17,'HITS':28,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':3,'RBI':12,'WALKS':14,'STRIKEOUTS':52,},
{'NAME':'Leonys Martin','AGE':29,'TEAM':'TOT','POSITION':'CF','ATBATS':128,'RUNS':14,'HITS':22,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':3,'RBI':9,'WALKS':8,'STRIKEOUTS':33,},
{'NAME':'Jeimer Candelario','AGE':23,'TEAM':'TOT','POSITION':'3B','ATBATS':127,'RUNS':18,'HITS':36,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':3,'RBI':16,'WALKS':13,'STRIKEOUTS':30,},
{'NAME':'Jefry Marte','AGE':26,'TEAM':'LAA','POSITION':'1B','ATBATS':127,'RUNS':10,'HITS':22,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':4,'RBI':14,'WALKS':13,'STRIKEOUTS':34,},
{'NAME':'Christian Arroyo','AGE':22,'TEAM':'SFG','POSITION':'3B','ATBATS':125,'RUNS':9,'HITS':24,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':3,'RBI':14,'WALKS':8,'STRIKEOUTS':32,},
{'NAME':'Tommy La Stella','AGE':28,'TEAM':'CHC','POSITION':'2B','ATBATS':125,'RUNS':18,'HITS':36,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':5,'RBI':22,'WALKS':20,'STRIKEOUTS':18,},
{'NAME':'Carlos Ruiz','AGE':38,'TEAM':'SEA','POSITION':'C','ATBATS':125,'RUNS':14,'HITS':27,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':3,'RBI':11,'WALKS':14,'STRIKEOUTS':38,},
{'NAME':'Luis Torrens','AGE':21,'TEAM':'SDP','POSITION':'C','ATBATS':123,'RUNS':7,'HITS':20,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':0,'RBI':7,'WALKS':12,'STRIKEOUTS':30,},
{'NAME':'Colby Rasmus','AGE':30,'TEAM':'TBR','POSITION':'LF','ATBATS':121,'RUNS':17,'HITS':34,'DOUBLES':7,'TRIPLES':1,'HOMERUNS':9,'RBI':23,'WALKS':7,'STRIKEOUTS':45,},
{'NAME':'Jesse Winker','AGE':23,'TEAM':'CIN','POSITION':'RF','ATBATS':121,'RUNS':21,'HITS':36,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':7,'RBI':15,'WALKS':15,'STRIKEOUTS':24,},
{'NAME':'Max Moroff','AGE':24,'TEAM':'PIT','POSITION':'2B','ATBATS':120,'RUNS':19,'HITS':24,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':3,'RBI':21,'WALKS':16,'STRIKEOUTS':43,},
{'NAME':'Boog Powell','AGE':24,'TEAM':'TOT','POSITION':'CF','ATBATS':117,'RUNS':24,'HITS':33,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':3,'RBI':12,'WALKS':15,'STRIKEOUTS':30,},
{'NAME':'Austin Slater','AGE':24,'TEAM':'SFG','POSITION':'LF','ATBATS':117,'RUNS':15,'HITS':33,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':3,'RBI':16,'WALKS':8,'STRIKEOUTS':29,},
{'NAME':'Luke Voit','AGE':26,'TEAM':'STL','POSITION':'1B','ATBATS':114,'RUNS':18,'HITS':28,'DOUBLES':9,'TRIPLES':0,'HOMERUNS':4,'RBI':18,'WALKS':7,'STRIKEOUTS':31,},
{'NAME':'Matt Reynolds','AGE':26,'TEAM':'NYM','POSITION':'3B','ATBATS':113,'RUNS':12,'HITS':26,'DOUBLES':1,'TRIPLES':2,'HOMERUNS':1,'RBI':5,'WALKS':14,'STRIKEOUTS':37,},
{'NAME':'Ruben Tejada','AGE':27,'TEAM':'BAL','POSITION':'SS','ATBATS':113,'RUNS':17,'HITS':26,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':8,'STRIKEOUTS':15,},
{'NAME':'Dustin Garneau','AGE':29,'TEAM':'TOT','POSITION':'C','ATBATS':112,'RUNS':10,'HITS':21,'DOUBLES':8,'TRIPLES':0,'HOMERUNS':2,'RBI':9,'WALKS':12,'STRIKEOUTS':36,},
{'NAME':'Erik Gonzalez','AGE':25,'TEAM':'CLE','POSITION':'2B','ATBATS':110,'RUNS':18,'HITS':28,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':4,'RBI':11,'WALKS':3,'STRIKEOUTS':37,},
{'NAME':'Eric Young','AGE':32,'TEAM':'LAA','POSITION':'LF','ATBATS':110,'RUNS':24,'HITS':29,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':4,'RBI':16,'WALKS':5,'STRIKEOUTS':31,},
{'NAME':'Lane Adams','AGE':27,'TEAM':'ATL','POSITION':'LF','ATBATS':109,'RUNS':19,'HITS':30,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':5,'RBI':20,'WALKS':10,'STRIKEOUTS':37,},
{'NAME':'Jorge Alfaro','AGE':24,'TEAM':'PHI','POSITION':'C','ATBATS':107,'RUNS':12,'HITS':34,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':5,'RBI':14,'WALKS':3,'STRIKEOUTS':33,},
{'NAME':'Drew Robinson','AGE':25,'TEAM':'TEX','POSITION':'3B','ATBATS':107,'RUNS':11,'HITS':24,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':6,'RBI':13,'WALKS':14,'STRIKEOUTS':42,},
{'NAME':'Josh Rutledge','AGE':28,'TEAM':'BOS','POSITION':'3B','ATBATS':107,'RUNS':10,'HITS':24,'DOUBLES':2,'TRIPLES':1,'HOMERUNS':0,'RBI':9,'WALKS':9,'STRIKEOUTS':31,},
{'NAME':'Nick Franklin','AGE':26,'TEAM':'TOT','POSITION':'LF','ATBATS':106,'RUNS':9,'HITS':19,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':2,'RBI':12,'WALKS':10,'STRIKEOUTS':22,},
{'NAME':'Arismendy Alcantara','AGE':25,'TEAM':'CIN','POSITION':'2B','ATBATS':105,'RUNS':13,'HITS':18,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':1,'RBI':7,'WALKS':2,'STRIKEOUTS':38,},
{'NAME':'Willy Garcia','AGE':24,'TEAM':'CHW','POSITION':'RF','ATBATS':105,'RUNS':15,'HITS':25,'DOUBLES':5,'TRIPLES':3,'HOMERUNS':2,'RBI':12,'WALKS':11,'STRIKEOUTS':31,},
{'NAME':'Tomas Telis','AGE':26,'TEAM':'MIA','POSITION':'1B','ATBATS':104,'RUNS':13,'HITS':25,'DOUBLES':5,'TRIPLES':3,'HOMERUNS':0,'RBI':9,'WALKS':3,'STRIKEOUTS':10,},
{'NAME':'Kaleb Cowart','AGE':25,'TEAM':'LAA','POSITION':'2B','ATBATS':102,'RUNS':18,'HITS':23,'DOUBLES':5,'TRIPLES':1,'HOMERUNS':3,'RBI':11,'WALKS':10,'STRIKEOUTS':28,},
{'NAME':'Craig Gentry','AGE':33,'TEAM':'BAL','POSITION':'RF','ATBATS':101,'RUNS':17,'HITS':26,'DOUBLES':5,'TRIPLES':1,'HOMERUNS':2,'RBI':11,'WALKS':11,'STRIKEOUTS':24,},
{'NAME':'Ryan Hanigan','AGE':36,'TEAM':'COL','POSITION':'C','ATBATS':101,'RUNS':9,'HITS':27,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':2,'RBI':12,'WALKS':8,'STRIKEOUTS':26,},
{'NAME':'Kevin Plawecki','AGE':26,'TEAM':'NYM','POSITION':'C','ATBATS':100,'RUNS':11,'HITS':26,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':3,'RBI':13,'WALKS':14,'STRIKEOUTS':17,},
{'NAME':'Jorge Soler','AGE':25,'TEAM':'KCR','POSITION':'RF','ATBATS':97,'RUNS':7,'HITS':14,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':2,'RBI':6,'WALKS':12,'STRIKEOUTS':36,},
{'NAME':'Rickie Weeks','AGE':34,'TEAM':'TBR','POSITION':'DH','ATBATS':97,'RUNS':13,'HITS':21,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':2,'RBI':8,'WALKS':12,'STRIKEOUTS':49,},
{'NAME':'Andrew Toles','AGE':25,'TEAM':'LAD','POSITION':'LF','ATBATS':96,'RUNS':17,'HITS':26,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':5,'RBI':15,'WALKS':5,'STRIKEOUTS':16,},
{'NAME':'Stephen Drew','AGE':34,'TEAM':'WSN','POSITION':'SS','ATBATS':95,'RUNS':9,'HITS':24,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':1,'RBI':17,'WALKS':8,'STRIKEOUTS':21,},
{'NAME':'Zack Granite','AGE':24,'TEAM':'MIN','POSITION':'CF','ATBATS':93,'RUNS':14,'HITS':22,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':13,'WALKS':12,'STRIKEOUTS':9,},
{'NAME':'Franchy Cordero','AGE':22,'TEAM':'SDP','POSITION':'CF','ATBATS':92,'RUNS':15,'HITS':21,'DOUBLES':3,'TRIPLES':3,'HOMERUNS':3,'RBI':9,'WALKS':6,'STRIKEOUTS':44,},
{'NAME':'Adam Eaton','AGE':28,'TEAM':'WSN','POSITION':'CF','ATBATS':91,'RUNS':24,'HITS':27,'DOUBLES':7,'TRIPLES':1,'HOMERUNS':2,'RBI':13,'WALKS':14,'STRIKEOUTS':18,},
{'NAME':'Ty Kelly','AGE':28,'TEAM':'TOT','POSITION':'2B','ATBATS':89,'RUNS':11,'HITS':17,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':2,'RBI':14,'WALKS':8,'STRIKEOUTS':25,},
{'NAME':'Teoscar Hernandez','AGE':24,'TEAM':'TOT','POSITION':'LF','ATBATS':88,'RUNS':16,'HITS':23,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':8,'RBI':20,'WALKS':6,'STRIKEOUTS':36,},
{'NAME':'Cameron Perkins','AGE':26,'TEAM':'PHI','POSITION':'LF','ATBATS':88,'RUNS':9,'HITS':16,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':1,'RBI':8,'WALKS':5,'STRIKEOUTS':23,},
{'NAME':'Rob Refsnyder','AGE':26,'TEAM':'TOT','POSITION':'2B','ATBATS':88,'RUNS':8,'HITS':15,'DOUBLES':2,'TRIPLES':1,'HOMERUNS':0,'RBI':0,'WALKS':8,'STRIKEOUTS':17,},
{'NAME':'Brett Phillips','AGE':23,'TEAM':'MIL','POSITION':'CF','ATBATS':87,'RUNS':9,'HITS':24,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':4,'RBI':12,'WALKS':9,'STRIKEOUTS':34,},
{'NAME':'Mike Aviles','AGE':36,'TEAM':'MIA','POSITION':'SS','ATBATS':86,'RUNS':5,'HITS':20,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':8,'WALKS':6,'STRIKEOUTS':15,},
{'NAME':'Paulo Orlando','AGE':31,'TEAM':'KCR','POSITION':'RF','ATBATS':86,'RUNS':9,'HITS':17,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':2,'RBI':6,'WALKS':1,'STRIKEOUTS':20,},
{'NAME':'Harrison Bader','AGE':23,'TEAM':'STL','POSITION':'CF','ATBATS':85,'RUNS':10,'HITS':20,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':3,'RBI':10,'WALKS':5,'STRIKEOUTS':24,},
{'NAME':'Brian Anderson','AGE':24,'TEAM':'MIA','POSITION':'3B','ATBATS':84,'RUNS':11,'HITS':22,'DOUBLES':7,'TRIPLES':1,'HOMERUNS':0,'RBI':8,'WALKS':10,'STRIKEOUTS':28,},
{'NAME':'Juan Graterol','AGE':28,'TEAM':'LAA','POSITION':'C','ATBATS':84,'RUNS':5,'HITS':17,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':0,'RBI':10,'WALKS':1,'STRIKEOUTS':13,},
{'NAME':'Jim Adduci','AGE':32,'TEAM':'DET','POSITION':'RF','ATBATS':83,'RUNS':14,'HITS':20,'DOUBLES':6,'TRIPLES':2,'HOMERUNS':1,'RBI':10,'WALKS':10,'STRIKEOUTS':27,},
{'NAME':'Stuart Turner','AGE':25,'TEAM':'CIN','POSITION':'C','ATBATS':82,'RUNS':4,'HITS':11,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':2,'RBI':7,'WALKS':5,'STRIKEOUTS':22,},
{'NAME':'Conor Gillaspie','AGE':29,'TEAM':'SFG','POSITION':'3B','ATBATS':80,'RUNS':8,'HITS':13,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':2,'RBI':8,'WALKS':5,'STRIKEOUTS':10,},
{'NAME':'Daniel Robertson','AGE':31,'TEAM':'CLE','POSITION':'RF','ATBATS':80,'RUNS':9,'HITS':18,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':1,'RBI':7,'WALKS':7,'STRIKEOUTS':3,},
{'NAME':'Shane Peterson','AGE':29,'TEAM':'TBR','POSITION':'LF','ATBATS':79,'RUNS':9,'HITS':20,'DOUBLES':5,'TRIPLES':0,'HOMERUNS':2,'RBI':11,'WALKS':5,'STRIKEOUTS':21,},
{'NAME':'Jordan Luplow','AGE':23,'TEAM':'PIT','POSITION':'RF','ATBATS':78,'RUNS':6,'HITS':16,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':3,'RBI':11,'WALKS':6,'STRIKEOUTS':22,},
{'NAME':'Brock Stassi','AGE':27,'TEAM':'PHI','POSITION':'1B','ATBATS':78,'RUNS':6,'HITS':13,'DOUBLES':2,'TRIPLES':1,'HOMERUNS':2,'RBI':7,'WALKS':12,'STRIKEOUTS':22,},
{'NAME':'Gavin Cecchini','AGE':23,'TEAM':'NYM','POSITION':'2B','ATBATS':77,'RUNS':4,'HITS':16,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':4,'STRIKEOUTS':19,},
{'NAME':'Sam Travis','AGE':23,'TEAM':'BOS','POSITION':'1B','ATBATS':76,'RUNS':13,'HITS':20,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':6,'STRIKEOUTS':23,},
{'NAME':'Chris Coghlan','AGE':32,'TEAM':'TOR','POSITION':'3B','ATBATS':75,'RUNS':7,'HITS':15,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':9,'STRIKEOUTS':22,},
{'NAME':'Travis Jankowski','AGE':26,'TEAM':'SDP','POSITION':'LF','ATBATS':75,'RUNS':10,'HITS':14,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':9,'STRIKEOUTS':28,},
{'NAME':'Chris Heisey','AGE':32,'TEAM':'WSN','POSITION':'LF','ATBATS':74,'RUNS':8,'HITS':12,'DOUBLES':3,'TRIPLES':1,'HOMERUNS':1,'RBI':5,'WALKS':5,'STRIKEOUTS':22,},
{'NAME':'Ramon Torres','AGE':24,'TEAM':'KCR','POSITION':'2B','ATBATS':74,'RUNS':9,'HITS':18,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':4,'STRIKEOUTS':12,},
{'NAME':'Jared Hoying','AGE':28,'TEAM':'TEX','POSITION':'CF','ATBATS':72,'RUNS':13,'HITS':16,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':4,'STRIKEOUTS':23,},
{'NAME':'Franklin Barreto','AGE':21,'TEAM':'OAK','POSITION':'SS','ATBATS':71,'RUNS':10,'HITS':14,'DOUBLES':1,'TRIPLES':2,'HOMERUNS':2,'RBI':6,'WALKS':5,'STRIKEOUTS':33,},
{'NAME':'Jacob deGrom','AGE':29,'TEAM':'NYM','POSITION':'P','ATBATS':71,'RUNS':6,'HITS':15,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':2,'STRIKEOUTS':22,},
{'NAME':'Eric Fryer','AGE':31,'TEAM':'STL','POSITION':'C','ATBATS':71,'RUNS':7,'HITS':11,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':11,'STRIKEOUTS':18,},
{'NAME':'Adrian Sanchez','AGE':26,'TEAM':'WSN','POSITION':'2B','ATBATS':71,'RUNS':6,'HITS':19,'DOUBLES':7,'TRIPLES':0,'HOMERUNS':0,'RBI':11,'WALKS':1,'STRIKEOUTS':25,},
{'NAME':'J.P. Crawford','AGE':22,'TEAM':'PHI','POSITION':'3B','ATBATS':70,'RUNS':8,'HITS':15,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':0,'RBI':6,'WALKS':16,'STRIKEOUTS':22,},
{'NAME':'Carson Kelly','AGE':22,'TEAM':'STL','POSITION':'C','ATBATS':69,'RUNS':5,'HITS':12,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':6,'WALKS':5,'STRIKEOUTS':11,},
{'NAME':'Aaron Hill','AGE':35,'TEAM':'SFG','POSITION':'NONE','ATBATS':68,'RUNS':7,'HITS':9,'DOUBLES':2,'TRIPLES':1,'HOMERUNS':1,'RBI':7,'WALKS':11,'STRIKEOUTS':13,},
{'NAME':'Richard Urena','AGE':21,'TEAM':'TOR','POSITION':'SS','ATBATS':68,'RUNS':6,'HITS':14,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':6,'STRIKEOUTS':28,},
{'NAME':'Mac Williamson','AGE':26,'TEAM':'SFG','POSITION':'RF','ATBATS':68,'RUNS':8,'HITS':16,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':3,'RBI':6,'WALKS':5,'STRIKEOUTS':25,},
{'NAME':'Dusty Coleman','AGE':30,'TEAM':'SDP','POSITION':'SS','ATBATS':66,'RUNS':6,'HITS':15,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':4,'RBI':9,'WALKS':2,'STRIKEOUTS':33,},
{'NAME':'Gio Gonzalez','AGE':31,'TEAM':'WSN','POSITION':'P','ATBATS':66,'RUNS':3,'HITS':6,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':4,'STRIKEOUTS':29,},
{'NAME':'Ryan Raburn','AGE':36,'TEAM':'WSN','POSITION':'LF','ATBATS':65,'RUNS':7,'HITS':17,'DOUBLES':1,'TRIPLES':2,'HOMERUNS':2,'RBI':6,'WALKS':4,'STRIKEOUTS':25,},
{'NAME':'Jeff Samardzija','AGE':32,'TEAM':'SFG','POSITION':'P','ATBATS':64,'RUNS':3,'HITS':6,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':0,'STRIKEOUTS':25,},
{'NAME':'Brett Nicholas','AGE':28,'TEAM':'TEX','POSITION':'C','ATBATS':63,'RUNS':7,'HITS':15,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':2,'RBI':11,'WALKS':2,'STRIKEOUTS':13,},
{'NAME':'J.D. Davis','AGE':24,'TEAM':'HOU','POSITION':'3B','ATBATS':62,'RUNS':8,'HITS':14,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':4,'RBI':7,'WALKS':4,'STRIKEOUTS':20,},
{'NAME':'Alejandro De Aza','AGE':33,'TEAM':'WSN','POSITION':'RF','ATBATS':62,'RUNS':8,'HITS':12,'DOUBLES':2,'TRIPLES':3,'HOMERUNS':0,'RBI':9,'WALKS':3,'STRIKEOUTS':16,},
{'NAME':'Zack Greinke','AGE':33,'TEAM':'ARI','POSITION':'P','ATBATS':62,'RUNS':4,'HITS':13,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':2,'STRIKEOUTS':18,},
{'NAME':'Carlos Martinez','AGE':25,'TEAM':'STL','POSITION':'P','ATBATS':62,'RUNS':5,'HITS':11,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':11,'WALKS':1,'STRIKEOUTS':19,},
{'NAME':'Max Scherzer','AGE':32,'TEAM':'WSN','POSITION':'P','ATBATS':62,'RUNS':4,'HITS':10,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':4,'STRIKEOUTS':16,},
{'NAME':'Jake Arrieta','AGE':31,'TEAM':'CHC','POSITION':'P','ATBATS':61,'RUNS':2,'HITS':8,'DOUBLES':0,'TRIPLES':1,'HOMERUNS':1,'RBI':5,'WALKS':1,'STRIKEOUTS':32,},
{'NAME':'R.A. Dickey','AGE':42,'TEAM':'ATL','POSITION':'P','ATBATS':61,'RUNS':0,'HITS':9,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':0,'STRIKEOUTS':12,},
{'NAME':'Efren Navarro','AGE':31,'TEAM':'DET','POSITION':'1B','ATBATS':61,'RUNS':9,'HITS':14,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':2,'RBI':2,'WALKS':8,'STRIKEOUTS':21,},
{'NAME':'Tyler White','AGE':26,'TEAM':'HOU','POSITION':'1B','ATBATS':61,'RUNS':7,'HITS':17,'DOUBLES':6,'TRIPLES':0,'HOMERUNS':3,'RBI':10,'WALKS':4,'STRIKEOUTS':16,},
{'NAME':'Mike Freeman','AGE':29,'TEAM':'TOT','POSITION':'SS','ATBATS':60,'RUNS':6,'HITS':6,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':1,'WALKS':6,'STRIKEOUTS':19,},
{'NAME':'Austin Hays','AGE':21,'TEAM':'BAL','POSITION':'RF','ATBATS':60,'RUNS':4,'HITS':13,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':8,'WALKS':2,'STRIKEOUTS':16,},
{'NAME':'Justin Ruggiano','AGE':35,'TEAM':'SFG','POSITION':'RF','ATBATS':60,'RUNS':2,'HITS':13,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':2,'RBI':4,'WALKS':1,'STRIKEOUTS':17,},
{'NAME':'Magneuris Sierra','AGE':21,'TEAM':'STL','POSITION':'NONE','ATBATS':60,'RUNS':10,'HITS':19,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':4,'STRIKEOUTS':14,},
{'NAME':'Victor Caratini','AGE':23,'TEAM':'CHC','POSITION':'C','ATBATS':59,'RUNS':6,'HITS':15,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':4,'STRIKEOUTS':13,},
{'NAME':'Chase d''Arnaud','AGE':30,'TEAM':'TOT','POSITION':'SS','ATBATS':58,'RUNS':12,'HITS':11,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':4,'STRIKEOUTS':20,},
{'NAME':'Phil Ervin','AGE':24,'TEAM':'CIN','POSITION':'NONE','ATBATS':58,'RUNS':8,'HITS':15,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':3,'RBI':10,'WALKS':4,'STRIKEOUTS':15,},
{'NAME':'Marco Hernandez','AGE':24,'TEAM':'BOS','POSITION':'NONE','ATBATS':58,'RUNS':7,'HITS':16,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':15,},
{'NAME':'Jurickson Profar','AGE':24,'TEAM':'TEX','POSITION':'LF','ATBATS':58,'RUNS':8,'HITS':10,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':9,'STRIKEOUTS':14,},
{'NAME':'Tyler Wade','AGE':22,'TEAM':'NYY','POSITION':'2B','ATBATS':58,'RUNS':7,'HITS':9,'DOUBLES':4,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':5,'STRIKEOUTS':19,},
{'NAME':'Cody Asche','AGE':27,'TEAM':'CHW','POSITION':'DH','ATBATS':57,'RUNS':5,'HITS':6,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':3,'STRIKEOUTS':21,},
{'NAME':'Jimmy Nelson','AGE':28,'TEAM':'MIL','POSITION':'P','ATBATS':57,'RUNS':0,'HITS':6,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':35,},
{'NAME':'Clayton Richard','AGE':33,'TEAM':'SDP','POSITION':'P','ATBATS':57,'RUNS':2,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':1,'STRIKEOUTS':31,},
{'NAME':'Andrew Stevenson','AGE':23,'TEAM':'WSN','POSITION':'RF','ATBATS':57,'RUNS':5,'HITS':9,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':7,'STRIKEOUTS':20,},
{'NAME':'Julio Teheran','AGE':26,'TEAM':'ATL','POSITION':'P','ATBATS':57,'RUNS':4,'HITS':8,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':6,'WALKS':1,'STRIKEOUTS':17,},
{'NAME':'Patrick Corbin','AGE':27,'TEAM':'ARI','POSITION':'P','ATBATS':56,'RUNS':6,'HITS':7,'DOUBLES':0,'TRIPLES':1,'HOMERUNS':0,'RBI':0,'WALKS':6,'STRIKEOUTS':28,},
{'NAME':'Franklin Gutierrez','AGE':34,'TEAM':'LAD','POSITION':'LF','ATBATS':56,'RUNS':8,'HITS':13,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':8,'WALKS':7,'STRIKEOUTS':16,},
{'NAME':'Tzu-Wei Lin','AGE':23,'TEAM':'BOS','POSITION':'2B','ATBATS':56,'RUNS':7,'HITS':15,'DOUBLES':0,'TRIPLES':2,'HOMERUNS':0,'RBI':2,'WALKS':9,'STRIKEOUTS':17,},
{'NAME':'Gerrit Cole','AGE':26,'TEAM':'PIT','POSITION':'P','ATBATS':55,'RUNS':3,'HITS':9,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':1,'STRIKEOUTS':21,},
{'NAME':'Tanner Roark','AGE':30,'TEAM':'WSN','POSITION':'P','ATBATS':55,'RUNS':1,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':22,},
{'NAME':'Dan Straily','AGE':28,'TEAM':'MIA','POSITION':'P','ATBATS':55,'RUNS':2,'HITS':4,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':33,},
{'NAME':'Jhoulys Chacin','AGE':29,'TEAM':'SDP','POSITION':'P','ATBATS':54,'RUNS':0,'HITS':12,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':0,'STRIKEOUTS':11,},
{'NAME':'Jon Lester','AGE':33,'TEAM':'CHC','POSITION':'P','ATBATS':54,'RUNS':5,'HITS':8,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':1,'RBI':6,'WALKS':4,'STRIKEOUTS':26,},
{'NAME':'Rafael Lopez','AGE':29,'TEAM':'TOR','POSITION':'C','ATBATS':54,'RUNS':9,'HITS':12,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':4,'RBI':12,'WALKS':7,'STRIKEOUTS':21,},
{'NAME':'Lance Lynn','AGE':30,'TEAM':'STL','POSITION':'P','ATBATS':54,'RUNS':2,'HITS':4,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':25,},
{'NAME':'Gift Ngoepe','AGE':27,'TEAM':'PIT','POSITION':'2B','ATBATS':54,'RUNS':10,'HITS':12,'DOUBLES':2,'TRIPLES':1,'HOMERUNS':0,'RBI':6,'WALKS':8,'STRIKEOUTS':26,},
{'NAME':'Jhonny Peralta','AGE':35,'TEAM':'STL','POSITION':'3B','ATBATS':54,'RUNS':3,'HITS':11,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':4,'STRIKEOUTS':13,},
{'NAME':'Stephen Strasburg','AGE':28,'TEAM':'WSN','POSITION':'P','ATBATS':54,'RUNS':5,'HITS':7,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':2,'RBI':3,'WALKS':2,'STRIKEOUTS':14,},
{'NAME':'John Lackey','AGE':38,'TEAM':'CHC','POSITION':'P','ATBATS':53,'RUNS':2,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':3,'STRIKEOUTS':23,},
{'NAME':'Adalberto Mondesi','AGE':21,'TEAM':'KCR','POSITION':'2B','ATBATS':53,'RUNS':4,'HITS':9,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':3,'STRIKEOUTS':22,},
{'NAME':'Robbie Ray','AGE':25,'TEAM':'ARI','POSITION':'P','ATBATS':53,'RUNS':5,'HITS':13,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':3,'STRIKEOUTS':23,},
{'NAME':'Chase Anderson','AGE':29,'TEAM':'MIL','POSITION':'P','ATBATS':52,'RUNS':1,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':0,'STRIKEOUTS':29,},
{'NAME':'Juan Centeno','AGE':27,'TEAM':'HOU','POSITION':'C','ATBATS':52,'RUNS':5,'HITS':12,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':2,'RBI':4,'WALKS':4,'STRIKEOUTS':12,},
{'NAME':'Kyle Freeland','AGE':24,'TEAM':'COL','POSITION':'P','ATBATS':52,'RUNS':3,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':1,'STRIKEOUTS':30,},
{'NAME':'Jeremy Hazelbaker','AGE':29,'TEAM':'ARI','POSITION':'LF','ATBATS':52,'RUNS':10,'HITS':18,'DOUBLES':2,'TRIPLES':2,'HOMERUNS':2,'RBI':10,'WALKS':9,'STRIKEOUTS':20,},
{'NAME':'Jae-gyun Hwang','AGE':29,'TEAM':'SFG','POSITION':'3B','ATBATS':52,'RUNS':2,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':5,'STRIKEOUTS':15,},
{'NAME':'Travis Taijeron','AGE':28,'TEAM':'NYM','POSITION':'RF','ATBATS':52,'RUNS':3,'HITS':9,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':5,'STRIKEOUTS':24,},
{'NAME':'Taijuan Walker','AGE':24,'TEAM':'ARI','POSITION':'P','ATBATS':52,'RUNS':6,'HITS':12,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':1,'STRIKEOUTS':19,},
{'NAME':'Alex Wood','AGE':26,'TEAM':'LAD','POSITION':'P','ATBATS':52,'RUNS':1,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':2,'STRIKEOUTS':29,},
{'NAME':'Ivan Nova','AGE':30,'TEAM':'PIT','POSITION':'P','ATBATS':51,'RUNS':0,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':31,},
{'NAME':'Christian Colon','AGE':28,'TEAM':'TOT','POSITION':'2B','ATBATS':50,'RUNS':4,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':5,'STRIKEOUTS':10,},
{'NAME':'Jaff Decker','AGE':27,'TEAM':'OAK','POSITION':'CF','ATBATS':50,'RUNS':4,'HITS':10,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':0,'RBI':1,'WALKS':8,'STRIKEOUTS':17,},
{'NAME':'Kyle Hendricks','AGE':27,'TEAM':'CHC','POSITION':'P','ATBATS':50,'RUNS':3,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':0,'STRIKEOUTS':28,},
{'NAME':'Orlando Calixte','AGE':25,'TEAM':'SFG','POSITION':'NONE','ATBATS':49,'RUNS':5,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':6,'WALKS':3,'STRIKEOUTS':16,},
{'NAME':'Clayton Kershaw','AGE':29,'TEAM':'LAD','POSITION':'P','ATBATS':49,'RUNS':6,'HITS':9,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':4,'STRIKEOUTS':13,},
{'NAME':'Luis Sardinas','AGE':24,'TEAM':'SDP','POSITION':'NONE','ATBATS':49,'RUNS':3,'HITS':8,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':4,'STRIKEOUTS':11,},
{'NAME':'Trayce Thompson','AGE':26,'TEAM':'LAD','POSITION':'NONE','ATBATS':49,'RUNS':6,'HITS':6,'DOUBLES':2,'TRIPLES':1,'HOMERUNS':1,'RBI':2,'WALKS':6,'STRIKEOUTS':23,},
{'NAME':'Zach Davies','AGE':24,'TEAM':'MIL','POSITION':'P','ATBATS':48,'RUNS':7,'HITS':6,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':7,'STRIKEOUTS':15,},
{'NAME':'Philip Gosselin','AGE':28,'TEAM':'TOT','POSITION':'2B','ATBATS':48,'RUNS':3,'HITS':7,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':2,'STRIKEOUTS':12,},
{'NAME':'Chad Kuhl','AGE':24,'TEAM':'PIT','POSITION':'P','ATBATS':48,'RUNS':2,'HITS':5,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':16,},
{'NAME':'Aaron Nola','AGE':24,'TEAM':'PHI','POSITION':'P','ATBATS':48,'RUNS':3,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':4,'STRIKEOUTS':25,},
{'NAME':'Jose Urena','AGE':25,'TEAM':'MIA','POSITION':'P','ATBATS':48,'RUNS':3,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':28,},
{'NAME':'Lewis Brinson','AGE':23,'TEAM':'MIL','POSITION':'NONE','ATBATS':47,'RUNS':2,'HITS':5,'DOUBLES':0,'TRIPLES':1,'HOMERUNS':2,'RBI':3,'WALKS':7,'STRIKEOUTS':17,},
{'NAME':'Mike Leake','AGE':29,'TEAM':'TOT','POSITION':'P','ATBATS':47,'RUNS':2,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':3,'STRIKEOUTS':15,},
{'NAME':'Matt Moore','AGE':28,'TEAM':'SFG','POSITION':'P','ATBATS':47,'RUNS':3,'HITS':6,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':2,'STRIKEOUTS':19,},
{'NAME':'Johnny Cueto','AGE':31,'TEAM':'SFG','POSITION':'P','ATBATS':46,'RUNS':3,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':15,},
{'NAME':'Pedro Florimon','AGE':30,'TEAM':'PHI','POSITION':'NONE','ATBATS':46,'RUNS':6,'HITS':16,'DOUBLES':4,'TRIPLES':1,'HOMERUNS':0,'RBI':6,'WALKS':3,'STRIKEOUTS':16,},
{'NAME':'Mitch Garver','AGE':26,'TEAM':'MIN','POSITION':'C','ATBATS':46,'RUNS':5,'HITS':9,'DOUBLES':1,'TRIPLES':3,'HOMERUNS':0,'RBI':3,'WALKS':6,'STRIKEOUTS':15,},
{'NAME':'Alex Mejia','AGE':26,'TEAM':'STL','POSITION':'3B','ATBATS':46,'RUNS':6,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':2,'STRIKEOUTS':13,},
{'NAME':'Luis Perdomo','AGE':24,'TEAM':'SDP','POSITION':'P','ATBATS':46,'RUNS':3,'HITS':5,'DOUBLES':1,'TRIPLES':4,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':20,},
{'NAME':'Michael Wacha','AGE':25,'TEAM':'STL','POSITION':'P','ATBATS':46,'RUNS':3,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':22,},
{'NAME':'Rich Hill','AGE':37,'TEAM':'LAD','POSITION':'P','ATBATS':45,'RUNS':1,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':0,'STRIKEOUTS':18,},
{'NAME':'Pete Kozma','AGE':29,'TEAM':'TOT','POSITION':'3B','ATBATS':45,'RUNS':6,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':3,'STRIKEOUTS':20,},
{'NAME':'German Marquez','AGE':22,'TEAM':'COL','POSITION':'P','ATBATS':45,'RUNS':4,'HITS':8,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':0,'STRIKEOUTS':18,},
{'NAME':'Ty Blach','AGE':26,'TEAM':'SFG','POSITION':'P','ATBATS':44,'RUNS':5,'HITS':10,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':4,'STRIKEOUTS':21,},
{'NAME':'Nick Pivetta','AGE':24,'TEAM':'PHI','POSITION':'P','ATBATS':44,'RUNS':3,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':21,},
{'NAME':'Garrett Cooper','AGE':26,'TEAM':'NYY','POSITION':'1B','ATBATS':43,'RUNS':3,'HITS':14,'DOUBLES':5,'TRIPLES':1,'HOMERUNS':0,'RBI':6,'WALKS':1,'STRIKEOUTS':12,},
{'NAME':'Mike Foltynewicz','AGE':25,'TEAM':'ATL','POSITION':'P','ATBATS':42,'RUNS':1,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':27,},
{'NAME':'Zack Godley','AGE':27,'TEAM':'ARI','POSITION':'P','ATBATS':42,'RUNS':1,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':2,'STRIKEOUTS':26,},
{'NAME':'Geovany Soto','AGE':34,'TEAM':'CHW','POSITION':'C','ATBATS':42,'RUNS':5,'HITS':8,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':3,'RBI':9,'WALKS':4,'STRIKEOUTS':10,},
{'NAME':'Adam Wainwright','AGE':35,'TEAM':'STL','POSITION':'P','ATBATS':42,'RUNS':7,'HITS':11,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':2,'RBI':11,'WALKS':1,'STRIKEOUTS':15,},
{'NAME':'Rymer Liriano','AGE':26,'TEAM':'CHW','POSITION':'LF','ATBATS':41,'RUNS':4,'HITS':9,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':6,'WALKS':5,'STRIKEOUTS':14,},
{'NAME':'Scott Van Slyke','AGE':30,'TEAM':'LAD','POSITION':'LF','ATBATS':41,'RUNS':6,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':2,'RBI':3,'WALKS':7,'STRIKEOUTS':15,},
{'NAME':'Trevor Williams','AGE':25,'TEAM':'PIT','POSITION':'P','ATBATS':41,'RUNS':1,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':2,'STRIKEOUTS':17,},
{'NAME':'Tyler Austin','AGE':25,'TEAM':'NYY','POSITION':'NONE','ATBATS':40,'RUNS':4,'HITS':9,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':2,'RBI':8,'WALKS':4,'STRIKEOUTS':17,},
{'NAME':'Tyler Chatwood','AGE':27,'TEAM':'COL','POSITION':'P','ATBATS':39,'RUNS':5,'HITS':6,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':1,'STRIKEOUTS':9,},
{'NAME':'Taylor Featherston','AGE':27,'TEAM':'TBR','POSITION':'2B','ATBATS':39,'RUNS':6,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':2,'RBI':6,'WALKS':5,'STRIKEOUTS':15,},
{'NAME':'Kenta Maeda','AGE':29,'TEAM':'LAD','POSITION':'P','ATBATS':39,'RUNS':2,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':0,'STRIKEOUTS':3,},
{'NAME':'Emilio Bonifacio','AGE':32,'TEAM':'ATL','POSITION':'NONE','ATBATS':38,'RUNS':2,'HITS':5,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':9,},
{'NAME':'Ryan Flaherty','AGE':30,'TEAM':'BAL','POSITION':'2B','ATBATS':38,'RUNS':5,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':4,'STRIKEOUTS':10,},
{'NAME':'Jon Gray','AGE':25,'TEAM':'COL','POSITION':'P','ATBATS':38,'RUNS':3,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':1,'STRIKEOUTS':27,},
{'NAME':'Chris Marrero','AGE':28,'TEAM':'SFG','POSITION':'LF','ATBATS':38,'RUNS':2,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':2,'STRIKEOUTS':9,},
{'NAME':'Will Middlebrooks','AGE':28,'TEAM':'TEX','POSITION':'3B','ATBATS':38,'RUNS':5,'HITS':8,'DOUBLES':2,'TRIPLES':2,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':14,},
{'NAME':'Carlos Moncrief','AGE':28,'TEAM':'SFG','POSITION':'RF','ATBATS':38,'RUNS':4,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':3,'STRIKEOUTS':15,},
{'NAME':'Jameson Taillon','AGE':25,'TEAM':'PIT','POSITION':'P','ATBATS':38,'RUNS':2,'HITS':6,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':15,},
{'NAME':'Tony Kemp','AGE':25,'TEAM':'HOU','POSITION':'LF','ATBATS':37,'RUNS':6,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':1,'STRIKEOUTS':5,},
{'NAME':'Michael Martinez','AGE':34,'TEAM':'TOT','POSITION':'2B','ATBATS':37,'RUNS':2,'HITS':6,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':5,'STRIKEOUTS':15,},
{'NAME':'Tyler Naquin','AGE':26,'TEAM':'CLE','POSITION':'CF','ATBATS':37,'RUNS':4,'HITS':8,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':2,'STRIKEOUTS':9,},
{'NAME':'Jacob May','AGE':25,'TEAM':'CHW','POSITION':'CF','ATBATS':36,'RUNS':2,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':3,'STRIKEOUTS':17,},
{'NAME':'Mike Morse','AGE':35,'TEAM':'SFG','POSITION':'1B','ATBATS':36,'RUNS':1,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':3,'STRIKEOUTS':14,},
{'NAME':'Greg Allen','AGE':24,'TEAM':'CLE','POSITION':'CF','ATBATS':35,'RUNS':7,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':6,'WALKS':2,'STRIKEOUTS':8,},
{'NAME':'Matt Garza','AGE':33,'TEAM':'MIL','POSITION':'P','ATBATS':35,'RUNS':1,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':0,'STRIKEOUTS':13,},
{'NAME':'Dinelson Lamet','AGE':24,'TEAM':'SDP','POSITION':'P','ATBATS':35,'RUNS':0,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':22,},
{'NAME':'Madison Bumgarner','AGE':27,'TEAM':'SFG','POSITION':'P','ATBATS':34,'RUNS':4,'HITS':7,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':3,'RBI':5,'WALKS':2,'STRIKEOUTS':11,},
{'NAME':'Willie Calhoun','AGE':22,'TEAM':'TEX','POSITION':'LF','ATBATS':34,'RUNS':3,'HITS':9,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':2,'STRIKEOUTS':7,},
{'NAME':'Andre Ethier','AGE':35,'TEAM':'LAD','POSITION':'NONE','ATBATS':34,'RUNS':3,'HITS':8,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':2,'RBI':3,'WALKS':4,'STRIKEOUTS':10,},
{'NAME':'Scott Feldman','AGE':34,'TEAM':'CIN','POSITION':'P','ATBATS':34,'RUNS':0,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':16,},
{'NAME':'Robert Gsellman','AGE':23,'TEAM':'NYM','POSITION':'P','ATBATS':34,'RUNS':2,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':6,'STRIKEOUTS':14,},
{'NAME':'Matt Harvey','AGE':28,'TEAM':'NYM','POSITION':'P','ATBATS':34,'RUNS':2,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':13,},
{'NAME':'Cesar Puello','AGE':26,'TEAM':'TOT','POSITION':'NONE','ATBATS':34,'RUNS':6,'HITS':7,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':4,'STRIKEOUTS':12,},
{'NAME':'Brett Eibner','AGE':28,'TEAM':'LAD','POSITION':'NONE','ATBATS':33,'RUNS':3,'HITS':6,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':2,'RBI':6,'WALKS':2,'STRIKEOUTS':17,},
{'NAME':'Phillip Evans','AGE':24,'TEAM':'NYM','POSITION':'NONE','ATBATS':33,'RUNS':4,'HITS':10,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':4,'STRIKEOUTS':8,},
{'NAME':'Jaime Garcia','AGE':30,'TEAM':'TOT','POSITION':'P','ATBATS':33,'RUNS':2,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':7,'WALKS':1,'STRIKEOUTS':8,},
{'NAME':'Miguel Gomez','AGE':24,'TEAM':'SFG','POSITION':'NONE','ATBATS':33,'RUNS':3,'HITS':8,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':6,},
{'NAME':'Jeremy Hellickson','AGE':30,'TEAM':'TOT','POSITION':'P','ATBATS':33,'RUNS':1,'HITS':3,'DOUBLES':1,'TRIPLES':1,'HOMERUNS':0,'RBI':2,'WALKS':3,'STRIKEOUTS':9,},
{'NAME':'Jeff Hoffman','AGE':24,'TEAM':'COL','POSITION':'P','ATBATS':33,'RUNS':1,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':0,'STRIKEOUTS':17,},
{'NAME':'Joe Ross','AGE':24,'TEAM':'WSN','POSITION':'P','ATBATS':33,'RUNS':1,'HITS':6,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':16,},
{'NAME':'Pedro Alvarez','AGE':30,'TEAM':'BAL','POSITION':'NONE','ATBATS':32,'RUNS':4,'HITS':10,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':4,'WALKS':2,'STRIKEOUTS':10,},
{'NAME':'Matt Cain','AGE':32,'TEAM':'SFG','POSITION':'P','ATBATS':32,'RUNS':1,'HITS':5,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':20,},
{'NAME':'Antonio Senzatela','AGE':22,'TEAM':'COL','POSITION':'P','ATBATS':32,'RUNS':1,'HITS':4,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':5,'WALKS':0,'STRIKEOUTS':20,},
{'NAME':'Christian Villanueva','AGE':26,'TEAM':'SDP','POSITION':'NONE','ATBATS':32,'RUNS':5,'HITS':11,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':4,'RBI':7,'WALKS':0,'STRIKEOUTS':10,},
{'NAME':'Rob Brantly','AGE':27,'TEAM':'CHW','POSITION':'NONE','ATBATS':31,'RUNS':4,'HITS':9,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':2,'RBI':5,'WALKS':3,'STRIKEOUTS':14,},
{'NAME':'Jerad Eickhoff','AGE':26,'TEAM':'PHI','POSITION':'P','ATBATS':31,'RUNS':3,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':13,},
{'NAME':'Shane Robinson','AGE':32,'TEAM':'LAA','POSITION':'NONE','ATBATS':31,'RUNS':7,'HITS':6,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':3,'STRIKEOUTS':5,},
{'NAME':'Hyun-Jin Ryu','AGE':30,'TEAM':'LAD','POSITION':'P','ATBATS':30,'RUNS':3,'HITS':4,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':3,'STRIKEOUTS':18,},
{'NAME':'Anthony Santander','AGE':22,'TEAM':'BAL','POSITION':'NONE','ATBATS':30,'RUNS':1,'HITS':8,'DOUBLES':3,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':8,},
{'NAME':'Tim Adleman','AGE':29,'TEAM':'CIN','POSITION':'P','ATBATS':29,'RUNS':0,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':10,},
{'NAME':'Luis Castillo','AGE':24,'TEAM':'CIN','POSITION':'P','ATBATS':29,'RUNS':0,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':11,},
{'NAME':'Bryan Holaday','AGE':29,'TEAM':'DET','POSITION':'C','ATBATS':29,'RUNS':1,'HITS':7,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':1,},
{'NAME':'Seth Lugo','AGE':27,'TEAM':'NYM','POSITION':'P','ATBATS':29,'RUNS':4,'HITS':4,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':1,'RBI':2,'WALKS':0,'STRIKEOUTS':10,},
{'NAME':'Pedro Severino','AGE':23,'TEAM':'WSN','POSITION':'C','ATBATS':29,'RUNS':0,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':2,'STRIKEOUTS':10,},
{'NAME':'Homer Bailey','AGE':31,'TEAM':'CIN','POSITION':'P','ATBATS':28,'RUNS':4,'HITS':7,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':11,},
{'NAME':'Stephen Cardullo','AGE':29,'TEAM':'COL','POSITION':'NONE','ATBATS':28,'RUNS':2,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':3,'STRIKEOUTS':7,},
{'NAME':'Tuffy Gosewisch','AGE':33,'TEAM':'SEA','POSITION':'C','ATBATS':28,'RUNS':1,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':14,},
{'NAME':'Daniel Vogelbach','AGE':24,'TEAM':'SEA','POSITION':'NONE','ATBATS':28,'RUNS':0,'HITS':6,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':3,'STRIKEOUTS':9,},
{'NAME':'Christopher Bostick','AGE':24,'TEAM':'PIT','POSITION':'NONE','ATBATS':27,'RUNS':6,'HITS':8,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':4,'STRIKEOUTS':9,},
{'NAME':'Mike Montgomery','AGE':27,'TEAM':'CHC','POSITION':'P','ATBATS':27,'RUNS':5,'HITS':5,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':0,'STRIKEOUTS':10,},
{'NAME':'Sean Newcomb','AGE':24,'TEAM':'ATL','POSITION':'P','ATBATS':27,'RUNS':1,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':2,'STRIKEOUTS':17,},
{'NAME':'Dwight Smith','AGE':24,'TEAM':'TOR','POSITION':'NONE','ATBATS':27,'RUNS':2,'HITS':10,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':10,},
{'NAME':'Jake Smolinski','AGE':28,'TEAM':'OAK','POSITION':'NONE','ATBATS':27,'RUNS':1,'HITS':7,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':6,},
{'NAME':'Mike Tauchman','AGE':26,'TEAM':'COL','POSITION':'NONE','ATBATS':27,'RUNS':2,'HITS':6,'DOUBLES':0,'TRIPLES':1,'HOMERUNS':0,'RBI':2,'WALKS':5,'STRIKEOUTS':10,},
{'NAME':'Zack Wheeler','AGE':27,'TEAM':'NYM','POSITION':'P','ATBATS':27,'RUNS':1,'HITS':2,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':12,},
{'NAME':'Tyler Anderson','AGE':27,'TEAM':'COL','POSITION':'P','ATBATS':26,'RUNS':1,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':17,},
{'NAME':'Bronson Arroyo','AGE':40,'TEAM':'CIN','POSITION':'P','ATBATS':26,'RUNS':0,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':10,},
{'NAME':'Paul Janish','AGE':34,'TEAM':'BAL','POSITION':'SS','ATBATS':26,'RUNS':0,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':1,'STRIKEOUTS':6,},
{'NAME':'Ben Lively','AGE':25,'TEAM':'PHI','POSITION':'P','ATBATS':26,'RUNS':2,'HITS':6,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':2,'RBI':8,'WALKS':0,'STRIKEOUTS':9,},
{'NAME':'Kirk Nieuwenhuis','AGE':29,'TEAM':'MIL','POSITION':'NONE','ATBATS':26,'RUNS':3,'HITS':3,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':1,'WALKS':4,'STRIKEOUTS':15,},
{'NAME':'Edinson Volquez','AGE':33,'TEAM':'MIA','POSITION':'P','ATBATS':26,'RUNS':0,'HITS':5,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':11,},
{'NAME':'Rafael Bautista','AGE':24,'TEAM':'WSN','POSITION':'RF','ATBATS':25,'RUNS':2,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':2,'STRIKEOUTS':5,},
{'NAME':'Mark Leiter','AGE':26,'TEAM':'PHI','POSITION':'P','ATBATS':25,'RUNS':0,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':12,},
{'NAME':'Rafael Montero','AGE':26,'TEAM':'NYM','POSITION':'P','ATBATS':25,'RUNS':1,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':0,'STRIKEOUTS':10,},
{'NAME':'Kristopher Negron','AGE':31,'TEAM':'ARI','POSITION':'NONE','ATBATS':25,'RUNS':3,'HITS':4,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':4,'STRIKEOUTS':7,},
{'NAME':'Jose Quintana','AGE':28,'TEAM':'TOT','POSITION':'P','ATBATS':25,'RUNS':2,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':4,'WALKS':1,'STRIKEOUTS':17,},
{'NAME':'Jarrod Saltalamacchia','AGE':32,'TEAM':'TOR','POSITION':'NONE','ATBATS':25,'RUNS':1,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':16,},
{'NAME':'Adam Conley','AGE':27,'TEAM':'MIA','POSITION':'P','ATBATS':24,'RUNS':3,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':2,'STRIKEOUTS':14,},
{'NAME':'Cam Gallagher','AGE':24,'TEAM':'KCR','POSITION':'C','ATBATS':24,'RUNS':2,'HITS':6,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':1,'RBI':5,'WALKS':3,'STRIKEOUTS':4,},
{'NAME':'Tom Murphy','AGE':26,'TEAM':'COL','POSITION':'NONE','ATBATS':24,'RUNS':1,'HITS':1,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':2,'STRIKEOUTS':9,},
{'NAME':'Victor Robles','AGE':20,'TEAM':'WSN','POSITION':'NONE','ATBATS':24,'RUNS':2,'HITS':6,'DOUBLES':1,'TRIPLES':2,'HOMERUNS':0,'RBI':4,'WALKS':0,'STRIKEOUTS':6,},
{'NAME':'Sal Romano','AGE':23,'TEAM':'CIN','POSITION':'P','ATBATS':24,'RUNS':0,'HITS':1,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':1,'STRIKEOUTS':15,},
{'NAME':'Max Stassi','AGE':26,'TEAM':'HOU','POSITION':'C','ATBATS':24,'RUNS':5,'HITS':4,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':2,'RBI':4,'WALKS':6,'STRIKEOUTS':4,},
{'NAME':'Vince Velasquez','AGE':25,'TEAM':'PHI','POSITION':'P','ATBATS':24,'RUNS':1,'HITS':6,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':1,'STRIKEOUTS':4,},
{'NAME':'Brandon McCarthy','AGE':33,'TEAM':'LAD','POSITION':'P','ATBATS':23,'RUNS':2,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':3,'STRIKEOUTS':16,},
{'NAME':'Robert Stephenson','AGE':24,'TEAM':'CIN','POSITION':'P','ATBATS':23,'RUNS':1,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':15,},
{'NAME':'Alex Verdugo','AGE':21,'TEAM':'LAD','POSITION':'NONE','ATBATS':23,'RUNS':1,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':1,'WALKS':2,'STRIKEOUTS':4,},
{'NAME':'Drew Stubbs','AGE':32,'TEAM':'SFG','POSITION':'CF','ATBATS':22,'RUNS':0,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':2,'STRIKEOUTS':9,},
{'NAME':'Vance Worley','AGE':29,'TEAM':'MIA','POSITION':'P','ATBATS':22,'RUNS':0,'HITS':4,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':3,'WALKS':0,'STRIKEOUTS':8,},
{'NAME':'Zach Eflin','AGE':23,'TEAM':'PHI','POSITION':'P','ATBATS':21,'RUNS':1,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':13,},
{'NAME':'Edwin Jackson','AGE':33,'TEAM':'TOT','POSITION':'P','ATBATS':21,'RUNS':3,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':15,},
{'NAME':'Tom Koehler','AGE':31,'TEAM':'TOT','POSITION':'P','ATBATS':21,'RUNS':0,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':0,'WALKS':0,'STRIKEOUTS':15,},
{'NAME':'Steven Matz','AGE':26,'TEAM':'NYM','POSITION':'P','ATBATS':21,'RUNS':1,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':0,'STRIKEOUTS':7,},
{'NAME':'Kyle Farmer','AGE':26,'TEAM':'LAD','POSITION':'NONE','ATBATS':20,'RUNS':1,'HITS':6,'DOUBLES':1,'TRIPLES':0,'HOMERUNS':0,'RBI':2,'WALKS':0,'STRIKEOUTS':3,},
{'NAME':'Nolan Fontana','AGE':26,'TEAM':'LAA','POSITION':'NONE','ATBATS':20,'RUNS':1,'HITS':1,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':1,'WALKS':3,'STRIKEOUTS':8,},
{'NAME':'Jacob Hannemann','AGE':26,'TEAM':'SEA','POSITION':'NONE','ATBATS':20,'RUNS':3,'HITS':3,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':1,'WALKS':0,'STRIKEOUTS':4,},
{'NAME':'Carlos Perez','AGE':26,'TEAM':'LAA','POSITION':'C','ATBATS':20,'RUNS':1,'HITS':2,'DOUBLES':0,'TRIPLES':0,'HOMERUNS':1,'RBI':3,'WALKS':1,'STRIKEOUTS':6,},
{'NAME':'Rob Segedin','AGE':28,'TEAM':'LAD','POSITION':'NONE','ATBATS':20,'RUNS':3,'HITS':4,'DOUBLES':2,'TRIPLES':0,'HOMERUNS':0,'RBI':1,'WALKS':0,'STRIKEOUTS':7,},
]
    
main()
