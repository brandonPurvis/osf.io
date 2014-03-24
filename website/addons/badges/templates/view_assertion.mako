<link rel="stylesheet" href="/static/vendor/bower_components/bootstrap/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="/static/vendor/bower_components/bootstrap/dist/css/bootstrap-theme.min.css">
<script src="/static/vendor/bower_components/jQuery/dist/jquery.min.js"></script>
<script src="/addons/static/badges/png-baker.js"></script>
<script src="/addons/static/badges/bake-badges.js"></script>

<br />
<div class="media well">
  <a class="pull-left" href="json/">
    <img class="media-object open-badge" badge-url="json/" src="${image}" width="150px" height="150px" id="image">
  </a>
  <div class="media-body">
    <h4 class="media-heading"> <a href="${url}">${name}</a>
        <small> ${description} </small>
        <small class="pull-right">Endorsed by <a href="${issuer}">${issuer_name}</a></small>
        </h4>
    %if evidence:
      <a href="${evidence}">${criteria}</a>
    %else:
      ${criteria}
    %endif
    <br />
    <h5>Awarded to <a href="/${recipient['identity']}/">${project_name}</a> and it's contributors<small> on ${issued_on}</small></h5>
  </div>
  <ul>
    %for contributor in contributors:
    <li>
        <a href="${contributor._id}">${contributor.fullname}</a>
    </li>
    %endfor

  </ul>
</div>
