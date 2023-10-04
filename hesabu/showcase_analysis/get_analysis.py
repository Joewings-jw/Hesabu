def get_analysed_latex():
  return [
      {
         "latex_expr": "6 \\cdot ( x - 1 ) + 3  =  4 x + 5",
         "status": "correct"
      },
      {
         "latex_expr": "6 x - 6 + 3  =  4 x + 5",
         "status": "correct"
      },
      {
         "latex_expr": "6 x - 9  =  4 x + 5",
         "status": "wrong"
      },
      {
         "latex_expr": "2 x   =  14",
         "status": "cons_error"
      },
      {
         "latex_expr": "x  =  7",
         "status": "cons_error"
      }
   ]



