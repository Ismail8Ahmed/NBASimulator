import random

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

nba_teams = ["Golden State Warriors", "Cleveland Cavaliers"]


def four_factors():
    # Based on 2020-2021 regular season data on Basketball Reference
    efg = {"GSW":0.551, "CLE":0.508}
    tov = {"GSW":13.3, "CLE":13.9}
    orr = {"GSW":17.9, "CLE":23.6}
    ftr = {"GSW":0.188, "CLE":0.194}

    off_four_factors_formula = {"GSW":(efg.get("GSW") - tov.get("GSW") - orr.get("GSW") - ftr.get("GSW")), "CLE":(efg.get("CLE") - tov.get("CLE") - orr.get("CLE") - ftr.get("CLE"))}
    print("OFF FOUR FACTORS FORMULA", off_four_factors_formula)
    return off_four_factors_formula


four_factors()

def scoring_distro():
    # randomizes the distribution of actual points scored by both teams in the 2020-2021 regular season
    gsw_df = pd.read_csv("simple_warriors_game_log.csv")
    cle_df = pd.read_csv("simple_cavs_game_log.csv")
    gsw_df_numpy = gsw_df.to_numpy()
    cle_df_numpy = cle_df.to_numpy()
    print("GSW GAME LOG", gsw_df.describe)
    print("\n\nCLE GAME LOG", cle_df.describe)


    random_off_gsw = random.gauss(gsw_df_numpy[0].mean(), gsw_df_numpy[0].std())
    random_off_cle = random.gauss(cle_df_numpy[0].mean(), cle_df_numpy[0].std())
    random_off_both = [random_off_gsw, random_off_cle]


    random_def_gsw = random.gauss(gsw_df_numpy[1].mean(), gsw_df_numpy[1].std())
    random_def_cle = random.gauss(cle_df_numpy[1].mean(), cle_df_numpy[1].std())
    random_def_both = [random_def_gsw, random_def_cle]


    random_off_and_def = [random_off_both, random_def_both]
    return random_off_and_def


    print("RANDOM OFF GSW", random_off_gsw)
    print("\nRANDOM OFF CLE", random_off_cle)

    print("\nRANDOM DEF GSW", random_def_gsw)
    print("\nRANDOM DEF CLE", random_def_cle)


scoring_distro()


first_dubs_standard_deviation = float(four_factors().get("GSW") * 0.05)
print("\nGSW: FOUR FACTORS RETURN VALUE", four_factors())
print("\nGSW: FOUR FACTORS RETURN VALUE GSW NUMBER", four_factors().get("GSW"))
random_four_factor_dubs = random.gauss(float(four_factors().get("GSW")), first_dubs_standard_deviation)

print("GSW Scoring Distro Return", scoring_distro())
raw_dubs_score = int( float( float(scoring_distro()[0][0]) - random_four_factor_dubs) / 1.3)

second_dubs_standard_deviation = raw_dubs_score * 0.05
randomized_dubs_score = int(random.gauss(raw_dubs_score, second_dubs_standard_deviation))

first_cavs_standard_deviation = float(four_factors().get("CLE") * 0.05)
print("\nCLE: FOUR FACTORS RETURN VALUE", four_factors())
print("\nCLE: FOUR FACTORS RETURN VALUE CLE NUMBER", four_factors().get("CLE"))
random_four_factor_cavs = random.gauss(float(four_factors().get("CLE")), first_cavs_standard_deviation)

print("CLE Scoring Distro Return", scoring_distro())
raw_cavs_score = int( float( float(scoring_distro()[1][1]) - random_four_factor_cavs) / 1.3)

second_cavs_standard_deviation = raw_dubs_score * 0.05
randomized_cavs_score = int(random.gauss(raw_cavs_score, second_cavs_standard_deviation))


print("*****************************************************\n\n*****    Random Four Factor Dubs:    ", random_four_factor_dubs)

print("*****************************************************\n\n*****    DUBS SCORE:    ", randomized_dubs_score)

print("*****************************************************\n\n*****    Random Four Factor Cavs:    ", random_four_factor_cavs)

print("*****************************************************\n\n*****    Cavs SCORE:    ", randomized_cavs_score)

plt.hist(randomized_dubs_score, randomized_cavs_score)

