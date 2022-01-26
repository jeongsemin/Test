def bayes_theorem(p_A, p_Spade, p_A_given_Spade):
    p_A_given_Spade = (p_A_given_Spade * p_A) / p_Spade
    return p_A_given_Spade

p_A = 4/52

p_Spade = 13/52

p_A_given_Spade = 1/13

result = bayes_theorem(p_A, p_Spade, p_A_given_Spade)