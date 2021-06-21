import helperfuncs
import distance_matrices

KEYWORD = input('Enter your Search Query ')
sq_formatter = helperfuncs.TextFormatting()
KEYWORD = sq_formatter.SearchStringCompatibility(KEYWORD)

distance_matrices.GetData(KEYWORD, include_features=False)
SHAPE = int(input('Enter number of entries you want to compare '))
matrix = distance_matrices.distance_calc(shape=SHAPE)
distance_matrices.compare(matrix, confidence_score=0.75, omit=False)
