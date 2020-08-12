from tennisMatchProbability import matchProb
from p_estimation import prediction_point
from scipy.optimize import minimize



# Calculate p and q ------------------

# Input ProbA, the probability of player A winning the match pre-game odds. Uses scipy optimise to find a minimum of the matchProb function
# Does not produce a unique minimum but is set to be close to 0.7,0.3 for win serve and win return. 
def findp(ProbA):

	probB = 1-probA


	def f(x):
		return matchProb(x[0], x[1], gv=0, gw=0, sv=0, sw=0, mv=0, mw=0, sets=3) - probA

	def con(x):
	    return matchProb(x[0], x[1], gv=0, gw=0, sv=0, sw=0, mv=0, mw=0, sets=3) - probB

	cons = [{'type':'eq', 'fun': con}]



	x0 = [0.7,0.3]
	result = minimize(f, x0, constraints=cons)
	if result.success:
	    fitted_params = result.x
	    p,q = fitted_params
	else:
	    raise ValueError(result.message)

	return p,q



# Produces odd for each point and stores in odds list, given p and q
odds = []
for i in points:
	odds.append(matchProb(p, q, gv=gv, gw=gw, sv=sv, sw=sw, mv=mv, mw=mw, sets=3))






