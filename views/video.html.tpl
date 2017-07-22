%rebase('main.html.tpl', title='Video')

<div class="container">
  <div class="row">

    <div class="col col-md-12">
      <h3>{{video['title']}}</h3>
    </div>

    <div>&nbsp;</div>

    <form method="post" action="/video/delete">
      <input type="hidden" name="id" value="{{video['id']}}" />
      <a href="/video/{{video['id']}}/edit" class="btn btn-link">Edit</a>
      <span class="text-muted">|</span>
      <button type="submit" class="btn btn-link"><span class="text-danger">Delete</span></button>
      <span class="text-muted">|</span>
      <a href="{{video['url']}}" class="btn btn-link">Watch</a>
    </form>
    <div>&nbsp;</div>

    <p>
      <dl class="dl-horizontal">
	<dt>URL</dt>
	<dd><a href="{{video['url']}}">{{video['url']}}</a></dd>

	<dt>Added</dt>
	<dd>{{video['add_date']}}</dd>

	<dt>Length</dt>
	<dd>{{video['length']}}</dd>

	<dt>Viewed</dt>
	%if video['viewed'] == 0:
	<dd>no</dd>
	%else:
	<dd>yes</dd>
	%end

	<dt>Tags</dt>
	<dd>{{video['tags']}}</dd>

	<dt>Timestamp</dt>
	%if video['timestamp'] == '':
	<dd class="text-muted"><i>none</i></dd>
	%else:
	<dd>{{video['timestamp']}}</dd>
	%end

      </dl>
    </p>

  </div>
</div>
