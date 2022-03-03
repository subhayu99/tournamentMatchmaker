#!/bin/python3

import random
import sys
import csv

def printBanner():
    print("\n\033[1;32;40m────────TOURNAMENT MATCHMAKING SCRIPT────────\033[0;37;40m\
            \n           Made by:\033[1;32;40m Subhayu Kr Bala\033[0;37;40m\
            \n        Website: \033[1;32;40mhttps://subhayu.codes\033[0;37;40m\
            \n─────────────────────────────────────────────\033[0;37;40m")


def readTeamsData():
    teamsList = []
    global nTeams
    choice = input("\n\033[1;31;40mHaving a file with team details? [\033[1;36;40my\033[1;31;40m/\033[1;36;40mn\033[1;31;40m] : \033[1;37;40m")
    if( choice == "y" or choice == "Y" ):
        csvFile = input("\033[1;31;40mFile name (\033[1;36;40mmust be present in same dir\033[1;31;40m) : \033[1;37;40m")
        try:
            with open(csvFile, newline='') as f:
                reader = csv.reader(f)
                teamsList = list(reader)
                if( len(teamsList[1]) == 1 ):
                    t=[]
                    for i in range(len(teamsList)):
                        t.append(teamsList[i][0])
                    teamsList=t
            nTeams = len(teamsList)
            print("\033[1;31;40mNo. of teams found :\033[1;37;40m", nTeams)
        except:
            print("\033[0;35;40mError! No matching file found.\033[0;36;40m\nTry again\033[1;37;40m")
            return readTeamsData()
    else:
        nTeams = int(input("\033[1;31;40mEnter no. of players : \033[1;37;40m"))
        teamsList.extend(range(1, nTeams+1))
        #  print("\nTeam data :", teamsList)
    return teamsList


def createGroups(teamsList, nGroups, groupSize):
    groupsList = []
    for teamNow in range(nGroups):
        xGroup = []
        for teamNum in range(groupSize):
            teamNow = random.choice(teamsList)
            teamsList.remove(teamNow)
            xGroup.append(teamNow)
        groupsList.append(xGroup)
    xGroup = []
    if(nTeams%groupSize != 0):
        for teamNum in range(nTeams%groupSize):
            teamNow = random.choice(teamsList)
            teamsList.remove(teamNow)
            xGroup.append(teamNow)
        groupsList.append(xGroup)
        for teamNum in range(groupSize-(nTeams%groupSize)):
            groupsList[nGroups].append('')
    nGroups = int(nTeams/groupSize) + (nTeams % groupSize > 0)
    #  print(groupsList, nGroups)
    return groupsList


def createMatches(groupList, nGroups, groupSize):
    matchList = []
    for group in enumerate(groupList):
        for player in enumerate(group[1]):
            matches = []
            for i in range(0, groupSize, 2):
                match = []
                match.append(group[1][i])
                match.append(group[1][i+1])
                matches.append(match)
        matchList.append(matches)
    return matchList


def printMatches(matchList, nGroups, groupSize):
    nGroups = len(matchList)
    print("\n\033[1;34;40mMatches are listed in a tree\033[0;37;40m\n")
    for group in enumerate(matchList):
        if(group[0] < nGroups-1):
            print("\033[0;37;40m├──\033[1;35;40mGroup", group[0]+1)
            for player in enumerate(group[1]):
                if(player[0] < (groupSize/2)-1):
                    print("\033[0;37;40m│  ├──\033[1;36;40mMatch", player[0]+1)
                    print("\033[0;37;40m│  │  ├──\033[1;32;40m",player[1][0])
                    print("\033[0;37;40m│  │  └──\033[1;32;40m",player[1][1],"\n\033[0;37;40m│  │  ")
                else:
                    print("\033[0;37;40m│  └──\033[1;36;40mMatch", player[0]+1)
                    print("\033[0;37;40m│     ├──\033[1;32;40m",player[1][0])
                    print("\033[0;37;40m│     └──\033[1;32;40m",player[1][1],"\n\033[0;37;40m│     ")
        else:
            print("\033[0;37;40m└──\033[1;35;40mGroup", group[0]+1)
            for player in enumerate(group[1]):
                if(player[0] < (groupSize/2)-1):
                    print("\033[0;37;40m   ├──\033[1;36;40mMatch", player[0]+1)
                    print("\033[0;37;40m   │  ├──\033[1;32;40m",player[1][0])
                    print("\033[0;37;40m   │  └──\033[1;32;40m",player[1][1],"\n\033[0;37;40m   │  ")
                else:
                    print("\033[0;37;40m   └──\033[1;36;40mMatch", player[0]+1)
                    print("\033[0;37;40m      ├──\033[1;32;40m",player[1][0])
                    print("\033[0;37;40m      └──\033[1;32;40m",player[1][1],"\n\033[0;37;40m      ")


def printGroups(groupList, nGroups, groupSize):
    print("\n\033[1;34;40mGroups are listed in a tree\033[0;37;40m\n")
    nGroups = len(groupList)
    for group in enumerate(groupsList):
        if(group[0] < nGroups-1):
            print("\033[0;37;40m├──\033[1;35;40mGroup", group[0]+1)
            for player in enumerate(group[1]):
                if(player[0] < groupSize-1):
                    print("\033[0;37;40m│  ├──\033[1;36;40m", player[1])
                else:
                    print("\033[0;37;40m│  └──\033[1;36;40m", player[1], "\n\033[0;37;40m│  ")
        else:
            print("\033[0;37;40m└──\033[1;35;40mGroup", group[0]+1)
            for player in enumerate(group[1]):
                if(player[0] < groupSize-1):
                    print("\033[0;37;40m   ├──\033[1;36;40m", player[1])
                else:
                    print("\033[0;37;40m   └──\033[1;36;40m", player[1], "\n")

def outputChoice():
    print("\n\033[1;31;40mHow you want the output to be?\
            \n\t\033[1;36;40m1 \033[1;31;40m: Matching within Groups in Tree format\
            \n\t\033[1;36;40m2 \033[1;31;40m: Only Groups in Tree format\
            \n\t\033[1;36;40m3 \033[1;31;40m: Both")
    choice = int(input("\033[1;31;40mSelect only the corresponding number : \033[1;37;40m"))
    if(choice == 1):
        printMatches(matchList, nGroups, groupSize)
    elif(choice == 2):
        printGroups(groupsList, nGroups, groupSize)
    elif(choice == 3):
        printMatches(matchList, nGroups, groupSize)
        printGroups(groupsList, nGroups, groupSize)
    else:
        print("\033[1;36;40mTry Again\033[1;37;40m")
        outputChoice()


def saveIt(groupsList, matchList):
    save = input("\033[1;31;40mDo you want to save the output? [\033[1;36;40my\033[1;31;40m/\033[1;36;40mn\033[1;31;40m] : \033[1;37;40m")
    if( save == "y" or save == "Y" ):
        nGroups = len(groupsList)
        original_stdout = sys.stdout
        with open('groupsAsTree.txt', 'w') as f:
            sys.stdout = f
            printBanner()
            print("\n\n\033[1;36;40mNo. of teams :\033[1;37;40m", nTeams)
            print("\n\033[1;36;40mNo. of groups :\033[1;37;40m", nGroups)
            print("\n\033[1;36;40mTeams per group :\033[1;37;40m", groupSize)
            print("\n\n\033[1;35;40m─────────────────────────────────────────────\033[0;37;40m\n")
            printGroups(groupsList, nGroups, groupSize)
            print("\n\033[1;35;40m─────────────────────────────────────────────\033[0;37;40m\n")

        with open('groupsAsPlainText.txt', 'w') as l:
            sys.stdout = l
            printBanner()
            print("\n\n\033[1;36;40mNo. of teams :\033[1;37;40m", nTeams)
            print("\n\033[1;36;40mNo. of groups :\033[1;37;40m", nGroups)
            print("\n\033[1;36;40mTeams per group :\033[1;37;40m", groupSize)
            print("\n\n\033[1;35;40m─────────────────────────────────────────────\033[0;37;40m\n")
            print("\n\033[1;34;40mGroups are listed in plain text\033[0;37;40m\n")
            for group in range(len(groupsList)):
                print("\033[1;35;40mGroup", group+1, "\033[1;36;40m")
                for player in groupsList[group]:
                    print(player)
                print()
            print("\n\033[1;35;40m─────────────────────────────────────────────\033[0;37;40m\n")
        with open('matchesAsTree.txt', 'w') as k:
            sys.stdout = k
            printBanner()
            print("\n\n\033[1;36;40mNo. of teams :\033[1;37;40m", nTeams)
            print("\n\033[1;36;40mNo. of groups :\033[1;37;40m", nGroups)
            print("\n\033[1;36;40mTeams per group :\033[1;37;40m", groupSize)
            print("\n\033[1;36;40mTotal matches :\033[1;37;40m", int(nTeams/2))
            print("\n\n\033[1;35;40m─────────────────────────────────────────────\033[0;37;40m\n")
            printMatches(matchList, nGroups, groupSize)
            print("\n\033[1;35;40m─────────────────────────────────────────────\033[0;37;40m\n")
            # Reset the standard output
            sys.stdout = original_stdout
        print("\n\033[1;31;40mSaved to files : \033[1;37;40mgroupsAsTree.txt\033[1;31;40m, \033[1;37;40mgroupsAsPlainText.txt \033[1;31;40mand \033[1;37;40mmatchesAsTree.txt\033[1;37;40m\n")


if __name__ == '__main__':
    global nGroups
    printBanner()
    teamsList = readTeamsData()
    groupSize = int(input("\033[1;31;40mEnter Group size (\033[1;36;40mmust be even\033[1;31;40m) : \033[1;37;40m"))
    if(groupSize%2 == 1):
        groupSize += 1
        print("\033[0;35;40mGroup size must be even\033[1;37;40m")
        print("\033[1;31;40mChanged Group size to :\033[1;37;40m", groupSize)
    nTeams = len(teamsList)
    nGroups = int(nTeams/groupSize)
    groupsList = createGroups(teamsList, nGroups, groupSize)
    matchList = createMatches(groupsList, nGroups, groupSize)
    outputChoice()
    saveIt(groupsList, matchList)

