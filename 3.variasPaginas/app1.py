import dash
from server import server
app = dash.Dash(name='app1', sharing=True, server=server, url_base_pathname='/app1')