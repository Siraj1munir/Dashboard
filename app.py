# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import json
# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('profile_kg.html')  # return a string

@app.route('/welcome')
def welcome():
    return render_template('profile_kg.html')  # render a template

@app.route('/profile_kg')
def profile_kg():
    return render_template('profile_kg.html')
	
	
# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
@app.route('/cafe')
def cafe():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[4]], axis=1)
	data = data.drop_duplicates()
	test1 = data.loc[(data['Location']=="Cafe")]
	test1 = test1.drop(data.columns[[1,2,3]], axis  = 1)
	test1 = test1.drop_duplicates()
	return render_template('cafe.html',tables=[test1.to_html(classes='Switch_id')],titles= data.columns.values)

@app.route('/canopy')
def canopy():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[4]], axis=1)
	data = data.drop_duplicates()
	test1 = data.loc[(data['Location']=="Canopy")]
	test1 = test1.drop(data.columns[[1,2,3]], axis  = 1)
	test1 = test1.drop_duplicates()
	return render_template('canopy.html',tables=[test1.to_html(classes='Switch_id')],titles= data.columns.values)

@app.route('/parking')
def parking():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[4]], axis=1)
	data = data.drop_duplicates()
	test1 = data.loc[(data['Location']=="Parking")]
	test1 = test1.drop(data.columns[[1,2,3]], axis  = 1)
	test1 = test1.drop_duplicates()
	return render_template('parking.html',tables=[test1.to_html(classes='Switch_id')],titles= data.columns.values)

@app.route('/library')
def library():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[4]], axis=1)
	data = data.drop_duplicates()
	test1 = data.loc[(data['Location']=="Library")]
	test1 = test1.drop(data.columns[[1,2,3]], axis  = 1)
	test1 = test1.drop_duplicates()
	return render_template('library.html',tables=[test1.to_html(classes='Switch_id')],titles= data.columns.values)
	
@app.route('/located_on_time')
def located_on_time():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[0,1,4]], axis=1)
	test1 = data.loc[(data['Location']=='Canopy') & (data['Time']== '2:40:51')]
	test1 = test1.drop(data.columns[[0]], axis  = 1)
	return render_template('located_on_time.html',tables=[test1.to_html(classes='Switch_id')],titles= data.columns.values)

@app.route('/j_visited')
def j_visited():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[1, 2, 4]], axis=1)
	data = data.drop_duplicates()
	test1 = data.loc[(data['Name']=='Jahanzaib')]
	test1 = test1.drop(data.columns[[0]], axis  = 1)
	return render_template('j_visited.html',tables=[test1.to_html(classes='Location')],titles= data.columns.values)

@app.route('/a_visted')
def a_visted():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[1, 2, 4]], axis=1)
	data = data.drop_duplicates()
	test1 = data.loc[(data['Name']=='Asad')]
	test1 = test1.drop(data.columns[[0]], axis  = 1)
	return render_template('j_visited.html',tables=[test1.to_html(classes='Location')],titles= data.columns.values)

@app.route('/m_visited')
def m_visited():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[1, 2, 4]], axis=1)
	data = data.drop_duplicates()
	test1 = data.loc[(data['Name']=='Mohib')]
	test1 = test1.drop(data.columns[[0]], axis  = 1)
	return render_template('j_visited.html',tables=[test1.to_html(classes='Location')],titles= data.columns.values)

@app.route('/r_visited')
def r_visited():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[1, 2, 4]], axis=1)
	data = data.drop_duplicates()
	test1 = data.loc[(data['Name']=='Reyan')]
	test1 = test1.drop(data.columns[[0]], axis  = 1)
	return render_template('r_visited.html',tables=[test1.to_html(classes='Location')],titles= data.columns.values)
	
@app.route('/switch_3')
def switch_3():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[1, 2, 3]], axis=1)
	data = data.drop_duplicates()
	test1 = data.loc[(data['Switch_id']==3)]
	test1 = test1.drop(data.columns[[1]], axis  = 1)
	return render_template('switch_3.html',tables=[test1.to_html(classes='Location')],titles= data.columns.values)
	
@app.route('/inference')
def inference():
	data = pd.read_csv('log.csv')
	data = data.drop(data.columns[[2, 4]], axis=1)
	data = data.drop_duplicates()
	test1 = data.loc[(data['Name']=="Hamza Gaya") & (data['Date'] == "Siraj Munir")]
	test1 = test1.drop(data.columns[[0,1]], axis  = 1)
	return render_template('inference.html',tables=[test1.to_html(classes='Location')],titles= data.columns.values)
	
# start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug=True)