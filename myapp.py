from wsgiref.simple_server import make_server
import cgi
from cgi import parse_qs, escape


html = """
<html>
<body>
<form method="post">
            <input type="text" name="field1">
            <input type="text" name="field2">
            <input type="submit" value="Submit">
        </form>
   <form method="get" action="get.wsgi">
         <input type="text" name="field1">
         <input type="text" name="field2">
         <input type="submit" value="Submit">
      </form>
	
   <p>
      field1: %s<br>
      field2: %s
    </p>
   </body>
</html>"""

def application(environ, start_response):
    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        response_body = 'field1 = ' + post['field1'].value + '\nfield2 = ' + post['field2'].value
    else:
        d = parse_qs(environ['QUERY_STRING'])
        f1 = d.get('field1', []) 
        f2 = d.get('field2', []) 

   
        response_body = html % (f1 or 'Empty',
                (f2 or 'Empty'))

        status = '200 OK'

   # Now content type is text/html
        response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
        start_response(status, response_headers)

    return [response_body]

