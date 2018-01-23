#!/usr/bin/env python

"""
a simple script can run and test your html rendering classes.

Uncomment the steps as you add to your rendering.

"""

from io import StringIO

# importing the html_rendering code with a short name for easy typing.
import html_render as html_render
# reloading in case you are running this in iPython
#  -- we want to make sure the latest version is used
import importlib
importlib.reload(html_render)


# writing the file out:
def render_page(page, filename):
    """
    render the tree of elements

    This uses StringIO to render to memory, then dump to console and
    write to file -- very handy!
    """

    f = StringIO()
    page.render(f, "    ")

    f.seek(0)

    print(f.read())

    f.seek(0)
    open(filename, 'w').write(f.read())


# Step 1
#########

# page = html_render.Element()

# page.append("Here is a paragraph of text -- there could be more of them, "
#             "but this is enough  to show that we can do some text")

# page.append("And here is another piece of text -- you should be able to add any number")

# render_page(page, "test_html_output1.html")

# The rest of the steps have been commented out.
#  Uncomment them a you move along with the assignment.

# ## Step 2
# ##########

# page = html_render.Html()

# body = html_render.Body()

# body.append(html_render.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text"))

# body.append(html_render.P("And here is another piece of text -- you should be able to add any number"))

# page.append(body)

# render_page(page, "test_html_output2.html")

# # Step 3
# ##########

# page = html_render.Html()

# head = html_render.Head()
# head.append(html_render.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = html_render.Body()

# body.append(html_render.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text"))
# body.append(html_render.P("And here is another piece of text -- you should be able to add any number"))

# page.append(body)

# render_page(page, "test_html_output3.html")

# # Step 4
# ##########

# page = html_render.Html()

# head = html_render.Head()
# head.append(html_render.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = html_render.Body()

# body.append(html_render.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# page.append(body)

# render_page(page, "test_html_output4.html")

# # Step 5
# #########

# page = html_render.Html()

# head = html_render.Head()
# head.append(html_render.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = html_render.Body()

# body.append(html_render.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# body.append(html_render.Hr())

# page.append(body)

# render_page(page, "test_html_output5.html")

# # Step 6
# #########

# page = html_render.Html()

# head = html_render.Head()
# head.append(html_render.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = html_render.Body()

# body.append(html_render.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#               style="text-align: center; font-style: oblique;"))

# body.append(html_render.Hr())

# body.append("And this is a ")
# body.append( html_render.A("http://google.com", "link") )
# body.append("to google")

# page.append(body)

# render_page(page, "test_html_output6.html")

# # Step 7
# #########

page = html_render.Html()

head = html_render.Head()
head.append(html_render.Title("PythonClass = Revision 1087:"))

page.append(head)

body = html_render.Body()

body.append( html_render.H(2, "PythonClass - Class 6 example") )

body.append(html_render.P("Here is a paragraph of text -- there could be more of them, "
                 "but this is enough  to show that we can do some text",
              style="text-align: center; font-style: oblique;"))

body.append(html_render.Hr())

list = html_render.Ul(id="TheList", style="line-height:200%")

list.append( html_render.Li("The first item in a list") )
list.append( html_render.Li("This is the second item", style="color: red") )

item = html_render.Li()
item.append("And this is a ")
item.append( html_render.A("http://google.com", "link") )
item.append("to google")

list.append(item)

body.append(list)

page.append(body)

render_page(page, "test_html_output7.html")

# # Step 8
# ########

# page = html_render.Html()


# head = html_render.Head()
# head.append( html_render.Meta(charset="UTF-8") )
# head.append(html_render.Title("PythonClass = Revision 1087:"))

# page.append(head)

# body = html_render.Body()

# body.append( html_render.H(2, "PythonClass - Class 6 example") )

# body.append(html_render.P("Here is a paragraph of text -- there could be more of them, "
#                  "but this is enough  to show that we can do some text",
#                  style="text-align: center; font-style: oblique;"))

# body.append(html_render.Hr())

# list = html_render.Ul(id="TheList", style="line-height:200%")

# list.append( html_render.Li("The first item in a list") )
# list.append( html_render.Li("This is the second item", style="color: red") )

# item = html_render.Li()
# item.append("And this is a ")
# item.append( html_render.A("http://google.com", "link") )
# item.append("to google")

# list.append(item)

# body.append(list)

# page.append(body)

# render_page(page, "test_html_output8.html")
