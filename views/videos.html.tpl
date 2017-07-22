%rebase('main.html.tpl', title='Videos')

<div class="row">
  <div class="col col-md-12">
    %if meta['count'] == 1:
    <h2>{{meta['count']}} Video</h2>
    %else:
    <h2>{{meta['count']}} Videos</h2>
    %end
    %if len(videos) == 0:
    <em class="text-muted">There are no videos.</em>
    %else:
    <div class="table-responsive">
      <table class="table table-responsive table-condensed table-striped table-hover table-nowrap">
	<thead>
	  <tr>
	    <th>Title</th>
	    <th>Length</th>
	    <th>Viewed</th>
	    <th>Added</th>
	  </tr>
	</thead>

	<tbody>
	  %for video in videos:
	  <tr>
	    <td>
	      <a href="{{video['url']}}" class="text-muted"><small>WATCH</small></a>
	      <span>&nbsp;&nbsp;&nbsp;&nbsp;</span>
	      <span>{{video['id']}}</span>
	      <a href="/video/{{video['id']}}">{{video['title']}}</a>
	    </td>
	    <td>{{video['length']}}</td>
	    %if video['viewed'] == 1:
	    <td>yes</td>
	    %else:
	    <td>no</td>
	    %end
	    <td>{{video['add_date']}}</td>
	  </tr>
	  %end
	</tbody>

      </table>
    </div>
    %end
  </div>
</div>

%if len(videos) > 0:
<div class="row">
  <div class="col col-md-12">
    %if meta['page'] > 1:
    <a href="/videos?{{meta['query_string']}}&page={{meta['page']-1}}">&lt; Previous</a>
    %else:
    <span disabled class="invisible">&lt; Previous</span>
    %end

    <span>&nbsp;&nbsp;&nbsp;</span>
    <span style="display: inline-block; min-width: 80px; text-align: center;">
      {{meta['page']}} / {{meta['num_pages']}}
    </span>
    <span>&nbsp;&nbsp;&nbsp;</span>

    %if meta['page'] < meta['num_pages']:
    <a href="/videos?{{meta['query_string']}}&page={{meta['page'] + 1}}">Next &gt;</a>
    %else:
    <span disabled class="invisible">Next &gt;</span>
    %end
      
  </div>
</div>
%end
