from statsbombpy import sb
import pandas as pd
from matplotlib.patches import Ellipse
import matplotlib.patheffects as path_effects
from mplsoccer.pitch import Pitch


events = sb.events(match_id=3835319,fmt="dict")
count1 = 0
count2 = 0
flag1 = 0
flag2 = 0
flag3 = 0

print("England Women's -> black")
print("Austria Women's -> red")

for k in events.keys():
  if events[k]['type']['name'] == 'Pass':
    if events[k]['pass'].get('shot_assist') is not None or events[k]['pass'].get('goal_assist') is not None:
      squad = 0
      t = events[k]['team']
      time = events[k]['timestamp']
      loc = events[k]['location']
      s =  events[k]['pass']['assisted_shot_id']
      pitch = Pitch(pitch_type = 'statsbomb')
      fig, ax = pitch.draw()
      if t['name'] == "England Women's":
          squad = 1
          count1 += 1
      else:
        count2 +=1
      if squad == 1:
        pitch.scatter(events[k]['location'][0],events[k]['location'][1],ax=ax, c='black')
        pitch.scatter(events[s]['location'][0],events[s]['location'][1],ax=ax, c='black')
        pitch.plot([loc[0], events[s]['location'][0]],[loc[1], events[s]['location'][1]],ax=ax, c='black')
      else:
        pitch.scatter(events[k]['location'][0],events[k]['location'][1],ax=ax, c='red')
        pitch.scatter(events[s]['location'][0],events[s]['location'][1],ax=ax, c='red')
        pitch.plot([loc[0], events[s]['location'][0]],[loc[1], events[s]['location'][1]],ax=ax, c='red')

      for relatEv in events.keys():
        flag1 = 0
        if events[relatEv]['type']['name'] == 'Pass' and events[relatEv]['timestamp'] <= time and events[relatEv]['team'] == t:
          if events[relatEv]['pass']['end_location'][0] == loc[0] and events[relatEv]['pass']['end_location'][1] == loc[1]:
            if squad == 1:
              pitch.scatter(events[relatEv]['location'][0],events[relatEv]['location'][1],ax=ax, c='black')
              pitch.plot([events[relatEv]['location'][0], loc[0]],[events[relatEv]['location'][1], loc[1]],ax=ax, c='black')
            else :
              pitch.scatter(events[relatEv]['location'][0],events[relatEv]['location'][1],ax=ax, c='red')
              pitch.plot([events[relatEv]['location'][0], loc[0]],[events[relatEv]['location'][1], loc[1]],ax=ax, c='red')

            loc2 = events[relatEv]['location']
            flag1 = 1
          
        if events[relatEv]['type']['name'] == 'Carry' and events[relatEv]['carry']['end_location'][0] == loc[0] and events[relatEv]['carry']['end_location'][1] == loc[1] and events[relatEv]['timestamp'] <= time and events[relatEv]['team'] == t:
            if squad == 1:
              pitch.plot([events[relatEv]['location'][0],loc[0]], [events[relatEv]['location'][1],loc[1]], ax=ax, ls='--', c='black')
            else:
              pitch.plot([events[relatEv]['location'][0],loc[0]], [events[relatEv]['location'][1],loc[1]], ax=ax, ls='--', c='red')

            loc2 = events[relatEv]['location']
            flag1 = 1

        if flag1 == 1:
          for rel2 in events.keys():
                flag2 = 0
                if events[rel2]['type']['name'] == 'Pass' and events[rel2]['timestamp'] <= time and events[rel2]['team'] == t:
                  if events[rel2]['pass']['end_location'][0] == loc2[0] and events[rel2]['pass']['end_location'][1] == loc2[1]:
                    if squad == 1:
                      pitch.scatter(events[rel2]['location'][0],events[rel2]['location'][1],ax=ax, c='black')
                      pitch.plot([events[rel2]['location'][0], loc2[0]], [events[rel2]['location'][1], loc2[1]], ax=ax, c='black')
                    else :
                      pitch.scatter(events[rel2]['location'][0],events[rel2]['location'][1],ax=ax, c='red')
                      pitch.plot([events[rel2]['location'][0], loc2[0]], [events[rel2]['location'][1], loc2[1]], ax=ax, c='red')

                    loc3 = events[rel2]['location']
                    flag2 = 1

                if events[rel2]['type']['name'] == 'Carry' and events[rel2]['carry']['end_location'][0] == loc2[0] and events[rel2]['carry']['end_location'][1] == loc2[1] and events[rel2]['timestamp'] <= time and events[rel2]['team'] == t:
                    if squad == 1:
                      pitch.plot([events[rel2]['location'][0],loc2[0]], [events[rel2]['location'][1],loc2[1]], ax=ax, ls='--', c='black')
                    else:
                      pitch.plot([events[rel2]['location'][0],loc2[0]], [events[rel2]['location'][1],loc2[1]], ax=ax, ls='--', c='red')

                    loc3 = events[rel2]['location']
                    flag2 = 1
                      
                if flag2 == 1:
                  for rel3 in events.keys():
                          flag3 = 0
                          if events[rel3]['type']['name'] == 'Pass' and events[rel3]['timestamp'] <= time and events[rel3]['team'] == t:
                              if events[rel3]['pass']['end_location'][0] == loc3[0] and events[rel3]['pass']['end_location'][1] == loc3[1]:
                                  if squad == 1:
                                    pitch.scatter(events[rel3]['location'][0],events[rel3]['location'][1],ax=ax, c='black')
                                    pitch.plot([events[rel3]['location'][0], loc3[0]],[events[rel3]['location'][1], loc3[1]],ax=ax, c='black')
                                  else:
                                    pitch.scatter(events[rel3]['location'][0],events[rel3]['location'][1],ax=ax, c='red')
                                    pitch.plot([events[rel3]['location'][0], loc3[0]],[events[rel3]['location'][1], loc3[1]],ax=ax, c='red')

                                  loc4 = events[rel3]['location']
                                  flag3 = 1
                              
                          if events[rel3]['type']['name'] == 'Carry' and events[rel3]['carry']['end_location'][0] == loc3[0] and events[rel3]['carry']['end_location'][1] == loc3[1] and events[rel3]['timestamp'] <= time and events[rel3]['team'] == t:
                                if squad == 1:
                                  pitch.plot([events[rel3]['location'][0],loc3[0]], [events[rel3]['location'][1],loc3[1]], ax=ax, ls='--', c='black')
                                else:
                                  pitch.plot([events[rel3]['location'][0],loc3[0]], [events[rel3]['location'][1],loc3[1]], ax=ax, ls='--', c='red')

                                loc4 = events[rel3]['location']
                                flag3 = 1

                          if flag3 == 1:
                            for rel4 in events.keys():
                                if events[rel4]['type']['name'] == 'Pass' and events[rel4]['timestamp'] <= time and events[rel4]['team'] == t:
                                    if events[rel4]['pass']['end_location'][0] == loc4[0] and events[rel4]['pass']['end_location'][1] == loc4[1]:
                                        if squad == 1:
                                          pitch.scatter(events[rel4]['location'][0],events[rel4]['location'][1],ax=ax, c='black')
                                          pitch.plot([events[rel4]['location'][0], loc4[0]],[events[rel4]['location'][1], loc4[1]],ax=ax, c='black')
                                        else:
                                          pitch.scatter(events[rel4]['location'][0],events[rel4]['location'][1],ax=ax, c='red')
                                          pitch.plot([events[rel4]['location'][0], loc4[0]],[events[rel4]['location'][1], loc4[1]],ax=ax, c='red')
                                    
                                if events[rel4]['type']['name'] == 'Carry' and events[rel4]['carry']['end_location'][0] == loc4[0] and events[rel4]['carry']['end_location'][1] == loc4[1] and events[rel4]['timestamp'] <= time and events[rel4]['team'] == t:
                                      if squad == 1:
                                        pitch.plot([events[rel4]['location'][0],loc4[0]], [events[rel4]['location'][1],loc4[1]], ax=ax, ls='--', c='black')
                                      else:
                                        pitch.plot([events[rel4]['location'][0],loc4[0]], [events[rel4]['location'][1],loc4[1]], ax=ax, ls='--', c='red')

print("Attacking Englad = ", count1)
print("Attacking Austria = ", count2)
print("-- = Carry")
print("- = Pass")