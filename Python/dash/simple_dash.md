
# Simple Dash

	These are simple code examples to understand how to work with different components of dash
	
## Run server

	import dash
	import dash_core_components as dcc
	import dash_html_components as html



		
	app = dash.Dash()
	app.layout = html.Div([
		html.H1('Yo G bear!'),
		html.Div('Dash - A data product development framework from plotly')
		])

		
	if __name__ == '__main__':
		
		app.run_server(port = 9092)
    
## help, more info on components. type direcly into python console

	help(html.Div)
	
	
## add a graph

	import plotly.express as px

	import dash
	import dash_core_components as dcc
	import dash_html_components as html

	app = dash.Dash()
	app.layout = html.Div([
		html.H1('Yo G bear!'),
		html.Div('Dash - A data product development framework from plotly'),
		
		dcc.Graph(
			id = 'Sample Graph',
			figure = { 
				'data': [
					{'x': [1, 1.25, 2, 2.75, 3], 'y': [4, 3.2, 3, 3.2, 4], 'type': 'line', 'name':'mouth', 'color':'green'}, 
					{'x': [2], 'y': [6], 'type': 'scatter', 'name':'nose', 'color':'green'}],
				
			'layout': {
				'title' : 'Simple chart'}
			}
			)
		])
		
	if __name__ == '__main__':
		
		app.run_server(port = 9092)
		
## Add style to the headers

	import plotly.express as px

	import dash
	import dash_core_components as dcc
	import dash_html_components as html


	app = dash.Dash()
	app.layout = html.Div([
		html.H1(children = 'Yo G bear!',
				style = {
					'textAlign' : 'center',
					'color' : '#456FBV'
					}),
		html.Div(children = 'Dash - A data product development framework from plotly',style = {
					'textAlign' : 'center',
					'color' : '#456FBV'
					}),
		
		dcc.Graph(
			id = 'Sample Graph',
			figure = { 
				'data': [
					{'x': [1, 1.25, 2, 2.75, 3], 'y': [4, 3.2, 3, 3.2, 4], 'type': 'line', 'name':'mouth', 'color':'green'}, 
					{'x': [2], 'y': [6], 'type': 'scatter', 'name':'nose', 'color':'green'}],
				
			'layout': {
				'title' : 'Simple chart'}
			}
			)
		])
		
	if __name__ == '__main__':
		
		app.run_server(port = 9092)
		
		
## change layout settings of graph

	import plotly.express as px

	import dash
	import dash_core_components as dcc
	import dash_html_components as html


	app = dash.Dash()
	app.layout = html.Div([
		html.H1(children = 'Yo G bear!',
				style = {
					'textAlign' : 'center',
					'color' : '#456FBV'
					}),
		html.Div(children = 'Dash - A data product development framework from plotly',style = {
					'textAlign' : 'center',
					'color' : '#456FBV'
					}),
		
		dcc.Graph(
			id = 'Sample Graph',
			figure = { 
				'data': [
					{'x': [1, 1.25, 2, 2.75, 3], 'y': [4, 3.2, 3, 3.2, 4], 'type': 'line', 'name':'mouth', 'color':'green'}, 
					{'x': [2], 'y': [6], 'type': 'scatter', 'name':'nose', 'color':'green', 'size' : '5'}],
				
			'layout': {
				
				'paper_bgcolor' : '#D3D3D1',
				'plot_bgcolor' : '#D3D3D3',
				'font' : {
					'color' : '#456FBV'
					},
				'title' : 'Simple chart'}
			}
			)
		])
		
	if __name__ == '__main__':
		
		app.run_server(port = 9092)
		
		
## variables for colors

	# %% imports
	import plotly.express as px

	import dash
	import dash_core_components as dcc
	import dash_html_components as html

	# %% inputs

	colors = {
		'text' :        '#456FBV',
		'paper_color' : '#D3D3D1',
		'plot_color' :  '#D3D3D3'
		}

	# %% app
	app = dash.Dash()
	app.layout = html.Div([
		html.H1(children = 'Yo G bear!',
				style = {
					'textAlign' : 'center',
					'color' : colors['text']
					}),
		html.Div(children = 'Dash - A data product development framework from plotly',style = {
					'textAlign' : 'center',
					'color' : colors['text']
					}),
		
		dcc.Graph(
			id = 'Sample Graph',
			figure = { 
				'data': [
					{'x': [1, 1.25, 2, 2.75, 3], 'y': [4, 3.2, 3, 3.2, 4], 'type': 'line', 'name':'mouth'}, 
					{'x': [2], 'y': [6], 'type': 'scatter', 'name':'nose'}],
				
			'layout': {
				
				'paper_bgcolor' : colors['paper_color'],
				'plot_bgcolor' : colors['plot_color'],
				'font' : {
					'color' : colors['text']
					},
				'title' : 'Simple chart'}
			}
			)
		])
		

	# %% main
	if __name__ == '__main__':
		
		app.run_server(port = 9092)

## adding plotly scatter plots for eyes

	# %% imports
	import plotly.express as px
	import plotly.graph_objs as go

	import dash
	import dash_core_components as dcc
	import dash_html_components as html


	# %% inputs

	colors = {
		'text' :        '#456FBV',
		'paper_color' : '#D3D3D1',
		'plot_color' :  '#D3D3D3'
		}

	# %% app
	app = dash.Dash()
	app.layout = html.Div([
		html.H1(children = 'Yo G bear!',
				style = {
					'textAlign' : 'center',
					'color' : colors['text']
					}),
		html.Div(children = 'Dash - A data product development framework from plotly',style = {
					'textAlign' : 'center',
					'color' : colors['text']
					}),
		
		dcc.Graph(
			id = 'Sample Graph',
			figure = { 
				'data': [
					{'x': [1.6, 1.65, 2, 2.35, 2.4], 'y': [5, 3.2, 3, 3.2, 5], 'type': 'line', 'name':'mouth'}, 
					{'x': [2], 'y': [6], 'type': 'scatter', 'name':'nose', 'marker_size' : 20},
					go.Scatter(x = [2], y = [6], mode = 'markers', marker_size = 20), # overwrite the small nose
					go.Scatter(x = [1.7, 2.3], y = [8,8], mode = 'markers', marker_size = 10)
					],
				
			'layout': {
				
				'paper_bgcolor' : colors['paper_color'],
				'plot_bgcolor' : colors['plot_color'],
				'font' : {
					'color' : colors['text']
					},
				'title' : 'Simple chart'}
			}
			)
		])
		

	# %% main
	if __name__ == '__main__':
		
		app.run_server(port = 9092)
		
		
## plotly scatterplots only with layout(hovermode)

	# %% imports
	import plotly.graph_objs as go

	import dash
	import dash_core_components as dcc
	import dash_html_components as html



	# %% app
	app = dash.Dash()
	app.layout = html.Div([
		
		dcc.Graph(
			id = 'scatter chart',
			figure = { 
				'data' : [
					go.Scatter(
						x = [1,2,3,4,5,6],
						y = [1,20,5,20,10,20],
						mode = 'lines, markers'
						)
					],
				'layout' : go.Layout(
					title = 'Wedge Up Pattern',
					xaxis = {'title': 'Time'},
					yaxis = {'title': 'Price'},
					hovermode='closest'
					)
				}
			)
		])
		

	# %% main
	if __name__ == '__main__':
		
		app.run_server(port = 9092)
		
		
## more dropdown options and sliders, input boxes, Radio Items, DatePickers, Markdown


	# %% imports
	import dash
	import dash_core_components as dcc
	import dash_html_components as html

	import datetime



	# %% app
	app = dash.Dash()
	app.layout = html.Div([
		
		html.Label('Choose a City'),
		html.Br(),
		dcc.Dropdown(
			id = 'first-dropdown',
			options = [
				{'label' : 'San Fransisco', 'value' : 'SFC'},
				{'label' : 'Des Moines', 'value' : 'DSM'},
				{'label' : 'Springfield', 'value' : 'SFG', 'disabled' : False}
				],
			value = 'NYC',
			multi = True,
			placeholder = 'Select a City',
			disabled = False
			),
		
		html.Br(),
		html.Label('This is a slider'),
		dcc.Slider(
			min = 1,
			max = 10,
			value = 5,
			step = .5,
			marks = {i: str(i) for i in range(10)}
			),
		
		html.Br(),
		html.Label('This is a range slider'),
		dcc.RangeSlider(
			min = 1,
			max = 10,
			step = .5,
			value = [3,7],
			marks = {i: str(i) for i in range(10)}
			),
		
		html.Br(),
		html.Label('This is an input box: '),
		dcc.Input(
			placeholder = 'Input  your name',
			type = 'text',
			value = ''
			), 
		
		html.Br(),
		html.Br(),
		html.Label('This is a text area: '),
		html.Br(),
		dcc.Textarea(
			placeholder = 'Input your Feedback',
			value = 'text',
			style = {'width' : '20%'}
			),
		
		html.Br(),
		html.Button('Submit', id = 'submit-form'),
		
		html.Br(),
		html.Br(),
		html.Label('This is a Checklist: '),
		dcc.Checklist(
			options = [
				{'label' : 'San Fransisco', 'value' : 'SFC'},
				{'label' : 'Des Moines', 'value' : 'DSM'},
				{'label' : 'Springfield', 'value' : 'SFG'}
				],
			value = ['SF', 'NYC']
			),
		
		html.Br(),
		html.Br(),
		html.Label('These are RadioItems: '),
		dcc.RadioItems(
					options = [
				{'label' : 'San Fransisco', 'value' : 'SFC'},
				{'label' : 'Des Moines', 'value' : 'DSM'},
				{'label' : 'Springfield', 'value' : 'SFG'}
				],
			value = 'SF'
			),
		
		html.Br(),
		html.Br(),
		html.Label('Here is a DatePickerSingle: '),
		dcc.DatePickerSingle(
			id = 'dt-pick-single',
			date = datetime.datetime(2015,5,10)
			),
		
		
		html.Br(),
		html.Br(),
		html.Label('Here is a DatePickerSingle: '),
		dcc.DatePickerRange(
			id = 'dt-pick-range',
			start_date = datetime.datetime(2015,5,10),
			end_date_placeholder_text = 'Select date'),
		
		
		html.Br(),
		html.Br(),
		html.Label('Here some markdown text '),
		dcc.Markdown(
			'''
			Dash supports a lot, see more here: https://commonmark.org/help/
			
			Cliffnotes: \n
				   **bold text** \n
				   *italics* \n
				   [links](http://commonmark.org/help) \n
				   inline `code` snippets \n
				   lists, quotes, and more
			
			'''
			)
		
		])    

	# %% main
	if __name__ == '__main__':
		
		app.run_server(port = 9092, debug=True)
