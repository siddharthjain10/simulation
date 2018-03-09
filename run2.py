import random
import numpy as np

Row = [0.0]*20
Map = np.zeros((20,20))
l = b = len(Row)
flag = 0
update = []
neighbour = []
connections = []
#var = 0;
v = np.zeros((4,2))
vcheck = np.zeros(4)
v[1][0] = 10
v[1][1] = 10
v[2][0] = 19
v[2][1] = 19
v[3][0] = 0
v[3][1] = 19

count=0
#-------------------------------------------------------------------------
#-------------------FUNCTIONS---------------------------------------------no
#-------------------------------------------------------------------------
#caught function
def caught(cx,cy,v):
    global count
    for i in range(0,4):
        if(v[i][0] == cy and v[i][1] == cx):
            print "CONGRATULATIONS, YOU HAVE CAUGHT THE CRIMINAL!"
            return 1


    if((cy == 0 and cx == 0) or (cy == 19 and cx == 0) or (cy == 0 and cx == 19) or (cy == 19 and cx == 19)):
        print "SORRY, YOU COULD NOT CATCH THE CRIMINAL"
        return -1

# check vicinity function
def vicinity(cx,cy,v,Map):
    vcheck = np.zeros(4);
    tempvar = 0;
    for t in range(0, len(vcheck)):
        if(abs(cy - v[t][0]) <= 1 and abs(cx - v[t][1]) <= 1):
            tempvar = 1;
            vcheck[t] = 1;
    if (tempvar == 1):
        for i in range(0,20):
            for j in range(0,20):
                Map[i][j] = 0.0;
        Map[cy][cx] = 1.0;

    return Map, vcheck;

# square matrix generation in vicinity of criminal and vehicle
def crimquad(mat, v, vcheck):
    for i in range(0,len(vcheck)):
            if (vcheck[i] > 0):
                try:
                    mat[v[i][0] + 1][v[i][1]] += 10;
                    mat[v[i][0] - 1][v[i][1]] += 10;
                    mat[v[i][0]][v[i][1] + 1] += 10;
                    mat[v[i][0]][v[i][1] - 1] += 10;
                    mat[v[i][0] + 1][v[i][1] + 1] += 5;
                    mat[v[i][0] - 1][v[i][1] - 1] += 5;
                except IndexError:
                    pass

    cy = np.unravel_index(np.argmin(mat, axis=None), mat.shape)[0];
    cx = np.unravel_index(np.argmin(mat, axis=None), mat.shape)[1];
    return cy,cx;


#probabilty assignment
def assign(tempmap, Map, connections, flag1):
     aMap = np.zeros((20,20));
     for i in range(0,20):
         for j in range(0,20):
            aMap[i][j] += Map[i][j];
     temp = np.zeros((20,20));
     if(flag1 == 1):
         cy = np.transpose(np.nonzero(Map))[0][0];
         cx = np.transpose(np.nonzero(Map))[0][1];
         try:
            aMap[cy-1][cx] += (connections[cy][cx]**(-1))*aMap[cy][cx]
            aMap[cy+1][cx] += (connections[cy][cx]**(-1))*aMap[cy][cx]
            aMap[cy][cx-1] += (connections[cy][cx]**(-1))*aMap[cy][cx]
            aMap[cy][cx+1] += (connections[cy][cx]**(-1))*aMap[cy][cx]
            aMap[cy][cx] = 0.0
         except IndexError:
            pass
         flag1 = 0;
         return tempmap,aMap,flag1;
     else:
         for i in range(0,20):
             for j in range(0,20):
                if(aMap[i][j] > 0 and temp[i][j] == 0):
                    try:
                        aMap[i][j + 1] += aMap[i][j]*((connections[i][j] - 1)**(-1));
                        aMap[i][j - 1] += aMap[i][j]*((connections[i][j] - 1)**(-1));
                        aMap[i + 1][j] += aMap[i][j]*((connections[i][j] - 1)**(-1));
                        aMap[i - 1][j] += aMap[i][j]*((connections[i][j] - 1)**(-1));
                        aMap[i][j] = 0.0;
                        temp[i][j + 1] = 1;
                        temp[i][j - 1] = 1;
                        temp[i - 1][j] = 1;
                        temp[i + 1][j] = 1;
                    except IndexError:
                        continue
         for i in range(0,20):
             for j in range(0,20):
                 if(tempmap[i][j] > 0):
                     aMap[i][j] = 0.0;
         tempmap = Map;
         return tempmap,aMap, flag1;

##    Map[cy-1][cx] += 0.25*Map[cy][cx]
##    Map[cy+1][cx] += 0.25*Map[cy][cx]
##    Map[cy][cx-1] += 0.25*Map[cy][cx]
##    Map[cy][cx+1] += 0.25*Map[cy][cx]
##    Map[cy][cx] = 0.0



def add():              #Add into the neighbour matrix the neighbouring nodes
    global Map
    for i in range(l):   # y co-ordinate
        neighbour.append([])
        for j in range(b):     # x co-ordinate
            neighbour[i].append([])
            check = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]

            for k in check:

                if (k[0]>=0 and k[1]>=0):
                    try:
                        Map[k[0]][k[1]]       #  is index present in the defined map
                        neighbour[i][j].append(k)
                    except IndexError:
                        continue



#-------------------------------------------------------------------------no
for test_case in range(1000):
    Row = [0.0]*20
    Map = np.zeros((20,20))
    l = b = len(Row)
    flag = 0
    update = []
    neighbour = []
    connections = []
    #var = 0;
    v = np.zeros((4,2))
    vcheck = np.zeros(4)
    v[1][0] = 10
    v[1][1] = 10
    v[2][0] = 19
    v[2][1] = 19
    v[3][0] = 0
    v[3][1] = 19
    ##for i in range(len(Row)):
    ##    Map.append([0.0]*20)

    cy = random.randint(0,l-1)
    cx = random.randint(0,b-1)

    add()
    ##for i in neighbour:
    ##    print i
    l=0
    for i in neighbour:
        connections.append([])
        for j in i:
             connections[l].append(len(j))
        l+=1

    print cx,cy

    Map[cy][cx] = 1.0

    ##for a in Map:
    ##    print (a)
    ##print ("--------------------")

    tempmap = np.zeros((20,20));
    tempmap[cy][cx] = 1;  #tempmap stores previous to previous iteration's map matrix
    flag1 = 1;
    try:
        for g in range(1,500):#iterations
            Map, vcheck = vicinity(cx,cy,v,Map);

            # print(Map)
            if (vcheck.any() > 0):
                flag1 = 1;
                for i in range(0,len(vcheck)):
                    if (vcheck[i] > 0):
                        if (abs(cy - v[i][0]) == 1 and abs(cx - v[i][1]) == 1):
                            tempnum = random.uniform(0,1)
                            if tempnum > 0.5:
                                    v[i][0] = cy;
                            else:
                                    v[i][1] = cx;
                        elif(abs(cy - v[i][0]) == 1):
                            v[i][0] = cy;
                        elif(abs(cx - v[i][1]) == 1):
                            v[i][1] = cx;
                    else:
                        tempnum = random.uniform(0,1)
                        if tempnum > 0.5:
                            if(cy - v[i][0]) > 0:
                                v[i][0] += 1;
                            else:
                                v[i][0] -= 1;
                        else:
                            if(cx - v[i][1]) > 0:
                                v[i][1] += 1;
                            else:
                                v[i][1] -= 1;


        ####cx cy update functions in case it is in vicinity
                mat = 1000*np.ones((20,20));
                if cx<=l//2 and cy<=b//2:
                    try:
                        mat[cy-1][cx] = 1;
                        mat[cy+1][cx] = 2;
                        mat[cy][cx-1] = 1;
                        mat[cy][cx+1] = 2;
                        cy,cx = crimquad(mat, v, vcheck);
                    except IndexError:
                        pass
                elif cx>l//2 and cy<=b//2:
                    try:
                        mat[cy-1][cx] = 1;
                        mat[cy+1][cx] = 2;
                        mat[cy][cx-1] = 2;
                        mat[cy][cx+1] = 1;
                        cy,cx = crimquad(mat, v, vcheck);
                    except IndexError:
                        pass

                elif cx<=l//2 and cy>b//2:
                    try:
                        mat[cy-1][cx] = 2;
                        mat[cy+1][cx] = 1;
                        mat[cy][cx-1] = 1;
                        mat[cy][cx+1] = 2;
                        cy,cx = crimquad(mat, v, vcheck);
                    except IndexError:
                        pass
                else:
                    try:
                        mat[cy-1][cx] = 2;
                        mat[cy+1][cx] = 1;
                        mat[cy][cx-1] = 2;
                        mat[cy][cx+1] = 1;
                        cy,cx = crimquad(mat, v, vcheck);
                    except IndexError:
                        pass
                #print cx,cy
                #print v
                check_end=caught(cx,cy,v);
                if (check_end==1):
                    count+=1;
                    raise AssertionError;
                if (check_end==-1):
                    raise AssertionError;

            else:
                tempmap, Map, flag1 = assign(tempmap, Map, connections,flag1);
        ##        for a in Map:
        ##            print (a)
        ##        print ("--------------------")
                for t in range(0,len(vcheck)):
                    temp = 0.0;
                    hprob = np.amax(Map)
                    distv = 1000;
                    probx = 0;
                    proby = 0;
                    for i in range(0,20):
                        for j in range(0,20):
                            if(Map[i][j] == hprob):
                                temp = abs(i - v[t][0]) + abs(j - v[t][1]);
                                if temp < distv:
                                    distv = temp;
                                    proby = i;
                                    probx = j;

                    tempnum = random.uniform(0,1)
                    if tempnum > 0.5:
                        if(proby - v[t][0]) > 0:
                            v[t][0] += 1;
                        else:
                            v[t][0] -= 1;
                    else:
                        if(probx - v[t][1]) > 0:
                            v[t][1] += 1;
                        else:
                            v[t][1] -= 1;

                    ###cx and cy update functions here
                        '''
                    nomenclature for quadrants:
                    ++ =1; -+=2; -- =3; +-=4
                    '''
                    # Quadrant 2
                if cx<=l//2 and cy<=b//2:
                    if cx>0 and cy>0:
                        tempnum = random.uniform(0,1);
                        if tempnum > 0.5:
                            cy -= 1;
                        else:
                            cx -= 1;
                    elif cx>0:
                        cx-=1
                    else:
                        cy-=1
                    # Quadrant 1
                elif cx>l//2 and cy<=b//2:
                    if cx<l-1 and cy>0:
                        tempnum = random.uniform(0,1);
                        if tempnum > 0.5:
                            cy -= 1;
                        else:
                            cx += 1;
                    elif cy>0:
                        cy-=1
                    else:
                        cx+=1
                # Quadrant 3
                elif cx<=l//2 and cy>b//2:
                    if cy<b-1 and cx>0:
                        tempnum = random.uniform(0,1);
                        if tempnum > 0.5:
                            cy += 1;
                        else:
                            cx -= 1;
                    elif cx>0:
                        cx-=1
                    else:
                        cy+=1
                # Quadrant 4
                else:
                    if cx<l-1 and cy<b-1:
                        tempnum = random.uniform(0,1);
                        if tempnum > 0.5:
                            cy += 1;
                        else:
                            cx += 1;
                    elif cx<l-1:
                        cx+=1
                    else:
                        cy+=1;
                #print cx,cy;
                #print v
                check_end=caught(cx,cy,v);
                if (check_end==1):

                    count+=1;
                    raise AssertionError;
                if (check_end==-1):
                    raise AssertionError;
    except AssertionError:
        continue
print("number of times the criminal was caught is ",count)
