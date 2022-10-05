# Import useful library
import pandas as pd
import numpy as np
from statsbombpy import sb
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import seaborn as sns


class App:
    def __init__(self):
        # Select the possible competitions with 360 data
        self.competitionsDB = pd.DataFrame(sb.competitions())
        self.competitionsDB.dropna(subset=['match_available_360'], inplace=True)
        self.competitions_names = self.competitionsDB['competition_name'].to_numpy()

        # Create the tkinter interface
        self.app = tk.Tk()
        self.app.geometry('1400x750')

        # Create the title of the interface
        self.title = tk.Label(text="Python rocks!")
        self.title.pack()

        ## Add the competition selector Menu
        self.competition_name_variable = tk.StringVar(self.app)
        self.competition_name_variable.set(self.competitions_names[0])

        self.opt_compet = tk.OptionMenu(self.app, self.competition_name_variable, *self.competitions_names)
        self.opt_compet.config(width=90, font=('Helvetica', 12))
        self.opt_compet.pack(side="top")

        ## Add Team Selector Menu
        # Create default Option Menu for team (will update with modification on opt_competition)

        # Get the ID of the competition from the previous selector
        self.selected_competition = self.competitionsDB[
            self.competitionsDB['competition_name'] == self.competition_name_variable.get()]
        self.competition_identifiers = (self.selected_competition['competition_id'].to_numpy()[0],
                                        self.selected_competition['season_id'].to_numpy()[0])

        # Get the matches corresponding to selected competition
        self.competition_matches = sb.matches(self.competition_identifiers[0], self.competition_identifiers[1])
        self.all_teams = np.unique(np.concatenate((self.competition_matches['home_team'].to_numpy(),
                                                   self.competition_matches['away_team'].to_numpy())))

        # Create the team name variable
        self.team_name_variable = tk.StringVar(self.app)
        self.team_name_variable.set(self.all_teams[0])

        # Create the selector
        self.opt_team = tk.OptionMenu(self.app, self.team_name_variable, *self.all_teams)
        # Update the options of the selector for each modification on competition selector
        self.competition_name_variable.trace("w", self.update_teams_menu)
        # Add the selector to the app
        self.opt_team.config(width=90, font=('Helvetica', 12))
        self.opt_team.pack(side="top")

        ## Add Game Selector Menu
        # FIXME : Add another selector later to handle multiple phase of the competition
        # Select the game corresponding to the team and the competition selected
        self.team_matches = self.competition_matches.loc[
            (self.competition_matches['home_team'] == self.team_name_variable.get()) | (
                    self.competition_matches['away_team'] == self.team_name_variable.get())]
        self.all_opponents = list(
            np.unique([opponent_name for opponent_name in self.team_matches['home_team'].to_numpy()] +
                      [opponent_name for opponent_name in self.team_matches['away_team'].to_numpy()]))
        self.all_opponents.remove(self.team_name_variable.get())

        # Create the team name variable
        self.opponent_name_variable = tk.StringVar(self.app)
        self.opponent_name_variable.set(self.all_opponents[0])

        # Create the selector
        self.opt_opponent = tk.OptionMenu(self.app, self.opponent_name_variable, *self.all_opponents)
        # Update the options of the selector for each modification on competition selector
        self.team_name_variable.trace("w", self.update_matches_menu)
        # Add the selector to the app
        self.opt_opponent.config(width=90, font=('Helvetica', 12))
        self.opt_opponent.pack(side="top")

        # Create the range for the min / max minute of the event
        self.min_min = tk.Scale(self.app, from_=0, to=90, orient='horizontal')
        self.min_min.set(0)
        self.min_min.pack()
        self.max_min = tk.Scale(self.app, from_=0, to=90, orient='horizontal')
        self.max_min.set(90)
        self.max_min.pack()

        # Create button to activate the heatmap
        button = tk.Button(self.app, text="Get Heatmap", command=self.create_heatmaps)
        button.pack()

        self.app.mainloop()

    def update_teams_menu(self, *args):
        # Delete previous team selector options
        self.opt_team['menu'].delete(0, 'end')

        # Get the ID of the competition from the previous selector
        self.selected_competition = self.competitionsDB[
            self.competitionsDB['competition_name'] == self.competition_name_variable.get()]
        self.competition_identifiers = (self.selected_competition['competition_id'].to_numpy()[0],
                                        self.selected_competition['season_id'].to_numpy()[0])

        # Get the matches corresponding to selected competition
        self.competition_matches = sb.matches(self.competition_identifiers[0], self.competition_identifiers[1])
        self.all_teams = np.unique(np.concatenate((self.competition_matches['home_team'].to_numpy(),
                                                   self.competition_matches['away_team'].to_numpy())))
        self.team_name_variable.set(self.all_teams[0])

        # Write new options for each team in the competitions
        for team in self.all_teams:
            self.opt_team['menu'].add_command(label=team, command=lambda value=team: self.team_name_variable.set(value))

    def update_matches_menu(self, *args):
        # Delete previous team selector options
        self.opt_opponent['menu'].delete(0, 'end')

        self.team_matches = self.competition_matches.loc[
            (self.competition_matches['home_team'] == self.team_name_variable.get()) | (
                    self.competition_matches['away_team'] == self.team_name_variable.get())]
        self.all_opponents = list(
            np.unique([opponent_name for opponent_name in self.team_matches['home_team'].to_numpy()] +
                      [opponent_name for opponent_name in self.team_matches['away_team'].to_numpy()]))
        self.all_opponents.remove(self.team_name_variable.get())

        self.opponent_name_variable.set(self.all_opponents[0])

        # Write new options for each team in the competitions
        for team in self.all_opponents:
            self.opt_opponent['menu'].add_command(label=team,
                                                  command=lambda value=team: self.opponent_name_variable.set(value))

    def create_heatmaps(self, *args):
        """"""
        # Get match_id
        # FIXME : Handle multiple game with these characteristics
        match_home = self.team_matches.loc[(self.team_matches['home_team'] == self.team_name_variable.get()) &
                                           (self.team_matches['away_team'] == self.opponent_name_variable.get())]
        match_away = self.team_matches.loc[(self.team_matches['home_team'] == self.opponent_name_variable.get()) &
                                           (self.team_matches['away_team'] == self.team_name_variable.get())]
        self.match = pd.concat([match_home, match_away])
        self.match_id = self.match.iloc[0]['match_id']

        # Get all events corresponding to the game
        self.events_df = pd.DataFrame(sb.events(self.match_id))
        # FIXME : Depending on the timestamp as well
        self.events_df = self.events_df.loc[
            (self.events_df['minute'] >= self.min_min.get()) & (self.events_df['minute'] <= self.max_min.get())]

        # Get all 360 corresponding to the game
        # FIXME : Problem to retrieve data from some matches
        self.frames_df = pd.DataFrame(sb.frames(self.match_id))

        self.x_pos = []
        self.y_pos = []

        for frame in self.frames_df.iterrows():
            self.corres_event = self.events_df[self.events_df['id'] == frame[1]['id']]
            if self.corres_event.empty:
                continue
            team_possession = True if self.corres_event['team'].to_numpy()[0] == self.team_name_variable.get() else False

            if ((team_possession) & (frame[1]['teammate'])) | ((not team_possession) & (not frame[1]['teammate'])):
                self.x_pos.append(frame[1]['location'][0])
                self.y_pos.append(frame[1]['location'][1])

        # Draw the pitch

        # Create figure
        fig = plt.figure()
        fig.set_size_inches(7, 5)
        ax = fig.add_subplot(1, 1, 1)

        # Pitch Outline & Centre Line
        plt.plot([0, 0], [0, 90], color="black")
        plt.plot([0, 130], [90, 90], color="black")
        plt.plot([130, 130], [90, 0], color="black")
        plt.plot([130, 0], [0, 0], color="black")
        plt.plot([65, 65], [0, 90], color="black")

        # Left Penalty Area
        plt.plot([16.5, 16.5], [65, 25], color="black")
        plt.plot([0, 16.5], [65, 65], color="black")
        plt.plot([16.5, 0], [25, 25], color="black")

        # Right Penalty Area
        plt.plot([130, 113.5], [65, 65], color="black")
        plt.plot([113.5, 113.5], [65, 25], color="black")
        plt.plot([113.5, 130], [25, 25], color="black")

        # Left 6-yard Box
        plt.plot([0, 5.5], [54, 54], color="black")
        plt.plot([5.5, 5.5], [54, 36], color="black")
        plt.plot([5.5, 0.5], [36, 36], color="black")

        # Right 6-yard Box
        plt.plot([130, 124.5], [54, 54], color="black")
        plt.plot([124.5, 124.5], [54, 36], color="black")
        plt.plot([124.5, 130], [36, 36], color="black")

        # Prepare Circles
        centreCircle = plt.Circle((65, 45), 9.15, color="black", fill=False)
        centreSpot = plt.Circle((65, 45), 0.8, color="black")
        leftPenSpot = plt.Circle((11, 45), 0.8, color="black")
        rightPenSpot = plt.Circle((119, 45), 0.8, color="black")

        # Draw Circles
        ax.add_patch(centreCircle)
        ax.add_patch(centreSpot)
        ax.add_patch(leftPenSpot)
        ax.add_patch(rightPenSpot)

        # Prepare Arcs
        leftArc = Arc((11, 45), height=18.3, width=18.3, angle=0, theta1=310, theta2=50, color="black")
        rightArc = Arc((119, 45), height=18.3, width=18.3, angle=0, theta1=130, theta2=230, color="black")

        # Draw Arcs
        ax.add_patch(leftArc)
        ax.add_patch(rightArc)

        # Tidy Axes
        plt.axis('off')

        sns.kdeplot(self.x_pos, self.y_pos, shade=True, n_levels=15, thresh=0)
        plt.ylim(0, 90)
        plt.xlim(0, 130)

        # Display Pitch
        plt.show()
