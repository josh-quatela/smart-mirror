f = open('calendar','w')

message = """
<html>
<body style="background-color:black; position:relative; top:300px;">

<h2 style = "color:white; opacity:10; "><b>November</b></h2>

<pre><p style="color:white; opacity:10;"><b>Sun   Mon   Tue   Wed   Thu   Fri   Sat</b></p></pre>
<pre><p style="color:white; opacity:10;"><b>                              1     2  </b></p></pre>
<pre><p style="color:white; opacity:10;"><b>3     4     5     6     7     8     9  </b></p></pre>
<pre><p style="color:white; opacity:10;"><b>10    11    12    13    14    15    16 </b></p></pre>
<pre><p style="color:white; opacity:10;"><b>17    18   (19)   20    21    22    23 </b></p></pre>
<pre><p style="color:white; opacity:10;"><b>24    25    26    27    28    29    30 </b></p></pre>

</body>
</html>
"""
f.write(message)
f.close()