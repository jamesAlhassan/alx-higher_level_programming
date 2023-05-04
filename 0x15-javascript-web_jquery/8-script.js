const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
$.getJSON(url, function(content) {
	const results = content["results"];
	results.map((result) => {
		$("UL#list_movies").append("<li>"+result['title']+"</li>");
	});
});
