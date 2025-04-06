pip install matplotlib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'football_mini.csv'
try:
    data = pd.read_csv(file_path, encoding='latin1')
except FileNotFoundError:
    st.error(f"Error: The file {file_path} was not found. Please ensure it is in the same directory as the script.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the CSV file: {e}")
    st.stop()

# Clean up unnecessary columns (both GK and non-GK)
all_columns = ['Name', 'Age', 'Nationality', 'Club', 'Position', 'Value', 'Wage',
               'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes',
               'Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys',
               'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl',
               'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
               'Marking', 'StandingTackle', 'SlidingTackle']
data = data[all_columns]

# Streamlit app
st.set_page_config(layout="wide")

# Updated title
st.title("Football Player Database")

# Search functionality
player_name = st.text_input("Enter a player's name:")

if player_name:
    player = data[data['Name'].str.contains(player_name, case=False, na=False)].copy()

    if player.empty:
        st.write("Player not found.")
    else:
        for index, row in player.iterrows():
            # Player Info
            st.subheader(f"{row['Name']}")
            st.write(f"**{row['Age']} years. {row['Nationality']}**")
            st.write(f"**{row['Position']} • {row['Club']}**")

            # Metrics in columns
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Value", f"${float(row['Value'])/1000:.1f}M")
            with col2:
                st.metric("Wage", f"${float(row['Wage']):.0f}K/wk")
            with col3:
                st.metric("Position", f"{row['Position']}")

            st.markdown("---")  # Divider

            # Determine if the player is a central back or full back
            if row['Position'] in ['LCB', 'RCB', 'LB', 'RB']:
                st.subheader("Defensive Attributes")
                labels = ['Aggression', 'Interceptions', 'Positioning', 'Vision', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle']
                values = [row['Aggression'], row['Interceptions'], row['Positioning'], row['Vision'], row['Composure'], row['Marking'], row['StandingTackle'], row['SlidingTackle']]

                # Horizontal Bar Chart
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.barh(labels, values, color="#1f77b4")  # Use a blue color
                ax.set_xlabel('Rating')
                ax.set_ylabel('Attributes')
                ax.set_title('Defensive Attributes')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                # Add labels to the bars
                for i, v in enumerate(values):
                    ax.text(v + 3, i, str(v), color='black', va='center')

                plt.gca().invert_yaxis()  # Invert y-axis to show the highest value at the top
                plt.tight_layout()

                st.pyplot(fig)

            else:
                # Visualization for other positions
                st.subheader("Player Attributes")
                labels = ['Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing',
                          'Volleys', 'Dribbling', 'Curve', 'FKAccuracy',
                          'LongPassing', 'BallControl']
                values = [row['Crossing'], row['Finishing'], row['HeadingAccuracy'],
                          row['ShortPassing'], row['Volleys'], row['Dribbling'],
                          row['Curve'], row['FKAccuracy'], row['LongPassing'],
                          row['BallControl']]

                # Horizontal Bar Chart
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.barh(labels, values, color="#1f77b4")  # Use a blue color
                ax.set_xlabel('Rating')
                ax.set_ylabel('Attributes')
                ax.set_title('Attributes')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)

                # Add labels to the bars
                for i, v in enumerate(values):
                    ax.text(v + 3, i, str(v), color='black', va='center')

                plt.gca().invert_yaxis()  # Invert y-axis to show the highest value at the top
                plt.tight_layout()

                st.pyplot(fig)

            st.markdown("---")
