import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_and_clean_data():
    try:
        data = pd.read_csv("scores.csv")
    except FileNotFoundError:
        print("Error: File 'scores.csv' not found.")
        return pd.DataFrame()

    required_columns = ["Player", "Match", "Score"]

    if not all(column in data.columns for column in required_columns):
        print("Error: CSV must contain Player, Match and Score columns.")
        return pd.DataFrame()

    valid_rows = []

    for index, row in data.iterrows():
        row_number = index + 1
        player = row["Player"].strip()
        score = pd.to_numeric(row["Score"], errors="coerce")
        match = pd.to_numeric(row["Match"], errors="coerce")

        if pd.isna(score):
            print(
                f"Row {row_number} skipped: "
                f"invalid Score '{row['Score']}'."
            )
            continue

        if score < 0:
            print(
                f"Row {row_number} skipped: "
                "Score cannot be negative."
            )
            continue

        if player == "":
            print(f"Row {row_number} skipped: missing Player.")
            continue

        if pd.isna(match) or match <= 0:
            print(f"Row {row_number} skipped: invalid Match.")
            continue

        valid_rows.append({
            "Player": player,
            "Match": int(match),
            "Score": float(score)
        })

    cleaned_data = pd.DataFrame(
        valid_rows,
        columns=required_columns
    )

    if cleaned_data.empty:
        print("No valid data to analyse.")

    return cleaned_data


def show_player_stats(data):
    player_avg = data.groupby("Player")["Score"].mean()
    player_best = data.groupby("Player")["Score"].max()
    player_total = data.groupby("Player")["Score"].sum()

    for player in player_avg.index:
        print(
            f"{player}: Avg {player_avg[player]:.2f} | "
            f"Best {player_best[player]:g} | "
            f"Total {player_total[player]:g}"
        )

    top_player = player_avg.idxmax()

    print(
        f"Top performer: {top_player} "
        f"(Avg {player_avg[top_player]:.2f})"
    )

    # Population standard deviation for each player
    player_std = data.groupby("Player")["Score"].std(ddof=0)
    for player in player_std.index:
        print(f"{player} Std Dev: {player_std[player]:.2f}")

def show_statistics_and_trend(data):
    scores = data["Score"]

    print(f"Mean: {np.mean(scores):.2f}")
    print(f"Median: {np.median(scores):.2f}")
    print(f"Std Dev: {np.std(scores):.2f}")
    print(f"Max: {np.max(scores):g}")
    print(f"Min: {np.min(scores):g}")

    highest_row = data.loc[scores.idxmax()]

    print(
        f"Highest scoring performance: "
        f"({highest_row['Player']}, "
        f"Match {highest_row['Match']})"
    )

    match_avg = data.groupby("Match")["Score"].mean()

    print("Match-wise average:")

    for match, average in match_avg.items():
        print(f"Match {match}: {average:.2f}")

    # Line chart: average score by match
    plt.figure(figsize=(8, 5))
    plt.plot(match_avg.index, match_avg.values, marker="o")
    plt.title("Score Trend")
    plt.xlabel("Match Number")
    plt.ylabel("Average Score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Bar chart: average score by player
    player_avg = data.groupby("Player")["Score"].mean()

    plt.figure(figsize=(8, 5))
    plt.bar(player_avg.index, player_avg.values)
    plt.title("Player Average Scores")
    plt.xlabel("Player")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.show()


def main():
    data = load_and_clean_data()

    if data.empty:
        return

    while True:
        print("\n===== SPORTS PERFORMANCE ANALYZER =====")
        print("1. Player stats")
        print("2. Statistics and trend")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_player_stats(data)

        elif choice == "2":
            show_statistics_and_trend(data)

        elif choice == "3":
            print("Exiting Sports Performance Analyzer.")
            break

        else:
            print("Invalid option. Enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
