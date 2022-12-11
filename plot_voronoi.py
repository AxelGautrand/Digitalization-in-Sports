from statsbombpy import sb

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc
import pandas as pd
from matplotlib.patches import Ellipse
import matplotlib.patheffects as path_effects

from mplsoccer.pitch import Pitch

def createPitch(length,width, unity,linecolor): # in meters
    # Code by @JPJ_dejong

    """
    creates a plot in which the 'length' is the length of the pitch (goal to goal).
    And 'width' is the width of the pitch (sideline to sideline). 
    Fill in the unity in meters or in yards.
    """
    #Set unity
    if unity == "meters":
        # Set boundaries
        if length >= 120.5 or width >= 75.5:
            return(str("Field dimensions are too big for meters as unity, didn't you mean yards as unity?\
                       Otherwise the maximum length is 120 meters and the maximum width is 75 meters. Please try again"))
        #Run program if unity and boundaries are accepted
        else:
            #Create figure
            fig=plt.figure()
            #fig.set_size_inches(7, 5)
            ax=fig.add_subplot(1,1,1)
           
            #Pitch Outline & Centre Line
            plt.plot([0,0],[0,width], color=linecolor)
            plt.plot([0,length],[width,width], color=linecolor)
            plt.plot([length,length],[width,0], color=linecolor)
            plt.plot([length,0],[0,0], color=linecolor)
            plt.plot([length/2,length/2],[0,width], color=linecolor)
            
            #Left Penalty Area
            plt.plot([16.5 ,16.5],[(width/2 +16.5),(width/2-16.5)],color=linecolor)
            plt.plot([0,16.5],[(width/2 +16.5),(width/2 +16.5)],color=linecolor)
            plt.plot([16.5,0],[(width/2 -16.5),(width/2 -16.5)],color=linecolor)
            
            #Right Penalty Area
            plt.plot([(length-16.5),length],[(width/2 +16.5),(width/2 +16.5)],color=linecolor)
            plt.plot([(length-16.5), (length-16.5)],[(width/2 +16.5),(width/2-16.5)],color=linecolor)
            plt.plot([(length-16.5),length],[(width/2 -16.5),(width/2 -16.5)],color=linecolor)
            
            #Left 5-meters Box
            plt.plot([0,5.5],[(width/2+7.32/2+5.5),(width/2+7.32/2+5.5)],color=linecolor)
            plt.plot([5.5,5.5],[(width/2+7.32/2+5.5),(width/2-7.32/2-5.5)],color=linecolor)
            plt.plot([5.5,0.5],[(width/2-7.32/2-5.5),(width/2-7.32/2-5.5)],color=linecolor)
            
            #Right 5 -eters Box
            plt.plot([length,length-5.5],[(width/2+7.32/2+5.5),(width/2+7.32/2+5.5)],color=linecolor)
            plt.plot([length-5.5,length-5.5],[(width/2+7.32/2+5.5),width/2-7.32/2-5.5],color=linecolor)
            plt.plot([length-5.5,length],[width/2-7.32/2-5.5,width/2-7.32/2-5.5],color=linecolor)
            
            #Prepare Circles
            centreCircle = plt.Circle((length/2,width/2),9.15,color=linecolor,fill=False)
            centreSpot = plt.Circle((length/2,width/2),0.8,color=linecolor)
            leftPenSpot = plt.Circle((11,width/2),0.8,color=linecolor)
            rightPenSpot = plt.Circle((length-11,width/2),0.8,color=linecolor)
            
            #Draw Circles
            ax.add_patch(centreCircle)
            ax.add_patch(centreSpot)
            ax.add_patch(leftPenSpot)
            ax.add_patch(rightPenSpot)
            
            #Prepare Arcs
            leftArc = Arc((11,width/2),height=18.3,width=18.3,angle=0,theta1=308,theta2=52,color=linecolor)
            rightArc = Arc((length-11,width/2),height=18.3,width=18.3,angle=0,theta1=128,theta2=232,color=linecolor)
            
            #Draw Arcs
            ax.add_patch(leftArc)
            ax.add_patch(rightArc)
            #Axis titles

    #check unity again
    elif unity == "yards":
        #check boundaries again
        if length <= 95:
            return(str("Didn't you mean meters as unity?"))
        elif length >= 131 or width >= 101:
            return(str("Field dimensions are too big. Maximum length is 130, maximum width is 100"))
        #Run program if unity and boundaries are accepted
        else:
            #Create figure
            fig=plt.figure()
            #fig.set_size_inches(7, 5)
            ax=fig.add_subplot(1,1,1)
           
            #Pitch Outline & Centre Line
            plt.plot([0,0],[0,width], color=linecolor)
            plt.plot([0,length],[width,width], color=linecolor)
            plt.plot([length,length],[width,0], color=linecolor)
            plt.plot([length,0],[0,0], color=linecolor)
            plt.plot([length/2,length/2],[0,width], color=linecolor)
            
            #Left Penalty Area
            plt.plot([18 ,18],[(width/2 +18),(width/2-18)],color=linecolor)
            plt.plot([0,18],[(width/2 +18),(width/2 +18)],color=linecolor)
            plt.plot([18,0],[(width/2 -18),(width/2 -18)],color=linecolor)
            
            #Right Penalty Area
            plt.plot([(length-18),length],[(width/2 +18),(width/2 +18)],color=linecolor)
            plt.plot([(length-18), (length-18)],[(width/2 +18),(width/2-18)],color=linecolor)
            plt.plot([(length-18),length],[(width/2 -18),(width/2 -18)],color=linecolor)
            
            #Left 6-yard Box
            plt.plot([0,6],[(width/2+7.32/2+6),(width/2+7.32/2+6)],color=linecolor)
            plt.plot([6,6],[(width/2+7.32/2+6),(width/2-7.32/2-6)],color=linecolor)
            plt.plot([6,0],[(width/2-7.32/2-6),(width/2-7.32/2-6)],color=linecolor)
            
            #Right 6-yard Box
            plt.plot([length,length-6],[(width/2+7.32/2+6),(width/2+7.32/2+6)],color=linecolor)
            plt.plot([length-6,length-6],[(width/2+7.32/2+6),width/2-7.32/2-6],color=linecolor)
            plt.plot([length-6,length],[(width/2-7.32/2-6),width/2-7.32/2-6],color=linecolor)
            
            #Prepare Circles; 10 yards distance. penalty on 12 yards
            centreCircle = plt.Circle((length/2,width/2),10,color=linecolor,fill=False)
            centreSpot = plt.Circle((length/2,width/2),0.8,color=linecolor)
            leftPenSpot = plt.Circle((12,width/2),0.8,color=linecolor)
            rightPenSpot = plt.Circle((length-12,width/2),0.8,color=linecolor)
            
            #Draw Circles
            ax.add_patch(centreCircle)
            ax.add_patch(centreSpot)
            ax.add_patch(leftPenSpot)
            ax.add_patch(rightPenSpot)
            
            #Prepare Arcs
            leftArc = Arc((11,width/2),height=20,width=20,angle=0,theta1=312,theta2=48,color=linecolor)
            rightArc = Arc((length-11,width/2),height=20,width=20,angle=0,theta1=130,theta2=230,color=linecolor)
            
            #Draw Arcs
            ax.add_patch(leftArc)
            ax.add_patch(rightArc)
                
    #Tidy Axes
    plt.axis('off')
    
    return fig,ax

if __name__ == '__main__':
    match_frames = sb.frames(match_id=3835319, fmt="dict")
    comp_frames = sb.competition_frames(
        country="Europe",
        division= "UEFA Women's Euro",
        season="2022",
        gender="female",
        fmt="dict"
    )
    event_360 = {}

    for event in range(len(match_frames)):
        same_team = []
        opponent_team = []
        for player in range(len(match_frames[event]['freeze_frame'])):
            if match_frames[event]['freeze_frame'][player]['teammate']:
                same_team.append(match_frames[event]['freeze_frame'][player]['location'])
            else:
                opponent_team.append(match_frames[event]['freeze_frame'][player]['location'])
        event_360[match_frames[event]['event_uuid']] = {'sameTeamLocation' : same_team, 'opponentTeamLocation' : opponent_team}

    events = sb.events(match_id=3835319,fmt="dict")
    events_id = {}
    for k in events.keys():
        if events[k]['type']['name']!='Starting XI' and events[k].get('location') is not None:
            t = {'team' : events[k]['possession_team'], 'location' : events[k]['location'], 'period' : events[k]['period'], "type" : events[k]['type']['name']}
            events_id[events[k]['id']] = {'value' : t}


    event = {}

    for k in events_id.keys():
        if k in event_360.keys():
            event[k] = {'ball' : events_id[k]['value'], 'sameTeam' : event_360[k]['sameTeamLocation'], 'opponentTeam' : event_360[k]['opponentTeamLocation']}

    count = 0    
    for k in event.keys():
        if count > 1:
            break
        count = count + 1

        (fig,ax) = createPitch(120,80,'yards','gray')
        
        if event[k]['ball']['period']==1:
            if event[k]['ball']['team']['id']==865:
                x = event[k]['ball']['location'][0]
                y = event[k]['ball']['location'][1]
                positionBall = plt.Circle((x,y),2,color="red")
                ax.add_patch(positionBall)

                for i in range(len(event[k]['sameTeam'])):
                    x=event[k]['sameTeam'][i][0]
                    y=event[k]['sameTeam'][i][1]
                    position = plt.Circle((x,y),2,color="black")
                    ax.add_patch(position)

                for j in range(len(event[k]['opponentTeam'])):
                    x=event[k]['opponentTeam'][j][0]
                    y=event[k]['opponentTeam'][j][1]
                    position = plt.Circle((x,y),2,color="blue")
                    ax.add_patch(position)
            else:
                x = event[k]['ball']['location'][0]
                y = event[k]['ball']['location'][1]
                positionBall = plt.Circle((120-x,y),2,color="red")
                ax.add_patch(positionBall)

                for i in range(len(event[k]['sameTeam'])):
                    x=event[k]['sameTeam'][i][0]
                    y=event[k]['sameTeam'][i][1]
                    position = plt.Circle((120-x,y),2,color="blue")
                    ax.add_patch(position)

                for j in range(len(event[k]['opponentTeam'])):
                    x=event[k]['opponentTeam'][j][0]
                    y=event[k]['opponentTeam'][j][1]
                    position = plt.Circle((120-x,y),2,color="black")
                    ax.add_patch(position)
                    
        else:
            print('II tempo')
            if event[k]['ball']['team']['id']==865:
                x = event[k]['ball']['location'][0]
                y = event[k]['ball']['location'][1]
                positionBall = plt.Circle((120-x,y),2,color="red")
                ax.add_patch(positionBall)

                for i in range(len(event[k]['sameTeam'])):
                    x=event[k]['sameTeam'][i][0]
                    y=event[k]['sameTeam'][i][1]
                    position = plt.Circle((120-x,y),2,color="black")
                    ax.add_patch(position)

                for j in range(len(event[k]['opponentTeam'])):
                    x=event[k]['opponentTeam'][j][0]
                    y=event[k]['opponentTeam'][j][1]
                    position = plt.Circle((120-x,y),2,color="blue")
                    ax.add_patch(position)
            else:
                x = event[k]['ball']['location'][0]
                y = event[k]['ball']['location'][1]
                positionBall = plt.Circle((x,y),2,color="red")
                ax.add_patch(positionBall)

                for i in range(len(event[k]['sameTeam'])):
                    x=event[k]['sameTeam'][i][0]
                    y=event[k]['sameTeam'][i][1]
                    position = plt.Circle((x,y),2,color="blue")
                    ax.add_patch(position)

                for j in range(len(event[k]['opponentTeam'])):
                    x=event[k]['opponentTeam'][j][0]
                    y=event[k]['opponentTeam'][j][1]
                    position = plt.Circle((x,y),2,color="black")
                    ax.add_patch(position)

        fig.set_size_inches(10, 7)
        plt.show()
            

    type_event = []
    for k in event.keys():
        type_event.append(event[k]['ball']['type'])

    type_event = set(type_event)
    
    from matplotlib.colorbar import constrained_layout

    type_event = []
    for k in event.keys():
        type_event.append(event[k]['ball']['type'])

    type_event = set(type_event)

    for x in type_event:
      for k in event.keys():
         
          if x == event[k]['ball']['type']:
              print('--------------------' + x+ '--------------------')
              home_team_x = []
              home_team_y = []
              away_team_x = []
              away_team_y = []
              home_t = []
              away_t = []

              (fig,ax) = createPitch(120,80,'yards','gray')
              
              if event[k]['ball']['period']==1:
                  if event[k]['ball']['team']['id']==865:
                      x = event[k]['ball']['location'][0]
                      y = event[k]['ball']['location'][1]
                      positionBall = plt.Circle((x,y),2,color="black")
                      ax.add_patch(positionBall)

                      for i in range(len(event[k]['sameTeam'])):
                          x=event[k]['sameTeam'][i][0]
                          y=event[k]['sameTeam'][i][1]
                          position = plt.Circle((x,y),2,color="red")
                          ax.add_patch(position)
                          home_team_x.append(x)
                          home_team_y.append(y)
                          home_t.append(0)

                      for j in range(len(event[k]['opponentTeam'])):
                          x=event[k]['opponentTeam'][j][0]
                          y=event[k]['opponentTeam'][j][1]
                          position = plt.Circle((x,y),2,color="blue")
                          ax.add_patch(position)
                          away_team_x.append(x)
                          away_team_y.append(y)
                          away_t.append(1)

                  else:
                      x = event[k]['ball']['location'][0]
                      y = event[k]['ball']['location'][1]
                      positionBall = plt.Circle((120-x,y),2,color="black")
                      ax.add_patch(positionBall)

                      for i in range(len(event[k]['sameTeam'])):
                          x=event[k]['sameTeam'][i][0]
                          y=event[k]['sameTeam'][i][1]
                          position = plt.Circle((120-x,y),2,color="blue")
                          ax.add_patch(position)
                          away_team_x.append(120-x)
                          away_team_y.append(y)
                          away_t.append(1)


                      for j in range(len(event[k]['opponentTeam'])):
                          x=event[k]['opponentTeam'][j][0]
                          y=event[k]['opponentTeam'][j][1]
                          position = plt.Circle((120-x,y),2,color="red")
                          ax.add_patch(position)
                          home_team_x.append(120-x)
                          home_team_y.append(y)
                          home_t.append(0)
                          
              else:
                  if event[k]['ball']['team']['id']==865:
                      x = event[k]['ball']['location'][0]
                      y = event[k]['ball']['location'][1]
                      positionBall = plt.Circle((120-x,y),2,color="black")
                      ax.add_patch(positionBall)

                      for i in range(len(event[k]['sameTeam'])):
                          x=event[k]['sameTeam'][i][0]
                          y=event[k]['sameTeam'][i][1]
                          position = plt.Circle((120-x,y),2,color="red")
                          ax.add_patch(position)
                          home_team_x.append(120-x)
                          home_team_y.append(y)
                          home_t.append(0)

                      for j in range(len(event[k]['opponentTeam'])):
                          x=event[k]['opponentTeam'][j][0]
                          y=event[k]['opponentTeam'][j][1]
                          position = plt.Circle((120-x,y),2,color="blue")
                          ax.add_patch(position)
                          away_team_x.append(120-x)
                          away_team_y.append(y)
                          away_t.append(1)
                  else:
                      x = event[k]['ball']['location'][0]
                      y = event[k]['ball']['location'][1]
                      positionBall = plt.Circle((x,y),2,color="black")
                      ax.add_patch(positionBall)

                      for i in range(len(event[k]['sameTeam'])):
                          x=event[k]['sameTeam'][i][0]
                          y=event[k]['sameTeam'][i][1]
                          position = plt.Circle((x,y),2,color="blue")
                          ax.add_patch(position)
                          away_team_x.append(x)
                          away_team_y.append(y)
                          away_t.append(1)

                      for j in range(len(event[k]['opponentTeam'])):
                          x=event[k]['opponentTeam'][j][0]
                          y=event[k]['opponentTeam'][j][1]
                          position = plt.Circle((x,y),2,color="red")
                          ax.add_patch(position)
                          home_team_x.append(x)
                          home_team_y.append(y)
                          home_t.append(0)


              df = pd.DataFrame({'x' : home_team_x+away_team_x, 'y' : home_team_y+away_team_y, 'team' : home_t+away_t})

              pitch = Pitch(pitch_type = 'statsbomb')
              team1, team2 = pitch.voronoi(df.x, df.y, df.team)

              t1 = pitch.polygon(team1, ax=ax, fc='blue', ec='white', lw=3, alpha=.4)
              t2 = pitch.polygon(team2, ax=ax, fc='red', ec='white', lw=3, alpha=.4)

              fig.set_size_inches(10, 7)
              plt.show()
              break
