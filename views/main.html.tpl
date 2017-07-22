<html>
  <head>
    <title>{{title or 'Videos App'}}</title>
    <link href="/static/css/bootstrap.min.css" rel="stylesheet"/>
  </head>

  <body>
    <div class="container">

      <div>&nbsp;</div>
      <div class="row">
        <div class="col col-md-12">
          <a href="/" class="text-muted"><b>VIDEOSAPP</b></a>
          <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <a href="/videos" class="text-muted"><b>Videos</b></a>
          <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <a href="/video/new" class="text-muted"><b>Create</b></a>
          <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
          <a href="/videos/search" class="text-muted"><b>Search</b></a>
          <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

          <a href="/exit" class="text-muted pull-right"><b>Exit</b></a>
	</div>
      </div>
      <hr />

{{!base}}

    </div>

  </body>
</html>
