def workConversion(hours, months):
    """hours -> internal design hourly calculation, months -> # of months
    converts design hours to a monthly cost that includes overhead
    to present to client.

    hours, allow are numbers, floats or ints
    returns a dollar amount"""
    
    cd = [0, 0, 25*months, 'Creative Director']
    gd = [0, 0, 30*months, 'Graphic Designer']
    am = [0, 0, 20*months, 'Account Manager']
    pm = [0, 0, 25*months, 'Production Manager']

    monthlyRatio = 55.0/40.0
    cdRatio = 25.0/55.0
    gdRatio = 30.0/55.0
    amRatio = 20.0/55.0
    #pm is equal to creative director

    cdRate = 175.00
    gdRate = 75.00
    amRate = 75.00
    pmRate = 75.00

    #0th index is the hourly amount for that position
    convertedHours = hours * monthlyRatio
    cd[0] = round(convertedHours * cdRatio)
    gd[0] = round(convertedHours * gdRatio)
    am[0] = round(convertedHours * amRatio)
    pm[0:1] = cd[0:1] #no calculation required

    #1st index is the dollar amount for that position
    cd[1] = cd[0] * cdRate
    gd[1] = gd[0] * gdRate
    am[1] = am[0] * amRate
    pm[1] = pm[0] * pmRate

    totalCost = cd[1] + gd[1] + am[1] + pm[1]
    totalHours = cd[0] + gd[0] + am[0] + pm[0]

    print cd[-1], 'hours:', cd[0], '| cost:', cd[1]
    print gd[-1], 'hours:', gd[0], '| cost:', gd[1]
    print am[-1], 'hours:', am[0], '| cost:', am[1]
    print pm[-1], 'hours:', pm[0], '| cost:', pm[1]
    print '\nTotal cost', totalCost
    print 'Total hours', totalHours
    print '\nAd Hoc hours remaining:'
    print cd[-1], '-', (cd[2] - cd[0]) 
    print gd[-1], '-', (gd[2] - gd[0])
    print am[-1], '-', (am[2] - am[0])
    print pm[-1], '-', (pm[2] - pm[0])
    print 'Total:', 100*months - totalHours
    print 'Ad Hoc costs reamining:', 10000*months - totalCost
    print '\nActual Juan hours remaining:'
    print 40*months - hours
