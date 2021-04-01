from flask import Flask, render_template, request
import random

web_site = Flask(__name__)


@web_site.route('/about')
def about():
    foodList = [
        'mac and cheese', 'burgers', 'ice cream, obvi', 'pizza', 'brownies',
        'cookies'
    ]
    food = random.choice(foodList)

    return render_template('about.html', ffood=food)


@web_site.route('/')
def home():
  
  return render_template('index.html')

@web_site.route('/submit', methods=['POST'])
def submit_form():
  exunval = request.form.get('exunval')
  exratunval= request.form.get('exratunval')
  
  def validation(x):
    x.isnumeric()
    if x.isnumeric() == True:
    
      return x
    if x.isnumeric() == False:
      return "Error. Please imput a number with no decimals or negatives."
  if validation(exunval) == exunval:
    exval = exunval
    exvalboo = False
  else:
   exvalboo = True
  if exvalboo == False:
    print("Miles Walked: ",exval)
  else:
    print("Error. Please imput a number with no decimals or negatives.")
  if validation(exratunval) == exratunval:
    exratval = exratunval
    exratvalboo = False
  else:
    exratvalboo = True
  if exratvalboo == False:
    print("You want to get ",exratval,"minutes per mile you walk.")
  else:
    print("Error, please imput a number with no decimal points or negatives.")

  def get_game_minutes(exercise,ratio):
    if exratvalboo or exvalboo:
      return "NOPE."
    else:
      return exercise*ratio
    ## Just an idea, but maybe once we had most of this done, we could put confetti or one of those little party hat things bursting as a little rewarding animation? It would only last like two sec but I think it would be cool
  if not exratvalboo and  not exvalboo:
    nexratval =  int(exratval)
    nexval = int(exval)
  if get_game_minutes(1, 1) == 1:
  ## I decided to do one and one just to reduce complexity
      exmink = nexval*nexratval
  return render_template('submit.html', exmin=exmink)
  

web_site.run(host='0.0.0.0', port=8080)
