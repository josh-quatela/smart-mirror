f = open('todo','w')

message = """
<html>
<body style="background-color:black; position:relative; left:820px; top:400px;">

<h2 style = "color:white; opacity:10; "><b>To-Do List</b></h2>

<ul style = "list-style-type:circle;">
    <li style="color:white; opacity:10;"><b>Feed the dog</b></li>
    <li style="color:white; opacity:10;"><b>Take out the trash</b></li>
    <li style="color:white; opacity:10;"><b>Text Karen</b></li>
</ul>

</body>
</html>
"""
f.write(message)
f.close()
