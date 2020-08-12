from tennisMatchProbability import matchProb



def prediction_point(scA,scB,scsA,scsB,pointA,pointB,price):
 #Predict the next prices for win and lose a point
 #scA,scB - the match score
 #scsA,scsB - the score in the current set
 #pointA,pointB - point score
 #price - the current price
	probr = round(1.0/price,2)
	dct = 
	if pointA == "Av" : pointA = 50
	if pointB == "Av" : pointB = 50
	if scsA == 6 and scsB == 6:
		if pointA > 7 :
			d = pointA - 7
			pointA = 7
			pointB -= d
	prob_match = dct[(scA,scB,scsA,scsB,pointA,pointB)]
	prob_game =[0] + [i*0.01 for i in range(30,71)] + [1.0]
	x = np.array(prob_match)
	y = np.array(prob_game)
	f_match_game = interpolate.interp1d(x, y)
	probp = float( f_match_game(1.0/price))
	scAw,scBw,scsAw,scsBw,pointAw,pointBw = win_score(scA,scB,scsA,scsB,pointA,pointB)
	scAl,scBl,scsAl,scsBl,pointAl,pointBl = lose_score(scA,scB,scsA,scsB,pointA,pointB)
	probmw = calc_prob_match_from_point2(scAw,scBw,scsAw,scsBw,pointAw,pointBw,probp)
	if probmw == 0: probmw = 0.01
	pricew = round(1/probmw,2)
	probml = calc_prob_match_from_point2(scAl,scBl,scsAl,scsBl,pointAl,pointBl,probp)
	if probml == 0: probml = 0.01
	pricel = round(1/probml,2)
	return pricew,pricel

