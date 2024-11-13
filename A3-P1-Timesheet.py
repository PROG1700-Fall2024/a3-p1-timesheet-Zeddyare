#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on each of five work days from the user, then displays different information calculated about those entries as output. 

#Student #: W0433704
#Student Name: Zachary Rudolf 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #list/variable initialize 
    days=["Day #1","Day #2","Day #3","Day #4","Day #5",] 
    dayHrs=[] 

    def getHrs(day):
        hours=int(input("Enter hours worked on {0}: ".format(day)))
        return hours

    #Welcome message/desc
    print("Enter your hours worked for each day this week cycle.\n") 

    #input for days worked 
    for i in range(5):
        hours=getHrs(days[i]) 
        dayHrs.insert(i, hours)  

    #highest day
    def longestDay():
        print("The most hours worked was on:")
        for i in range(0,len(dayHrs)): 
            if dayHrs[i]==max(dayHrs):
                print("Day #{0} when you worked {1} hours.".format((i+1), dayHrs[i])) 
        #total hours output and average output
    def averageDay():
        totalHrs=sum(dayHrs)
        avgDay=totalHrs/len(dayHrs) 
        print("The total number of hours worked was: {0}".format(totalHrs))
        print("The average number of hours worked was: {0:.1f}".format(avgDay))
        
    #shortest day
    def slackDays(minHrs):
        if any(i < 7 for i in dayHrs): 
            print("Days you slacked off (i.e. worked less than 7 hours): ")
            for i in range(0, len(dayHrs)):
                if (dayHrs[i]) <minHrs:
                    print("Day #{0}: {1} hours.".format((i+1), (dayHrs[i])))
        else:
            print("You didn't slack off this week, great work!") 
            



    #ouputs
    print("---------------------------------------")
    longestDay()
    print("---------------------------------------")
    averageDay()
    print("---------------------------------------")
    slackDays(7)



    # YOUR CODE ENDS HERE

main()