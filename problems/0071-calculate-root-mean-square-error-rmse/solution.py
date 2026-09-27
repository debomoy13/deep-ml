
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	y_true=np.array(y_true)
	y_pred=np.array(y_pred)
	n=len(y_true)
	rmse_res = np.sqrt(np.mean((y_true - y_pred) ** 2))

	return round(rmse_res,3)
