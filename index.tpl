<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Program Design for Socio-Environmental Startups">

  <title>Jaaga &ndash; Project Sphere &ndash; Responses</title>

  <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/pure-min.css">

  <!--[if lte IE 8]>

  <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/grids-responsive-old-ie-min.css">

  <![endif]-->
  <!--[if gt IE 8]><!-->

  <link rel="stylesheet" href="http://yui.yahooapis.com/pure/0.6.0/grids-responsive-min.css">

  <!--<![endif]-->

  <!--[if lte IE 8]>
  <link rel="stylesheet" href="{{ get_url('static', filename='marketing-old-ie.css') }}">
  <![endif]-->

  <!--[if gt IE 8]><!-->
  <link rel="stylesheet" type="text/css"
  href="{{ get_url('static', filename='marketing.css') }}" />
  <!--<![endif]-->

</head>
<body>

  <div class="content">

    <h1 class="content-head is-center"><a href="/">Jaaga - Project Sphere</a></h1>
    <h4 class="content-head is-center">Program design for socio-environmental entrepreneurs</h4>

    <form class="pure-form" action="/" method="post">
      <input name="phrase" type="text" placeholder="Search responses" />
    </form>

    <div id="content">
      <h1>Stakeholders</h1>
      <div class="columns">
         <ul>
        %for key in data:
        <li><a href="/stakeholder/{{key}}">{{key}}</a></li>
        %end
      </div>
    </div>

  </div>

  <div class="footer l-box is-center">
    Made with love by the <a href="http://jaaga.in">Jaaga</a> Crew
  </div>

</body>
</html>
