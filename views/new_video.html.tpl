%rebase('main.html.tpl', title='New Video')

<div class="container">
  <div class="row">
    <div class="col col-md-12">
      <h3>New Video</h3>

      <div>&nbsp;</div>
      <div>&nbsp;</div>

      <form method="post" action="/video" class="form-horizontal">

	<div class="form-group">
	  <label for="form-title" class="col-md-3 control-label">Title</label>
	  <div class="col-md-7">
	    <input type="text" class="form-control" id="form-title" name="title" placeholder="Title" />
	  </div>
	</div>

	<div class="form-group">
	  <label for="form-url" class="col-md-3 control-label">URL</label>
	  <div class="col-md-7">
	    <input type="text" class="form-control" id="form-url" name="url" placeholder="http://www.example.com" />
	  </div>
	</div>

	<div class="form-group">
	  <label for="form-length" class="col-md-3 control-label">Length</label>
	  <br />
	  <div class="col-md-7">
	    <select class="form-control" id="form-length" name="length">
	      <option value="short">short</option>
	      <option value="long">long</option>
	    </select>
	  </div>
	</div>

	<div class="form-group">
	  <label for="form-viewed" class="col-md-3 control-label">Viewed</label>
	  <div class="col-md-7">
	    <input type="checkbox" id="form-viewed" name="viewed"/>
	  </div>
	</div>

	<div class="form-group">
	  <label for="form-timestamp" class="col-md-3 control-label">Timestamp</label>
	  <div class="col-md-7">
	      <input type="text" class="form-control" id="form-timestamp" name="timestamp" placeholder="00h05m30s" />
	    </div>
	</div>

	<div class="form-group">
	  <label for="form-tags" class="col-md-3 control-label">Tags</label>
	  <div class="col-md-7">
	    <input type="text" class="form-control" id="form-tags" name="tags" placeholder="News,Interesting,Education" />
	  </div>
	</div>

	<div>&nbsp;</div>
	<div>&nbsp;</div>

	<div class="form-group">
	  <div class="col-md-offset-3 col-md-7">
	    <button type="submit" class="btn btn-default">Create</button>
	  </div>
	</div>
      </form>
    </div>
  </div>
</div>
