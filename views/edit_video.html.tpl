%rebase('main.html.tpl', title='Edit Video')

<div class="container">
  <div class="row">
    <div class="col col-md-12">
      <h3>{{video['title']}}</h3>

      <div>&nbsp;</div>
      <div>&nbsp;</div>

      <form method="post" action="/video" class="form-horizontal">

	<div class="form-group">
	  <label for="form-title" class="col-md-3 control-label">Title</label>
	  <div class="col-md-7">
	    <input type="text" class="form-control" id="form-title" name="title" value="{{video['title']}}" />
	  </div>
	</div>

	<div class="form-group">
	  <label for="form-url" class="col-md-3 control-label">URL</label>
	  <div class="col-md-7">
	    <input type="text" class="form-control" id="form-url" name="url" value="{{video['url']}}" />
	  </div>
	</div>

	<div class="form-group">
	  <label for="form-length" class="col-md-3 control-label">Length</label>
	  <br />
	  <div class="col-md-7">
	    <select class="form-control" id="form-length" name="length">
	      %if video['length'] == 'short':
	      <option value="short">short</option>
	      <option value="long">long</option>
	      %else:
	      <option value="long">long</option>
	      <option value="short">short</option>
	      %end
	    </select>
	  </div>
	</div>

	<div class="form-group">
	  <label for="form-viewed" class="col-md-3 control-label">Viewed</label>
	  <div class="col-md-7">
	    %if video['viewed'] == 0:
	    <input type="checkbox" id="form-viewed" name="viewed"/>
	    %else:
	    <input type="checkbox" id="form-viewed" name="viewed" checked/>
	    %end
	  </div>
	</div>

	<div class="form-group">
	  <label for="form-timestamp" class="col-md-3 control-label">Timestamp</label>
	  <div class="col-md-7">
	    <input type="text" class="form-control" id="form-timestamp" name="timestamp" value="{{video['timestamp']}}" />
	  </div>
	</div>

	<div class="form-group">
	  <label for="form-tags" class="col-md-3 control-label">Tags</label>
	  <div class="col-md-7">
	    <input type="text" class="form-control" id="form-tags" name="tags" value="{{video['tags']}}" />
	  </div>
	</div>

	<div>&nbsp;</div>
	<div>&nbsp;</div>

	<input type="hidden" name="id" value="{{video['id']}}" />

	<div class="form-group">
	  <div class="col-md-offset-3 col-md-7">
	    <button type="submit" class="btn btn-default">Save</button>
	    <a href="/video/{{video['id']}}" class="btn btn-link">Cancel</a>
	  </div>
	</div>
      </form>

    </div>
  </div>
</div>
