import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("fifa2021.csv")  # Update this to match your file name
    return data

# Main app function
def main():
    # Load the dataset
    try:
        df = load_data()
    except FileNotFoundError:
        st.error("Dataset 'fifa2021.csv' not found. Please download it from Kaggle and place it in the same directory as this script.")
        return

    # Title and description
    st.title("Footballer-dex")
    st.markdown("Search for a footballer and explore their stats, Pokédex-style!")

    # Search bar
    player_name = st.text_input("Enter footballer name:", "").strip().lower()
    
    if player_name:
        # Filter the dataframe based on the input name
        player_data = df[df["name"].str.lower().str.contains(player_name, na=False)]
        
        if not player_data.empty:
            # Display the first matching player
            player = player_data.iloc[0]
            
            # Note: FIFA 21 dataset doesn't include direct image URLs, so we'll skip that
            st.write("No player image available in this dataset.")

            # Display key stats in a Pokédex-like format
            st.subheader(f"#{player['sofifa_id']} - {player['name']}")
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Club**: {player['club_name']}")
                st.write(f"**Nationality**: {player['nationality_name']}")
                st.write(f"**Position**: {player['player_positions']}")
                st.write(f"**Age**: {player['age']}")
                st.write(f"**Height**: {player['height_cm']} cm")
                st.write(f"**Weight**: {player['weight_kg']} kg")
            
            with col2:
                st.write(f"**Overall Rating**: {player['overall']}")
                st.write(f"**Value**: €{player['value_eur']:,}")
                st.write(f"**Wage**: €{player['wage_eur']:,}")
                st.write(f"**Preferred Foot**: {player['preferred_foot']}")
                st.write(f"**Pace**: {player['pace']}")
                st.write(f"**Shooting**: {player['shooting']}")

            # Pokédex-style description
            st.markdown("---")
            st.write(f"**Entry**: {player['name']} is a {player['player_positions']} from {player['nationality_name']}. "
                     f"With a pace of {player['pace']} and shooting skill of {player['shooting']}, "
                     f"this player shines for {player['club_name']}!")
        else:
            st.error("No footballer found with that name. Try again!")
    else:
        st.info("Enter a name to search for a footballer.")

# Run the app
if __name__ == "__main__":
    main()